import os
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
from textwrap import dedent

from django.test import SimpleTestCase

SETTINGS = dedent("""
    from datetime import timedelta

    from axes.tiers import LockoutTier

    SECRET_KEY = "test"
    INSTALLED_APPS = ["django.contrib.auth", "django.contrib.contenttypes", "axes"]
    DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}
    AXES_LOCKOUT_TIERS = [LockoutTier(failures=3, cooloff=timedelta(minutes=15))]
    """)

CHECK = dedent("""
    import django
    from django.conf import settings

    django.setup()
    print(settings.AXES_VERBOSE, settings.AXES_LOCKOUT_TIERS[0].failures)
    """)


class LockoutTierImportTestCase(SimpleTestCase):
    def test_lockout_tier_can_be_imported_from_a_settings_module(self):
        """
        Importing LockoutTier in settings must not make axes read the settings
        before they are loaded, which left every AXES_* default unset (#1544).
        """
        with TemporaryDirectory() as tmp:
            (Path(tmp) / "tier_settings.py").write_text(SETTINGS)
            result = subprocess.run(
                [sys.executable, "-c", CHECK],
                cwd=tmp,
                env={
                    **os.environ,
                    "DJANGO_SETTINGS_MODULE": "tier_settings",
                    "PYTHONPATH": tmp,
                },
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.split(), ["True", "3"])

    def test_lockout_tier_is_still_importable_from_axes_conf(self):
        from axes.conf import LockoutTier as ConfLockoutTier
        from axes.tiers import LockoutTier

        self.assertIs(ConfLockoutTier, LockoutTier)

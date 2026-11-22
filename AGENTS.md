# AGENTS.md

Guidance for using LLMs and coding agents on django-axes. It is
written for the people who use these tools and for the tools
themselves.

The key words MUST, SHOULD and MAY are used as in
[RFC 2119](https://www.rfc-editor.org/rfc/rfc2119). MAY NOT means
"is not allowed to".

## Fair use of LLMs

- LLMs MAY be used to assist development and maintenance: writing and
  reviewing code, tests and documentation, and investigating issues.
- LLM attribution MAY be used where wanted, for example a
  `Co-Authored-By` commit trailer or a note in the pull request. It
  can improve the transparency and traceability of the tools and
  preferences behind a change. It is not required.
- LLMs MAY NOT be used to submit issues or pull requests
  automatically. A human being SHOULD review and verify every issue
  and pull request before it is submitted.
- The person who submits a contribution is its author. They are
  responsible for it and SHOULD be able to explain it and answer
  review questions about it.
- Issues, pull request descriptions and review replies SHOULD be as
  short as the change allows, and SHOULD describe behaviour the
  submitter has checked.
- Security problems MUST be reported privately with "Report a
  vulnerability" on the repository's Security tab, not in a public
  issue.

## Code

- LLM generated code SHOULD be as concise as possible.
- All code MUST be human readable, or documented well enough that
  maintainers can work on it several years from now without knowing
  the specific issue that was being solved, the discussion around it,
  or other nuances from the time of writing.
- A change SHOULD be limited to what its purpose needs, without
  unrelated refactoring or reformatting.
- A bug fix SHOULD come with a test that fails without the fix.
- The public API SHOULD stay backwards compatible. A breaking change
  SHOULD be agreed in an issue first.

## Commits

- Commits SHOULD be split into small logical pieces. Each one handles
  a logical whole or one aspect that needs work: a feature, a bug fix,
  a documentation update, and so on.
- A commit message SHOULD say what changed and why.

## Documentation

- Every added feature SHOULD be documented in the Read the Docs
  documentation under `docs/`. The shorter the better.
- Every feature flag and code path SHOULD include an example of its
  intended use.
- A change that users can notice SHOULD get a line in `CHANGES.rst`.

## Working in this repository

- Set up with `python -m pip install -r requirements.txt`.
- Run the tests with `pytest`. `tox` runs them on every supported
  Python and Django version.
- Run the checks with `tox -e py314-djqa`: `mypy`, `prospector` and
  `black --check`.
- Build the documentation with
  `sphinx-build -b html docs docs/_build/html`.
- The package version comes from the git tag. Version numbers MUST NOT
  be written into the code.
- The supported Python and Django versions are listed in
  `pyproject.toml`, which also holds the tox configuration, in
  `.github/workflows/test.yml` and in `docs/1_requirements.rst`. They
  SHOULD be changed together.
- Actions in `.github/workflows` MUST be pinned to a full commit SHA.
  The repository rejects workflows that use anything else.
- Changes to the translations in `axes/locale` SHOULD be reviewed by
  someone who speaks the language.

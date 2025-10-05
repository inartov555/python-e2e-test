# Note:
!!! This is just an example of the code, this framework cannot be used for testing Instagram or running multiple times !!!

# E2E Test Framework (Python + Pytest + Playwright)

Modern, scalable, and maintainable test framework built with **Pytest** and **Playwright** using **Page Object Model**,
OOP, and SOLID principles.

## How to run

NOTE: when you start the source run_tests.sh script, it copies the project to other directory to avoid adding cached files, and venv directory to the project folder

To start tests, you need:

Run the run_tests.sh file next way: source run_tests.sh PATH_TO_THE_PROJECT PATH_TO_INI_CONFIG
Copied project folder, run results like logs, etc., are located in: /home/$user_name/TEST1/workspace
Artifacts (run results, logs, etc.) are located in: /home/$user_name/TEST1/workspace/artifact

BEFORE you start tests, you need to fill in [`pytest.ini`](./pytest.ini) parameters.
To set `password` parameter, encrypt account password using [`tools/temp_encr.py`](./tools/temp_encr.py)

## Structure

```
python-e2e-test/
  src/
    core/          # config, browser, logging, base abstractions
    components/    # reusable UI components (PostCard)
    pages/         # Page Objects (public + private)
  tests/           # pytest tests
  artifacts/       # logs, test results, screenshots, videos, etc.
```

## Decisions & Rationale (Summary)

- **Playwright** chosen over Selenium for stability, auto-waits, tracing, and easier parallelism — reduces flakiness and
  keeps PageObjects slim while still SOLID.
- **Page Object + Components**: complex parts of the feed are encapsulated into a `PostCard` component with clear actions
  (e.g., `like()`, `save()`, `open_comments()`) to favor single responsibility and reusability.
- **Typing & lint-friendly**: type hints and docstrings added; methods return self or domain objects for fluent usage.
- **Fixtures**: `browser_context` and `page` fixtures centralize setup/teardown; base_url and viewport are unified (HD).
- **Capture issue** this issue can be covered by wait_to_handle_capture_manually = true and after that handle it manually
  while test is waiting 120 seconds. I'd say that capture issue will not happen when tests are run just a few times.

See [`TASK_DESCRIPTION.md`](./TASK_DESCRIPTION.md) for more info.

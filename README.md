## Note:
!!! This is just an example of the code, this framework cannot be used for testing Instagram or running multiple times !!!

## E2E Test Framework (Python + Pytest + Playwright)

Modern, scalable, and maintainable test framework built with **Pytest** and **Playwright** using **Page Object Model**,
OOP, and SOLID principles.

## How to run

NOTE: when you start the source run_tests.sh script, it copies the project to other directory to avoid adding cached files, and venv directory to the project folder. 

To start tests, you need:

1. Open as a logged in user: (https://www.instagram.com/accounts/edit/).
2. Switch the "Show account suggestions on profiles" option OFF.
3. Follow at least one person who make some posts.
4. Log out and then log in back.
5. Open a terminal window and run `sudo apt-get install libavif16`
6. Fill in [`pytest.ini`](./pytest.ini) parameters. 
   To set `password` parameter, encrypt account password using [`tools/temp_encr.py`](./tools/temp_encr.py).
7. Run the `run_tests.sh` file next way: `source run_tests.sh $PATH_TO_THE_PROJECT $PATH_TO_INI_CONFIG` (if you don't pass ini config file, then default one is used [`pytest.ini`](./pytest.ini)). 
   Copied project folder, run results like logs, etc., are located in: `/home/$user_name/TEST1/workspace`. 
   Artifacts (run results, logs, etc.) are located in: `/home/$user_name/TEST1/workspace/artifact`.

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
- **Capcha issue** this issue can be covered by `wait_to_handle_capture_manually = true` and after that handle it manually 
  while test is waiting 120 seconds. I'd say that Capcha issue will not happen when tests are run just a few times.
- **Password encryption** It's a good thing to keep sensitive data like password, etc., encrypted to avoid data leakage.
- **PlaywrightDriver** This adapter was added for dependency inversion. Also, it'll provide abiltiy to easily add unit tests for pages.
- **Locators with text**: The text needs to be placed to the localization classes later to support different languages

See [`WHAT_TESTS_DO.md`](./WHAT_TESTS_DO.md) to get the test description.
See [`TASK_DESCRIPTION.md`](./TASK_DESCRIPTION.md) to get the test description.

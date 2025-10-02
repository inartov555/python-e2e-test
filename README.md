# Instagram E2E Test Framework (Python + Pytest + Playwright)

Modern, scalable, and maintainable test framework built with **Pytest** and **Playwright** using **Page Object Model**,
OOP, and SOLID principles. Designed per the task to model Instagram public pages and an authenticated feed page.
> Note: Tests that require authentication are **skipped** unless a valid Playwright `storage_state.json` is provided (to avoid CAPTCHA).

## Quick Start

```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# (Optional) Generate browsers for Playwright
python -m playwright install

# Copy .env.example to .env and adjust if needed
cp .env.example .env

# If you have cookies (storage state) export them as storage_state.json and place in ./artifacts/auth/
# Or set STORAGE_STATE in .env to its path.

# Run tests
pytest -q
```

## Structure

```
instagram_e2e_framework/
  src/
    core/          # config, browser, logging, base abstractions
    components/    # reusable UI components (PostCard)
    pages/         # Page Objects (public + private)
  tests/           # pytest tests
  artifacts/       # screenshots, videos, auth storage state
```

## Decisions & Rationale (Summary)

- **Playwright** chosen over Selenium for stability, auto-waits, tracing, and easier parallelism — reduces flakiness and
  keeps PageObjects slim while still SOLID.
- **Page Object + Components**: complex parts of the feed are encapsulated into a `PostCard` component with clear actions
  (e.g., `like()`, `save()`, `open_comments()`) to favor single responsibility and reusability.
- **Config via .env / environment**: allows CI customization without code changes.
- **Auth handling**: tests that need login rely on `storage_state.json` if present; otherwise they’re skipped — avoiding CAPTCHA logic in code.
- **Typing & lint-friendly**: type hints and docstrings added; methods return self or domain objects for fluent usage.
- **Fixtures**: `browser_context` and `page` fixtures centralize setup/teardown; base_url and viewport are unified (FULLHD).

See [`TASK_TRANSLATION.md`](./TASK_TRANSLATION.md) for the translated assignment.

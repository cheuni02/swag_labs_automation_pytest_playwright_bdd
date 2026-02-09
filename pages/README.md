# Swag Labs Webapp Automated by Pytest-Playwright and Pytest-BDD

This is basically the test automation of https://www.saucedemo.com/inventory.html with pytest-playwright and pytest-bdd to demonstrate that cucumber can be integrated, and slightly improve a pure POM repo in that it makes it more user, rather than page focussed.

## Setup
1) make sure to have python 3
2) cd < dir to cloned repo >
3) python3 -m venv .venv
4) source .venv/bin/activate
5) pip install --upgrade pip
6) pip install -r requirements.txt
7) playwright install

## Running
### All tests

```
pytest -s
```

### Specific test

```
pytest -s -k < name of test >
```

### Env variables to prefix commands above

```
HEADLESS={false|true} SLOW_MO={value in 10s} 
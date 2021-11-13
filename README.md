# Introduction

Learning project for jinja 2


# Development Setup

Create virual environment and install dependencies for local development:

```
python3.8 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

Exporting variables doesn't make for a great development experience so I recommend using the enviroment manager tools of your editor and for testing create a ./pytest.ini that looks like this:

```
[pytest]
env =
    SKIP_INTEGRATION=True
    DBC_PROJECT_PATH=./example/jaffle_shop
```

**REMINDER: do NOT commit any files that contain security tokens**

Git ignore already contains an exclusion for pytest.ini


# Build

Build python wheel:
```
python setup.py sdist bdist_wheel
````

# Test
s
No tests, for learning only.


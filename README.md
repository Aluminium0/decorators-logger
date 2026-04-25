# Decorators Logger

Homework for Lecture 3: *Decorators*

## Description

This project implements:

* a basic `logger` decorator
* a parameterized `logger(path)` decorator

Both log:

* timestamp
* function name
* arguments (args, kwargs)
* return value

## Files

* `task_1.py` - basic decorator
* `task_2.py` - parameterized decorator
* `previous_homework.py` - logger applied to previous assignment

## Run

```bash
python task_1.py
python task_2.py
python previous_homework.py
```

## Notes

* Logs are written in append mode (`.log` files)
* `functools.wraps` is used
* Path is handled via closure in `logger(path)`

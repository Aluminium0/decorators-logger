# Logger Decorators

Домашнее задание по декораторам:
- обычный декоратор `logger` (лог в `main.log`)
- параметризованный декоратор `logger(path)` / `logger_with_path(path)`
- применение логгера к коду из темы «iterators / generators / yield»

## Files
- `logger.py` — единая реализация логирования:
  - `_format_log_line(...)` формирует строку лога
  - `_write_log(...)` пишет строку в файл в режиме добавления
  - `logger` и `logger_with_path`
- `main.py` — проверка обычного декоратора (`test_1`)
- `main_2.py` — проверка параметризованного декоратора (`test_2`), имя декоратора сохранено как `logger(path)`
- `iterators_app.py` — пример применения логгера к функциям из темы про итераторы/генераторы

## Usage

```python
from logger import logger_with_path

@logger_with_path('log.txt')
def add(a, b):
    return a + b
```

## Run checks

```bash
python main.py
python main_2.py
python iterators_app.py
```

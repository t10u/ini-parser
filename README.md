# Docker .INI file parser

## Add an option
```
$ cat test.ini | docker run --rm -i tonigrigoriu/ini-parse section option value > test_updated.ini
```

## Delete an option
```
$ cat test.ini | docker run --rm -i tonigrigoriu/ini-parse section option delete > test_updated.ini
```
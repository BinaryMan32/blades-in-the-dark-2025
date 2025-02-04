# Blades in the Dark 2025

Documentation is built as a static site using [mkdocs][] and the [material][mkdocs-material] theme.
If you want to do something else, check the [mkdocs catalog][mkdocs-catalog].

[mkdocs]: https://www.mkdocs.org/
[mkdocs-material]: https://squidfunk.github.io/mkdocs-material
[mkdocs-catalog]: https://github.com/mkdocs/catalog

## Local Preview with Virtualenv

Create virtualenv:
```sh
python3 -m venv .venv/ && source .venv/bin/activate && pip3 install -r requirements.txt
```

Preview:
```sh
mkdocs serve
```

## Local Preview with Docker

```sh
./preview-docker.sh
```

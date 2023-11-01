# Cookiecutter Versatile Data Kit Plugin

![test workflow](https://github.com/tozka/cookiecutter-vdk-plugin/actions/workflows/test.yml/badge.svg)

Cookiecutter to get started creating [Versatile Data Kit Plugin](https://github.com/vmware/versatile-data-kit/tree/main/projects/vdk-plugins) plugin for creating new data sources.

## Features

* Python project skeleton with src directory, setup.py, tests directory
* Testing setup with vdk-test-utils and pytest and example test
* Plugin CI template (.plugin-ci.yml) used to integrate with Plugin CI in VDK repo

## Quickstart
Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):

```
pip install -U cookiecutter
```

Generate a VDK Plugin package project:

```
cookiecutter https://github.com/versatile-data-kit-dev/new-vdk-data-source.git
```

Then

* Include your implementation files inside the `src` folder;
* Include any tests inside the `tests` so they can be ran by CI framework automatically.



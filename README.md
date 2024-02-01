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

* Follow all the **TODO** in the code files and README and complete them. 
* Include extra your implementation files inside the `src` folder; Follow the 
* Include any tests inside the `tests` so they can be ran by CI framework automatically.

## Concepts

### Data Source

A Data Source is a central component responsible for establishing and managing a connection to a specific set of data. It interacts with a given configuration and maintains a stateful relationship with the data it accesses. This stateful relationship can include information such as authentication tokens, data markers, or any other form of metadata that helps manage the data connection. The Data Source exposes various data streams through which data can be read.

### Data Source Stream

A Data Source Stream is an abstraction over a subset of data in the Data Source. It can be thought of as a channel through which data flows. Each Data Source Stream has a unique name to identify it and includes methods to read data from the stream. For example for Database based data source , each table could be a separate stream. Streams can be ingested in parallel potentially.

Reading from the stream yields a sequence of Data Source Payloads

### Data Source Payload

The Data Source Payload is a data structure that encapsulates the actual data along with its metadata. The payload consists of four main parts:

Data: containing the core data that needs to be ingested (e.g in database the table content)
Metadata: A dictionary containing additional contextual information about the data (for example timestamps, environment specific metadata, etc.)
State: Contains the state of the data soruce stream as of this payload. For example in case of incremental ingestion from a database table it would contain the value of a incremental key columns (le.g updated_time column in teh table) which can be used to restart/continue the ingestion later.


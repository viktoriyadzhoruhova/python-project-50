### Hexlet tests and linter status:
[![Actions Status](https://github.com/viktoriyadzhoruhova/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/viktoriyadzhoruhova/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/cb7aa6e6b19f122697e2/maintainability)](https://codeclimate.com/github/viktoriyadzhoruhova/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/cb7aa6e6b19f122697e2/test_coverage)](https://codeclimate.com/github/viktoriyadzhoruhova/python-project-50/test_coverage)

# Python Project 50

Project 50 is a command-line utility designed for comparing two configuration files. 
This tool is particularly useful for software developers and system administrators 
who need to understand differences in configuration states between different environments. 
It can compare both JSON and YAML file formats,
providing the output in a variety of readable formats.


## Installation

Clone the repository and install the dependencies using `poetry`:

```sh
git clone https://github.com/viktoriyadzhoruhova/python-project-50
cd python-project-50
poetry install
```

## Usage

To view help and usage information:

```sh
poetry run gendiff -h
```

### Example Usage

To compare two files:

```sh
poetry run gendiff file1.json file2.yml
```

The output will be shown in a readable format. For example:

```sh
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

## Command Line Options

- `-h, --help` — Show help message and exit.
- `-f FORMAT, --format FORMAT` — Set the output format (supported formats: `stylish`, `plain`, `json`).

## Output Formats

### Stylish (Default)
The default format shows changes in a structured, tree-like view, highlighting additions, removals, and modifications.

### Plain
A straightforward text format for easily understanding what has changed, without any hierarchy:

```sh
Property 'common.follow' was added with value: false
```

### JSON
Provides the difference in JSON format, suitable for further automated processing or integration with other tools.


### Running Tests
To run the test suite:

```sh
poetry run pytest
```

### Linting
To check the code for linting issues:

```sh
make lint
```

## CI/CD
The project uses GitHub Actions for continuous integration, ensuring code quality through automated testing and linting. 
The status badges at the top reflect the current state of the latest build.

## Demonstration
See the tool in action:

[![asciicast](https://asciinema.org/a/690376.svg)](https://asciinema.org/a/690376)

# Prompt Engineering Toolkit for Rapid Prototyping of Aleph Alpha Luminous and OpenAI Applications

- [Prompt Engineering Toolkit for Rapid Prototyping of Aleph Alpha Luminous and OpenAI Applications](#prompt-engineering-toolkit-for-rapid-prototyping-of-aleph-alpha-luminous-and-openai-applications)
  - [Idea](#idea)
  - [Folderstructure for Input Data](#folderstructure-for-input-data)
  - [Components](#components)
  - [Installation](#installation)
  - [Usage](#usage)

## Idea
This repository can be used to fastly iterate over prompt engineering problems and prompts.



## Folderstructure for Input Data
Folderstructure:

```
├── data
│   ├── groundtruth
│   └── input
├── prompts
│   └── extraction
```

## Components

This repository uses the libraries in the following table


|Library|Reason|
|----|----|
|Langchain|Easily Access and use LLMs and build Chains|
|Weights & Biases|Monitoring and Logging of the LLM Chains|
|Aleph Alpha Client|LMM Provider|
|Loguru|Logging for the application|


## Installation

To use the repository i would recommend installing and using pyenv.

The Python Version of this is Python 3.11

```bash
pip install poetry
poetry install
```

## Usage

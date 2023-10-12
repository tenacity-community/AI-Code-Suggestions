# AI Code Suggestions for Tenacity Learn

![Tenacity Learn Logo](https://tenacity.social/img/Tenacity%20Logo%20White%20Transparent.png)

This open-source project is an integral part of the Tenacity Learn website and app, designed to provide a personalized learning experience for coding enthusiasts. In this README, you'll find detailed information about the project, how it works, and how you can contribute to this exciting venture.

## Table of Contents

- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

At Tenacity Learn, our mission is to empower learners of all levels with tools and guidance to enhance their coding skills. We believe in the power of personalized learning, and this project is a key component of our platform.

Our AI Code Suggestions feature leverages the capabilities of Azure OpenAI to analyze the code written by users and provide live suggestions to improve their code. The AI system does not simply provide answers but rather offers hints and suggestions, helping users understand and rectify their mistakes. This collaborative learning approach is designed to foster a deeper understanding of coding concepts.

## Project Overview

The core of this project is the `model.py` file, which serves as the interface between our Tenacity Learn platform and Azure OpenAI. Let's take a closer look at the key components of this file:

### Environment Variables

To ensure the security of our Azure OpenAI integration, we use environment variables to store sensitive information, such as the API key and endpoint. These variables include:
- `AZURE_OAI_KEY`: Your Azure OpenAI API key.
- `AZURE_OAI_ENDPOINT`: The endpoint for the Azure OpenAI service.
- `AZURE_OAI_MODEL`: The specific Azure OpenAI model to be used.
- `PROMPT`: The initial prompt to be provided to the AI system.

### Code Example

The code example in the `code` variable serves as the input for the AI system. Users can replace this code with their own, and the AI will provide suggestions based on the input provided.

### OpenAI Configuration

We set up the OpenAI configuration by specifying the API type, base URL, version, and API key. This ensures that the AI requests are directed to the appropriate Azure OpenAI model.

### Sending Requests to Azure OpenAI

We send a request to the Azure OpenAI model with the user's code and initial prompt. The response from the AI system is then displayed to the user, providing suggestions and feedback on the code.

## Getting Started

To get started with this project, you'll need to have the necessary environment variables set up. Make sure to create a `.env` file and store your Azure OpenAI API key, endpoint, model, and prompt as mentioned in the `model.py` file.

## Usage

The usage of this project is straightforward. Users can replace the example code in the `code` variable with their own code. When they run the `model.py` script, it sends a request to Azure OpenAI, and the AI system provides suggestions based on the code provided.

Here's a brief overview of the steps:

1. Set up your environment variables in the `.env` file.
2. Replace the `code` variable with your code.
3. Run the `model.py` script.
4. Review the AI-generated suggestions for your code.

## Contributing

We welcome contributions from the open-source community, especially as part of Hacktoberfest. If you're interested in improving and expanding this project, please follow these steps:

1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear and concise messages.
4. Submit a pull request to the `main` branch of this repository.

We value contributions that enhance the functionality, usability, and documentation of the project. Your involvement is greatly appreciated!

## License

This project is licensed under the MIT License. You can find more details in the [LICENSE](LICENSE) file.

We hope you find this project interesting and useful. If you have any questions, feedback, or suggestions, please feel free to reach out to us. Happy coding with Tenacity Learn! 🚀

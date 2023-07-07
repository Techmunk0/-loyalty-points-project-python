
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>Loyalty points project in Python with Temporal
</h1>
<h3>◦ Unlock your rewards with a loyalty points Workflow!</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
</p>
<img src="https://img.shields.io/github/languages/top/rachfop/loyalty-points-project-python?style&color=5D6D7E" alt="GitHub top language" />
<img src="https://img.shields.io/github/languages/code-size/rachfop/loyalty-points-project-python?style&color=5D6D7E" alt="GitHub code size in bytes" />
<img src="https://img.shields.io/github/commit-activity/m/rachfop/loyalty-points-project-python?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/license/rachfop/loyalty-points-project-python?style&color=5D6D7E" alt="GitHub license" />
</div>

---

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [⚙️ Features](#-features)
- [📂 Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The Loyalty Points Project in Python is a codebase that implements a loyalty program management system with the Temporal SDK. It provides a Flask application with REST API endpoints for managing loyalty points, such as adding or removing points and sending emails. The project utilizes the Temporal workflow engine to handle program logic, ensuring efficient and reliable execution. With its robust functionality and modular design, the Loyalty Points Project offers a valuable solution for businesses looking to implement and manage their loyalty programs effectively.

---

## ⚙️ Features

| Feature                | Description                           |
| ---------------------- | ------------------------------------- |
| **⚙️ Architecture**     | The codebase follows a microservices architecture pattern, where different components handle specific functionalities. The Flask application (`app.py`) serves as the frontend, providing REST API endpoints for managing the loyalty program. The LoyaltyProgram workflow (`loyalty_workflow.py`) implements the program logic, including point management and email sending. The worker (`main.py`) listens to a task queue and runs the LoyaltyProgram workflow and the send_email activity. The codebase uses the Temporal workflow engine to handle the program logic efficiently. The architecture allows for scalability and modularity, with each component responsible for a specific task.|
| **📖 Documentation**   | The codebase lacks comprehensive documentation. Although some files have docstrings explaining their purpose, there is a lack of high-level documentation, architectural overview, and usage instructions. Improving the documentation would make it easier for developers to understand the codebase and contribute to the project.|
| **🔗 Dependencies**    | The codebase relies on several external libraries and systems. Notable dependencies include Flask for building the REST API, Temporal as the workflow engine, and Redis for task queue management. The codebase also relies on the standard Python libraries such as os, requests, and json. The dependencies are managed using Pipenv, as seen in the `Pipfile` and `Pipfile.lock` files.|
| **🧩 Modularity**      | The codebase demonstrates a reasonable level of modularity. Each file serves a specific purpose, such as defining data classes, implementing workflows, or managing the worker. The codebase follows a logical separation of concerns, making it easier to maintain and extend. However, there is room for improvement in organizing the code into more granular and interchangeable components, promoting reusability and maintainability.|
| **✔️ Testing**          | The codebase does not have comprehensive test coverage. There are no specific test files or test folders present. Implementing tests using a testing framework like pytest or unittest would help ensure the correctness of the codebase and facilitate future development. The lack of testing strategies and tools poses a risk to the stability and reliability of the project.|
| **⚡️ Performance**      | The codebase does not have any performance optimizations explicitly implemented. However, the usage of the Temporal workflow engine can improve efficiency by handling the program logic in a distributed manner. The codebase does not exhibit any resource-intensive operations or performance bottlenecks. Proper profiling and optimization techniques can be applied if performance becomes a concern in the future.|
| **🔐 Security**        | The codebase does not explicitly demonstrate security measures. However, since it utilizes Flask, it can leverage Flask's security features such as protecting against common web vulnerabilities (e.g., Cross-site Scripting (XSS), Cross-Site Request Forgery (

---


## 📂 Project Structure


```bash
repo
├── README.md
├── activity.py
├── app.py
├── loyalty_workflow.py
├── main.py
├── poetry.lock
├── pyproject.toml
└── scripts
    ├── aaron.py
    └── script.py

2 directories, 9 files
```

---

## 🧩 Modules

<details closed><summary>Root</summary>

| File                                                                                                          | Summary                                                                                                                                                                                                                                                                       |
| ---                                                                                                           | ---                                                                                                                                                                                                                                                                           |
| [activity.py](https://github.com/rachfop/loyalty-points-project-python/blob/main/activity.py)                 | The code snippet defines a data class called Email with attributes for recipient, subject, and body. It also defines an activity function send_email that takes an Email object as input and prints the email details. The function returns a success message.                |
| [loyalty_workflow.py](https://github.com/rachfop/loyalty-points-project-python/blob/main/loyalty_workflow.py) | This code snippet implements a LoyaltyProgram workflow that allows adding and removing points, sending emails, and tracking loyalty details.                                                                                                                                  |
| [app.py](https://github.com/rachfop/loyalty-points-project-python/blob/main/app.py)                           | This code snippet is a Flask application that provides REST API endpoints for managing a loyalty program. It uses the Temporal workflow engine to handle the program logic, including starting the program, spending/add points, and exiting the program for a specific user. |
| [main.py](https://github.com/rachfop/loyalty-points-project-python/blob/main/main.py)                         | The provided code snippet connects to a local client and initializes a worker. The worker is responsible for executing the LoyaltyProgram workflow and the send_email activity. It listens to a task queue named "loyalty-program-task-queue" and runs indefinitely.          |

</details>

<details closed><summary>Scripts</summary>

| File                                                                                              | Summary                                                                                                                                                                                                                                                   |
| ---                                                                                               | ---                                                                                                                                                                                                                                                       |
| [aaron.py](https://github.com/rachfop/loyalty-points-project-python/blob/main/scripts/aaron.py)   | The code snippet utilizes the "os" module to make 124 POST requests to a local API endpoint, each with a different value for the "i" parameter in the URL. The requests use the "curl" command to send a POST request with a fixed payload of 500 points. |
| [script.py](https://github.com/rachfop/loyalty-points-project-python/blob/main/scripts/script.py) | The code snippet uses the os module to make HTTP POST requests to a local server. It iterates from 1 to 124, sending requests to increment points for each iteration. Each request adds 100 points to the specified endpoint.                             |

</details>

---

## 🚀 Getting Started

### ✔️ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ Requirement 1`
> - `ℹ️ Requirement 2`
> - `ℹ️ ...`

### 📦 Installation

1. Clone the loyalty-points-project-python repository:
```sh
git clone https://github.com/rachfop/loyalty-points-project-python
```

2. Change to the project directory:
```sh
cd loyalty-points-project-python
```

3. 🎮 Install the dependencies:
```sh
# terminal one
poetry run python app.py
# terminal two
poetry run python main.py
```

---

## 🏁 Usage

## Start a Workflow

```command
# terminal one
poetry run python app.py
# terminal two
poetry run python main.py
```

## Example commands

```bash
curl -X POST http://localhost:5000/123
curl -X POST http://localhost:5000/123/add_points/1000
curl -X POST http://localhost:5000/123/add_points/30
curl -X POST http://localhost:5000/123/add_points/20
curl -X GET http://localhost:5000/123
```

## Get Points

```bash
curl -X GET http://localhost:5000/123
```

## Add points

```bash
curl -X POST http://localhost:5000/123/add_points/850
```

## Spend points

```bash
curl -X POST http://localhost:5000/123/spend_points/10
```

## End Workflow

```bash
curl -X DELETE http://localhost:5000/123/exit
```

## Terminate

```bash
temporal workflow terminate --workflow-id 123
```

## Reset

Execute Batch Reset command:

```bash
temporal workflow reset-batch --query "WorkflowType='LoyaltyProgram'" --reason "Sev2: id.1259" --type LastWorkflowTask
```

Dry run a Batch Reset command:

```bash
temporal workflow reset-batch --query "WorkflowType='LoyaltyProgram'" --reason "Sev2: id.1259" --type LastWorkflowTask --dry-run
```


```bash
# create (not needed)
temporal operator search-attribute create --name points --type int
# list
temporal operator search-attribute list
# describe
temporal workflow list \
  --query "(points >= 1000) AND ExecutionStatus='Running'"
```

## 🗺 Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Refactor Y`
> - [ ] `ℹ️ ...`


---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.


---

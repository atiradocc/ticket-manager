# Ticket Manager

Ticket Manager is a Python program that automates the creation of JIRA tickets for the RULE and KB projects. It reads input files in YAML format, extracts the necessary information, and generates the respective JIRA tickets.

## Features

- Create RULE tickets with relevant fields and links to MAP tickets and KB tickets.
- Create KB tickets with relevant fields and links to an Epic ticket.

## Prerequisites

- Python 3.10 or higher
- JIRA API Token

## Installation

1. Clone the repository:

```shell
git clone https://github.com/your-username/ticket-manager.git
```

2. Install the required dependencies:

```shell
pip install -r requirements.txt
```

## Usage

1. Prepare your input files in YAML format with the required fields.
2. Run the program:

```shell
python main.py /path/to/input/files/folder
```

3. The program will read the input files, create the JIRA tickets, and provide the ticket details and links.

## Configuration

Before running the program, make sure to update the configuration file config.yaml with your JIRA URL, project keys, and other necessary settings.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

# License

If you work with the Conformity team, this project is licensed under the MIT License. See the LICENSE file for more information. Otherwise, do not access this repository in any direct or indirect manner.

from jira_manager import JiraManager
from input_parser import InputParser

def main():
    # Path to the input file
    input_file = 'path/to/input_file.yaml'

    # Parse input file
    parser = InputParser(input_file)
    input_data = parser.parse_input()

    # Create JiraManager instance
    jira_manager = JiraManager()

    # Create RULE ticket
    rule_ticket = jira_manager.create_rule_ticket(input_data)

    # Create KB ticket
    kb_ticket = jira_manager.create_kb_ticket(input_data)

    # Print the created tickets
    print("RULE Ticket:")
    print(rule_ticket)
    print("\nKB Ticket:")
    print(kb_ticket)

if __name__ == "__main__":
    main()

import unittest
from input_parser import InputManager


class InputManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.input_manager = InputManager()

    def test_load_input_file(self):
        input_file = "input.yaml"
        data = self.input_manager.load_input_file(input_file)
        self.assertIsInstance(data, dict)
        self.assertIn("Summary", data)
        self.assertIn("Reporter", data)
        # Add more assertions for other fields

    def test_process_input_data(self):
        input_data = {
            "Summary": "Sample summary",
            "Reporter": "test@example.com",
            # Add other fields and their values
        }
        rule_ticket, kb_ticket = self.input_manager.process_input_data(input_data)
        self.assertIsNotNone(rule_ticket)
        self.assertIsNotNone(kb_ticket)
        # Add more assertions to validate the tickets


if __name__ == "__main__":
    unittest.main()

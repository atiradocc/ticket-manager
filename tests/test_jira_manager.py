import unittest
from unittest.mock import patch
from jira_manager import jira_manager


class TestJiraManager(unittest.TestCase):
    @patch("ticket_manager.jira_manager.requests.post")
    def test_create_ticket(self, mock_post):
        # Mock the post method of the requests module
        mock_post.return_value.status_code = 201

        # Test creating a ticket
        ticket_data = {
            "summary": "Test Summary",
            "description": "Test Description",
            "assignee": "testuser",
            "project": "TEST",
        }
        response = jira_manager.create_ticket(ticket_data)

        # Assert that the post method was called with the correct data
        mock_post.assert_called_once_with(
            url="https://your-jira-instance.com/rest/api/2/issue/",
            json={
                "fields": {
                    "summary": "Test Summary",
                    "description": "Test Description",
                    "assignee": {"name": "testuser"},
                    "project": {"key": "TEST"},
                    "issuetype": {"name": "Story"},
                }
            },
            headers={"Content-Type": "application/json"},
            auth=("api-token", "api-token"),
        )

        # Assert the response status code
        self.assertEqual(response.status_code, 201)


if __name__ == "__main__":
    unittest.main()

import json
import urllib.request
import urllib.error

class JiraManager:
    def __init__(self, jira_url, api_token):
        self.jira_url = jira_url
        self.api_token = api_token
    
    def create_ticket(self, project, summary, description, assignee=None, epic_link=None):
        # Prepare the JIRA ticket payload
        payload = {
            'fields': {
                'project': {'key': project},
                'summary': summary,
                'description': description,
                'issuetype': {'name': 'Story'}
            }
        }
        
        # Add assignee if provided
        if assignee:
            payload['fields']['assignee'] = {'name': assignee}
        
        # Add epic link if provided
        if epic_link:
            payload['fields']['customfield_10000'] = epic_link
        
        # Send a POST request to create the ticket
        try:
            req = urllib.request.Request(f'{self.jira_url}/rest/api/2/issue',
                                          data=json.dumps(payload).encode(),
                                          headers={'Content-Type': 'application/json'},
                                          method='POST')
            req.add_header('Authorization', f'Bearer {self.api_token}')
            urllib.request.urlopen(req)
            print('Ticket created successfully')
        except urllib.error.HTTPError as e:
            print(f'Failed to create ticket: {e.code} {e.reason}')
    
    def link_tickets(self, source_ticket, target_ticket, link_type):
        # Prepare the JIRA link payload
        payload = {
            'type': {'name': link_type},
            'inwardIssue': {'key': source_ticket},
            'outwardIssue': {'key': target_ticket}
        }
        
        # Send a POST request to create the link between tickets
        try:
            req = urllib.request.Request(f'{self.jira_url}/rest/api/2/issueLink',
                                          data=json.dumps(payload).encode(),
                                          headers={'Content-Type': 'application/json'},
                                          method='POST')
            req.add_header('Authorization', f'Bearer {self.api_token}')
            urllib.request.urlopen(req)
            print('Tickets linked successfully')
        except urllib.error.HTTPError as e:
            print(f'Failed to link tickets: {e.code} {e.reason}')

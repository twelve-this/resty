from typing import Protocol


class JiraAPI(Protocol):

    def __init__(self, conf) -> None:
        self.conf = conf

    def get_issue_by_key(self, key):
        """Get a Jira ticket by key"""

    def create_issue(self, body):
        """Creates a ticket in Jira"""

    def create_component(self, body):
        """Creates a component in a Jira project"""


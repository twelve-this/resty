from src.protocols.jira_api import JiraAPI


class FakeJiraApi(JiraAPI):

    def get_issue_by_key(self, key: str):
        pass
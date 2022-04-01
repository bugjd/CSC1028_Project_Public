class IntegrationLibraryInterface:
    """A blue print on how to intergrate with github and I ideas on how to intergrate with others in the future"""

    def make_github_issue(self, title: str, body: str, assignee: str, milestone: str,
                          labels: [str]) -> int:
        """A method that will allow github issues to be created by the human program. Returns issue id or -1 if
        invalid """
        pass

    def read_github_issue_assignee(self, issue_id: int) -> str:
        """Reads the  issue and returns the current assignee"""
        pass

    def read_github_issue_labels(self, issue_id: int) -> [str]:
        """Reads the  issue and returns the current labels"""
        pass

    def read_github_issue_milestone(self, issue_id: int) -> str:
        """Reads the issue and returns the current milestone"""
        pass

    def read_github_issue_title(self, issue_id: int) -> str:
        """Reads the issue and returns the current title"""
        pass

    def read_github_issue_body(self, issue_id: int) -> str:
        """Reads the issue and returns the current body"""
        pass

    def amend_github_issue(self, title: str, body: str, assignee: str, milestone: str,
                           labels: [str], issue_id: int) -> int:
        """A method to allow issues to be ammended"""
        pass

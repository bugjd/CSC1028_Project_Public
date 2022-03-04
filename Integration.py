import requests


# GitHub Documentation https://docs.github.com/en/rest/reference/issues
# Good gist I found for this sort of thing https://gist.github.com/JeffPaine/3145490

# Class current has no functionality. It needs to be implemented.
class Integration:  # The class that integrates with APIS
    def __init__(self, token, github_url):  # This class will Require the token and GitHub url
        self.token = token
        self.gitHubUrl = github_url

    def make_github_issue(self, title, body, assignee, milestone, labels):  # This method will allow GitHub issues to
        # be created.
        print("Not yet implemented" + self.gitHubUrl)

    def read_github_issue(self, title, body=None, assignee=None, milestone=None, labels=None):  # This method will
        # allow GitHub issues to be read.
        print("Not yet implemented" + self.gitHubUrl)

    def amend_github_issue(self, title, body, assignee, milestone, labels, url):  # This will append GitHub issues
        print("Not yet implemented" + self.gitHubUrl)

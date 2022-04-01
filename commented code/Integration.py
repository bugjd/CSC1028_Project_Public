# GitHub Documentation https://docs.github.com/en/rest/reference/issues
# Good gist I found for this sort of thing https://gist.github.com/JeffPaine/3145490

# Class current has no functionality. It needs to be implemented by a member of the community.
from IntegrationLibraryInterface import IntegrationLibraryInterface


class Integration(IntegrationLibraryInterface):  # The class that integrates with APIS
    def __init__(self, token, github_url):
        """The Creation of an Integration Instance"""
        self.token = token # the GitHub token. https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
        self.gitHubUrl = github_url # https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/GitHub-URL-find-use-example

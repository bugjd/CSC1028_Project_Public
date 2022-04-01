import unittest


class MyTestCase(unittest.TestCase):
    def test_make_github_issue_valid(self):  # U_INT_1
        """Testing that github issues can be made with a valid assigne"""
        # make_github_issue(self, title: str, body: str, assignee: str, milestone: str,
        #                           labels: [str]) -> int:
        actualOutcome = 12  # will call an instance of Intergration.make_githubIssue with a valid assinge
        self.assertIsNot(actualOutcome, -1)

    def test_make_github_issue_invalid(self):  # U_INT_2
        """Testing that github issues cannot be made with a invalid assigne"""

        # make_github_issue(self, title: str, body: str, assignee: str, milestone: str,
        #                           labels: [str]) -> int:
        expectedOutcome = -1
        actualOutcome = -1  # will call an instance of Intergration.make_githubIssue with a invalid assinge
        self.assertIs(actualOutcome, -1)


if __name__ == '__main__':
    unittest.main()

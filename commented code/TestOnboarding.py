import unittest


class OnBoardingTest(unittest.TestCase):
    def test_create_team_validName(self): # U_ON_1
        """Creating a team with a valid team name"""
        name = "Donkey Group"
        # acutalResult Onboard.create_team(name)
        actualResult = 12 # example of what it could be
        self.assertIsNot(actualResult, -1)

    def test_create_team_INvalidName(self): # U_ON_2
        """Creating a team with an invalid team name"""
        name = "pseudopseudohypoparathyroidism" # 30letter word.
        # acutalResult Onboard.create_team(name)
        actualResult = -1  # example of what it could be
        self.assertIs(actualResult, -1)

if __name__ == '__main__':
    unittest.main()

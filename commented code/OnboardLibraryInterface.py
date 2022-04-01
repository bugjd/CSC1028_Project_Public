# Python Interface
class OnboardLibraryInterface:
    """Creation of New Groups and Teams, Providing the onboaridng process"""

    def create_team(self, team_name: str) -> int:
        """A method to allow for the creation of the team. It will ask for a team name and provide the team ID
        number. If the team name is invalid a negative int will be returned. this method will add a team to the JSON
        file. """

        def check_team_name() -> bool:
            """A Method to check if a team name is valid nested function as will only be used when creating a team."""
            if len(team_name) <= 0 or len(team_name) > 30:
                return False
            else:
                return True

        pass

    def create_person(self, person_name: str, person_email: str, person_github_str) -> int:
        """A method to allow for the creation of a person and add them to the JSON File. If any details are incorrect
        an negative int will be provided otherwise their id will be returned """

        def check_github() -> bool:
            """Will use GitHub API to make sure person exists on github """
            pass

        def check_person_name() -> bool:
            """A Method to check if a person name is valid nested function as will only be used when creating a
            person. """
            if len(person_name) <= 0:
                return False
            else:
                return True

        def check_email() -> bool:
            """Will check if email is valid up to due if you want a basic implemntation or a more advanced such as
            checking website DNS to makesure website exists """
            pass

        pass

    def add_person_to_team(self, person_id: int, team_id: int) -> bool:
        """A method to allow a person to be added to a team. Will use check_team_valid and check_person_valid to
        check they exist. Will return true if able to add person """
        pass

    def remove_person_to_team(self, person_id: int, team_id: int) -> bool:
        """A method to allow a person to be removed to a team. Will use check_team_valid and check_person_valid to
        check they exist. Will return true if able to removed person """
        pass

    def check_team_valid(self, team_id: int) -> bool:
        """A method to check if a team is valid"""
        pass

    def check_person_valid(self, person_id: int) -> bool:
        """A method to check if a person is valid"""
        pass

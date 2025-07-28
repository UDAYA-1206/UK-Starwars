from SWAPIClient import SWAPIClient
from LoggerUtil import LoggerUtil

class UIKeywords:
    def __init__(self):
        self.logger = LoggerUtil()
        self.client = SWAPIClient()

    def verify_species_in_movie(self, api_base, title, expected_species):
        films = self.client.get_movies(api_base)
        film = next((f for f in films if f['title'] == title), None)
        if not film:
            self.logger.log_fail(f"Movie titled {title} not found")

        for species_url in film['species']:
            species_data = self.client.get_json(species_url)
            if species_data['name'] == expected_species:
                self.logger.log_pass(f"Species {expected_species} found in {title}")
                return

        self.logger.log_fail(f"Species {expected_species} NOT found in {title}")

    def verify_planet_not_in_movie(self, api_base, title, planet_name):
        films = self.client.get_movies(api_base)
        film = next((f for f in films if f['title'] == title), None)
        if not film:
            self.logger.log_fail(f"Movie titled {title} not found")

        for planet_url in film['planets']:
            planet_data = self.client.get_json(planet_url)
            if planet_data['name'] == planet_name:
                self.logger.log_fail(f"Planet {planet_name} is unexpectedly present in {title}")

        self.logger.log_pass(f"Planet {planet_name} is not present in {title} as expected")

    def verify_sorted_last_movie_title(self, api_base, expected_title):
        films = self.client.get_movies(api_base)
        sorted_titles = sorted([film['title'] for film in films])
        actual_last = sorted_titles[-1]
        if actual_last == expected_title:
            self.logger.log_pass(f"Last movie title after sort is '{expected_title}'")
        else:
            self.logger.log_fail(f"Expected '{expected_title}', but got '{actual_last}'")
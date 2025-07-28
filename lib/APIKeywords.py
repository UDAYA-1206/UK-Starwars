from SWAPIClient import SWAPIClient
from LoggerUtil import LoggerUtil

class APIKeywords:
    def __init__(self):
        self.logger = LoggerUtil()
        self.client = SWAPIClient()

    def verify_movies_count(self, api_base, expected_count):
        movies = self.client.get_movies(api_base)
        count = len(movies)
        if count == int(expected_count):
            self.logger.log_pass(f"Movies count is {count} as expected")
        else:
            self.logger.log_fail(f"Movies count is {count}, expected {expected_count}")

    def verify_movie_director(self, api_base, index, expected_director):
        movies = self.client.get_movies(api_base)
        director = movies[int(index) - 1]['director']
        if director == expected_director:
            self.logger.log_pass(f"Director is {director} as expected")
        else:
            self.logger.log_fail(f"Director is {director}, expected {expected_director}")

    def verify_producer_not_match(self, api_base, index, not_expected_producer):
        movies = self.client.get_movies(api_base)
        producers = movies[int(index) - 1]['producer']
        if producers != not_expected_producer:
            self.logger.log_pass(f"Producers do not match disallowed value: {not_expected_producer}")
        else:
            self.logger.log_fail(f"Producers matched disallowed value: {not_expected_producer}")
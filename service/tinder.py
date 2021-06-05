from repository.tinder import *


class TinderService:

    @classmethod
    def get_random_looks(self,user_id):
        return random_looks_from_db(user_id)

    @classmethod
    def get_test_looks(self, test):
        return test_looks_from_db(test)

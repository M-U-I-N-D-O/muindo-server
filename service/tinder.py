from repository.tinder import *


class TinderService:

    @classmethod
    def get_random_looks(self,user_id, item_id):
        return random_looks_from_db(user_id=user_id, item_id=item_id)

    @classmethod
    def confirm_looks(self, confirm):

        if add_confirm(confirm) != None:
            update_look_info(confirm.get('opinion') == 'like', confirm.get('id'))
            return get_confirm_info(confirm.get('id'))


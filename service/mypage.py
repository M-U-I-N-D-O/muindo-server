from repository.mypage import *
from flask import jsonify

class MyPageService:

    @classmethod
    def get_my_looks(self, user_id):
        return my_looks_from_db(user_id)

    @classmethod
    def get_my_look_detail(self, look_id):
        return my_look_detail_from_db(look_id)

    @classmethod
    def get_items_info(self, hat_id, top_id, bottom_id, shoes_id, bag_id ):
        return item_info_from_db(hat_id, top_id, bottom_id, shoes_id, bag_id)
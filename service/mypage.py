from repository.mypage import *


class MyPageService:

    @classmethod
    def get_my_looks(self, uid):
        return my_looks_from_db(uid)

    @classmethod
    def get_my_look_detail(self, look_id):
        return my_look_detail_from_db(look_id)
from repository.mypage import *


class MyPageService:

    @classmethod
    def my_looks(self, uid):
        return get_my_looks(uid)
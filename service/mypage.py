from repository.mypage import *

class MyPageService:

    @classmethod
    def get_my_looks(self, user_id):
        return my_looks_from_db(user_id)

    @classmethod
    def get_my_look_detail(self, look_id):
        look=my_look_detail_from_db(look_id)
        look_info_dict=init_look_info_dict(look)
        look_info=item_info_from_db(look_info_dict)
        look_info["my_look"]=look
        return look_info

    @classmethod
    def get_my_thumbs(self, user_id=None, look_id=None):
        if look_id == '':
            look_id = None
        return get_thumbs(user_id, look_id)


def init_look_info_dict(look):
    look_info_dict = {}
    look_info_dict["hat_id"] = look.hat
    look_info_dict["top_id"] = look.top
    look_info_dict["bottom_id"] = look.bottom
    look_info_dict["shoes_id"] = look.shoes
    look_info_dict["bag_id"] = look.bag
    return look_info_dict
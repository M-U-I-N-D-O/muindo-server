from repository import look
from flask_jwt_extended import get_jwt
from serializers.look import LookSchema


class ItemService:

    @classmethod
    def check_none(self, data):

        if data == '':
            return None

        return data

    @classmethod
    def get_musinsa_items(self, filter):

        middlecategory = self.check_none(filter.get('middlecategory'))
        subcategory = self.check_none(filter.get('subcategory'))
        brand = self.check_none(filter.get('brand'))
        type = filter.get('type')
        itemid = self.check_none(filter.get('itemid'))
        userid = filter.get('userid')

        if not middlecategory and not subcategory:
            from utils import category_dict
            middlecategory = category_dict.get(type)


        return look.get_items(middlecategory, subcategory, brand, itemid, userid)




class LookService:


    @classmethod
    def upload_look(self, request):
        from azure.storage.blob import BlobClient
        from datetime import datetime
        import base64

        # imgdata = base64.b64decode(request.get('data').get('img'))
        #
        # blob = BlobClient.from_connection_string(
        #     conn_str='DefaultEndpointsProtocol=https;AccountName=sherlockodds;AccountKey=RIlkLeL57ZPdy3umfCGh6UjQIcdm7bRs3buFNrKiCOLlynk7T/ljVwVJI+RFZQtkW9GrAlx0zbrJfylATzS1fg==;EndpointSuffix=core.windows.net',
        #     container_name='look',
        #     blob_name=datetime.now().__str__()+'.jpg')
        #
        # blob.upload_blob(imgdata)

        items = request.get('items')
        items['url'] = ''
        items['userid'] = get_jwt()['sub']
        newlook = look.add_look(items)

        return newlook

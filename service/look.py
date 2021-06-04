from repository import look
from flask_jwt_extended import get_jwt


class ItemService:


    @classmethod
    def get_musinsa_items(self, middlecategory, subcategory, brand, type):

        from utils import category_dict
        middlecategory = category_dict.get(type)[0]
        results = look.get_items(middlecategory=middlecategory, subcategory=subcategory, brand=brand)
        return results

class LookService:

    @classmethod
    def upload_look_azure(self, request):
        from azure.storage.blob import BlobClient
        from datetime import datetime
        import base64

        imgdata = base64.b64decode(request.get('data').get('img'))

        blob = BlobClient.from_connection_string(
            conn_str='DefaultEndpointsProtocol=https;AccountName=sherlockodds;AccountKey=RIlkLeL57ZPdy3umfCGh6UjQIcdm7bRs3buFNrKiCOLlynk7T/ljVwVJI+RFZQtkW9GrAlx0zbrJfylATzS1fg==;EndpointSuffix=core.windows.net',
            container_name='look',
            blob_name=datetime.now().__str__()+'.jpg')

        blob.upload_blob(imgdata)

        items = request.get('items')
        items['userid'] = get_jwt()['sub']
        items['url'] = blob.url

        return look.add_look(items)

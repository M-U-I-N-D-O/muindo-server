from repository import look


class ItemService:


    @classmethod
    def get_musinsa_items(self, middlecategory, subcategory, brand, type):
        results = look.get_items(middlecategory=middlecategory, subcategory=subcategory, brand=brand)
        return results

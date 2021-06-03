from repository import look


class ItemService:


    @classmethod
    def get_musinsa_items(self, query:dict):
        results = look.get_items(middlecategory=query.get('middlecategory'), subcategory=query.get('subcatebory'), brand=query.get('brand'))
        return results

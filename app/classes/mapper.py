import json

class Mapper:

    def __init__(self, actc_type):
        with open("models/mappers/actc_mapper.json") as file:
            self.mapper = json.loads(file.read())
            self.mapper = {value: key for key, value in self.mapper.items()}

    def get_map(self):
        return self.mapper

    def map_item(self, item):
        return self.mapper[item]

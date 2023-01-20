import json

class Config:

    CONFIG_NAME = 'config.json'

    @staticmethod
    def read_property(property):
        f = open(Config.CONFIG_NAME)
        data = json.load(f)
        f.close()
        return data[property]
        
import os
import json
import yaml


PARSERS = {
    '.yaml': YAMLParser,
    '.yml': YAMLParser,
    '.json': JSONParser}


class ConfigFactory: # основная фабрика принимает путь 
    # получет расширение и вызывает нужный класс для обработки согласно ему
    def factory(filepath):
        _, extension = os.path.splitext(filepath)
        raw_data = open(filepath).read()
        parser = PARSERS[extension]().get_parse(raw_data) # не забываем скобки иначе класс не вызовется
        return Config(parser) # возвращает новый экземпляр класса
    
class JSONParser:
    def get_parse(self, data):
        self.data = json.loads(data)
        return self.data
    
class YAMLParser:
    def get_parse(self, data):
        self.data = yaml.safe_load(data)
        return self.data
    
class Config:
    def __init__(self, data=None):
        if data is None:
            data = {}
        self.data = data

    def get_value(self, key):
        result = self.data[key]
        if isinstance(result, dict):
            return Config(result)
        return result

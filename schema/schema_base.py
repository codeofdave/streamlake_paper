import csv

class SchemaBase:
    def __init__(self):
        pass
    def get_schema(self, file_path=None, file_type='xlsx'):
        with open(file_path,'r') as file:



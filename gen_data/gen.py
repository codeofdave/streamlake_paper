from schema import http_schema
from init.config import g_config
class Http:
    def __init__(self):
        gen_config = g_config.get('gen')
        self.file_path = gen_config.get('file_path')
        self.size_mb = gen_config.get('size_mb')
        self.
    def gen_data(self):
        data_frame =
        with open(self.file, 'w') as f:
            f.write()

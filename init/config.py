import yaml
import os


class Config:
    def __init__(self):
        self.config_file = os.path.dirname(os.path.dirname(__file__)) + '/config.yaml'

    def parse_config(self):
        with open(self.config_file, 'r', encoding='utf-8') as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)


# global config
g_config = Config().parse_config()

import sys

from schema import http_schema
from init.config import g_config
from concurrent.futures import ThreadPoolExecutor
from init.log import log
from loguru import logger

PROTOCOLS = ['http_protocol', 'g_protocol', 'dns_protocol', 'email_protocol', 'ftp_protocol']


class Generator:
    def __init__(self):
        self.gen_config = g_config.get('gen')
        self.file_path = self.gen_config.get('file_path')
        self.size_mb = self.gen_config.get('size_mb')
        self.max_size_mb_per_file = self.gen_config.get('max_size_mb_per_file')
        self.protocols = [p for p in self.gen_config.keys() if 'protocol' in p]
        self.tp = ThreadPoolExecutor(max_workers=len(self.protocols))
        for proto in self.protocols:
            if proto not in PROTOCOLS:
                log.error('found unsupported protocol %s', proto)
                sys.exit(1)

        print(self.file_path)
        print(self.size_mb)
        print(self.max_size_mb_per_file)
        print(self.protocols)

    def gen_data(self):
        for proto in self.protocols:
            pass
            # self.tp.map()

    def worker(self, protocol):
        default_file_path = self.gen_config.get('file_path')
        default_size_mb = self.gen_config.get('size_mb')
        file_path = self.gen_config.get(protocol).get('file_path', default_file_path)
        size_mb = self.gen_config.get(protocol).get('size_mb', default_size_mb)
        if not file_path:
            log.error('file path not set')
            sys.exit(1)
        if not size_mb:
            log.error('file size not set')
        if 'http_protocol' == protocol:
            self.gen_config.get(protocol)


generator = Generator()
generator.gen_data()

from schema.schema_base import SchemaBase
from random import randint, choice

BASE_STR = '0123456789abcdefghijklmnopqrstuvwxyz'


class HttpSchema(SchemaBase):
    def __init__(self):
        super().__init__()
        self.HTTPVersion = randint(1, 3)
        self.MessageType = randint(1, 8)
        self.MessageStatus = randint(-200, 200)
        self.FirstHTTPResponseTime = randint(0, 10000)
        self.LastContentPacketTime = randint(0, 10000)
        self.LastACKTime = randint(0, 10000)
        self.HOSTLength = randint(1, 64)
        self.HOST = '%s.%s.com' % (''.join([choice(BASE_STR) for i in range(randint(2, 8))]),
                                   ''.join([choice(BASE_STR) for i in range(randint(2, 4))]))
        self.URILength = randint(1, 128)
        self.URI = 'http://%s.%s.com/?user=%s&request=%s' % (''.join([choice(BASE_STR) for i in range(randint(2, 8))]),
                                                             ''.join([choice(BASE_STR) for i in range(randint(2, 4))]),
                                                             ''.join([choice(BASE_STR) for i in range(randint(4, 12))]),
                                                             ''.join([choice(BASE_STR) for i in range(randint(1, 4))]))
        self.X_Online_HostLength = randint(0, 4)
        self.X_Online_Host = choice(['head1', 'head2', 'head3', 'head4'])
        self.User_AgentLength = randint(16, 32)
        self.User_Agent = choice(['Iphone-%s' % ''.join([choice(BASE_STR) for i in range(randint(2, 8))]),
                                  'Windows-%s' % ''.join([choice(BASE_STR) for i in range(randint(2, 8))]),
                                  'Mac-%s' % ''.join([choice(BASE_STR) for i in range(randint(2, 8))]),
                                  'Android-%s' % ''.join([choice(BASE_STR) for i in range(randint(2, 8))])])
        self.HTTP_content_type = ''
        self.refer_URILength = randint(32, 128)
        self.refer_URI = 'http://%s.%s.com/?user=%s&request=%s' % (
            ''.join([choice(BASE_STR) for i in range(randint(2, 8))]),
            ''.join([choice(BASE_STR) for i in range(randint(2, 4))]),
            ''.join([choice(BASE_STR) for i in range(randint(4, 12))]),
            ''.join([choice(BASE_STR) for i in range(randint(1, 4))]))
        self.CookieLength = randint(32, 128)
        self.Cookie = ''.join([choice(BASE_STR) for i in range(randint(2, 16))])
        self.Content_Length = randint(32, 128)
        self.keyword = ''.join([choice(BASE_STR) for i in range(randint(2, 8))])
        self.ServiceBehaviorFlag = choice([1, 2, 3, 4])
        self.ServiceCompFlag = choice([1, 2, 3, 4])
        self.ServiceTime = randint(0, 1000)
        self.IE = choice([0, 1])
        self.Portal = choice([0, 1])
        self.Locationlength = randint(32, 128)
        self.location = randint(1000, 9999)
        self.firstrequest = choice([0, 1])
        self.Useraccount = ''.join([choice(BASE_STR) for i in range(randint(4, 12))])
        self.URItype = randint(1, 32)
        self.URIsub_type = randint(1, 32)


import json

x = HttpSchema()
print(json.dumps(x.__dict__))

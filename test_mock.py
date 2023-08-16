from urllib.parse import urlparse, parse_qs


URL1 = 'https://google.com:80?a=b&c=d&lala=value'

class Url:
    def __init__(self, adress):
        self.adress = urlparse(adress)

    def get_scheme(self):
        return self.adress[0]

    def get_hostname(self):
        hostname = self.adress[1]
        if hostname.endswith(":80"):
            hostname = hostname[:-3]
            return hostname
        return hostname

    def get_query_params(self):
        return parse_qs(self.adress.query)
       
    
    def get_query_param(self, key, val=None):
        aa = parse_qs(self.adress.query)
        return str(aa.get(key, val))
    
    def __eq__(self, other):
        pass
    
c = Url(URL1)

# print(c.adress)
# print(c.get_hostname())
# print(c.get_scheme())
# print(c.get_query_params())
print(c.get_query_param('key'))
# print(c.get_query_param('key2', 'lala'))
# print(c.get_query_param('new', 'ehu'))


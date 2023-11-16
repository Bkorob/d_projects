from urllib.parse import urlparse, parse_qs


# BEGIN (write your solution here)
class Url:
    def __init__(self, sequence):
        self.seq = sequence
        self._url = urlparse(self.seq)
        self._params = self.seq.split('?')[1]

    def get_scheme(self):
        return self._url.scheme
    
    def get_hostname(self):
        return self._url.hostname
    
    def get_query_params(self):
        self.params = parse_qs(self._params)
        return self.params
    
    def get_query_param(self, key, val=None):
        return self.params.get(key, val)[0]
    
url = Url('http://hexlet.io:80?key=value&key2=value2')
# print(url.get_scheme())
# print(url.get_hostname())
print(url.get_query_params())
print(url.get_query_param('key2'))
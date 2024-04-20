import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('Não foi possível acessar')
else:
    print('Foi possível acessar o site')
    print(site.read())

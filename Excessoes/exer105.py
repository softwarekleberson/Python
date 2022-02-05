from copy import error
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.facebook.com')
    
except:
    print('site indisponivel ')

else:
    print('Site está online')
    print('Esse é o html do site')
    print(site.read())
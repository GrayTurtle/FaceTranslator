

import urllib.request
from urllib.error import HTTPError, URLError


# Function that downloads a file
def downloadFile(file_name, file_mode, base_url):
    # Create the url
    url = base_url + file_name + "/picture?type=large"

    # Open the url
    try:
            f = urllib.request.urlopen(url)
            print("downloading ", url)

            # Open our local file for writing
            local_file = open(file_name+".jpg", "w" + file_mode)
            local_file.write(f.read())
            local_file.close()

    # Handle errors
    except HTTPError as e:
            print("HTTP Error:", e.code, url)
    except URLError as e:
            print("URL Error:", e.reason, url)

profile = 100002630705962
base_url = 'https://graph.facebook.com/'
s_index = str(profile)
file_name = s_index
# Now download the image. b for binary
downloadFile(file_name, "b", base_url)

'''

import httplib
import urllib2
import requests
conn = httplib.HTTPConnection("graph.facebook.com")
conn.request("GET", "/v2.10/5500958/picture")
r1 = conn.getresponse()
print r1.status, r1.reason
data1 = r1.read()
print data1
conn.close()
'''

'''
import urllib.request
import simplejson

def getProfilePicUrl(user_id):
 api_query = urllib.urlopen('https://graph.facebook.com/'+user_id)
 dict = simplejson.loads(api_query.read())
 print dict
 return dict['picture']

pic_url = getProfilePicUrl('5500958/picture')
pic = urllib.urlopen(pic_url) # retrieve the picture
f = open("cocacola.jpg","wb")
f.write(pic.read()) # save the pic
f.close()

'''

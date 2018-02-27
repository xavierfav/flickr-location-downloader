import os
from pprint import pprint
import urllib
from flickrapi import FlickrAPI


flickrAPIKey = "14bdd7814d1209def7a960b39bd664d1"  # API key
flickrSecret = "3c5380fc67816b66"                  # shared "secret"
IMG_FOLDER = 'photos/'

if not os.path.exists(IMG_FOLDER):
    os.makedirs(IMG_FOLDER)


flickr = FlickrAPI(flickrAPIKey, flickrSecret, format='parsed-json')

# Search images around Tibidabo
bbox = "2.110685, 41.416910, 2.127851, 41.433900"
extras = "tags, original_format, license, geo, date_taken, date_upload, o_dims, views, url_m"
res = flickr.photos.search(text='', per_page=10, extras=extras, bbox=bbox)

photos = res['photos']['photo']
pprint(photos)

for count, photo in enumerate(photos):
    try:
        url=photo['url_m']
        print(url)
        count += 1
        urllib.urlretrieve(url,  IMG_FOLDER + str(count) +".jpg")
    except Exception as e:
        print(e, 'Download failure')

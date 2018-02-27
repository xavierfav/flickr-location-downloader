# Retrieve Flickr images by location

## Install
- Create a virtual environment and install requirements - *e.g.* with [Virtualenv](https://virtualenv.pypa.io/en/stable/):
 ```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt 

 ```

## How to
- The *old/* folder contains a script that was used for retrieving photos (cannot find the Python API client that was used).
- The *get_images.py* script retrieves and downloads images.
- The bbox variable should be set to the according location box (see the [flickir api photos search documentation](https://www.flickr.com/services/api/flickr.photos.search.html) and get the location value - *e.g.* using [this web tool](https://www.latlong.net/)).
- Run the script:
 ```
python get_images.py
 ```

## TODO
- Save metadata of the retrieved photos.
- Iterate through pages and download all photos.
- Give a way to specify several bbox location for allowing to retrieve images from precise locations.

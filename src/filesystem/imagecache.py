import os.path
import shutil
import requests


class ImageCache:
    def __init__(self, cache_dir):
        self.cache_dir = cache_dir
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)

    def get_image(self, url, image_type):
        image_filename = os.path.join(self.cache_dir, url.replace('/', '_'))

        url = f"https:{url}"
        url = url.replace("thumb", image_type)

        if not os.path.exists(image_filename):
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(image_filename, 'wb') as out_file:
                    shutil.copyfileobj(response.raw, out_file)
                del response

        return image_filename

import json

with open('sample_diction.json') as f:
    diction_string = f.read()

flickr_response = json.loads(diction_string)
photo_diction = flickr_response['photo']

class Photo:
    def __init__(self, photo):
        pass

Photo(photo_diction)

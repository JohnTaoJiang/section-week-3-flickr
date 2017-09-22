import json

with open('sample_diction.json') as f:
    diction_string = f.read()

flickr_response = json.loads(diction_string)

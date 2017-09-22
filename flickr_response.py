import json

with open('sample_diction.json') as f:  # with clause: file is closed automaticlly
    diction_string = f.read()

flickr_response = json.loads(diction_string)
photo_diction = flickr_response['photo']


class Photo(object):

    def __init__(self, photo):
        self.username = photo['owner']['username']

        self.tags = []
        for tag_dict in photo['tags']['tag']:
            self.tags.append(tag_dict['_content'])
        print(self.tags)

        self.id = photo['id']
        self.title = photo['title']['_content']
        self.url = photo['urls']['url'][0]['_content']

    def __str__(self):
        return '{0} by {1} ({0})'.format(self.title, self.username)

    def __repr__(self):
        return """Title: {0}
Author: {1}
URL: {2}
ID: {3}""".format(self.title, self.username, self.url, self.id)

    def __contains__(self, tag_name):
        # if 'string x' in object: do something
        result = tag_name in self.tags
        return result


pd = Photo(photo_diction)
# or print(str(pd)) Note that str() method is called by default
print("__str__\n", pd)
print("__repr__\n", repr(pd))  # or print(pd.__repr__())

if 'nature' in pd:
    print('Yes!')

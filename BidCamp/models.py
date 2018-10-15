from mongoengine import *
from BidCampProject.settings import DBNAME
connect(DBNAME)

class User(Document):
    #userName = StringField(required=True)
    #PhoneNumber = StringField(max_length=50, required=True)
    email = StringField(max_length=128, required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)

class Post(Document):
     title = StringField(max_length=128, required=True)
     content  = StringField(max_length=500, required= True)
     last_update = DateTimeField(required=True)
     author = ReferenceField(User, reverse_delete_rule=CASCADE)
     tags = ListField(StringField(max_length=30))
     comments = ListField(EmbeddedDocumentField(Comment))
     meta = {'allow_inheritance': True}


class TextPost(Post):
    content = StringField()

class ImagePost(Post):
    image_path = StringField()

class LinkPost(Post):
    link_url = StringField()


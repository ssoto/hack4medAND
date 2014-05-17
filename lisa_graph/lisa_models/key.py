from mongoengine import *

class Key_Model (Document):
	name = StringField(required=True)

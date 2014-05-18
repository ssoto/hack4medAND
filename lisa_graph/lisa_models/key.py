from mongoengine import *

class Key_Model (Document):
	name = StringField(unique=True)

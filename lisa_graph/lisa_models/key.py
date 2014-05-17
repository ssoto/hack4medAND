from mongoengine import *

class Key_Model (EmbeddedDocument):
	name = StringField()

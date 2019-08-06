import mongoengine


class Dialogue(Document):
    user = StringField(max_length=50)
    message = StringField()
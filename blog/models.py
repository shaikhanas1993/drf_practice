from django.db import models

# Create your models here.


class Comment:
    def __init__(self, email, username):
        self.email = email
        self.username = username

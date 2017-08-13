from django.db import models
from django.utils import timezone
import json

class User(models.Model):
    username = models.CharField(max_length=200)
    friend_update_date = models.DateTimeField('date when friend list is updated ')
    friend_list = models.CharField(max_length=1000)

    def set_friend_list(self, friend_list_json):
        self.friend_update_date = timezone.now()
        self.friend_list_json = json.dumps(friend_list_json)

    def get_friend_list(self):
        return json.loads(self.friend_list)

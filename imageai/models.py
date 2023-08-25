from django.db import models
from users.models import User

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class ImageModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="all_identify_requests")
    identify_object = models.CharField(max_length=255)
    inputted_image = models.ImageField(upload_to=upload_to,)
    input_image = models.CharField(max_length=255, null=True, blank=True)
    analysed_image = models.CharField(max_length=255, null=True, blank=True)
    result = models.CharField(max_length=255, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

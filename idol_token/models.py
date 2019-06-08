from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Idol(models.Model):
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 255)
    image = CloudinaryField('image', blank=True, null=True,)
    construct_id = models.CharField(max_length = 250, null=True, blank=True)

    def __str__(self):
        return "({0}): {1}".format(self.id, self.name)

class Idol_Item(models.Model):
    title = models.CharField(max_length = 50)
    idol = models.ForeignKey(Idol, on_delete = models.CASCADE)
    contents = models.CharField(max_length = 250, null = True, blank = True)
    price = models.IntegerField(default = 0)
    image = CloudinaryField('image', blank=True, null=True,)
    total_issue_value = models.IntegerField(default = 0)

    def __str__(self):
        return "({0}){1}, price: {2}, toral_issue_value: {3} by [{4}]".format(self.id, self.contents, self.price, self.total_issue_value, self.idol)

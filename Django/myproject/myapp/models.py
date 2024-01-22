from django.db import models

# Create your models here.
# python manage.py makemigrations    :-: to create model feature/database/save changes
# python manage.py migrate :-: to save changes(more like push origin after commiting in github)
# python manage.py createsuperuser :-:  to create admin/user
class Feature(models.Model):
    ## id: int   # now we are inherhinting models.Model we don't need id as it will automatically assign id's
    ## name: str  # instead
    ## details: str
    name = models.CharField(max_length = 20)
    details = models.CharField(max_length = 500)

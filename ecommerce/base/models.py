from django.db import models
import uuid

# Create your models here.

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key = True , editable = False , default = uuid.uuid4)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True
        # db_table = ''
        # managed = True
        # verbose_name = 'ModelName'
        # verbose_name_plural = 'ModelNames'
    

    # def __str__(self):
    #     return 

    # def __unicode__(self):
    #     return 
                                       
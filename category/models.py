from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
# Create your models here.

def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)


class Category(models.Model):
    category_name=models.CharField(_('category_name'),max_length=255,blank=True,null=True)
    class Meta:
        ordering = ["-id"]

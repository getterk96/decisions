from django.db import models
from codex.baseerror import LogicError

class Journal(models.Model):
    content = models.TextField()
    date = models.DateTimeField(db_index=True)

    evalution = models.IntegerField()
    Excellent = 0
    Good = 1
    Soso = 2
    Disgusting = 3

    def safe_get(**args):
        try:
            Journal.objects.get(args)
        except:
            raise LogicError("No Such Journal")

# Create your models here.

import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=True)

    class Meta:
        abstract = True

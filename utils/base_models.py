import uuid

import django
from django.db import models
from django.utils import timezone

# Ensure django is setup before calling models
django.setup()


class BaseModel(models.Model):


    indexing_id = models.AutoField(primary_key=True)

    # uuid4 field for retrieval, this field should also be indexed
    uid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.UUIDField(blank=True, null=True)

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)
    deleted_by = models.UUIDField(blank=True, null=True)
    is_active = models.BooleanField(default=True)


    class Meta:
        abstract = True

    def soft_delete(self, deleted_by: uuid.UUID):
        """
        :param deleted_by: user performing deletion
        perform deletion by setting is_deleted flag to True
        """
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.deleted_by = deleted_by
        self.save()

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False


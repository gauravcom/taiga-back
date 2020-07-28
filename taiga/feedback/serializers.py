from taiga.base.api import serializers
from . import models


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FeedbackEntry
        fields = ['id', 'full_name', 'email', 'comment', 'created_date']

from .models import Homesforsale
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import *

class SalesDocumentSerializer(DocumentSerializer):
    class Meta:
        model = Homesforsale
        document = SalesDocument

        fields = {'address', 'city', 'beds', 'bathrooms', 'id', 'description'}

        def get_location(self, obj):
            try:
                return obj.location.to_dict()
            except:
                return {}
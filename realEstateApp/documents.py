from django_elasticsearch_dsl import (
    Document, fields, Index
)

from .models import Homesforsale

PUBLISHER_INDEX = Index('elastic_demo')

PUBLISHER_INDEX.settings (
    number_of_shards = 1,
    number_of_replicas = 1
)

@PUBLISHER_INDEX.doc_type
class SalesDocument(Document):

    id = fields.TextField(
        fields = {
            "raw" : {
                "type" : 'keyword'
            }
        }
    )

    address = fields.TextField(
        fields = {
            "raw" : {
                "type" : 'keyword'
            }
        }
    )

    city = fields.TextField(
        fields = {
            "raw" : {
                "type" : 'keyword'
            }
        }
    )

    beds = fields.TextField(
        fields = {
            "raw" : {
                "type" : 'keyword'
            }
        }
    )

    bathrooms = fields.TextField(
        fields = {
            "raw" : {
                "type" : 'keyword'
            }
        }
    )

    description = fields.TextField(
        fields = {
            "raw" : {
                "type" : 'keyword'
            }
        }
    )

    class Django(object):
        model = Homesforsale
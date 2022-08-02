from rest_framework.serializers import ModelSerializer, IntegerField

from opendata.models import Opendata, OpendataAttachments, OpendataAttachmentsFiles


class OpendataListSerializer(ModelSerializer):
    files_count = IntegerField()

    class Meta:
        model = Opendata
        fields = ['slug', 'title', 'link', 'files_count',
                  'xml_link', 'csv_link', 'json_link', 'xls_link', 'rdf_link']


class OpendataAttachmentsFilesSerializer(ModelSerializer):

    class Meta:
        model = OpendataAttachmentsFiles
        fields = ['name', 'file']


class OpendataAttachmentsSerializer(ModelSerializer):
    files = OpendataAttachmentsFilesSerializer(many=True, read_only=True)
    files_count = IntegerField()

    class Meta:
        model = OpendataAttachments
        fields = ['title', 'files']

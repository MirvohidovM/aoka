from rest_framework.serializers import ModelSerializer, IntegerField


from opendata.models import Opendata, OpendataAttachments


class OpendataAttachmentsSerializer(ModelSerializer):

    class Meta:
        model = OpendataAttachments
        fields = ['name', 'file']


class OpendataListSerializer(ModelSerializer):
    files_count = IntegerField()
    attachments = OpendataAttachmentsSerializer(many=True, read_only=True)

    class Meta:
        model = Opendata
        fields = ['slug', 'title', 'link', 'files_count', 'attachments',
                  'xml_link', 'csv_link', 'json_link', 'xls_link', 'rdf_link']


class OpendataDetailSerializer(ModelSerializer):
    attachments = OpendataAttachmentsSerializer(many=True, read_only=True)
    files_count = IntegerField()

    class Meta:
        model = Opendata
        fields = ['title', 'link', 'files_count', 'attachments',
                  'xml_link', 'csv_link', 'json_link', 'xls_link', 'rdf_link']

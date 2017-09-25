from rest_framework import serializers
from shop.models import *


class SiteClassSerializer(serializers.Serializer):
    class_id = serializers.IntegerField(read_only=True)
    class_name = serializers.CharField(required=True, max_length=32)
    class_info = serializers.CharField(required=False, allow_blank=True, max_length=128)

    def create(self, validated_data):
        return SiteClass.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.class_name = validated_data.get("class_name", instance.class_name)
        instance.class_info = validated_data.get("class_info", instance.class_info)
        instance.save()
        return instance


class PortalSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortalSite
        fields = ('id', 'name')


class WebSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebSite
        fields = ('id', 'name', 'star', 'example', 'price', 'status', 'remark', 'has_phone', 'has_IM', 'has_link',
                    'portal_site', 'site_class', 'success_rate', 'area')       

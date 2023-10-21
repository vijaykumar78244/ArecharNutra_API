from rest_framework import serializers
from .models import *

class WhoAreWeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhoAreWeModel
        fields = '__all__'


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificationModel
        fields = '__all__'


class FeaturedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedImageModel
        fields = '__all__'
        
        
class SocialResponsibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialResponsibilityModel
        fields = '__all__'
        
class SocialMediaURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaURLModel
        fields = '__all__'
               
class ParentSerializer(serializers.Serializer):
    WhoAreWeModel_data = WhoAreWeSerializer(many=True)
    Certification_data = CertificationSerializer(many=True)
    FeaturedImage_data = FeaturedImageSerializer(many=True)
    SocialResponsibility_data = SocialResponsibilitySerializer(many=True)
    SocialMediaURL_data = SocialMediaURLSerializer(many=True)

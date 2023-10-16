from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


class WhoAreWeList(APIView):
    def get(self, request):
        who_are_we_list = WhoAreWeModel.objects.all()
        serializer = WhoAreWeSerializer(who_are_we_list, many=True)
        return Response(serializer.data)

class WhoAreWeDetail(APIView):
    def get_object(self, pk):
        try:
            return WhoAreWeModel.objects.get(pk=pk)
        except WhoAreWeModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        who_are_we_details = self.get_object(pk)
        serializer = WhoAreWeSerializer(who_are_we_details)
        return Response(serializer.data)


class CertificationList(APIView):
    def get(self, request):
        certifications = CertificationModel.objects.all()
        serializer = CertificationSerializer(certifications, many=True)
        return Response(serializer.data)


class CertificationDetail(APIView):
    def get_object(self, pk):
        try:
            return CertificationModel.objects.get(pk=pk)
        except CertificationModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        certification = self.get_object(pk)
        serializer = CertificationSerializer(certification)
        return Response(serializer.data)


class FeaturedImageList(APIView):
    def get(self, request):
        featured_images = FeaturedImageModel.objects.all()
        serializer = FeaturedImageSerializer(featured_images, many=True)
        return Response(serializer.data)

class FeaturedImageDetail(APIView):
    def get_object(self, pk):
        try:
            return FeaturedImageModel.objects.get(pk=pk)
        except FeaturedImageModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        featured_image = self.get_object(pk)
        serializer = FeaturedImageSerializer(featured_image)
        return Response(serializer.data)
    
class SocialResponsibilityList(APIView):
    def get(self, request):
        social_responsibility_list = SocialResponsibilityModel.objects.all()
        serializer = SocialResponsibilitySerializer(social_responsibility_list, many=True)
        return Response(serializer.data)

class SocialResponsibilityDetail(APIView):
    def get_object(self, pk):
        try:
            return SocialResponsibilityModel.objects.get(pk=pk)
        except SocialResponsibilityModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        social_responsibility_details = self.get_object(pk)
        serializer = SocialResponsibilitySerializer(social_responsibility_details)
        return Response(serializer.data)

class SocialMediaURLList(APIView):
    def get(self, request):
        social_media_url_list = SocialMediaURLModel.objects.all()
        serializer = SocialMediaURLSerializer(social_media_url_list, many=True)
        return Response(serializer.data)

class SocialMediaURLDetail(APIView):
    def get_object(self, pk):
        try:
            return SocialMediaURLModel.objects.get(pk=pk)
        except SocialMediaURLModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        social_media_url_details = self.get_object(pk)
        serializer = SocialMediaURLSerializer(social_media_url_details)
        return Response(serializer.data)



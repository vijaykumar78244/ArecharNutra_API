from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *




class WhoAreWeList(APIView):
    def get(self, request):
        who_are_we_list = WhoAreWeModel.objects.all()
        who_are_we_data = WhoAreWeSerializer(who_are_we_list, many=True).data

        response_data = {
            "response_code": "success",
            "http_status_code": 200,
            "context": {
                "success": {
                    "who_are_we_list": who_are_we_data
                }
            },
            "message": "OK",
        }
        return Response(response_data)

class WhoAreWeDetail(APIView):
    def get_object(self, pk):
        try:
            return WhoAreWeModel.objects.get(pk=pk)
        except WhoAreWeModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        try:
            who_are_we_details = self.get_object(pk)
            who_are_we_data = WhoAreWeSerializer(who_are_we_details).data

            response_data = {
                "response_code": "success",
                "http_status_code": 200,
                "context": {
                    "success": {
                        "who_are_we_detail": who_are_we_data
                    }
                },
                "message": "OK",
            }

            return Response(response_data)
        except WhoAreWeModel.DoesNotExist:
            return Response({"error": "Who Are We data not found."}, status=404)

class CertificationList(APIView):
    def get(self, request):
        certifications = CertificationModel.objects.all()
        certifications_data = CertificationSerializer(certifications, many=True).data

        response_data = {
            "response_code": "success",
            "http_status_code": 200,
            "context": {
                "success": {
                    "certification_list": certifications_data
                }
            },
            "message": "OK",
        }

        return Response(response_data)

class CertificationDetail(APIView):
    def get_object(self, pk):
        try:
            return CertificationModel.objects.get(pk=pk)
        except CertificationModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        try:
            certification = self.get_object(pk)
            certification_data = CertificationSerializer(certification).data

            response_data = {
                "response_code": "success",
                "http_status_code": 200,
                "context": {
                    "success": {
                        "certification_detail": certification_data
                    }
                },
                "message": "OK",
            }

            return Response(response_data)
        except CertificationModel.DoesNotExist:
            return Response({"error": "Certification data not found."}, status=404)

class FeaturedImageList(APIView):
    def get(self, request):
        featured_images = FeaturedImageModel.objects.all()
        featured_images_data = FeaturedImageSerializer(featured_images, many=True).data

        response_data = {
            "response_code": "success",
            "http_status_code": 200,
            "context": {
                "success": {
                    "featured_image_list": featured_images_data
                }
            },
            "message": "OK",
        }

        return Response(response_data)

class FeaturedImageDetail(APIView):
    def get_object(self, pk):
        try:
            return FeaturedImageModel.objects.get(pk=pk)
        except FeaturedImageModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        try:
            featured_image = self.get_object(pk)
            featured_image_data = FeaturedImageSerializer(featured_image).data

            response_data = {
                "response_code": "success",
                "http_status_code": 200,
                "context": {
                    "success": {
                        "featured_image_detail": featured_image_data
                    }
                },
                "message": "OK",
            }

            return Response(response_data)
        except FeaturedImageModel.DoesNotExist:
            return Response({"error": "Featured Image not found."}, status=404)
    


class SocialResponsibilityList(APIView):
    def get(self, request):
        social_responsibility_list = SocialResponsibilityModel.objects.all()
        social_responsibility_data = SocialResponsibilitySerializer(social_responsibility_list, many=True).data

        response_data = {
            "response_code": "success",
            "http_status_code": 200,
            "context": {
                "success": {
                    "social_responsibility_list": social_responsibility_data
                }
            },
            "message": "OK",
        }
        
        return Response(response_data)


class SocialResponsibilityDetail(APIView):
    def get_object(self, pk):
        try:
            return SocialResponsibilityModel.objects.get(pk=pk)
        except SocialResponsibilityModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        try:
            social_responsibility = self.get_object(pk)
            social_responsibility_data = SocialResponsibilitySerializer(social_responsibility).data
            response_data = {
                "response_code": "success",
                "http_status_code": 200,
                "context": {
                    "success": {
                        "social_responsibility": social_responsibility_data
                    }
                },
                "message": "OK",
            }
            
            return Response(response_data)
        except SocialResponsibilityModel.DoesNotExist:
            return Response({"error": "Social Responsibility data not found."}, status=404)

    def get(self, request, pk):
        social_responsibility_details = self.get_object(pk)
        serializer = SocialResponsibilitySerializer(social_responsibility_details)
        return Response(serializer.data)

class SocialMediaURLList(APIView):
    def get(self, request):
        social_media_url_list = SocialMediaURLModel.objects.all()
        social_media_url_data = SocialMediaURLSerializer(social_media_url_list, many=True).data

        response_data = {
            "response_code": "success",
            "http_status_code": 200,
            "context": {
                "success": {
                    "social_media_url_list": social_media_url_data
                }
            },
            "message": "OK",
        }

        return Response(response_data)

class SocialMediaURLDetail(APIView):
    def get_object(self, pk):
        try:
            return SocialMediaURLModel.objects.get(pk=pk)
        except SocialMediaURLModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        try:
            social_media_url = self.get_object(pk)
            social_media_url_data = SocialMediaURLSerializer(social_media_url).data

            response_data = {
                "response_code": "success",
                "http_status_code": 200,
                "context": {
                    "success": {
                        "social_media_url_details": social_media_url_data
                    }
                },
                "message": "OK",
            }

            return Response(response_data)
        except SocialMediaURLModel.DoesNotExist:
            return Response({"error": "Social Media URL not found."}, status=404)


class NestedDataView(APIView):
    def get(self, request):
        who_are_we_data = WhoAreWeModel.objects.all()
        certification_data = CertificationModel.objects.all()
        featured_image_data = FeaturedImageModel.objects.all()
        social_responsibility_data = SocialResponsibilityModel.objects.all()
        social_media_url_data = SocialMediaURLModel.objects.all()

        response_data = {
            "response_code": "success",
            "http_status_code": 200,
            "context": {
                "success": {
                    "WhoAreWeModel_data": WhoAreWeSerializer(who_are_we_data, many=True).data,
                    "Certification_data": CertificationSerializer(certification_data, many=True).data,
                    "FeaturedImage_data": FeaturedImageSerializer(featured_image_data, many=True).data,
                    "SocialResponsibility_data": SocialResponsibilitySerializer(social_responsibility_data, many=True).data,
                    "SocialMediaURL_data": SocialMediaURLSerializer(social_media_url_data, many=True).data,
                }
            },
            "message": "OK",
        }
        return Response(response_data)










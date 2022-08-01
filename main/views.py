from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes, action
from main.serializers import JobAdvertSerializer, JobApplicationSerializer
from .models import JobAdvert, JobApplication
from django.db.models import Count
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import NotFound


class JobPosting(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        """Allow logged in user to get adverts in the database. Published adverts come first followed by adverts with the highest applicant count and then recently created adverts come next.
        """
    
        adverts = JobAdvert.objects.prefetch_related("applications").all().annotate(applicant_count=Count('applications')).order_by("status",'-applicant_count', "-date_added")
        
       
        return Response(adverts.values(), status=status.HTTP_200_OK)


    @swagger_auto_schema(method="post", request_body=JobAdvertSerializer())
    @action(methods=["post"], detail=True)
    def post(self, request, format=None):
        """Allow logged in users to create new job adverts."""
        
        serializer = JobAdvertSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"success"}, status = status.HTTP_200_OK)
        
        return Response({"message":"failed", "error":serializer.errors}, status = status.HTTP_400_BAD_REQUEST)



class JobAdvertDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
        
    def get_object(self, advert_id):
        try:
            return JobAdvert.objects.prefetch_related("applications").get(id=advert_id)
        except JobAdvert.DoesNotExist:
            raise NotFound( detail={"message":"failed", "error":"not found"}, code = status.HTTP_404_NOT_FOUND) 

    def get(self, request, advert_id, format=None):
        """Gets the details of a job advert including all the applications for that job advert."""
        
        posting = self.get_object(advert_id)
        serializer = JobAdvertSerializer(posting)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(method="put", request_body=JobAdvertSerializer())
    @action(methods=["put"], detail=True)
    def put(self, request, advert_id, format=None):
        """Allows logged in users to edit the details of a job advert"""
        
        posting = self.get_object(advert_id)
        serializer = JobAdvertSerializer(posting, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, advert_id, format=None):
        """Deletes only published jobs"""
        
        posting = self.get_object(advert_id)
        if posting.status == "unpublished":
            
            posting.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'message':"failed","error":"cannot delete a published post"}, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(["GET"])
@permission_classes([AllowAny])
def published_adverts(request):
    """Allows guest users to view ONLY published job adverts."""
    
    if request.method == 'GET':
        adverts = JobAdvert.objects.filter(status="published").order_by("-date_added")
        
       
        return Response(adverts.values(), status=status.HTTP_200_OK)
    

@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def unpublish_advert(request, advert_id):
    """Allows logged in user to unpublish an advert"""
    
    if request.method == 'GET':
        try:
            advert = JobAdvert.objects.get(id=advert_id, status="published")
            advert.status = "unpublished"
            advert.save()
       
            return Response({"message":"success"}, status=status.HTTP_204_NO_CONTENT)
        
        except JobAdvert.DoesNotExist:
            return Response({"error":"not found","message":"failed"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def republish_advert(request, advert_id):
    """Allows logged in user to republish an advert"""
    
    if request.method == 'GET':
        try:
            advert = JobAdvert.objects.get(id=advert_id, status="unpublished")
            advert.status = "published"
            advert.save()
       
            return Response({"message":"success"}, status=status.HTTP_204_NO_CONTENT)
        
        except JobAdvert.DoesNotExist:
            return Response({"error":"not found","message":"failed"}, status=status.HTTP_404_NOT_FOUND)
        
        
@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def unpublish_advert(request, advert_id):
    """Allows logged in user to unpublish an advert"""
    
    if request.method == 'GET':
        try:
            advert = JobAdvert.objects.get(id=advert_id, status="published")
            advert.status = "unpublished"
            advert.save()
       
            return Response({"message":"success"}, status=status.HTTP_204_NO_CONTENT)
        
        except JobAdvert.DoesNotExist:
            return Response({"error":"not found","message":"failed"}, status=status.HTTP_404_NOT_FOUND)
        
        
        
@swagger_auto_schema(method="post", request_body=JobApplicationSerializer())
@api_view(["POST"])
@permission_classes([AllowAny])
def job_application(request):
    """Allows guest users to apply for only jobs that has been published."""
    
    if request.method == 'POST':
        serializer = JobApplicationSerializer(data=request.data)
        
        if serializer.is_valid():
            advert = serializer.validated_data.get("advert")
            if advert.status == "published":
                serializer.save()
        
                return Response({"message":"success"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"error":"cannot apply for this job. not yet published","message":"failed"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error":serializer.errors,"message":"failed"}, status=status.HTTP_400_BAD_REQUEST)
        

class JobApplicationDetail(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
        
    def get_object(self, application_id):
        try:
            return JobApplication.objects.get(id=application_id)
        except JobApplication.DoesNotExist:
            raise NotFound(detail={"message":"failed", "error":"not found"}, code = status.HTTP_404_NOT_FOUND) 

    def get(self, request, application_id, format=None):
        """Gets the details of a job application"""
        
        application = self.get_object(application_id)
        serializer = JobApplicationSerializer(application)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def delete(self, request, application_id, format=None):
        """Delete a single job application"""
        
        application = self.get_object(application_id)
        
            
        application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
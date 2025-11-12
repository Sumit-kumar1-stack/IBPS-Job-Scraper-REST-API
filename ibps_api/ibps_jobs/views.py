from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import Job
from .serializers import JobSerializer


class LoginView(APIView):
    """Handles user login and returns an auth token"""
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class JobListView(APIView):
    """List all scraped IBPS job postings"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        jobs = Job.objects.all().order_by('-posted_date')
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

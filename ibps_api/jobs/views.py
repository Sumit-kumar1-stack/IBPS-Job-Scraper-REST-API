from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from .models import Job
from ..ibps_jobs.serializers import JobSerializer
import pandas as pd
from pathlib import Path

# API View for job listings
class JobListView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]

# Login API (returns token)
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response({"error": "Invalid credentials"}, status=400)

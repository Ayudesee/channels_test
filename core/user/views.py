from django.contrib.auth import authenticate, login
from drf_spectacular.utils import extend_schema
from rest_framework import views
from rest_framework.response import Response

from user.serializers import LoginSerializer


class LoginView(views.APIView):

    @extend_schema(request=LoginSerializer)
    def post(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"detail": "Success"})
        else:
            return Response({"detail": "Wrong Credentials"}, status=400)

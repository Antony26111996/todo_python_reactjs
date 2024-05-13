from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.authtoken.models import Token

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

class TodoUpdateView(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDeleteView(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class LoginView(APIView):
    def post(self, request):
        # Extract username and password from request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate user
        user = authenticate(username=username, password=password)

        if user:
            # User authenticated, generate token if not exists
            token, _ = Token.objects.get_or_create(user=user)

            # Return success response with token
            return Response({'message': 'Login successful','token': token.key}, status=status.HTTP_200_OK)
        else:
            # Invalid credentials, return error response
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
from rest_framework import generics
from .models import Post
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from .serializers import PostSerializer, UserSerializer

# class PostList(generics.ListCreateAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     # permission_classes = (permissions.IsAdminUser,) 
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class UserList(generics.ListCreateAPIView): # new
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


from rest_framework import viewsets 
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAdminUser

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet): 
    permission_classes = [IsAdminUser] 
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
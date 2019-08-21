from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from userpost.models import UserPost
from userpost.serializer import UserSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

class UserPostViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = UserPost.objects.all()
    serializer_class = UserSerializer

    filter_backends = [SearchFilter]
    search_fields = ('title', 'body',)
 
    def get_queryset(self):

        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()
        return qs

    def perform_create(self,serializer):
        serializer.save(author=self.request.user)



    
from .serializers import RegisterSerializer
from .models import User
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

# Create your views here.


class Register(CreateAPIView):
    serializer_class = RegisterSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(**serializer.validated_data)
        return Response({"user: created user"})

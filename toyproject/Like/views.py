from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Like
from .serializers import LikeSerializer

# Create your views here.
@api_view(['GET'])
def HelloAPI(request):
    return Response("hello world!")

from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import Comment
from . serializers import BlogSerializer
# Create your views here.


@api_view(['POST'])
def hello(request):
    comment = Comment('a@shaikh', 'xxssssssssssssssssssss')
    serializer = BlogSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    print(serializer.data)
    return Response(serializer.data)

from rest_framework.generics import ListAPIView

from parser.models import Post

from parser.serializers import PostSerializer


class PostAPIView(ListAPIView):
    pagination_class = None
    serializer_class = PostSerializer
    queryset = Post.objects.all()

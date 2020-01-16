from amb_app.models import Lead,Post
from rest_framework.views import APIView
from rest_framework import viewsets,permissions,response
from .serializers import LeadSerializer, PostSerializer
import requests,json



#Lead Viewset

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer


class TestView(APIView):
    queryset = Post.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostSerializer

    def call_api(self, request, *args, **kwargs):
        headers = {}
        url = 'http://jsonplaceholder.typicode.com/users/'+args[0]
        method = request.method.lower()
        method_map = {
            'get': requests.get,
            'post': requests.post,
            'put': requests.put,
            'patch': requests.patch,
            'delete': requests.delete
        }
        return Response(method_map[method](url, headers=headers, data=json.dumps(request.data)).json())

    def get(self, request, *args, **kwargs):
        return self.call_api(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.call_api(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.call_api(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.call_api(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.call_api(request, *args, **kwargs)
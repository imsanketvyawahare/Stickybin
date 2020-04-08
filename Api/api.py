from .serializers import StickyApi
from django.http import JsonResponse
from Application.models import Sticky
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# @api_view(['GET', 'POST'])
# def stikcyapi(request):
#     if request.method == "GET":
#         s = Sticky.objects.all()
#         serializer = StickyApi(s, many=True)
#         return Response(serializer.data)
#
#     elif request.method == "POST":
#         serializer = StickyApi(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class API(APIView):
    def get(self, request):
        s = Sticky.objects.all()
        serializer = StickyApi(s, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = StickyApi(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
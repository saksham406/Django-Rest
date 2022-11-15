from rest_framework.response import Response
from watchlist_app.models import WatchList, StreamPlatform ,Review
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer
#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status


class WatchListAV(APIView):
    
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = WatchListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

class WatchListDetailAV(APIView):

    def get(self, request,pk):
        try:
            movies = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error':'not found'},status=status.HTTP_400_BAD_REQUEST)
        serializer = WatchListSerializer(movies)
        return Response(serializer.data)
    
    def put(self,request,pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        watchList = WatchList.objects.get(pk=pk)
        watchList.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class StreamPlatformAV(APIView):

    def get(self, request):
        platform = StreamPlatform.objects.all() 
        serializer = StreamPlatformSerializer(platform, many=True, context={'request': request})
        return Response(serializer.data) 
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        else:
            return Response(serializer.errors)

class StreamPlatformDetailAV(APIView):

    def get(self,request,pk):

        try:
            streamlist = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error':'not found'},status=status.HTTP_400_BAD_REQUEST)
        serializer = StreamPlatformSerializer(streamlist,context ={'request':request})
        return Response(serializer.data)

    def put(self,request,pk):
        platform = StreamPlatform.objects.get(pk = pk)
        serializer = StreamPlatformSerializer(platform , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class ReviewAV(APIView):

    def get(self, request,pk):
        try:
            movies = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response({'error':'not found'},status=status.HTTP_400_BAD_REQUEST)
        serializer = WatchListSerializer(movies)
        return Response(serializer.data)
from rest_framework.response import Response
from watchlist_app.models import WatchList, StreamPlatform
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer
#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

class StreamPlatformAV(APIView):

    def get(self, request):
        platform = StreamPlatform.objects.all() 
        serializer = StreamPlatformSerializer(platform,many = True)
        return Response(serializer.data) 
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        else:
            return Response(serializer.errors)

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

class StreamDetailAV(APIView):

    def get(self,request,pk):

        try:
            streamlist = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error':'not found'},status=status.HTTP_400_BAD_REQUEST)
        serializer = StreamPlatformSerializer(streamlist)
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


#@api_view(['GET','POST'])
#def WatchList_list(request):
#    
#    if request.method =='GET':
#        movies = Movie.objects.all() 
#        serializer = MovieSerializer(movies , many=True)
#        return Response(serializer.data) 
#    if request.method == 'POST':
#        serializer = MovieSerializer(data = request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        else:
#            return Response(serializer.errors)




#@api_view(['GET','PUT','DELETE'])
#def movie_detail(request,pk):
#    if request.method =='GET':
#        movie = Movie.objects.get(pk=pk)
#        serializer = MovieSerializer(movie)
#        return Response(serializer.data) 
#    
#    if request.method == 'PUT':
 #       movie = Movie.objects.get(pk=pk)
#        serializer = MovieSerializer(movie,data = request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        else:
#            return Response(serializer.errors)
#    if request.method == 'DELETE':
#        movie = Movie.objects.get(pk=pk) 
#        movie.delete() 
#        return Response()
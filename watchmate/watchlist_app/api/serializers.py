from rest_framework import serializers 
from watchlist_app.models import StreamPlatform,WatchList , Review





class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    #len_name = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many= True, read_only=True)
    
    class Meta:
        model = WatchList
        fields = "__all__"

    def create(self, validated_data):
       return WatchList.objects.create(**validated_data)
    
    def update(self, instance, validate_data):
        instance.name = validate_data.get('name',instance.name)
        instance.about = validate_data.get('about',instance.about)
        instance.active = validate_data.get('active',instance.active)
        instance.save() 
        return instance 


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):

    watchlist = WatchListSerializer(many = True , read_only = True)

    class Meta:
        model = StreamPlatform
        fields = "__all__" 

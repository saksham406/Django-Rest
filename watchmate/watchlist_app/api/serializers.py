from rest_framework import serializers 
from watchlist_app.models import StreamPlatform,WatchList



class WatchListSerializer(serializers.ModelSerializer):
    #len_name = serializers.SerializerMethodField()
    
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


class StreamPlatformSerializer(serializers.ModelSerializer):

    watchlist = WatchListSerializer(many = True , read_only = True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"
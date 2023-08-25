from rest_framework import serializers
from .models import ImageModel

class ImageSerializer(serializers.ModelSerializer):

    user_id = serializers.ReadOnlyField(source = 'user.id')
    inputted_image = serializers.ImageField(required=True)
    # inputted_image = serializers.ImageField(required=True)
    

    class Meta:
        model = ImageModel
        fields = '__all__'

        read_only_fields = ('id', 'user_id')
        required_fields = ('inputted_image')
        
 
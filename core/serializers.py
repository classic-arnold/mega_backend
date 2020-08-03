from rest_framework import serializers

from . import models as my_models

# Serializers

class ProfileSerializer(serializers.ModelSerializer):
	''' Serialize profile '''
	class Meta:
		model = my_models.Profile
		fields = '__all__'
		read_only_fields = ['id']
		
class FeatureSerializer(serializers.ModelSerializer):
	''' Serialize feature '''
	class Meta:
		model = my_models.Feature
		fields = '__all__'
		read_only_fields = ['id']
		
class DatabaseSerializer(serializers.ModelSerializer):
	''' Serialize database '''
	class Meta:
		model = my_models.Database
		fields = '__all__'
		read_only_fields = ['id']
		
class CommunitySerializer(serializers.ModelSerializer):
	''' Serialize community '''
	is_admin = serializers.BooleanField(read_only=True)
	class Meta:
		model = my_models.Community
		read_only_fields = ['id', 'key']
		exclude = ['admins', 'features', 'members']
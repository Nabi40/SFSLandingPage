from rest_framework import serializers
from .models import OurTeam, Head, HeadTeam, AllTeamDescrip, AllTeam


class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeam
        fields = ['id', 'description', 'image']


# HeadTeam and its parent Head

class HeadTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadTeam
        fields = ['id', 'head', 'image', 'name', 'designation']


class HeadSerializer(serializers.ModelSerializer):
    head = HeadTeamSerializer(many=True, read_only=True)  # reverse relation using related_name

    class Meta:
        model = Head
        fields = ['id', 'description', 'head']  # this now includes list of HeadTeam


# AllTeam and its parent AllTeamDescrip

class AllTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllTeam
        fields = ['id', 'allteam', 'name', 'position', 'profile_image']


class AllTeamDescripSerializer(serializers.ModelSerializer):
    Allteam = AllTeamSerializer(many=True, read_only=True)  # reverse relation using related_name

    class Meta:
        model = AllTeamDescrip
        fields = ['id', 'description', 'Allteam']  # this now includes list of AllTeam

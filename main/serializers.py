from rest_framework import serializers

from main.models import Saved, Candidate


class SavedCandidateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Saved
        fields = ('id', 'author', 'candidate')


class CandidateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Candidate
        fields = ('id', 'full_name', 'gender', 'age', 'address')


class CandidateDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Candidate
        fields = '__all__'
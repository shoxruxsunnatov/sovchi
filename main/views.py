from django.shortcuts import get_object_or_404

from rest_framework.views import Response, APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework import status

from main.models import Saved, Candidate
from main.serializers import SavedCandidateSerializer, CandidateSerializer, CandidateDetailSerializer


class SavedCandidatesView(APIView):

    def get(self, req, *args, **kwargs):

        saved = Saved.objects.filter(author=req.user)
        serializer = SavedCandidateSerializer(saved, many=True)

        return Response(serializer.data)
    
    def post(self, req, *args, **kwargs):

        req.data.pop('id', None)

        saved = Saved.objects.filter(**req.data)
        if saved:
            saved.delete()

            return Response({'detail': 'deleted'}, status=status.HTTP_204_NO_CONTENT)
        
        serializer = SavedCandidateSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class CandidatesView(ListCreateAPIView):
    queryset = Candidate.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CandidateDetailSerializer
        
        return CandidateSerializer


class CandidatesDetailView(APIView):

    def get(self, req, pk, *args, **kwargs):

        candidate = get_object_or_404(Candidate, id=pk)
        serializer = CandidateDetailSerializer(candidate)

        return Response(serializer.data)
    
    def delete(self, req, pk, *args, **kwargs):
        
        candidate = get_object_or_404(Candidate, id=pk)
        candidate.delete()

        return Response(
            {'detail': 'deleted'},
            status=status.HTTP_204_NO_CONTENT
        )



from .models import SkillModels
from .serializers import SkillSerializer
from rest_framework import generics
from rest_framework import permissions



class SkillListCreateView(generics.ListCreateAPIView):
    queryset = SkillModels.objects.all()
    serializer_class = SkillSerializer


class SlkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SkillModels.objects.all()
    serializer_class = SkillSerializer

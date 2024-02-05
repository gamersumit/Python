from django.shortcuts import render
from rest_framework import generics
from account.mixins import CalorieChartPermissionsMixin
from .models import CalorieChart
from .serializers import CalorieChartSerializer
# Create your views here.

class CalorieChartDetailAPIView(CalorieChartPermissionsMixin,  generics.RetrieveAPIView):
    queryset = CalorieChart.objects.all()
    serializer_class = CalorieChartSerializer

class CalorieChartCreateAPIView(CalorieChartPermissionsMixin, generics.CreateAPIView):
    queryset = CalorieChart.objects.all()
    serializer_class = CalorieChartSerializer
    
class CalorieChartListAPIView(CalorieChartPermissionsMixin, generics.ListAPIView):
    queryset = CalorieChart.objects.all()
    serializer_class = CalorieChartSerializer

class CalorieChartUpdateAPIView(CalorieChartPermissionsMixin, generics.UpdateAPIView):
    queryset = CalorieChart.objects.all()
    serializer_class = CalorieChartSerializer

class CalorieChartDeleteAPIView(CalorieChartPermissionsMixin, generics.DestroyAPIView):
    queryset = CalorieChart.objects.all()
    serializer_class = CalorieChartSerializer


    
#shortnaming
CalorieChart_create_view = CalorieChartCreateAPIView.as_view()
CalorieChart_detail_view = CalorieChartDetailAPIView.as_view()
CalorieChart_list_view = CalorieChartListAPIView.as_view()
CalorieChart_update_view = CalorieChartUpdateAPIView.as_view()
CalorieChart_delete_view = CalorieChartDeleteAPIView.as_view()

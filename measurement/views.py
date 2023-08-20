from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView, \
    CreateAPIView, RetrieveUpdateDestroyAPIView
# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class SensorAPIList(ListCreateAPIView): # для получения списка датчиков и их добавления
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class MeasurementAPICreate(CreateAPIView): # для добавления показаний датчиков
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

''' чтение, "перенос" датчиков в другое место, удаление датчиков'''
class SensorAPIRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer     # требуется получение всех данных по датчику!!!!

# class SensorAPIRetrieveUpdate(RetrieveUpdateAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorDetailSerializer  # требуется получение всех данных по датчику!!!!


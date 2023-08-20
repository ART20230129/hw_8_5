from django.contrib import admin
from django.urls import path

from measurement.views import SensorAPIList, MeasurementAPICreate, \
    SensorAPIRetrieveUpdateDestroy

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('admin/', admin.site.urls),
    path('sensors/', SensorAPIList.as_view()), # вывод информации о всех датчиках/добавление датчика
    path('sensors/<int:pk>/', SensorAPIRetrieveUpdateDestroy.as_view()), # вывод информации о конкретном датчике
    path('measurements/', MeasurementAPICreate.as_view()), # добавление показаний датчика
    path('delete/<int:pk>/', SensorAPIRetrieveUpdateDestroy.as_view()), # удаление датчика
    # path('sensors/<int:pk>/', SensorAPIRetrieveUpdate.as_view()), # вывод информации о конкретном датчике

]

from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=100,  verbose_name='Название')
    description = models.TextField( verbose_name='Описание')

    class Meta:
        verbose_name = "Датчик"
        verbose_name_plural = "Датчики"

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', verbose_name='Датчик')
    temperature = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='Температура')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время измеренения')
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Измерение"
        verbose_name_plural = "Измерения"


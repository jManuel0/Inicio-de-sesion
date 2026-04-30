from django.db import models


class Calificacion(models.Model):
    estudiante = models.CharField(max_length=100)
    asignatura = models.CharField(max_length=100)
    nota_1 = models.DecimalField(max_digits=4, decimal_places=2)
    nota_2 = models.DecimalField(max_digits=4, decimal_places=2)
    nota_3 = models.DecimalField(max_digits=4, decimal_places=2)
    promedio = models.DecimalField(max_digits=4, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.promedio = round((self.nota_1 + self.nota_2 + self.nota_3) / 3, 2)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.estudiante} - {self.asignatura}'

    class Meta:
        ordering = ['estudiante', 'asignatura']

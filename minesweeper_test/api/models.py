from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Game(models.Model):    
    game_id = models.CharField(verbose_name='id', unique=True, blank=False,
                            max_length=40)
    width = models.PositiveIntegerField(verbose_name='Ширина поля',
                                         validators=[MinValueValidator(1),
                                                     MaxValueValidator(30)])
    height = models.PositiveIntegerField(verbose_name='Высота поля',
                                         validators=[MinValueValidator(1),
                                                     MaxValueValidator(30)])
    mines_count = models.PositiveIntegerField(verbose_name='Количество мин',
                                         validators=[MinValueValidator(1),])
    completed = models.BooleanField(default=False)
    field = models.CharField(max_length=900, verbose_name='Хранимое поле игры')
    open_field = models.CharField(max_length=900, verbose_name='Поле доступное игроку')
    opend = models.PositiveIntegerField(verbose_name='Количество открытых полей',
                                         validators=[MinValueValidator(1),])
    

    class Meta:
        verbose_name = 'Сохраненная игра'
        verbose_name_plural = 'Игры'

    def __str__(self):
        return f'Игра {self.game_id}'

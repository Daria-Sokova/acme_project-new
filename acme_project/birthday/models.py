from django.db import models
from django.urls import reverse

from .validators import real_age


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', max_length=20, help_text='Необязательное поле', blank=True
    )
    # Валидатор указывается в описании поля
    birthday = models.DateField('Дата рождения', validators=(real_age,))
    image = models.ImageField('Фото', upload_to='birthdays_images/', blank=True)

    def get_absolute_url(self):
        return reverse(
            'birthday:detail',
            kwargs={'pk': self.pk},
        )
        
    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='unique_birthday_person',
            ),
        )


class Congratulation(models.Model):
    text = models.TextField()
    birthday = models.ForeignKey(
        Birthday,
        on_delete=models.CASCADE,
        related_name='congratulations',
    )
    created_at = models.DateTimeField(auto_now_add=True)
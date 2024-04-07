from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',) #ta linijka pozwala na sortowanie w panelu admina według alfabetu
        verbose_name_plural = "Kategorie" #ta linijak zamienia categorys w panelu admina na Kategorie

    def __str__(self):
        return self.name #ta linijka zmienia nazwe z category object x na nazwe
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE) #w przypadku usunięcia kategorii przedmioty również zostaną usunięte
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True) # wartości są true bo można bez opisu i ceny wystawić przedmiot
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False) # czy przedmiot jest sprzedany
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE) #cascade = if user deleted = items deleted

    class Meta:
        verbose_name_plural = "Przedmioty"

    def __str__(self):
        return self.name
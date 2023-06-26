from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Candidate(BaseModel):
    class Type(models.TextChoices):
        TOSHKENT = 'toshkent', 'Toshkent'
        ANDIJON = 'andijon', 'Andijon'
        BUXORO = 'boxoro', 'Buxoro'
        FARGONA = 'fargona', 'Fargona'
        JIZZAH = 'jizzah', 'Jizzah'
        NAMANGAN = 'namangan', 'Namangan'
        NAVOIY = 'navoiy', 'Navoiy'
        QASHQADARYO = 'qashqadaryo', 'Qashqadaryo'
        SAMARQAND = 'samarqand', 'Samarqand'
        SIRDARYO = 'sirdaryo', 'Sirdaryo'
        SURXONDARYO = 'surxondaryo', 'Surxondaryo'
        XORAZM = 'xorazm', 'Xorazm'
        QORAQALPOGISTON = 'qoraqalpogiston', 'Qoraqalpogiston'
        BOSHQA_RESPUBLIKA = 'boshqa_respublika', 'Boshqa_respublika'

    class Gender(models.TextChoices):
        ERKAK = 'erkak', 'Erkak'
        AYOL = 'ayol', 'Ayol'

    author = models.OneToOneField(User, on_delete=models.CASCADE)  # nomzod foydalanuvchi
    gender = models.CharField(max_length=5, choices=Gender.choices)  # nomzod jinsi
    address = models.CharField(max_length=25, choices=Type.choices)  # nomzod manzili
    full_name = models.CharField(max_length=25)  # nomzod ismi
    year = models.CharField(max_length=4)  # nomzod yili
    height = models.FloatField()  # nomzod bo'yi
    age = models.PositiveIntegerField()  # nomzod yoshi
    weight = models.IntegerField()  # nomzod vazni
    married = models.CharField(max_length=25)  # nomzod turmush qurganmi?
    profession = models.CharField(max_length=50)  # nomzod kasbi
    nation = models.CharField(max_length=25)  # nomzod millati
    health = models.CharField(max_length=50)  # nomzod sog'ligi
    prayed = models.CharField(max_length=50)  # nomzod ibodatlimi?
    desires = models.TextField()  # nomzod istaklari
    view_count = models.PositiveIntegerField(default=0)  # nomzod necha marta kurilgan

    def str(self):
        return self.full_name


class Saved(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
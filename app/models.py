"""
Definition of models.
"""

from django.db import models


class Dynastie(models.Model):
    def __str__(self):
        return  self.nazwa
    ID = models.AutoField(primary_key=True, editable=False)
    nazwa = models.CharField(verbose_name="Nazwa dynastii",
                             null=False, max_length=70)
    ppanowanie = models.IntegerField(
         verbose_name="Data rozpoczecia", null=False)
    kpanowanie = models.IntegerField(
         verbose_name="Data zakonczenia", null=False)
        


class Krolowie(models.Model):
    def __str__(self):
        return  self.imie
    ID = models.AutoField(primary_key=True, editable=False)
    imie = models.CharField(verbose_name="Imię króla",
                            null=False, max_length=70)
    ppanowanie = models.IntegerField(
        verbose_name="Data rozpoczecia panowania", null=False)
    kpanowanie = models.IntegerField(
        verbose_name="Data zakonczenia panowania", null=False)
    dynastia = models.ForeignKey(to=Dynastie, on_delete=models.DO_NOTHING)


class Material(models.Model):
    def __str__(self):
        return  self.chemia
    ID = models.AutoField(primary_key=True, editable=False)
    nazwa = models.CharField(
        verbose_name="Nazwa materiału", null=False, max_length=70)
    chemia = models.CharField(
        verbose_name="Chemiczne oznaczenie", null=False, max_length=70)
    gestosc = models.IntegerField(verbose_name="Gestość w kg/m^3")


class Mennica(models.Model):
    def __str__(self):
        return 'Mennica ' + self.nazwa
    ID = models.AutoField(primary_key=True, editable=False)
    nazwa = models.CharField(
        verbose_name="Nazwa mennicy", null=False, max_length=70)
    lokalizacja = models.CharField(
        verbose_name="Lokalizacja mennicy", null=False, max_length=70)


class Stan(models.Model):
    def __str__(self):
        return self.skrot
    ID = models.AutoField(primary_key=True, editable=False)
    nazwa = models.CharField(verbose_name="Nazwa stanu",
                             null=False, max_length=70)
    skrot = models.CharField(verbose_name="Skrót", null=False, max_length=10)


class Rzadkosc(models.Model):
    def __str__(self):
        return self.skrot
    ID = models.AutoField(primary_key=True, editable=False)
    nazwa = models.CharField(verbose_name="Nazwa", null=False, max_length=70)
    skrot = models.CharField(verbose_name="Skrót", null=False, max_length=10)


class Katalog(models.Model):
    def __str__(self):
        return self.nazwa
    ID = models.AutoField(primary_key=True, editable=False)
    nazwa = models.CharField(
        verbose_name="Nazwa katalogu", max_length=70)


class Moneta(models.Model):
    def __str__(self):
        return 'Moneta: ' + self.nazwa
    Nr = models.AutoField(primary_key=True, editable=False,
                          verbose_name="Numer katalogowy")
    nazwa = models.CharField(
        verbose_name="Nazwa monety", max_length=255, blank=False,null=True)
    opis = models.CharField(verbose_name="opis", max_length=255, blank=True,null=True)
    katalog = models.ForeignKey(
        to=Katalog, verbose_name="Do jakiego katalogu należy", on_delete=models.DO_NOTHING, blank=True,null=True)
    panowanie = models.ForeignKey(
        to=Krolowie, on_delete=models.DO_NOTHING,blank=True, null=True)
    rewers = models.ImageField(verbose_name="Rewers", blank=True, null=True)
    awers = models.ImageField(verbose_name="Awers", blank=True, null=True)
    rant = models.CharField(verbose_name="opis", max_length=255, blank=True, null=True)
    rok = models.IntegerField(verbose_name="Rok", blank=True, null=True)
    material = models.ForeignKey(
        to=Material, verbose_name="Materiał", on_delete=models.DO_NOTHING, blank=True, null=True)
    srednica = models.IntegerField(verbose_name="Średnica w mm", blank=True, null=True)
    waga = models.FloatField(verbose_name="Waga w gramach", blank=True)
    stan = models.ForeignKey(to=Stan, on_delete=models.DO_NOTHING, blank=True, null=True)
    mennica = models.ForeignKey(
        to=Mennica, on_delete=models.DO_NOTHING, blank=True)
    autor = models.CharField(verbose_name="autor", max_length=255, blank=True, null=True)
    rzadkosc = models.ForeignKey(
        to=Rzadkosc, on_delete=models.DO_NOTHING, blank=True, null=True)
    cena = models.FloatField(verbose_name="Cena katalogowa w €",  blank=True, null=True)
    cenaz = models.FloatField(verbose_name="Cena zapłacona w zł", blank=True, null=True)
    pochodzenie = models.CharField(verbose_name="url", max_length=255, blank=True, null=True)


# Create your models here.

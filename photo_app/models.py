from django.db import models
from django import forms

class Fotografija (models.Model):
    naziv = models.CharField (max_length = 255)
    opis = models.TextField()
    putanja = models.ImageField(upload_to='images')
    broj_pogleda = models.IntegerField()
    
    class Meta:
        ordering = ["-id"]

class Komentar (models.Model):
    fotografija = models.ForeignKey(Fotografija)
    komentar = models.TextField()
    vrijeme_komentiranja = models.DateTimeField()
    
class PhotoUploadForm(forms.Form):
    naziv = forms.CharField(widget=forms.TextInput(attrs={'size': 99}))
    opis = forms.CharField(widget=forms.Textarea(attrs={'cols': 75, 'rows': 2}))
    fotografija = forms.FileField(
        label='Fotografija',
    )

class CommentForm(forms.Form):
    komentar = forms.CharField(widget=forms.Textarea(attrs={'cols': 115, 'rows': 5}))
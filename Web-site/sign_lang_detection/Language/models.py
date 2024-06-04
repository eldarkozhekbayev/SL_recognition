from django.db import models

class Language(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Alphabet(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    letter = models.CharField(max_length=5)
    photo = models.ImageField(upload_to='alphabet_photos/')

    def __str__(self):
        return f"{self.letter} ({self.language.title})"

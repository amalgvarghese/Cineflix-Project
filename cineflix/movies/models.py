from django.db import models

import uuid

from embed_video.fields import EmbedVideoField

# Create your models here.

from multiselectfield import MultiSelectField

class BaseClass(models.Model):

    uuid= models.UUIDField(unique=True,default=uuid.uuid4)

    active_status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta :

        abstract = True

class IndustryChoices(models.TextChoices):

    MOLLYWOOD = 'Mollywood','Mollywood'

    HOLLYWOOD = 'Hollywood','Hollywood'

    BOLLYWOOD = 'Bollywood','Bollywood'

    TOLLYWOOD = 'Tollywood','Tollywood'

class CertificationChoices(models.TextChoices):

    A = 'A','A'

    UA = 'U/A','U/A'

    U = 'U','U'

    S = 'S','S'

class GenreChoices(models.TextChoices):

    ACTION = 'Action','Action'
    
    ROMANTIC = 'Romantic','Romantic'

    THRILLER = 'Thriller','Thriller'

    COMEDY = 'Comedy','Comedy'

    HORROR = 'Horror','Horror'

class ArtistChoices(models.TextChoices):

    MOHANLAL = 'Mohan Lal','Mohan Lal'

    MAMMOOTTY = 'Mammooty','Mammooty'

    NIVINPAULY = 'Nivin Pauly','Nivin Pauly'

class LanguageChoices(models.TextChoices):

    MALAYALAM ='Malayalam','Malayalam'

    ENGLIST = 'English','English'

    HINDI = 'Hindi','Hindi'

    TAMIL = 'Tamil','Tamil'

    TELUGU = 'Telugu','Telugu'

    KANNADA = 'Kannada','Kannada'

class Industry(BaseClass):

    name = models.CharField(max_length=50)

    class Meta :

        verbose_name = 'Industries'

        verbose_name_plural = 'Industries'

    def __str__(self):

        return f'{self.name}'
    


class Genre(BaseClass):

    name = models.CharField(max_length=50)

    class Meta :

        verbose_name = 'Genre'

        verbose_name_plural = 'Genre'

    def __str__(self):

        return f'{self.name}'
    

class Artist(BaseClass):

    name = models.CharField(max_length=50)

    dob = models.DateField()

    description = models.TextField()

    class Meta :

        verbose_name = 'Artists'

        verbose_name_plural = 'Artists'

    def __str__(self):

        return f'{self.name}'


class Language(BaseClass):

    name = models.CharField(max_length=50)

    class Meta :

        verbose_name = 'Languages'

        verbose_name_plural = 'Languages'

    def __str__(self):

        return f'{self.name}'
    




    

class Movie(BaseClass):

    name = models.CharField(max_length=50)

    description = models.TextField()

    release_year = models.DateField()

    industry = models.ForeignKey('Industry',on_delete=models.CASCADE) 

    # if we use CASCADE industry deleted movie will also deleted

     # if we want (movie industry value = null) when industry is deleted on_delete = models.SET_Null

    runtime = models.TimeField()

    certification = models.CharField(max_length=5,choices=CertificationChoices.choices)

    genre = models.ManyToManyField('Genre')

    artists = models.ManyToManyField('Artist')

    photo = models.ImageField(upload_to='movies/banner-images/')

    # thumbnail = models.ImageField(upload_to='movies/thumbnails')

    video = EmbedVideoField()

    tags = models.TextField()

    # languages = MultiSelectField(choices=LanguageChoices.choices)

    languages = models.ManyToManyField('Language')

    class Meta :

        verbose_name = 'Movies'

        verbose_name_plural = 'Movies'

    def __str__(self):

        return f'{self.name}'
    

    



    






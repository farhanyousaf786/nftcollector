from django.db import models

from django.urls import reverse

# Create your models here.


RATING= (
    ('1', '1 Star'),
    ('2', '2 Stars'),
    ('3', '3 Stars'),
    ('4', '4 Stars'),
    ('5', '5 Stars'),
)


class Chain(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('chains_detail', kwargs={'pk': self.id})



class Nft(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    type = models.TextField()
    chain = models.ManyToManyField()

    def get_absolute_url(self):
      return reverse('detail', kwargs={'nft_id': self.id})



class Rating(models.Model):
    date = models.DateField('date first observed')
    rating = models.CharField(
      max_length=1,
      choices=RATING,
      default=RATING[0][0]
    )
    
    nft = models.ForeignKey(Nft, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.get_rating_display()} on {self.date}'
    
    class Meta:
        ordering = ['-date']
from django.db import models


  
 

  
class Parents(models.Model):
  ebeveyn_bilgi= models.CharField(max_length=250)
  ebeveyn_iletisim= models.EmailField()
  
 
class Babys(models.Model):
   bebek_adi  = models.CharField(max_length=100)
   aciklama= models.TextField()
   resim=models.CharField(max_length=100)
   anasayfa=models.BooleanField(default=False)
   parent = models.ForeignKey(Parents, on_delete=models.CASCADE, related_name='babies',default=1) 

class sensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    air_quality = models.CharField(max_length=50)
    temperature = models.FloatField()
    humidity = models.FloatField()
    rain_detected = models.BooleanField()
    sound_level = models.FloatField()

      
    def __str__(self):
        return f"{self.timestamp} - {self.air_quality} - {self.temperature}°C - {self.humidity}% -  {'Rain' if self.rain_detected else 'No Rain'} - {self.sound_level} dB"
  
  


 

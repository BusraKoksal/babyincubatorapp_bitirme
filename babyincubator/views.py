from django.shortcuts import render,get_object_or_404
from .models import Babys,Parents
from django.urls import reverse
from .models import sensorData
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
#from django.http import HttpResponse, JsonResponse
from django.utils.dateparse import parse_datetime
import json 
#from .tasks import mqtt_listener


kategori_liste=["bebek verileri","bebek bilgisi","mesaj sayfasi"]
bebek_liste = [
      { 
     "id":"1",    
     "bebek_adi": "Sergen Çakmak",
     "aciklama": "Sergen Çakmak aciklama",
     "resim":"jpgbaby3.jpg",
     "anasayfa":True
      },
 
 
      {
     "id":"2",
     "bebek_adi": "Tarik Kaya",
     "aciklama": "Tarik Kaya aciklama",
     "resim":"jpgbaby2.jpg",
     "anasayfa":False
      },           
]



def home(request):
    data= {
        "kategoriler": kategori_liste,
        "bebekler": Babys.objects.filter(anasayfa=True)
    }
    return render(request,"index.html",data)
def babys(request):
    data= {
        "kategoriler": kategori_liste,
        "bebekler": Babys.objects.all()
        
    }
    return render(request,"babys.html",data)

def babydetails(request,id):
    data= {
        
        "baby": Babys.objects.get(id=id)
        
    }
    return render(request,"details.html",data)



'''def ebeveyn_iletisim(request):
    data={
        "ebeveyn": Parents.objects.get(id=id)
    }
   
 
    return render(request,"ebeveyn_iletisim",data)'''




def Ebeveyn_iletisim(request, parent_id):
    data= {
        
        "parent": Parents.objects.get(id=parent_id)
        
    }
    #parent = get_object_or_404(Parents, id=parent_id)
    return render(request, 'Ebeveyn_iletisim.html',data)
def sensorData_api(request):
    if request.method =='POST':
        data=json.loads(request.body)
        sensorData.objects.create(
            temperature=data['temperature'],
            humidity=data['humidity'],
            air_quality=data['air_quality'],
            #heart_rate=data['heart_rate'],
            #spo2=data['spo2'],
            rain_detected=data['rain_detected'],
            sound_level=data['sound_level']


        )
        return JsonResponse({'status':'success'},status=201) 
    return JsonResponse({'error':'invalid request'},status=400)
    
def bebekVerileri(request):
    data = sensorData.objects.all().order_by('-timestamp')[:10]  # Son 10 veriyi al
    context = {
        'sensor_data': data
    }
    return render(request, 'bebekVerileri.html', context)





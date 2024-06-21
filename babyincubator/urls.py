from django.urls import include, path
from . import views

from .views import bebekVerileri, sensorData_api
urlpatterns = [
    path("", views.home),
    path("home", views.home,name='home'),
    path("babys", views.babys,name='babys'),
    path("babys/<int:id>", views.babydetails,name='details'),
    path("bebekVerileri", views.bebekVerileri, name="bebekVerileri"),
    path("Ebeveyn_iletisim/<int:parent_id>", views.Ebeveyn_iletisim, name="Ebeveyn_iletisim"),
    path('api/sensorData/', sensorData_api, name='sensorData_api'),
    path('account/', include('account.urls'))
    
]

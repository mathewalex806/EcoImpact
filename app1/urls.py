from django.urls import path
from . import views

urlpatterns = [
    path("",views.index , name="index"),
    path("login/",views.login_view , name="login"),
    path("register/",views.register , name="register"),
    path("main/",views.main , name="main"),
    path("Airtravel/",views.Airtravelf , name="Airtravel"),
    path("Roadtravel/",views.Roadtravelf , name="Roadtravel"),
    path("Seatravel/",views.Seatravelf , name="Seatravel"),
    path("Info/",views.Infof , name="Info"),
    path("Energy/",views.Energyf , name="Energy"),
    path("Goods/",views.Goodsf , name="Goods"),
    path("Contribute/",views.Contributef , name="Contribute"),
    path("logout/",views.logout_view , name="logout"),
]
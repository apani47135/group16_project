from django.urls import path, include
from . import views

urlpatterns = [
	path('',views.home,name ="po-home"),
    path('about/',views.about,name="po-about"),
    path('history/',views.history,name="po-history"),
    path('result/',views.result,name="po-result"),
    path('reports/',views.reports,name="po-reports"),
    path('delivered/',views.delivered,name="po-delivered")
]
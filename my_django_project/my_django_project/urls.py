from django.urls import path, include

urlpatterns = [
   path('star-wars/', include('my_api.urls')),
]
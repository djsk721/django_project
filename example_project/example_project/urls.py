from example_app.views import hello
from django.urls import path

urlpatterns = [
   # ... 기존 코드 ...
   path('hello/', hello),
]


# TODO : 아래에 URL로 접근할 수 있다.
# from django.contrib import admin
# from django.urls import path, include
# from xcapp.views import *
# from django.contrib.auth import views as auth_views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('blogs/', include('blogs.urls')),
#     path('polls/', include('polls.urls')),
#     path('reviews/', include('reviews.urls'))
# ]
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('homeUrl',views.home,name='home'),
    path('userDetailsSave',views.userDetailsAdd,name='userDetailsSave'),
    path('edituser/<int:id>', views.edituser, name='edituser'),
    path('userDetailsUpdate/<int:id>', views.userDetailsUpdate, name='userDetailsUpdate'),
    path('deleteuser/<int:id>', views.userDetailsDelete, name='deleteuser'),
    path('image_upload',views.hotel_image_view, name='image_upload'),
    path('success',views.success, name='success'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
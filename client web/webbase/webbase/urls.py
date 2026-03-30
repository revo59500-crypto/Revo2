from django.contrib import admin
from django.urls import path, re_path
from allpg import views

admin.site.site_header = "REVO Admin"
admin.site.site_title = "REVO Admin Portal"
admin.site.index_title = "Welcome to REVO Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('services/', views.service, name='services'),
    path('contact/', views.contact, name='contact'),
    path('singlepg/', views.singlepg, name='singlepg'),
    path('staticpg/', views.staticpg, name='staticpg'),
    path('multipg/', views.multipg, name='multipg'),
    path('3d-design/', views.threedpg, name='3d-design'),
    path('services/single-page/', views.singlepg, name='services-single-page'),
    path('services/static/', views.staticpg, name='services-static'),
    path('services/multi-page/', views.multipg, name='services-multi-page'),
    path('services/webgl/', views.threedpg, name='services-webgl'),
    path('services/static1-formula/', views.static1_formula, name='services-static1-formula'),
    path('services/static2-story/', views.static2_story, name='services-static2-story'),
    path('services/static3-contact/', views.static3_contact, name='services-static3-contact'),
    path('services/multiplepg/', views.multiplepg, name='services-multiplepg'),
    path('services/chatbot/', views.chatbot, name='services-chatbot'),
    path('login/', views.login_view, name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('signup/',views.signup,name='signup'),
    path('chatbot/', views.chatbot, name='chatbot'),
]

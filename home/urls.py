from django.urls import path
from home import views
from django.contrib import admin

# django admin header customization
admin.site.site_header='Developer Jayant'
admin.site.site_title="Welcome to Jay's Dashboard"
admin.site.index_title="Welcome to this Portal"


# urls define for app

urlpatterns = [
    path('home/',views.home ),
    path('about/',views.about ),
    path('project/',views.project),
    path('contact',views.contact )
]

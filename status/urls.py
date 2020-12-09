from django.urls import path
from . import views

urlpatterns=[
    path('',views.finalAnalysis,name='finalAnalysis'),
    # path('about/',views.about,name='about'),
    # path('yesterday/',views.yesterday_data,name='yesterday'),

    #API ENDPOINTS
    # path('api/yesterday/',views.yesterday_api,name='api-yesterday'),
]
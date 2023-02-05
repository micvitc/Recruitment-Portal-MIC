from django.urls import path,include
from services import views

urlpatterns = [
    # path('',views.home,name = "home"),
    path('profile/<slug:slug>/view',views.profile,name = "profile"),
    
    #Recruitment
    path('update/<int:pk>/recruitment/drive',views.RecruitmentDriveUpdateView.as_view(),name = "update_recruitment"),
]
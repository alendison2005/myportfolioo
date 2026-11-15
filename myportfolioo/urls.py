"""
URL configuration for myportfolioo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from portfolio.views import Portfolioview
from portfolio.views import Eductionview
from portfolio.views import levelview
from portfolio.views import Projectview
from portfolio.views import Experinceview
from portfolio.views import certifationview
from portfolio.views import Achivmentview
from portfolio.views import Socialprofileview
from portfolio.views import Resumeview

urlpatterns = [
    path('admin/', admin.site.urls),
    path("student/",Portfolioview.as_view()),
    path("education/",Eductionview.as_view()),
    path("skills/",levelview.as_view()),
    path("projects/",Projectview.as_view()),
    path("experience/",Experinceview.as_view()),
    path("certifications/",certifationview.as_view()),    
    path("achievements/",Achivmentview.as_view()),    
    path("social-profiles/",Socialprofileview.as_view()),
    path("resume/",Resumeview.as_view()),



]


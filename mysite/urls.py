from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from mysite.core import views
from django.views.generic import TemplateView

from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('api/test', views.Api.test, name='test'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#--------------cron job--------------------------
class Apscheduler:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.job = None
        self.seconds = 5
        self.scheduleJobTest = ScheduleJobTest()

    def start_job(self):
        self.job = self.scheduler.add_job(self.scheduleJobTest.job, 'interval', seconds=self.seconds)
        try:
            self.scheduler.start()
        except:
            pass

class ScheduleJobTest:
    def __init__(self):
        print("ScheduleJobTest")

    def job(self):
        print("\n job",datetime.now())

# scheduleJobTest = ScheduleJobTest()
Apscheduler().start_job()

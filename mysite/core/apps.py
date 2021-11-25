from django.apps import AppConfig
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
# import threading
# import time
# import schedule

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' 
    name = 'mysite.core'

    # def ready(self):
    #     Apscheduler().start_job()

# class Apscheduler:
#     def __init__(self):
#         self.scheduler = BackgroundScheduler()
#         self.job = None

#     def start_job(self):
#         self.job = self.scheduler.add_job(scheduleJobTest.job, 'interval', seconds=5)
#         try:
#             self.scheduler.start()
#         except:
#             pass

# #----------------------------------------
# class ScheduleJobTest:
#     def __init__(self):
#         print("ScheduleJobTest")

#     def job(self):
#         print("\n job",datetime.now())

# scheduleJobTest = ScheduleJobTest()



# class CoreConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField' 
#     name = 'mysite.core'

#     def ready(self):
#         # Apscheduler().start_job()

#         def startSchedule():
#             scheduleJobTest = ScheduleJobTest()
#             schedule.every(5).seconds.do( scheduleJobTest.process )

#             while True:
#                 schedule.run_pending()
#                 time.sleep(1)

#         startSchedule()

#         # x = threading.Thread(target= startSchedule) # async
#         # x.start()

# class ScheduleJobTest:
#     def __init__(self):
#         print("ScheduleJobTest")

#     def process(self):
#         print("\n job",datetime.now())
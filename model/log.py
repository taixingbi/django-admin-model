from django.db import models

class Log(models.Model):
    time = models.CharField(max_length=255)
    log = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'model_log'  
        # verbose_name = "model_log"

# -------------------------------------------------------
class LogCrud:
    def __init__(self):
        print("LogCrud")
    
    def create(self, time, log):
        print("create")
        b = Log(time=time, log=log)
        b.save()

    def read(self):
        print("read")
        all_entries = Log.objects.all()
        times = all_entries.values_list('time', flat=True)
        logs = all_entries.values_list('log', flat=True)

        all_records = []
        for record in tuple(zip(times, logs)):
            all_records.append(record[0] + " " + record[1])
        return all_records

    def delete(self):
        print("delete")
        all_entries = Log.objects.all()
        all_entries.delete()


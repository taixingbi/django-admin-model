from django.views.generic import TemplateView
from django.http import JsonResponse
from model.log import LogCrud
from datetime import datetime

# views
class Home(TemplateView):
    template_name = 'home.html'

class Api(): 
    def test(request):  
        print("\n\n*************************************test*************************************")
        
        logCrud = LogCrud()
        logCrud.create( str(datetime.now()), "this is log test")
        logs = logCrud.read()
        print(logs)
        # logCrud.delete()

        dataJson= {
            "test": "test"
        }

        return JsonResponse(dataJson)

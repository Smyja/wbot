from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse
from .models import Log


@require_http_methods(["GET","POST"])
@csrf_exempt
def webhook(request):
    
    user = request.POST.get('From')
    message = request.POST.get('Body')
   
    print(f'{user} says {message}')
    cleaned_username=user.replace('whatsapp:','')

    response = MessagingResponse()
    response.message('What do you think of my Whatsapp Questions application?')
    Log.objects.create(phone_number=cleaned_username, message=message)
 
    return HttpResponse(str(response))

def webhook_logs(request):
  log_object = Log.objects.all()
  context = {
    "data": log_object
  }
  return render(request, 'logs.html', context)
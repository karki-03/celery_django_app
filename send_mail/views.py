from django.shortcuts import render
from rest_framework.views import APIView
from send_mail.tasks import send_email_task

# Create your views here.

class HomeView(APIView):
    def get(self, request):
        return render(request, "index.html")

class SendMailView(APIView):
    def post(self, request):
        # send mail here
        print(request.data.get("email") , request.data.get("msg"))
        is_mail_sent = send_email_task.delay(
            request.data.get("email"), request.data.get("msg")
        )
        print(is_mail_sent)
        if is_mail_sent:
            return render(request, "success.html")
        else:
            return render(request, "index.html")


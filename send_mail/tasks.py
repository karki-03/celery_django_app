from django.core.mail import send_mail
from celery import shared_task


@shared_task
def send_email_task(email_address, message):
    print("inside the tasks.py file")
    send_mail(
        "Your Feedback",
        f"\t{message}\n\nThank you!",
        "bidutkarki30@gmail.com",
        [email_address],
        fail_silently=False,
    )

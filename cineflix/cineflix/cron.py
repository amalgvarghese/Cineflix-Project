from apscheduler.schedulers.background import BackgroundScheduler

from django.utils import timezone

from subscriptions.models import UserSubscriptions

# def print_hello():
    
#     print('hello world')

def disable_subscriptions():

    current_date_time = timezone.now()

    UserSubscriptions.objects.filter(active=True,end_date__lte=current_date_time).update(active=False)

    



def sheduler_job():

    sheduler = BackgroundScheduler()

    sheduler.add_job(disable_subscriptions,'cron',minute=1,hour=0)

    sheduler.start()
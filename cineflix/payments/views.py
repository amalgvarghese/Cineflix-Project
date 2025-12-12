from django.shortcuts import render

from django.views import View

from subscriptions.models import SubscriptionPlans,UserSubscriptions

from django.utils.decorators import method_decorator

from authentication.permissions import permitted_user_roles

# Create your views here.


@method_decorator(permitted_user_roles(['User']),name='dispatch')   

class RazorPayView(View):

    template = 'payments/razorpay.html'

    def get(self,request,*args,**kwrags):

        uuid = kwrags.get('uuid')

        user = request.user

        plan = SubscriptionPlans.objects.get(uuid=uuid)

        user_subscription = UserSubscriptions.objects.create(profile=user,plan=plan)

        return render(request,self.template)



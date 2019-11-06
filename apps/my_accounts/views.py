from django.shortcuts import render
from django.views import View
from .models import SiteUser


# Create your views here.


class UserProfileView(View):
    def get(self, request, user_id):
        user = SiteUser.objects.get(id=user_id)
        context = {'user_obj': user}
        return render(request, 'account__/profile.html', context=context)


# class UpdateProfileView(View):
#     def get(self, request):
#         pass
#
#     def post(self, request):
#         pass

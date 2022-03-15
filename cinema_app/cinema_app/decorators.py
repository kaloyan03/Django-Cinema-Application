from functools import wraps
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from cinema_app.profiles.models import Profile


def has_completed_profile(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
        user = request.user
        profile = Profile.objects.filter(user=user)
        if not profile:
             return HttpResponseRedirect(reverse_lazy('complete profile'))
        else:
            return HttpResponseRedirect(reverse_lazy('profile', user.id))

  return wrap
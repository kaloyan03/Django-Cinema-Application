from functools import wraps
from django.http import HttpResponseRedirect


def profile_required(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
        user = request.user
        if user.has_completed_profile:
             return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/profile/complete_profile')

  return wrap
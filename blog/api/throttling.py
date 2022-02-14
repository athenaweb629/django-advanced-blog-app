# Throttling 
# https://ilovedjango.com/django/rest-api-framework/throttling-in-django-rest-framework/

# Burst and Scope (Also See settings.py)

from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
import random

class AnonSustainedThrottle(AnonRateThrottle):
    scope = "anon_sustained"


class AnonBurstThrottle(AnonRateThrottle):
    scope = "anon_burst"


class UserSustainedThrottle(UserRateThrottle):
    scope = "user_sustained"


class UserBurstThrottle(UserRateThrottle):
    scope = "user_burst"

# Custom Throttling Rules 
# https://www.django-rest-framework.org/api-guide/throttling/#custom-throttles
# Example which will randomly deny one in every ten requests
class RandomRateThrottle(throttling.BaseThrottle):
    def allow_request(self, request, view):
        return random.randint(1, 10) != 1
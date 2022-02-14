# Throttling 
# https://ilovedjango.com/django/rest-api-framework/throttling-in-django-rest-framework/

# Burst and Scope (See settings.py)

# Custom Throttling
# https://www.django-rest-framework.org/api-guide/throttling/#custom-throttles

from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class AnonSustainedThrottle(AnonRateThrottle):
    scope = "anon_sustained"


class AnonBurstThrottle(AnonRateThrottle):
    scope = "anon_burst"


class UserSustainedThrottle(UserRateThrottle):
    scope = "user_sustained"


class UserBurstThrottle(UserRateThrottle):
    scope = "user_burst"



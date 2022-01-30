#!/usr/bin/env python

from datetime import timedelta
from django.conf import settings
from django.utils import timezone
from blango_auth.models import User

import logging
logger = logging.getLogger(__name__)

# Clean Up Users that have registered but didn't validate their account.
def user_cleanup():
    inactive = User.objects.filter(
        is_active=False,
        date_joined__lt=timezone.now() - timedelta(days=settings.ACCOUNT_ACTIVATION_DAYS)
        )
    # log a message when an inactive user is found 
    # (logs directly before deleting inactive user)
    logger.info("Inactive User %d will be deleted. Email Address: %s",inactive.id, inactive.email)
    inactive.delete()


if __name__ == '__main__':
  user_cleanup()
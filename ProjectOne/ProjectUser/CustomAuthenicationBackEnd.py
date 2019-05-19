from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import logging
log = logging.getLogger(__name__)
log.info("Custom Authentication")
class EmailOrUsernameModelBackend(object):
    """
    This is a ModelBacked that allows authentication with either a username or an email address.

    """
    def authenticate(self, request, username=None, password=None):
        log.info("Attempt Authenication For User {}".format(username))
        #if the username @ character
        try:
            validate_email(username)
        except ValidationError as e:
            #not a valid email so fall back to username authenication
            kwargs = {'username': username}
        else:
            #use email authenication 
            kwargs = {'email': username}
            
        try:
            user = get_user_model().objects.get(**kwargs)
            if user.check_password(password):
                return user
        except get_user_model().DoesNotExist:
            return None

    def get_user(self, username):
        try:
            return get_user_model().objects.get(pk=username)
        except get_user_model().DoesNotExist:
            return None
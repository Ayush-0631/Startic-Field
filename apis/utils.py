from .models import *
from django.utils import timezone
from datetime import timedelta
from requests import post,put,get


def get_user_tokens(profile):
    user_tokens = CalendarToken.objects.filter(profile=profile)
    if user_tokens.exists():
        return user_tokens.first()
    return None

# This function creates token object
def create_or_update_user_tokens(profile,access_token,refresh_token,token_type,expires_in,token_uri,client_id,client_secret):
    user_tokens = get_user_tokens(profile)
    if user_tokens:
        user_tokens.access_token = access_token
        user_tokens.expires_in = expires_in
        user_tokens.token_uri = token

        user_tokens.save(update_fields=['access_token','expiry','token_uri'])
        return 
    # Setting a time object for when will the sesion expire
    expires_in = timezone.now() + timedelta(seconds=expires_in)
    # Creates a new tokens object
    tokens = CalendarToken(profile=profile,access_token=access_token,
                            expires_in=expires_in,token_type=token_type,
                            refresh_token=refresh_token,client_id=client_id,client_secret=client_secret
                            ,token_uri=token_uri)
    tokens.save()

def if_expired_refresh(profile):
    token = CalendarToken.objects.get(profile=profile)
    if token.expiry<=timezone.now():
        refresh_spotify_tokens(token)
        return token
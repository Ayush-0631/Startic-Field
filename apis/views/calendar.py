from django.shortcuts import render, redirect
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta, datetime
from django.http import JsonResponse
import pytz
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import Flow
from google.oauth2 import credentials
from ..utils import *
from django.utils.encoding import smart_str
from urllib3 import request

API_KEY = "AIzaSyAUjbPEXG72TVZB0HbWeAlsItxYLk8k2hk"

SCOPES = ['https://www.googleapis.com/auth/calendar']

service_account_email = "starticfield@starticfield.iam.gserviceaccount.com"


def authorize(request):
    profile = Profile.objects.get(user=request.user)
    flow = Flow.from_client_secrets_file(
        'client.json', 
        scopes=SCOPES, 
        redirect_uri='http://127.0.0.1:8000/api'
    )
    code = request.GET.get('code')
    if code:
        flow.fetch_token(code=code)
        creds = flow.credentials
        token = create_or_update_user_tokens(
            profile=profile, 
            access_token=creds.token, 
            refresh_token=creds.refresh_token, 
            token_uri=creds.token_uri, 
            expires_in=creds.expiry,
            client_id=creds.client_id,
            client_secret=creds.client_secret
            )
        return JsonResponse({})
    auth_url, _ = flow.authorization_url(prompt='consent')
    return redirect(auth_url)


def add_event_to_calendar(profile, event):
    token = CalendarToken.objects.get(profile=profile)
    creds = credentials.Credentials(
            token=token.access_token,
            refresh_token=token.refresh_token,
            token_uri=token.token_uri,
            client_id=token.client_id,
            client_secret=token.client_secret,
            scopes=SCOPES,
            expiry=token.expiry
        )
    if creds.expired:
        creds.refresh(request=request)
    service = build('calendar', 'v3', credentials=creds)

    start_datetime = datetime.now(tz=pytz.utc)
    event = service.events().insert(calendarId='primary', body={
        'summary': event.title,
        'description': event.desc,
        'start': {'dateTime': event.live_date.isoformat()},
        'end': {'dateTime': (event.live_date + timedelta(minutes=event.duration)).isoformat()},
    }).execute()

    return JsonResponse({})

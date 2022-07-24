from django.shortcuts import render, redirect
from rest_framework import generics,status
from rest_framework.views import APIView
from requests import Request, post, PreparedRequest, get
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
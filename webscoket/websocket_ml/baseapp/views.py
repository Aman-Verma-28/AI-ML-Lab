from datetime import datetime
from pydoc import doc
from aiohttp import JsonPayload
from django.http import JsonResponse
from django.shortcuts import render
from langcodes import Language
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .custom_auth import CustomAuthentication
# Create your views here.

class YoutubeAPI(APIView):
    def get(self, request, *args, **kwargs):
        print(request.data)
        singer = request.data.get('singer', 'Selena Gomez')
        language = request.data.get('language', 'English')
        emotion = request.data.get('emotion', 'happy')
        
        return JsonResponse( {
            'status': 'verified', 
            'endpoint': 'www.youtube.com', 
            'data': {
            'singer': singer,
            'language': language,
            'enpoint' : 'www.youtube.com',
            'emotion-detected' : emotion,
        },
        },
        status=200)

class CalendarAPI(APIView):
    def get(self, request, *args, **kwargs):
        appointment_date = request.data.get('appointment_date', datetime.today())
        appointment_time = request.data.get('appointment_time', datetime.now())
        doctor = request.data.get('doctor')
        patient = request.data.get('patient')
        doctor_id = request.data.get('doc_id')
        patient_id = request.data.get('patient_id')

        response = {
            'status': 'received',
            'endpoint': 'www.calendar.google.com',
            'book-time' : {
                'date': appointment_date,
                'time': appointment_time,
                'reminder': '30 mins before'
            },
            'doctor-name': doctor,
            'patient': patient,
            'doctor_id': doctor_id,
            'patient_id': patient_id,
            'meeting_info': {
                'link': '<calendar.link.google/meet-<generated-link>>',
                'reminder': '30 mins before',
                'host': doctor,
                'guest': patient,
            }
        }

        return JsonResponse(response, status=200)


'''
{
    "appointment_date": "2022-06-28",
    "appointment_time": "16:00",
    "doctor": "aparna",
    "patient": "aman",
    "doctor_id": 195,
    "patient_id": 196
}
'''

class TestView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomAuthentication]
    def get(self, request):
        return JsonResponse("Success", status=200)
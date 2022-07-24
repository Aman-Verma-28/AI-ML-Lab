from datetime import datetime
from pydoc import doc
import requests
import json
from django.http import JsonResponse
from django.shortcuts import render
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

class TurnitinView(APIView):
    def post(self, request, *args, **kwargs):
        
        text_to_check = request.data.get('text', 'text to check')

        burp0_url = "https://papersowl.com:443/plagiarism-checker-send-data"

        burp0_cookies = {"PHPSESSID": "qjc72e3vvacbtn4jd1af1k5qn1", "first_interaction_user": "%7B%22referrer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%2C%22internal_url%22%3A%22%5C%2Ffree-plagiarism-checker%22%2C%22utm_source%22%3Anull%2C%22utm_medium%22%3Anull%2C%22utm_campaign%22%3Anull%2C%22utm_content%22%3Anull%2C%22utm_term%22%3Anull%2C%22gclid%22%3Anull%2C%22msclkid%22%3Anull%2C%22adgroupid%22%3Anull%2C%22targetid%22%3Anull%2C%22appsflyer_id%22%3Anull%2C%22appsflyer_cuid%22%3Anull%2C%22cta_btn%22%3Anull%7D", "first_interaction_order": "%7B%22referrer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%2C%22internal_url%22%3A%22%5C%2Ffree-plagiarism-checker%22%2C%22utm_source%22%3Anull%2C%22utm_medium%22%3Anull%2C%22utm_campaign%22%3Anull%2C%22utm_content%22%3Anull%2C%22utm_term%22%3Anull%2C%22gclid%22%3Anull%2C%22msclkid%22%3Anull%2C%22adgroupid%22%3Anull%2C%22targetid%22%3Anull%2C%22appsflyer_id%22%3Anull%2C%22appsflyer_cuid%22%3Anull%2C%22cta_btn%22%3Anull%7D", "affiliate_user": "a%3A3%3A%7Bs%3A9%3A%22affiliate%22%3Bs%3A9%3A%22papersowl%22%3Bs%3A6%3A%22medium%22%3Bs%3A9%3A%22papersowl%22%3Bs%3A8%3A%22campaign%22%3Bs%3A9%3A%22papersowl%22%3B%7D", "sbjs_migrations": "1418474375998%3D1", "sbjs_current_add": "fd%3D2022-05-24%2019%3A01%3A22%7C%7C%7Cep%3Dhttps%3A%2F%2Fpapersowl.com%2Ffree-plagiarism-checker%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F", "sbjs_first_add": "fd%3D2022-05-24%2019%3A01%3A22%7C%7C%7Cep%3Dhttps%3A%2F%2Fpapersowl.com%2Ffree-plagiarism-checker%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F", "sbjs_current": "typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29", "sbjs_first": "typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29", "sbjs_udata": "vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%206.3%3B%20Win64%3B%20x64%3B%20rv%3A100.0%29%20Gecko%2F20100101%20Firefox%2F100.0", "sbjs_session": "pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fpapersowl.com%2Ffree-plagiarism-checker", "_ga_788D7MTZB4": "GS1.1.1653411683.1.0.1653411683.0", "_ga": "GA1.1.1828699233.1653411683", "trustedsite_visit": "1", "trustedsite_tm_float_seen": "1", "AppleBannercookie_hide_header_banner": "1", "COOKIE_PLAGIARISM_CHECKER_TERMS": "1", "plagiarism_checker_progress_state": "1"}

        burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0", "Accept": "*/*", "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://papersowl.com/free-plagiarism-checker", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://papersowl.com", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "no-cors", "Sec-Fetch-Site": "same-origin", "Pragma": "no-cache", "Cache-Control": "no-cache", "Te": "trailers", "Connection": "close"}

        burp0_data = {"is_free": "false", "plagchecker_locale": "en", "product_paper_type": "1", "title": '', "text": str(text_to_check)}

        r = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
        text_list = text_to_check.split(' ')
        result = json.loads(r.text)
        cur = []
        for match in result['matches']:
            new_match = {}
            new_match['url'] = match['url']
            new_match['percent']= match['percent']
            new_match['similarity'] = []
            for high in match['highlight']:
                new_match['similarity'].append(" ".join(text_list[int(high[0]):int(high[1])+1]))
            cur.append(new_match)
            
        return JsonResponse({"text": text_to_check,"matches":cur} , status=200)




        

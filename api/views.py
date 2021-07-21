from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
import urllib.request


class MadLib(APIView):
    @staticmethod
    def get(request):
        word_url = 'https://reminiscent-steady-albertosaurus.glitch.me/'
        verb = urllib.request.urlopen(word_url + 'verb').read().decode()[1:-1]
        adjective = urllib.request.urlopen(word_url + 'adjective').read().decode()[1:-1]
        noun = urllib.request.urlopen(word_url + 'noun').read().decode()[1:-1]
        sentence = "It was a {} day. I went downstairs to see if I could {} dinner. I asked, " \
                   "'Does the stew need fresh {}?'".format(adjective, verb, noun)
        return Response(sentence)

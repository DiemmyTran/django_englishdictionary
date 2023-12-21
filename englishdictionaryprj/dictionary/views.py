from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from pyparsing import Word
import pyttsx3
from PyDictionary import PyDictionary


# Create your views here.

def home(request):
    return render(request, 'home.html')


def search_word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()

    meaning = dictionary.meaning(search)
    synonym = dictionary.synonym(search)
    antonym = dictionary.antonym(search)

    context = {
        'search': search,
        'meaning': meaning,
        'synonym': synonym,
        'antonym': antonym,
    }
    return render(request, 'word.html', context)


def audio(request):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)  # for female voice
        engine.setProperty('rate', 150)

        search = request.GET.get('search')
        engine.say(search)

        audio_file = "output_voice.mp3"
        engine.save_to_file(search, audio_file)
        engine.runAndWait()

        return HttpResponse("Text converted to speech!")




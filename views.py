from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed


    if fullcaps=="on":
        analyzed=djtext.upper()
        params = {'purpose': 'converted to upper case', 'analyzed_text': analyzed}
        djtext=analyzed


    if newlineremover=="on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed=analyzed + char
        params = {'purpose': 'NewLineRemoved', 'analyzed_text': analyzed}
        djtext = analyzed


    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] ==" " and djtext[index+1] ==" "):
                analyzed=analyzed+char
        params = {'purpose': 'extraspaceremoved', 'analyzed_text': analyzed}
        djtext = analyzed


    if charcount =="on":
        analyzed=len(djtext)
        params = {'purpose': 'charcounted', 'analyzed_text': analyzed}


    if removepunc != "on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover != "on":
        return HttpResponse("please choose any of the options")


    return render(request, 'analyze.html', params)

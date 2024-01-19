from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse('''<h1>Home</h1>
    <a href='https://aniwatchtv.to/'>Aniwatch Website for Anime's</a>
    <a href='http://127.0.0.1:8000/capitalizeFirst'>capitalizeFirst</a>
    <a href='http://127.0.0.1:8000/removepunc'>removepunc</a>
    <a href='http://127.0.0.1:8000/newlineremover'>newlineremover</a>
    <a href='http://127.0.0.1:8000/spaceremover'>spaceremover</a>
    <a href='http://127.0.0.1:8000/charcount'>charcount</a>''')

def capitalizeFirst(request):
    return HttpResponse('''<h1>Capitalize first letter</h1>
    <a href='http://127.0.0.1:8000/Home'>Home</a>
    <a href='http://127.0.0.1:8000/removepunc'>removepunc</a>
    <a href='http://127.0.0.1:8000/newlineremover'>newlineremover</a>
    <a href='http://127.0.0.1:8000/spaceremover'>spaceremover</a>
    <a href='http://127.0.0.1:8000/charcount'>charcount</a>''')

def removepunc(request):
    djtext = request.POST.get('text', 'default')
    return HttpResponse('''<h1>Removed Punctuations</h1>
    <a href='http://127.0.0.1:8000/Home'>Home</a>
    <a href='http://127.0.0.1:8000/capitalizeFirst'>capitalizeFirst</a>
    <a href='http://127.0.0.1:8000/newlineremover'>newlineremover</a>
    <a href='http://127.0.0.1:8000/spaceremover'>spaceremover</a>
    <a href='http://127.0.0.1:8000/charcount'>charcount</a>''')

def newlineremover(request):
    return HttpResponse('''<h1>New Line Remover</h1>
    <a href='http://127.0.0.1:8000/Home'>Home</a>
    <a href='http://127.0.0.1:8000/capitalizeFirst'>capitalizeFirst</a>
    <a href='http://127.0.0.1:8000/removepunc'>removepunc</a>
    <a href='http://127.0.0.1:8000/spaceremover'>spaceremover</a>
    <a href='http://127.0.0.1:8000/charcount'>charcount</a>''')

def spaceremover(request):
    return HttpResponse('''<h1>Space Removed</h1>
    <a href='http://127.0.0.1:8000/Home'>Home</a>
    <a href='http://127.0.0.1:8000/capitalizeFirst'>capitalizeFirst</a>
    <a href='http://127.0.0.1:8000/removepunc'>removepunc</a>
    <a href='http://127.0.0.1:8000/newlineremover'>newlineremover</a>
    <a href='http://127.0.0.1:8000/charcount'>charcount</a>''')

def charcount(request):
    return HttpResponse('''<h1>Character Count</h1>
    <a href='http://127.0.0.1:8000/Home'>Home</a>
    <a href='http://127.0.0.1:8000/capitalizeFirst'>capitalizeFirst</a>
    <a href='http://127.0.0.1:8000/removepunc'>removepunc</a>
    <a href='http://127.0.0.1:8000/newlineremover'>newlineremover</a>
    <a href='http://127.0.0.1:8000/spaceremover'>spaceremover</a>''')


#TextUtils website backend codes starts from here the above ones are for experimenting with HTTPresponse
def about(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text from the user
    djtext = request.POST.get('text','default')

    # Check which check box is ticked
    rempunc = request.POST.get('removepunc', 'off')
    capitalizeFirst = request.POST.get('capitalizeFirst', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('spaceremover', 'off')
    charactercount = request.POST.get('charactercount', 'off')
    wordcount = request.POST.get('wordcount', 'off')

    punc_list = '''.,?!:;"'()[]{}-_/\&@#$%^*'''

    params={}
    #Remove Punctuations
    if rempunc == 'on':
        analyzed_text = ''
        for char in djtext:
            if char not in punc_list:
                analyzed_text = analyzed_text+char
        params = {'purpose':'Remove Punctuation', 'analyzed_text':analyzed_text}
        djtext = analyzed_text
        #return render(request, 'analyze.html', params)

    #Capitalize Every Letter in the text
    if capitalizeFirst == 'on':
        analyzed_text = ''
        analyzed_text = djtext.upper()
        params = {'purpose': 'capitalizeFirst', 'analyzed_text': analyzed_text}
        djtext = analyzed_text
        #return render(request, 'analyze.html', params)

    #Remove new lines from the text
    if newlineremover == 'on':
        analyzed_text = ''
        for char in djtext:
            if char != "\n" and char != '\r':
                analyzed_text = analyzed_text + char
        params = {'purpose':'New Line Remover', 'analyzed_text':analyzed_text}
        djtext = analyzed_text
        #return render(request, 'analyze.html', params)

    #Remove extra spaces from the text using indexing by enumerate function
    if extraspaceremover == 'on':
        analyzed_text = ''
        for index,char in enumerate(djtext):
            if djtext[index] == ' ' and djtext[index+1] == ' ':
                pass
            else:
                analyzed_text = analyzed_text+char
        params = {'purpose':'Extra Space Remover', 'analyzed_text':analyzed_text}
        djtext = analyzed_text
        #return render(request, 'analyze.html', params)

    #Count the number of characters in the text
    if charactercount == 'on':
        analyzed_text = ''
        count = len(djtext)
        params = {'purpose':'Count the Number of Characters', 'analyzed_text':count}
        return render(request,'analyze.html', params)

    if wordcount == 'on':
        analyzed_text = ''
        words = djtext.split(' ')
        count = len(words)
        params = {'purpose': 'Count the Number of words', 'analyzed_text': count}
        return render(request, 'analyze.html', params)
    #else:
    if rempunc == 'off' and capitalizeFirst == 'off' and newlineremover == 'off' and extraspaceremover == 'off':
        return HttpResponse('Error: Please check a check box')

    return render(request, 'analyze.html', params)


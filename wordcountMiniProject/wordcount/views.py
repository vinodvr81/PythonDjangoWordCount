from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,"homepage.html")


def word_count(request):
    fulltext = request.GET['subject']
    countfre = dict()
    words = fulltext.split()

    for word in words:
        if word in countfre:
            countfre[word] += 1
        else:
            countfre[word] = 1
    sortedwords = sorted(countfre.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,"counts.html",{'fulltext': fulltext, 'counttotal':len(words), 'sortedwords':sortedwords})

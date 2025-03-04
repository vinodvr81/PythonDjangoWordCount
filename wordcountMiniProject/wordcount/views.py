from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,"homepage.html")


def word_count(request):
    fulltext = request.GET['subject']
    countFrequency = dict()
    words = fulltext.split()

    for word in words:
        if word in countFrequency:
            countFrequency[word] += 1
        else:
            countFrequency[word] = 1
    sortedwords = sorted(countFrequency.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,"counts.html",{'fulltext': fulltext, 'counttotal':len(words), 'sortedwords':sortedwords})

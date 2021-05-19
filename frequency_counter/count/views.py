from collections import Counter
from django.shortcuts import render, redirect
from .models import frequency_model,count_model
from bs4 import BeautifulSoup
import requests
import operator
import re
import nltk
from .stop_words import stops
def frequency_form(request):
    global url
    if request.method=="POST":
        m=frequency_model()
        url=request.POST.get('url')
        m.website=url
        m.save()
        #print(url)
        return redirect(count_word)
    else:
        return render(request,'home.html')

def count_word(request):
        print(url)
        global results, raw_word_count, result
        results = {}
        errors = []
        try:
            r = requests.get(url)
        except:
            errors.append(
                "Unable to get URL. Please make sure it's valid and try again."
            )
            return render(request,'counter.html', {'errors':errors})
        if r:
            # text processing
            nltk.download('punkt')
            raw = BeautifulSoup(r.text, 'html.parser').get_text()
            nltk.data.path.append('./nltk_data/')  # set the path
            tokens = nltk.word_tokenize(raw)
            text = nltk.Text(tokens)
            # remove punctuation, count raw words
            nonPunct = re.compile('.*[A-Za-z].*')
            raw_words = [w for w in text if nonPunct.match(w)]
            raw_word_count = Counter(raw_words)
            # stop words
            no_stop_words = [w for w in raw_words if w.lower() not in stops]
            no_stop_words_count = Counter(no_stop_words)
            #print(no_stop_words_count)
            results = sorted(
                no_stop_words_count.items(),
                key=operator.itemgetter(1),
                reverse=True
            )[:10]
            result = count_model(
                count=no_stop_words_count
            )
            result.save()
            #print(results)
        return render(request,'counter.html',{'results':results})


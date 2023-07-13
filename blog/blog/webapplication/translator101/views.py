from django.shortcuts import render
from . import translate


# Create your views here.

def trans(requests):
    if requests.method == 'POST':

        original_text = requests.POST['my_textarea']
        output_text = translate.translate(original_text)
        return render(requests,'translator.html',{'output_text':output_text,'original_text':original_text})
    else:   
        return render(requests,"translator.html")

from django.shortcuts import render
from utils.scrape import img

def onePiece(request):
    list_of_img = img("one piece")
    if len(list_of_img) < 10:
        list_of_img = img("one piece")

    else :
        return render(request, 'customChara.html',{"imgs": list_of_img})

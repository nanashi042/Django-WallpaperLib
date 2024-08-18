from django.shortcuts import render
from utils.scrape import img

def onePiece(request):
    list_of_img = img("one piece")
    return render(request, 'customChara.html',{"imgs": list_of_img})

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json, ast
from setgame.models import Card
from setgame.setgame import is_a_set

def base(request):
    return render(request, 'setgame/base.html')

def update_cards(request):
    cards = Card.objects.order_by('?')[:12]
    return render(request, 'setgame/cards.html', {'cards': cards})

@csrf_exempt
def card_click(request):
    if request.method == 'POST':
        selected_cards = [ast.literal_eval(c) for c in json.loads(request.POST.get('selectedCards'))]
        if is_a_set(selected_cards):
            return HttpResponse(content='You found a set!')
        else:
            return HttpResponse(content='This is not a set. Try again.')

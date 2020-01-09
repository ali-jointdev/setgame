from django.urls import path

import setgame.views

urlpatterns = [
        path('', setgame.views.base),
        path('update-cards/', setgame.views.update_cards),
        path('selected/', setgame.views.card_click),
]

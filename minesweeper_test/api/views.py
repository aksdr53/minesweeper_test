from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from . models import Game
from . minesweeper import Minesweeper


@api_view(('POST',))
def new(request):
    data = request.data
    game = Minesweeper(data.get('mines_count'), data.get('width'), data.get('height'),)
    game.start()
    field = ''
    for row in game.field:
        field += ''.join([str(elem) for elem in row])
    open_field = ''
    for row in game.open_field:
        for column in row:
            open_field += column
    Game.objects.create(
        width=game.width,
        height=game.height,
        mines_count=game.mines,
        game_id=game.game_id,
        completed=game.completed,
        field=field,
        open_field=open_field,
        opend=game.opend
    )
    data = {
        'game_id': game.game_id,
        'width': game.width,
        'height': game.height,
        'mines_count': game.mines,
        'completed': game.completed,
        'field': game.open_field,
    }

    return Response(data=data)
    

@api_view(('POST',))
def turn(request):
    data = request.data
    game_id = data.get('game_id')
    col = data.get('col')
    row = data.get('row')
    game_obj = get_object_or_404(Game, game_id=game_id)
    count = 0
    open_field= []
    field= []
    for i in range(game_obj.height):
        open_field.append([])
        for j in range(game_obj.width):
            open_field[i].append(game_obj.open_field[count])
            count += 1
    count = 0
    for i in range(game_obj.height):
        field.append([])
        for j in range(game_obj.width):
            if game_obj.field[count] == 'M':
                field[i].append(game_obj.field[count])
                count += 1
            else:
                field[i].append(int(game_obj.field[count]))
                count += 1
    game = Minesweeper(game_obj.mines_count, game_obj.width,
                       game_obj.height, game_obj.completed,
                       open_field, field, game_obj.game_id,
                       game_obj.opend)
    game.turn(row, col)
    data = {
        'game_id': game.game_id,
        'width': game.width,
        'height': game.height,
        'mines_count': game.mines,
        'completed': game.completed,
        'field': game.open_field,
    }
    open_field = ''
    for row in game.open_field:
        for column in row:
            open_field += column
    game_obj.open_field = open_field
    game_obj.opend = game.opend
    game_obj.completed = game.completed
    game_obj.save(update_fields=['open_field', 'opend', 'completed'])
    
    return Response(data=data)

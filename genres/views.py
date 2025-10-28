import json
from django.http import JsonResponse
from genres.models import Genre
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

@csrf_exempt
def genre_create_list_view(request):
    if request.method == 'GET':
      genres = Genre.objects.all()
      data = [{"id": genre.id, "name": genre.name} for genre in genres]
      return JsonResponse(data, safe=False)
    elif request.method == 'POST':
     data = json.loads(request.body.decode('utf-8'))
     new_genre = Genre(name=data['name'])
     new_genre.save()
     return JsonResponse({"id": new_genre.id, "name": new_genre.name}, status=201)

@csrf_exempt   
def genre_detail_view(request, genre_id):
    try:
        genre = Genre.objects.get(id=genre_id)
        data = {"id": genre.id, "name": genre.name}
        return JsonResponse(data)
    except Genre.DoesNotExist:
        return JsonResponse({"error": "Genre not found"}, status=404)

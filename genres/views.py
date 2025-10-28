from django.http import JsonResponse
from genres.models import Genre


def genre_list_view(request):
    genres = Genre.objects.all()
    genre_list = [{"id": genre.id, "name": genre.name} for genre in genres]
    return JsonResponse(genre_list, safe=False)

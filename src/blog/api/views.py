from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def favorites(request):
    try:
        user = request.user
        favorites_id = [favorite.id for favorite in user.favorites.all()]
        return Response({'status': 'success', 'favorites': favorites_id})
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)})


@api_view(['POST'])
def add_favorite(request):
    try:
        user = request.user
        recipe_id = request.data.get('recipe_id')
        user.favorites.add(recipe_id)
        return Response({'status': 'success'})
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)})


@api_view(['POST'])
def delete_favorite(request):
    try:
        user = request.user
        recipe_id = request.data.get('recipe_id')
        user.favorites.remove(recipe_id)
        return Response({'status': 'success'})
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)})

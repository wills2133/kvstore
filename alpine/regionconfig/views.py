from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@csrf_exempt
def kvstore(request, key, value=None, format=None):

    if request.method == 'GET':
        valueBytes = r.get(key)
        if valueBytes:
            payload = {key:str(valueBytes, encoding='utf-8')}
            return Response(payload, status=status.HTTP_201_CREATED)
        else:
            payload = {key:"key is not found"}
            return Response(payload, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        created = r.set(key, value)
        payload = {key:value}
        if created:
            return Response(payload, status=status.HTTP_201_CREATED)
        else:
            return Response(payload, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        created = r.set(key, value)
        payload = {key:value}
        if created:
            return Response(payload, status=status.HTTP_201_CREATED)
        else:
            return Response(payload, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        deleted = r.delete(key)
        if deleted:
            payload = {key:"deleted"}
            return Response(payload, status=status.HTTP_201_CREATED)
        else:
            payload = {key:"key is not found"}
            return Response(key, status=status.HTTP_204_NO_CONTENT)
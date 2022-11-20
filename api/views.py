import jwt, datetime
from django.http import Http404

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated

from users.models import * 
from .serializers import *

@api_view(['GET'])
def get_routes(request):
    api_urls = {
        'register': '/api/register/',
        'login': '/api/login/',
        'logout': '/api/logout/',
        'get_series': '/api/get-series/',
        'series': '/api/series/${id}/',
        'create_series': '/api/create-series/',
        'update_series': '/api/update-series/${id}/',
        'delete_series': '/api/delete-series/${id}/',
        'get_issues_by_series': '/api/series/${id}/issues/',
        'issue': '/api/issues/${id}/',
        'create_issue': '/api/create-issue/',
        'update_issue': '/api/update-issue/${id}/',
        'delete_issue': '/api/delete-issue/${id}/'
    }

    return Response(api_urls)

# auth

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    email = request.data['email']
    password = request.data['password']

    user = User.objects.filter(email=email).first()

    if user is None:
        raise AuthenticationFailed('user not found!')
    if not user.check_password(password):
        raise AuthenticationFailed('incorrect password!')

    payload = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, 'secret', algorithm='HS256')
    response = Response()

    response.set_cookie(key='jwt', value=token, httponly=True)

    response.data = {'jwt': token}

    return response

@api_view(['POST'])
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {'message': 'success'}
    return response


# series

@api_view(['GET'])
def get_series(request):
    series_list = Series.objects.all()
    serializer = SeriesSerializer(series_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def series(request, pk):
    series = Series.objects.get(id=pk)
    serializer = SeriesSerializer(series)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_series(request):
    try:
        serializer = SeriesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    except:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_series(request, pk):
    series = Series.objects.get(id=pk)

    try:
        serializer = SeriesSerializer(instance=series, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    except:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_series(request, pk):
    try:
        series = Series.objects.get(id=pk)
        series.delete()

        if series is None:
            raise Http404

        return Response({'message': 'Success'}, status=status.HTTP_200_OK)

    except:
        return Response({'message': 'Unprocessible Entity'})

    
# issues

@api_view(['GET'])
def get_issues_by_series(request, pk):
    issues = Issue.objects.filter(
        series_id=str(pk)).all()
    serializer = IssueSerializer(issues, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def issue(request, pk):
    issue = Issue.objects.get(id=pk)
    serializer = IssueSerializer(issue)
    return Response(serializer.data, status=status.HTTP_200_OK)    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_issue(request):
    try:
        serializer = IssueSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    except:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_issue(request, pk):
    issue = Issue.objects.get(id=pk)

    try:
        serializer = IssueSerializer(instance=issue, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    except:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_issue(request, pk):
    try:
        issue = Issue.objects.get(id=pk)
        issue.delete()

        if issue is None:
            raise Http404

        return Response({'message': 'Success'}, status=status.HTTP_200_OK)

    except:
        return Response({'message': 'Unprocessible Entity'})
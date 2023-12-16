from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Dashboard
from .serializers import DashboardSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from project.models import Dashboard
from django.http import JsonResponse
from datetime import datetime
from django.shortcuts import render
from .forms import DashboardForm
import json
@csrf_exempt
def save_json(request):
    if request.method == "POST":
        try:
            received_data = json.loads(request.body)
            for payload in received_data:
                intensity = payload.get('intensity')
                sector = payload.get('sector')
                insight = payload.get('insight')
                url = payload.get('url')
                impact = payload.get('impact')
                # added = payload.get('added')
                # published = payload.get('published')
                added = datetime.strptime(payload.get('added'), '%B, %d %Y %H:%M:%S')
                published = datetime.strptime(payload.get('published'), '%B, %d %Y %H:%M:%S')
                pestle = payload.get('pestle')
                source = payload.get('source')
                likelihood = payload.get('likelihood')
                relevance = payload.get('relevance')
                start_year = payload.get('start_year')  # Assuming the JSON has start_year and end_year
                end_year = payload.get('end_year')
                country = payload.get('country')
                topic = payload.get('topic')
                region = payload.get('region')
                city = payload.get('city')
                title = payload.get('title')
                if start_year:
                    start_year = int(start_year)
                else:
                    start_year = None
                
                # Handle empty end_year field
                if end_year:
                    end_year = int(end_year)
                else:
                    end_year = None
            
                # Creating Dashboard object
                dashboard = Dashboard.objects.create(
                    intensity=intensity,
                    sector=sector,
                    insight=insight,
                    source=source,
                    pestle=pestle,
                    impact=impact,
                    url=url,
                    added=added,
                    published=published,
                    likelihood=likelihood,
                    relevance=relevance,
                    start_year=start_year,
                    end_year=end_year,
                    country=country,
                    topic=topic,
                    region=region,
                    city=city,
                    title = title,
                )
                
            return JsonResponse({'message': 'JSON data has been saved successfully'})
        
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON format', 'details': str(e)})
        
        except Exception as ex:
            return JsonResponse({'error': 'Error processing JSON data', 'details': str(ex)})

    return JsonResponse({'error': 'Please use a POST request to send JSON data'})

@api_view(['GET'])
def get(request):
    data = Dashboard.objects.all()
    serialized_data = DashboardSerializer(data, many=True)
    return Response({
        "data": serialized_data.data,
        "message": "All Dashboard data retrieved successfully"
    }, status=status.HTTP_200_OK)
@api_view(['POST'])
def create(request):
    serialized_data = DashboardSerializer(data=request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return Response({
            "data": serialized_data.data,
            "message": "New Dashboard created successfully"
        }, status=status.HTTP_201_CREATED)
    return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def get_detail(request, pk):
    try:
        data = Dashboard.objects.get(pk=pk)
        serialized_data = DashboardSerializer(data)
        return Response({
            "data": serialized_data.data,
            "message": f"Data of selected dashboard with ID {pk}"
        }, status=status.HTTP_200_OK)
    except Dashboard.DoesNotExist:
        return Response({
            "status": status.HTTP_404_NOT_FOUND,
            "code": "invalid-request",
            "message": "Dashboard not found"
        }, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update(request, pk):
    try:
        data = Dashboard.objects.get(pk=pk)
    except Dashboard.DoesNotExist:
        return Response({
            "status": status.HTTP_404_NOT_FOUND,
            "code": "invalid-request",
            "message": "Dashboard not found"
        }, status=status.HTTP_404_NOT_FOUND)
    
    serialized_data = DashboardSerializer(data, data=request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return Response({
            "data": serialized_data.data,
            "message": f"Data of selected dashboard with ID {pk} updated"
        }, status=status.HTTP_200_OK)
    
    return Response({
        "status": status.HTTP_400_BAD_REQUEST,
        "code": "invalid-data",
        "message": "Invalid data provided for update"
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete(request, pk):
    try:
        data = Dashboard.objects.get(pk=pk)
        data.delete()
        return Response({
            "message": f"Data of selected dashboard with ID {pk} deleted"
        }, status=status.HTTP_204_NO_CONTENT)
    except Dashboard.DoesNotExist:
        return Response({
            "status": status.HTTP_404_NOT_FOUND,
            "code": "invalid-request",
            "message": "Dashboard not found"
        }, status=status.HTTP_404_NOT_FOUND)


def index(request):
    data = Dashboard.objects.all()
    
    if request.method == 'POST':
        form =  DashboardForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DashboardForm()
        
    context = {
        "data": data,
        "form": form
    }
    
    return render(request,'index.html', context)

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def status(request):
    return Response({
        'status': 'success',
        'message': 'CSC 325 CI/CD Pipeline is working!',
        'version': 1
    })
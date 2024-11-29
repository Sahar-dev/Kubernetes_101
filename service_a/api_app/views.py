from django.http import JsonResponse

def data_view(request):
    data = {
        'items': ['Apple', 'Banana', 'Cherry']
    }
    return JsonResponse(data)

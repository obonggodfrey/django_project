from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Hello World from Django!</h1>")

def add(request):
    num1 = int(request.GET.get('num1'))
    num2 = int(request.GET.get('num2'))
    result = num1 + num2
    return HttpResponse(f"<h1>Result: {result}</h1>")
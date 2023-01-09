from django.shortcuts import render

# Create your views here.
def first(request):
    d={'chinnu':'manu','manu':'kutty'}
    return render(request,'first.html',d)
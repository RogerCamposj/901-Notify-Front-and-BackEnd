from django.shortcuts import render

# Create your views here.


def retornar_index(request):

    return render(request, 'index.html')

def mylinkview(request):

    # ... your python code/script
    return HttpResponseRedirect('## your redirect template url ##')
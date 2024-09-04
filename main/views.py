from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306275203',
        'name': 'Malika Atha Indurasmi',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
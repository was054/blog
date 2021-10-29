from django.shortcuts import render



def index(request):
    data = {
        'title': 'Главная страница',
        'values': '["Some","Hello"]',
        'obj':{
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }

    }
    return render(request, 'mainapp/index.html', data)

def about(request):
    return render(request, 'mainapp/about.html')
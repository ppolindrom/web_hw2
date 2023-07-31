from django.shortcuts import render


def index(request):
    """Контроллер, который отвечает за отображение домашней страницы."""

    return render(request, 'catalog/home.html')


def contacts(request):
    """Контроллер, который отвечает за отображение контактной информации."""

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')

    return render(request, 'catalog/contacts.html')
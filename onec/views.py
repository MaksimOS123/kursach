from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}

    return render(request, 'main_page.html', context)

def spravochnik(request):
    context = {}

    table_l = ['Общие', 'Константы', 'Справочники', 'Документы', 'Перечисления', 'Отчеты', 'Обработки', 'Регистры']
    context['table_l'] = table_l
    context['active'] = 'Общие'
    return render(request, 'spravochnik.html', context)
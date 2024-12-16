from django.shortcuts import render
from onec.forms import SignInForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from onec.models import UserProfile
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    context = {}
    if not request.user.is_anonymous:
        context['User'] = request.user
        

    return render(request, 'main_page.html', context)

def spravochnik(request):
    context = {}

    if not request.user.is_anonymous:
        context['User'] = request.user

    table_l = [{'text': 'Общие', 'name': 'ob'}, {'text': 'Константы', 'name': 'const'}, {'text': 'Справочники', 'name': 'spr'}, \
               {'text': 'Документы', 'name': 'doc'}, {'text': 'Перечисления', 'name': 'per'}, {'text': 'Отчеты', 'name': 'otch'}, \
                {'text': 'Обработки', 'name': 'obr'}, {'text': 'Регистры', 'name': 'reg'}]
    context['table_l'] = table_l
    context['active'] = 'ob'

    table_r = [
        {'name':'ob', 'text': ['Вкладка «Общие» в конфигураторе 1С позволяет настроить параметры, связанные с общими объектами конфигурации.', 'На этой вкладке описываются такие объекты, как подсистемы, общие модули, параметры сеанса, роли, планы обмена, критерии отбора, общие формы, интерфейсы, общие макеты, общие картинки, стили, языки.', 'Эти объекты предназначены для установки правил работы пользователей с данными, для описания вспомогательных объектов, используемых для формирования различных форм, в механизме обмена данными, а также содержат общие модули и макеты, доступные из любого модуля конфигурации.', 'Кроме того, на закладке «Общие» указывается, нужно ли только создавать объекты управляемого приложения или следует создавать объекты, которые есть и в обычном приложении.']},  
        {'name':'const', 'text': ["Константы в 1С — это прикладные объекты конфигурации, которые позволяют хранить в информационной базе данные, которые не изменяются во времени или изменяются очень редко.", "Одна константа хранит одно значение. Например, в константе может храниться наименование организации, её УНП (ИНН), дата регистрации и другая информация.", "В константах 1С 8.3 можно хранить значение по умолчанию (название организации, основную валюту, единицы измерения, данные для обновления в типовых конфигурациях, настройки программы 1С).", "Чтобы добавить константу в конфигурацию, необходимо открыть дерево объектов метаданных, выделить узел «Константы» и нажать кнопку «ins» или можно добавить с помощью контекстного меню при помощи мыши."]},
        {'name':'spr', 'text': ['Справочники в 1С — это прикладные объекты конфигурации, позволяющие хранить в информационной базе данные, имеющие одинаковую структуру и списочный характер.', 'В справочниках могут храниться, например, списки сотрудников, перечень товаров, список поставщиков или покупателей.', 'Справочники наполняются самостоятельно компанией и используются в соответствии с видом деятельности и потребностями.']},
        {'name': 'doc', 'text': ['Документы в 1С — это объекты конфигурации, которые позволяют хранить информацию о совершённых хозяйственных операциях или о событиях, произошедших на предприятии.', 'Это могут быть, например, приходные накладные, приказы о приёме на работу, счета, платёжные поручения и т. д.', 'Структура документа включает:', '·Реквизиты (номер, дата, время создания документа, данные о поставщике).', '·Табличную часть (информация о товаре, сумме сделки, складе, на который приходуется продукция)', '·Строку для комментария', 'Каждому документу система автоматически присваивает порядковый номер, дату и время создания. Это позволяет установить строгую временную последовательность совершения операций.']},
        {'name': 'per', 'text': ['Перечисления в 1С — это объекты конфигурации, которые содержат в себе постоянные значения, не изменяемые в процессе работы с программой.', 'Они задаются на этапе конфигурирования, и их нельзя менять пользователю во время работы программы.', 'Перечисления используются, чтобы хранить в информационной базе 1С фиксированный список значений, который не изменяется в процессе работы пользователей.']},
        {'name': 'otch', 'text': ['Отчёты в 1С — это прикладные объекты конфигурации, предназначенные для обработки накопленной информации и получения сводных данных в удобном для просмотра и анализа виде.', 'С их помощью можно создавать документы, отражающие показатели по всем направлениям деятельности организации.', 'Также в 1С предусмотрен набор типовых отчётов для бухгалтерского учёта, например: оборотно-сальдовая ведомость, шахматная ведомость, оборотно-сальдовая ведомость по счёту и другие.']},
        {'name': 'obr', 'text': ['Обработки в 1С — это специальные объекты конфигурации, предназначенные для изменения информации в базе данных или создания нового функционала для администратора или пользователей.', 'Они способствуют автоматизации и ускорению выполнения рутинных задач.', 'Условно обработки 1С можно разделить на две группы:', '1. Вспомогательные (встроенные). Используются для автоматизации небольших участков работы программистами 1С. Могут быть выведены как дополнительные интерфейсные решения (рабочий стол пользователя, обзор конфигурации), либо как часть функционала конфигурации (начальное заполнение базы данных, закрытие месяца).', '2. Внешние обработки. Это обработки, которые не входят в состав прикладного решения и не привязаны к конкретной конфигурации. Такие обработки можно использовать в решениях без изменения их структуры.', 'С помощью обработок можно, например, удалять из системы устаревшие данные, импортировать информацию из других систем и многое другое.']},
        {'name': 'reg', 'text': ['Регистры в 1С — это таблицы для накопления оперативных данных и получения сводной информации. Данные в регистры добавляются только при проведении документов.', 'Регистры подразделяются на четыре вида:', '1. Регистры сведений. Самый простой вид регистра, ресурс которого может иметь как числовые значения, так и другой тип данных. Примеры регистров сведений: курсы валют, учётная политика, размер базовой величины и др.', '2. Регистры накопления. Имеют два подвида — «Остатки» и «Обороты», которые предназначены для разных целей. Регистр накопления «Остатки» используется для получения информации о состоянии «на момент времени», а «Обороты» — информации о данных «за период». Примеры регистров накопления: товары на складах, денежные средства, взаиморасчёты с контрагентами.', '3. Регистры бухгалтерии. Предназначены для систематизации данных о бухгалтерских проводках, которые обязательно должны быть связаны со специальным объектом «План счетов». Примеры регистров бухгалтерии: журнал проводок бухгалтерского учёта, журнал проводок управленческого учёта.', '4. Регистры расчётов. Имеют самую сложную структуру и используются для реализации сложных периодических расчётов. В конфигурациях 1С — это, в первую очередь, расчёты заработной платы и других выплат сотрудникам. Примеры регистров расчёта: начисления, удержания.']}
    ]

    context['table_r'] = table_r

    return render(request, 'spravochnik.html', context)

def modul(request):
    context = {}

    if not request.user.is_anonymous:
        context['User'] = request.user

    return render(request, 'modul.html', context)


def sign_up(request):
    context = {}

    if not request.user.is_anonymous:
        return HttpResponseRedirect('/')

    context['title'] = 'Регистрация'
    context['errors'] = []

    if request.method == 'POST':
        f = SignInForm(request.POST)

        if f.is_valid():
            u_n = f.data['user_name']
            u_em = f.data['user_email']
            u_pw = f.data['password']
            u_pw_c = f.data['password_conf']

            if not is_existing_user(User.objects.all(), u_n):
                if u_pw == u_pw_c:
                    new_user = User.objects.create_user(username=u_n, email=u_em, password=u_pw)
                    new_user.save()
                    userProfile = UserProfile.objects.create(user=new_user, status="None")
                    userProfile.save()
                    login_user = authenticate(username=u_n, password=u_pw)
                    login(request, login_user)
                    return HttpResponseRedirect('/cong/')
                else:
                    context['errors'].append("Введенные пароли не совпадают")
            else:
                context['errors'].append("Пользователь с таким логином уже существует")

            context['form'] = f
        else:
            context['form'] = f
    else:
        f = SignInForm()
        context['form'] = f

    return render(request, 'registration/reg.html', context)


def cong(request):
    context = {}

    if not request.user.is_anonymous:
        context['User'] = request.user



    return render(request, 'cong.html', context)


def profile(request):
    context = {}

    if not request.user.is_anonymous:
        context['User'] = request.user

    user = UserProfile.objects.get(user=request.user)
    context['User2'] = user

    return render(request, 'profile.html', context)

@login_required
def edit(request):
    context = {}
    context['errors'] = []

    if not request.user.is_anonymous:
        context['User'] = request.user

    user = UserProfile.objects.get(user=request.user)
    context['User2'] = user

    if request.method == "POST":
        if request.POST.get('username') == user.user.username:
            e = request.POST.get('email')
            f_n = request.POST.get('first_name')
            l_n = request.POST.get('last_name')
            ae = request.POST.get('age')
            w = request.POST.get('work')
            s = request.POST.get('special')

            request.user.email = e
            request.user.save()
            user.first_name = f_n
            user.last_name = l_n
            user.age = ae
            user.work = w
            user.special = s
            user.save()
            return HttpResponseRedirect('/profile/')
        else:
            context['errors'].append('Нельзя менять логин')

    return render(request, 'edit_profile.html', context)


def ex(request):
    context = {}

    if not request.user.is_anonymous:
        context['User'] = request.user

    return render(request, 'onec.html', context)


def onec(request):
    context = {}

    if not request.user.is_anonymous:
        context['User'] = request.user

    return render(request, 'onec_what.html', context)


def is_existing_user(users_list, username):
    for user in users_list:
        if user.username == username:
            return True

    return False
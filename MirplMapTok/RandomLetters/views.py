from django.shortcuts import render

# from .forms import NameForm


def index(request):
    return render(request,
                  'RandomLetters/app_wrapper.html',
                  {'size_from': 50, 'size_to': 70, 'amount': 10})

def random_index(request):
    if request.method == 'GET':
        size_from = request.GET.get('size_from')
        size_to = request.GET.get('size_to')
        amount = request.GET.get('amount')
        random_list = []
        for i in range(amount):
            random_list.append()
    else:
        print("Unespected error")

    return render(request,
                  'RandomLetters/app_get_random_leters.html',
                  {'size_from': size_from, 'size_to': size_to, 'amount': amount})




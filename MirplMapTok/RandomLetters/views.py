from django.shortcuts import render

from .functions.randomletters import randname


def index(request):
    return render(request,
                  'RandomLetters/app_wrapper.html',
                  {'size_from': 50, 'size_to': 70, 'amount': 10})

def random_index(request):
    if request.method == 'GET':
        size_from = request.GET.get('size_from')
        size_to = request.GET.get('size_to')
        amount = request.GET.get('amount')
        
        if(int(size_from) > int(size_to)):
            size_from, size_to = size_to, size_from

        name_list = []
        for i in range(int(amount)):
            try:
                name_list.append(randname(size_from=int(size_from), size_to=int(size_to)))
            except Exception as err:
                print(err)
    else:
        print("Unespected error")

    return render(request,
                  'RandomLetters/app_get_random_leters.html',
                  {'size_from': size_from, 'size_to': size_to, 'amount': amount, 'name_list': name_list})




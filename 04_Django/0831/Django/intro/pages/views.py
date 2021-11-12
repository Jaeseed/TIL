from django.shortcuts import render



def dinner(request, menu, number:int):
    context ={
        'menu' : menu,
        'people' : number
    }
    return render(request, 'dinner.html', context)

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")


def new(request):
    return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")

def create(request):
    return redirect('/')

def show(request,num):
    number={'number':num}
    return render(request,'blog.html', number)

def edit(request,num):
    number=num
    return HttpResponse(f'placeholder para editar el blog {number}')

def destroy(request,num):
    return redirect('/')

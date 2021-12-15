from django.shortcuts import render

# Create your views here.


def reg_view(request):
    return render(request, 'user/register.html', locals())
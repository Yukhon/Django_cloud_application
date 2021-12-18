from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Note


def check_login(fn):
    def wrap(request, *args, **kwargs):
        if 'username' not in request.session or 'uid' not in request.session:
            c_username = request.COOKIES.get('username')
            c_uid = request.COOKIES.get('uid')
            if not c_username or not c_uid:
                return HttpResponseRedirect('/user/login')
            else:
                request.session['username'] = c_username
                request.session['uid'] = c_uid
        return fn(request, *args, **kwargs)

    return wrap


# Create your views here.
@check_login
def add_note_view(request):
    if request.method == 'GET':
        return render(request, 'note/add_note.html')
    elif request.method == 'POST':
        uid = request.session['uid']
        title = request.POST['topic']
        content = request.POST['content']
        Note.objects.create(title=title, content=content, user_id=uid)
        return HttpResponse('add note successfully!')


@check_login
def note_index_view(request):
    s_id = request.session['uid']
    s_name = request.session['username']
    notes = Note.objects.filter(user_id=s_id)
    return render(request, 'note/note_index.html', locals())


@check_login
def update_view(request, id):
    note = Note.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'note/update_note.html', locals())
    elif request.method == 'POST':
        note.title = request.POST['topic']
        note.content = request.POST['content']
        note.save()
        return HttpResponse('updated successfully')



@check_login
def del_view(request, id):
    note = Note.objects.get(id=id)
    note.is_active = False
    note.save()
    return HttpResponseRedirect('/note/all')


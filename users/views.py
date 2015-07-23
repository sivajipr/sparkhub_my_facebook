from django.shortcuts import render_to_response,render
from users.forms import RegisterForm, ProfileForm, EditUserForm, UserImageForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.db.models import Q
from users.models import Profile, UserImage, Friend
from event.models import Picture
from Post.models import Post, Gallery
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
import json
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_exist = User.objects.filter(username=form.cleaned_data['username'])
            if not user_exist:
                user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'], first_name=form.cleaned_data['first_name'], password=form.cleaned_data['password1'], last_name=form.cleaned_data['last_name'])
                return HttpResponseRedirect('/login')
            else:
                 print 'username already exists'
    else:
        form = RegisterForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'users/register.html',
    variables,
    )

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login')

def home(request):
    user = request.user
    friends = user.profile.get_friends()
    if not user.is_authenticated():
        return render(request, 'users/logouthome.html')
    else:
        posts = Post.objects.filter(user__in =friends).order_by('-create_date')
        return render(request, 'users/loginhome.html', {'posts':posts})

def edit_profile(request):
    user=request.user
    users=User.objects.get(username=user)
    profile = Profile.objects.get(user=user)
    if request.method == 'POST':
        form1 = EditUserForm(request.POST, instance=users)
        # form2 = EditForm(request.POST)
        form2 = ProfileForm(request.POST, instance=profile)
        form3 = UserImageForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            if not form3.cleaned_data['profile_pic'] and form3.cleaned_data['cover_pic']:
                UserImage.objects.filter(user=user).update(is_active_cover = False)
            if not form3.cleaned_data['cover_pic'] and form3.cleaned_data['profile_pic']:
                UserImage.objects.filter(user=user).update(is_active_profile = False)
            if form3.cleaned_data['cover_pic'] and form3.cleaned_data['profile_pic']:
                UserImage.objects.filter(user=user).update(is_active_profile = False, is_active_cover= False)
            image = form3.save(commit=False)
            image.user = user
            image.is_active_profile = True
            image.is_active_cover = True
            image.is_public = True
            image.save()
            form2.save()
            form1.save()
            return HttpResponseRedirect('/home')
    else:
        form1 = EditUserForm(instance=users)
        form2 = ProfileForm(instance=profile)
        form3 = UserImageForm()

    variables = RequestContext(request, {'form1': form1, 'form2':form2, 'form3':form3})
 
    return render_to_response(
    'users/editprofile.html',
    variables,
    )

def showpost(request):
    user=request.user
    posts=Post.objects.filter(user=user).order_by('-create_date')
    return render(request, 'users/loginhome.html', {'posts':posts})

def user_page(request,user):
    req=request.user
    user=User.objects.get(username=user)
    frnd = Friend.objects.filter(Q(acceptor=req, creator=user)|Q(acceptor=user, creator=req))
    images = UserImage.objects.all().order_by('-create_date')
    posts=Post.objects.filter(user=user).order_by('-create_date')
    gal = Gallery.objects.last()
    pic = Picture.objects.last()
    requests = Friend.objects.filter(acceptor=user,status=0)
    number_of_requests=len(requests)
    return render(request,'users/userpage.html',{'number_of_requests':number_of_requests, 'entity':user, 'gal':gal,'pic':pic,'frnd':frnd, 'posts':posts, 'images':images})

def user_pic_show(request, user):
    user=User.objects.get(username=user)
    images = UserImage.objects.all().order_by('-create_date')
    pic = Picture.objects.last()
    gal = Gallery.objects.last()
    posts = Gallery.objects.all().order_by('-create_date')
    return render(request, 'users/userphotos.html',{'entity':user, 'posts':posts, 'images':images, 'gal':gal,'pic':pic})
    
def usersearch(request):
    name = request.GET['name']
    if ' ' in name:
        users = User.objects.filter(first_name=name.split(' ')[0],last_name=name.split(' ')[1])
    else:
        users = User.objects.filter(Q(username__iexact=name)|Q(first_name__iexact=name)|Q(last_name__iexact=name))
    return render(request,'users/usersearch.html',{'users':users, 'name':name})

def auto_complete(request):
    data=[]
    term = request.GET['term']
    users = User.objects.filter(Q(username__icontains=term)|Q(first_name__icontains=term)|Q(last_name__icontains=term))
    for user in users:
        d={}
        d['label'] = user.get_full_name()
        d['id'] = user.profile.get_avatar.url
        data.append(d)
    print data
    return HttpResponse(json.dumps(data), content_type="application/json")
    
def addfriend(request,id):
    user = request.user
    entity = User.objects.get(id=id)
    frnd = Friend(creator=user,acceptor=entity)
    frnd.save()
    return render(request,'users/usersearch.html')

def user_friend_list(request,user):
    user = get_object_or_404(User,username=user)
    friends_cre = Friend.objects.filter(creator=user,status=1)
    friends_acc = Friend.objects.filter(acceptor=user,status=1)
    return render(request, 'users/friends.html', {'friends_cre':friends_cre, 'friends_acc':friends_acc, 'entity':user})

def user_friend_request(request,user):
    user = get_object_or_404(User,username=user)
    friends = Friend.objects.filter(acceptor=user,status=0)
    return render(request, 'users/friendreq.html',{'friends':friends})

def accept(request,id):
    print 'fddfdf'
    re=request.user
    print re
    friend = Friend.objects.get(id=id)
    friend.status=1
    friend.save()
    print 'bbbbbbbbb'
    return render(request, 'users/friends.html',{'friend':friend})

def reject(request,id):
    print 'reject'
    re=request.user
    print re
    friend = Friend.objects.filter(id=id).delete()
    print 'rejsucss'
    return render(request, 'users/friends.html',{'friend':friend})
from django.shortcuts import render
from Post.models import Post
from event.models import Event
from generic.models import Like, Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
import json
from django.core.urlresolvers import reverse

# Create your views here.



def like_post(request,id):
	print 'likepostttttttttttttt'
	if request.method == 'POST':
		user = request.user
		post = Post.objects.get(id=id)
		if not Like.objects.filter(user=user, post=post).exists():
			like = Like(user=user, post=post)
			like.save()
			likes = Like.objects.filter(post=post).count()
			url = reverse('post-unlike',args=(post.id,))
			data = {'count':likes, 'url':url}
			return HttpResponse(json.dumps(data), content_type="application/json")

def unlike_post(request,id):
	print 'unlikepostttttttttttttt'
	if request.method == 'POST':
		user = request.user
		post = Post.objects.get(id=id)
		Like.objects.filter(user=user, post=post).delete()
		unlikes = Like.objects.filter(post=post).count()
		url = reverse('post-like',args=(post.id,))
		data = {'count':unlikes, 'url':url}
		return HttpResponse(json.dumps(data), content_type="application/json")

def comment_post(request, id):
    user=request.user
    post = Post.objects.get(id=id)
    html = None
    if request.method == 'POST':
        comment = request.POST['text']
        if comment:
            new_comment = Comment(user=user, post=post, comment=comment)
            new_comment.save()
            html=render_to_string('comment.html',{'comment':new_comment})
    return HttpResponse(json.dumps(html), content_type="application/json")

def like_event(request,id):
	if request.method == 'POST':
		user = request.user
		event = Event.objects.get(id=id)
		if not Like.objects.filter(user=user, event=event).exists():
			like = Like(user=user, event=event)
			like.save()
			likes = Like.objects.filter(event=event).count()
			url = reverse('event-unlike',args=(event.id,))
			data = {'count':likes, 'url':url}
			return HttpResponse(json.dumps(data), content_type="application/json")

def unlike_event(request,id):
	print 'aaaaaaaaaaa'
	if request.method == 'POST':
		user = request.user
		event = Event.objects.get(id=id)
		Like.objects.filter(user=user, event=event).delete()
		unlikes = Like.objects.filter(event=event).count()
		url = reverse('event-like',args=(event.id,))
		data = {'count':unlikes, 'url':url}
		return HttpResponse(json.dumps(data), content_type="application/json")

def comment_event(request, id):
    user=request.user
    event = Event.objects.get(id=id)
    html = None
    if request.method == 'POST':
        comment = request.POST['text']
        if comment:
            new_comment = Comment(user=user, event=event, comment=comment)
            new_comment.save()
            
            html=render_to_string('comment.html',{'comment':new_comment})
            html=render_to_string('last_comments.html',{'comment':new_comment})
            return HttpResponse(json.dumps(html), content_type="application/json")


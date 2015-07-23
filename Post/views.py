import json
import os
import uuid
from django.utils.text import slugify
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from image import resize
from django.shortcuts import render_to_response,render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.http import require_POST
# Create your views here.
from Post.forms import PostForm
from Post.models import Post, Gallery

UPLOAD_PATH = getattr(settings, 'AJAXIMAGE_DIR', 'uploads/')
FILENAME_NORMALIZER = getattr(settings, 'AJAXIMAGE_FILENAME_NORMALIZER', slugify)



def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = Post(title=form.cleaned_data['title'], text=form.cleaned_data['text'],
                       user=request.user)
            post.save()
            for url in request.POST.getlist('attach'):
                gal = Gallery(post=post,url=url)
                gal.save()
            return HttpResponseRedirect('/home')
    else:
        form = PostForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'Post/post.html',
    variables,
    )

@require_POST
def upload(request):
    files_ = request.FILES

    image_types = ['image/png', 'image/jpg', 'image/jpeg', 'image/pjpeg',
                   'image/gif']
    data_list=[]
    for file_ in files_.getlist('file'):
        if file_.content_type not in image_types:
            data = json.dumps({'error': 'Bad image format.'})
            return HttpResponse(data, content_type="application/json", status=403)
        else:
            file_ = resize(file_, '500', '700', 0)
            file_name, extension = os.path.splitext(file_.name)
            safe_name = '{0}{1}'.format(FILENAME_NORMALIZER(file_name), extension)
            ext = safe_name.split('.')[-1]
            safe_name = "%s.%s" % (uuid.uuid4(), ext)
            name = os.path.join(UPLOAD_PATH, safe_name)
            path = default_storage.save(name, file_)
            url = default_storage.url(path)
            data_list.append(url)
    return HttpResponse(json.dumps({'data': data_list}), content_type="application/json")

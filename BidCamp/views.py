from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import  RequestContext
from BidCamp.models import *
from django.views.decorators.csrf import requires_csrf_token, csrf_protect
import datetime

def index(request):
    return render_to_response('index.html', content_type= RequestContext(request))

def single(request):
    return render_to_response('single.html', content_type= RequestContext(request))

def product(request):
    return render_to_response('product.html', content_type= RequestContext(request))

def product2(request):
    return render_to_response('product2.html', content_type= RequestContext(request))


def typography(request):
    return render_to_response('typography.html', content_type= RequestContext(request))


def terms(request):
    return render_to_response('terms.html', content_type= RequestContext(request))


def single2(request):
    return render_to_response('single2.html', content_type= RequestContext(request))

def payment(request):
    return render_to_response('payment.html', content_type= RequestContext(request))


def contact(request):
    return render_to_response('contact.html',  RequestContext(request, {}))


@csrf_protect
def checkout(request):
    return render(request,'checkout.html', {})


def faqs(request):
    return render_to_response('faqs.html', content_type= RequestContext(request))

def about(request):
    return render_to_response('about.html', content_type= RequestContext(request))

def icons(request):
    return render_to_response('icons.html', content_type= RequestContext(request))


def privacy(request):
    return render_to_response('privacy.html', content_type= RequestContext(request))



def update(request):
    return render_to_response('update.html', context_type = RequestContext(request))


def delete(request):
    return render_to_response('delete.html', context_type= RequestContext(request))

def addUser():
    ross =  User(email = 'ross@gmail.com')
    ross.first_name = 'Ross'
    ross.last_name = 'Jack'
    ross.save()
    jack = User(email='jack@gmail.com')
    jack.first_name = 'Jack'
    jack.last_name = 'Validmer'
    jack.save()
def addPost():
    post = TextPost(title = 'This is the First Post with Mongo', author=ross)
    post.content ='Took a look at MongoEngine today, looks pretty cool.'
    post.tags = ['mongodb', 'mongoengine']
    post.save()
    post1 = LinkPost('Mongo Engine Documentation', author = jack)
    post1.link_url= 'http://docs.mongoengine.com/'
    post1.tags = ['mongoengine']
    post1.save()
def selectPost():
    for post in Post.objects:
        print(post.title)
        print('=' * len(post.title))

        if isinstance(post, TextPost):
            print(post.content)

        if isinstance(post, LinkPost):
            print('Link: {}'.format(post.link_url))
    for post in TextPost.objects:
        print(post.content)
def searchPost():
    for post in Post.objects(tags= 'mongodb'):
        print(post.title)
    num_posts = Post.objects(tags='mongodb').count()
    print('Found {} posts with tag "mongodb"'.format(num_posts))

def searchUsers():
    for user in User:
      print(user.email)

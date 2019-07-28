from django.shortcuts import render,HttpResponse
from first_app import models

# Create your views here.
def show_hello(request):
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request,'profile.html')

def my_cv(request):
    name =request.GET.get("name")
    data ={
        "name" :name,
        # "name":"Sudish Basnet",
        "skill":["Python","java","js","photoshop"]
    }
    return render(request,'mycv.html',data)

def add(request):
    a = request.GET.get("a")
    b =request.GET.get("b")
    c =int(a)+int(b)

    data ={
        "sum" :c,
        "a" :a,
        "b" :b,
    }
    return render(request, 'add.html', data)

def comment(req):
    if req.method=="POST":
        has_commeted=req.session.get("has_commented")
        if(not has_commeted):
            req.session["has_commented"]=True
            user=req.POST.get("user")
            comment = req.POST.get("comment")
            c =models.Comment(user=user,comment=comment)
            c.save()
            return render(req, 'comment.html')
        elif has_commeted:
            return HttpResponse("You have already commented")

    elif req.method=="GET":
        comments =models.Comment.objects.all()
        d={
            "comments":comments
        }
        return render(req, 'comment.html',d)


def test_session(req):
    c=req.session.get("count")
    if c==None:
        req.session["count"]=1
    else:
        c=c+1
        req.session["count"]=c
    return HttpResponse("You have visited this page"+str(c)+"times")

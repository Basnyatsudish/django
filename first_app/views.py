from django.shortcuts import render,HttpResponse
from first_app import models
from . import forms
# from django.contrib.auth.decorators import
from rest_framework.views import APIView,Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from first_app import serializers
from django.views.decorators.csrf import csrf_exempt



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

# @login_required(login_url='/auth/login')
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

def delComment(req):
    comment_id =req.POST.get("comment_id")
    models.Comments.objects,filter(pk=comment_id).delete()
    return HttpResponse("comment deleted")

def test_session(req):
    c=req.session.get("count")
    if c==None:
        req.session["count"]=1
    else:
        c=c+1
        req.session["count"]=c
    return HttpResponse("You have visited this page"+str(c)+"times")


def loginpage(req):
    if req.method=="GET":
        details_form =forms.Details()
        return render(req, 'loginpage.html',{"form":details_form})
    elif req.method=="POST":
        f=forms.Details(req.POST)
        if f.is_valid():
            f.save()
            return HttpResponse("success")
        else:
            return HttpResponse("failed")


class MusicList(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        music_list=models.Music.objects.all()
        music_json=serializers.MusicSerializer(music_list,many=True)
        return Response({"music_list":music_json.data})

class MusicView(APIView):
    permission_classes = [AllowAny]
    def get(self, request,music_id):
        try:
            music_list = models.Music.objects.get(pk=music_id)
            music_json = serializers.MusicSerializer(music_list)
            return Response({"music ": music_json.data})
        except:
            return Response({"status":"failed"})

    def post(self,request):
        music=serializers.MusicSerializer(data=request.data)


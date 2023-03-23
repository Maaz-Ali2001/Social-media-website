from django.shortcuts import render
from django.http import HttpResponse,request, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import User,Credential,Comment
from django.urls import reverse
from .forms import ImageForm

def login(request):
    if request.method== 'POST':
            # email = request.POST['email']
            # passw= request.POST['psw']
            # user=Credential.objects.get(pk= email,password=passw)
            # if user.DoesNotExist:
            #     raise KeyError

        full_name= request.POST['full_name']
        phone=request.POST['phone']
        email=request.POST['email']
        password= request.POST['psw']


        if not Credential.objects.filter(email=email, password=password).exists():
            new_user = Credential(email, full_name, password, phone)
            new_user.save()
            context= {'email':email}
            return render(request, 'socialmedia/login.html',context)
        else:
            return render(request, 'socialmedia/register.html', {
                'error_message': "Email is already taken",
            })


    else:
        return render(request, 'socialmedia/login.html',context=None)

def feed(request):



    email= request.POST.get('email')
    login_check= request.POST.get("login_check")
    again_check= request.POST.get('email_id')
    #return HttpResponse(email)
    #post_id = request.POST.get['img_id']
    #return HttpResponse(post_id)
    #return HttpResponse(email)
    password= request.POST.get('psw')
    comment_lst=[]
    comment_lst_new=[]



    if login_check=='imlogin':
        check= Credential.objects.filter(email=email, password=password).exists()
    else:
        check= Credential.objects.filter(email=again_check).exists()

    if check:

        user= User.objects.all()
        user_email = User.objects.filter(profile_id=email)
        comment_lst_new=[]
        count=0
        for i in user:
            #return HttpResponse(i.id)
            comment_lst=(Comment.objects.filter(post_id=i.id))
            index_no = 0
            length= len(comment_lst)
            comment_lst_new.append([])
            while length != index_no:
                #comment_lst_new.append()
                comment_lst_new[count].append(comment_lst[index_no])
                index_no+=1
            count+=1

            #email2 = request.POST.get('email_id')
        context = {'post': user, 'comment': comment_lst_new, 'email_id': email}
        if again_check:
            post = User.objects.get(profile_id=again_check)
            add_comment = request.POST['add_comment']
            post_id = request.POST.get['img_id']
            comment_new = Comment(comment=add_comment, post_id=post)
            comment_new.save()
            context = {'post': user, 'comment': comment_lst_new, 'email_id': again_check}


        # return HttpResponseRedirect(reverse('polls:feed', args=(email,)))

        #return HttpResponse(context)
        return render(request, 'socialmedia/feed.html',context)
    else:
        return HttpResponse('HI')
        return render(request, 'socialmedia/login.html', {
            'error_message': "Email or password is not correct",
        })


def register(request):
    return render(request, 'socialmedia/register.html')





def upload(request):
    # lastimage = User.objects.last()
    #
    # imagefile = lastimage.post

    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {
               'form': form
               }

    return render(request, 'socialmedia/upload.html', context)



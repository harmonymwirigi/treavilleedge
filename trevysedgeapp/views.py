from django.shortcuts import render

# Create your views here.
import sys

# Add the path to the Pyrebase package to the system path
sys.path.append('/home/addis/Desktop/Django/venv/lib/python3.10/site-packages')

# Import the Pyrebase package
import pyrebase
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import User,auth
from django.contrib import messages

import pyrebase
config={
'apiKey': "AIzaSyDuTsMCMGajfN01AcSC2gG0xiqnoT27YhA",
  'authDomain': "fir-auth-8968d.firebaseapp.com",
  'projectId': "fir-auth-8968d",
  'databaseURL':'https://fir-auth-8968d-default-rtdb.firebaseio.com/',
  'storageBucket': "fir-auth-8968d.appspot.com",
  'messagingSenderId': "964347549468",
  'appId': "1:964347549468:web:faf25374f3be61168a4cd9",
  'measurementId': "G-GDZK38J3LZ"
}
firebase=pyrebase.initialize_app(config)
auth=firebase.auth()
database=firebase.database()
# Create your views here.
def index(request):
    channel_name=database.child('Data').child('name').get().val()
    channel_sub=database.child('Data').child('subs').get().val()
    
    features=Feature.objects.all()
 
    return render(request,'index.html',{'features':features,'channel_name':channel_name,'channel_sub':channel_sub})
    
def counter(request):
    text=request.POST['text']
    text_count=len(text.split())
    

    return render(request,'counter.html',{'text_count':text_count})
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password']
        if password==password2:
            try:
                user=auth.create_user_with_email_and_password(email,password)
        # if User.objects.filter(email=email).exists():
        #         messages.info(request,'Email Already used!')
        #         return redirect('register')
        #     elif User.objects.filter(username=username).exists():
        #         messages.info(request,"Username already exists")
        #         return redirect('register')
        #     else:
        #         user=User.objects.create_user(username=username,email=email,password=password)
        #         user.save()
            except:
                messages.info(request,"Unable to create account try again?")
                return redirect('register')
            uid=user['localId']
            data={'name':username,'status':'1'}
            database.child('users').child(uid).child('details').set(data)
            
            return redirect('login')
        else:
            messages.info(request,'Password Not The Same')
            return redirect('register')


    else:
        # saving to the databa
        return render(request,'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['email']
        password=request.POST['password']
        try:
            user=auth.sign_in_with_email_and_password(username,password)

        except:
            messages.info(request,'Credintials invalid')
            return redirect('login')
        
        print(user['idToken'])
        session_id=user['idToken']
        request.session['uid']=str(session_id)
        # user=auth.authenticate(username=username,password=password)
        if user is not None:
            # auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credintials invalid')
            return redirect('login')
    else:
        return render(request,'login.html')
def logout(request):
    try:
        del request.session['uid']
    except KeyError:
        pass

    return redirect('login')
def post(request,pk):
    return render(request,'post.html',{'pk':pk})

def create(request):
    import time
    
    from datetime import datetime
    date=datetime.now()
    work=request.POST.get('work')
    progress=request.POST.get('progress')
    idtoken=request.session['uid']
    a=auth.get_account_info(idtoken)
    a=a['users']
    a=a[0]
    a=a['localId']

    print('info',str(a))
    
    data={'work':work,
    'progress':progress}
    print(data)
    database.child('users').child(a).child('reports').child('data').set(data)



    return render(request,'create.html')
def aboutus(request):
    return render(request,'aboutus.html')

def Error_404(request):
    return render(request,'404.html')
def clientsignup(request):
      if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password2=request.POST.get('password')
        company=request.POST.get('company')
        id=request.POST.get('id')
        area=request.POST.get('area')
        city=request.POST.get('city')
        mobile=request.POST.get('mobile')
        alt_no=request.POST.get('alt')
        username=request.POST.get('email')
        password=request.POST.get('password')
        form_type=request.POST.get('clientlogin')
        user_type=request.POST.get('user_type')
        if form_type=='clientlogin':
            try:
                user=auth.sign_in_with_email_and_password(username,password)

            except:
                messages.info(request,'Credintials invalid!')
                return redirect('clientsignup')
            if user is not None:
                # auth.login(request,user)
                return redirect('/')
            else:
                messages.info(request,'Credintials invalid!')
                return redirect('clientsignup')
        if form_type=='clientsignup':
            if password==password2:
                try:
                    user=auth.create_user_with_email_and_password(email,password)
                    messages.info(request,"Account create succefully")
                    uid=user['localId']
                    
                    data={'name':username,'status':'1','email':email,'company':company,'id':id,'area':area,'city':city,
                    'mobile':mobile,'Alternate Number':alt_no}
                    # database.child('users').child(uid).child('details').set(data)
                    database.child('Data').child('Client').set(data)

                    return redirect('clientsignup')
                    


                except:
                    messages.info(request,"Unable to create account try again?")
                    return redirect('clientsignup')
            
            
            return redirect('clientsignup')
        else:
            messages.info(request,'Password Not The Same')
            return redirect('clientsignup')

 
      else:
        return render(request,'clientsignup.html')
def helpandfaqs(request):
    return render(request,'helpandfaqs.html')
def howitworks(request):
    return render(request,'howitworks.html')
def reusecode(request):
    return render(request,'reusecode.html')
def services(request):
    return render(request,'services.html')
def transporter(request):
     if request.method=='POST':
        username=request.POST.get('fullname')
        email=request.POST.get('email')
        password2=request.POST.get('password2')
        company=request.POST.get('companyname')
        id=request.POST.get('idnumber')
        area=request.POST.get('area')
        city=request.POST.get('town')
        mobile=request.POST.get('ownermobile')
        alt_no=request.POST.get('alternativemobile')
        username=request.POST.get('email')
        password=request.POST.get('password')
        form_type=request.POST.get('clientlogin')
        paymentdetails=request.POST.get('paymentdetails')
        accountname=request.POST.get('accountname')
        bankmpesa=request.POST.get('bankmpesa')
        drivername=request.POST.get('drivername')
        driverid=request.POST.get('driverid')
        drivermobile=request.POST.get('drivermobile')
        alternativedrivermobile=request.POST.get('alternativedrivermobile')
        if form_type=='translogin':
            try:
                user=auth.sign_in_with_email_and_password(email,password)

            except:
                messages.info(request,'Credintials invalid!')
                return redirect('transporter')
            if user is not None:
                # auth.login(request,user)
                return redirect('transporterdashboard')
            else:
                messages.info(request,'Credintials invalid!')
                return redirect('transporter')
        if form_type=='transignup':
            if password==password2:
                try:
                    user=auth.create_user_with_email_and_password(email,password)
                    messages.info(request,"Account create succefully")
                    uid=user['localId']
                    
                    data={'name':username,'status':'1','email':email,'company':company,'id':id,'area':area,'city':city,
                    'mobile':mobile,'Alternate Number':alt_no,'paymentdetails':paymentdetails,
                    'accountname':accountname,'bankmpesa':bankmpesa,'drivername':drivername,
                    'driverid':driverid,'drivermobile':drivermobile,'alternativedrivermobile':alternativedrivermobile}
                    # database.child('users').child(uid).child('details').set(data)
                    database.child('Data').child('transporter').set(data)

                    return redirect('transporter')
                    


                except:
                    messages.info(request,"Unable to create account try again?")
                    return redirect('transporter')
            
            
            return redirect('transporter')
        else:
            messages.info(request,'Password Not The Same')
            return redirect('transporter')

 
     else:
        return render(request,'transporter.html')
def transporterdashboard(request):
    return render(request,'transporterdashboard.html')
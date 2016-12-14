from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import utilisateur
from django.db import connection
from django.http import JsonResponse

###________ For General View _________###
def firstView(request): 
    users = utilisateur.objects.all()
    userNameStr = ''
    password = ""
    result=''	
    usersFound=''
    print "OK firstViewfirstViewfirstView"		
    if request.method == 'POST': 
        usersFound = utilisateur.objects.filter(userName=request.POST.get('password')).filter(password=request.POST.get('password'))
    return render(request, 'web\\loginForm.html', {'ff':usersFound})

###________ For Save Form : When We Modify Account Info_________###	
def Enregistrer(request):
    userName=""	
    PassW=""	
    emailModified=""	
    if request.method == "POST":
        userName = request.POST.get('userName', "")
        emailModified = request.POST.get('emailModified', "")  
        if len(userName)>0 :
            user = utilisateur.objects.filter(userName=userName )			
            user.update(email=emailModified)			
    return JsonResponse({ 'emailModified': emailModified }) 

###________ For Check Login_________###		
def loginCheck(request):
    userName=""	
    PassW=""	
    emailUser=""	
    nbUserFound=0	
    if request.method == "POST":
        userName = request.POST.get('userName', "")	
        PassW = request.POST.get('PassW', "") 
        if len(userName)>0 :
            user = utilisateur.objects.filter(userName=userName ).filter(password=PassW)			
            nbUserFound = len(user)	
            if nbUserFound>0 :		
                userName=user[0].userName.encode('UTF-8') 			
                emailUser=user[0].email.encode('UTF-8') 
    return JsonResponse({ 'nbUserFound':  nbUserFound, 'emailUser' : emailUser, 'userName':userName})


###________ For SigUp_________###		
def SignUp(request):
    userName=""	
    PassW=""	
    emailUser=""	
    nbUserFound=0	
    if request.method == "POST":
        userName = request.POST.get('userNameSU', "")
        PassW = request.POST.get('PassWSU', "") 
        emailUser = request.POST.get('emailSU', "") 		
        if len(userName)>0 :
            user = utilisateur.objects.filter(userName=userName )	
            nbUserFound = len(user)	
            if nbUserFound>0 :		
                userName=user[0].userName.encode('UTF-8') 			
                emailUser=user[0].email.encode('UTF-8') 								
            else :			
                newUser = utilisateur(userName=userName, password=PassW, email=emailUser) 
                newUser.save()
    return JsonResponse({ 'nbUserFound':  nbUserFound, 'emailUser' : emailUser, 'userName':userName})
	
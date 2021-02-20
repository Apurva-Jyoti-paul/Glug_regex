from django.shortcuts import render
from .models import Texts
from .forms import regforms,ocform
from django.http import HttpResponse
import PyPDF2
import re
import os




def search(request):
    if request.method=='POST':
        m=regforms(request.POST,request.FILES)
        if m.is_valid():
            text=m.save(commit=False)
            print(type(text.maintext),text.maintext)
            print(type(text.searchtext),text.searchtext)
            text2=re.sub(text.searchtext,';',text.maintext)
            u=re.findall(text.searchtext,text.maintext)
            
            if u:
                stexts=u[0]
            else:
                stexts=text.searchtext
            l=[]
            k=''
            t=1
            for i in text2:
                if i==';':
                    l.append(k)
                    t=0
                    k=i
                    l.append(k)
                    k=''
                else:
                    t=1
                    k=k+i
            if t:
                l.append(k)

            


            print(text2)
            return render(request,'regex.html',{'text':text,'text2':text2,'l':l,'stexts':stexts})
    else:
        m=regforms()
        return render(request,'input.html',{'m':m})

# Create your views here.


def uppdf(request):
    if request.method=='POST':
        form=ocform(request.POST,request.FILES)
        if form.is_valid():
            inst=form.save(commit=False)
            #
            form.save()
            return HttpResponse('File uploaded!')
    else:
        form=ocform()
        return render(request,'ocinput.html',{'form':form})


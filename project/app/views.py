from django.shortcuts import render
from .forms import ItemInfoForm
from .models import ItemInfo

# Create your views here.
def home(request):
    form=ItemInfoForm()
    if request.method=="POST":
        form=ItemInfoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    data=ItemInfo.objects.all()
    return render(request,"home.html",{'form':form,'data':data})

def showdata(request):
    data=ItemInfo.objects.all()

    return render(request,'dashboard.html',{'data':data})
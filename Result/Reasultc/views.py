from django.shortcuts import render,redirect,get_object_or_404
from .models import Result
from django.contrib.auth.decorators import login_required

@ login_required
def add_marks(request):
  if request.method=="POST":
    s1_name=request.POST.get('s1_name')
    s1_marks=int(request.POST.get('s1_marks'))
    s2_name=request.POST.get('s2_name')
    s2_marks=int(request.POST.get('s2_marks'))
    s3_name=request.POST.get('s3_name')
    s3_marks=int(request.POST.get('s3_marks'))
    s4_name=request.POST.get("s4_name")
    s4_marks=int(request.POST.get("s4_marks"))
    Result.objects.create(user=request.user,s1_name=s1_name,s1_marks=s1_marks,
                                           s2_name=s2_name,s2_marks=s2_marks,
                                           s3_name= s3_name,s3_marks=s3_marks,
                                             s4_name= s4_name,s4_marks=s4_marks )
    return redirect('result_came')

def result_came(request):
  marks = Result.objects.filter(user=request.user).last()
  perce=(marks.s1_marks+marks.s2_marks+marks.s3_marks+marks.s4_marks)/4
  print("p",perce)
  marks.percentage=perce
  marks.save()
  context={
    "marks":marks
        }
  return render(request,'result.html',context)
  



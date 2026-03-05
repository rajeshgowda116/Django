from django.shortcuts import render,redirect
from .models import IdCard



def idhistory(request):
    idcards=IdCard.objects.all()
    context={'idcards':idcards}
    return render(request, 'idhistory.html',context)

def idgenerate(request):
    if request.method == 'POST':
        fullname=request.POST['full_name']
        college_name=request.POST['college_name']
        branch=request.POST['branch']
        year=request.POST['year']
        photo=request.FILES['photo']
        IdCard.objects.create(
            user=request.user if request.user.is_authenticated else None,
            fullname=fullname,
            college_name=college_name,
            branch=branch,
            year=year,
            photo=photo
        )
        return redirect('idhistory')
    else:
        return render(request, 'idgenerate.html')
  
    return render(request, 'idgenerate.html')

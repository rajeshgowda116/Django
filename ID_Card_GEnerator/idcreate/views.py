from django.shortcuts import render,redirect
from .models import IdCard
from django.contrib.auth.decorators import login_required


@login_required
def idhistory(request):
    idcards = IdCard.objects.filter(user=request.user).order_by('-created_at')
    context={'idcards':idcards}
    return render(request, 'idhistory.html',context)

@login_required
def idgenerate(request):
    if request.method == 'POST':
        fullname=request.POST['full_name']
        college_name=request.POST['college_name']
        branch=request.POST['branch']
        year=request.POST['year']
        photo=request.FILES['photo']
        IdCard.objects.create(
            user=request.user,
            fullname=fullname,
            college_name=college_name,
            branch=branch,
            year=year,
            photo=photo
        )
        return redirect('idhistory')

    return render(request, 'idgenerate.html')

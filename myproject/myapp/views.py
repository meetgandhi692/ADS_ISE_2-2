from django.shortcuts import render
from .models import User
import datetime

# Create your views here.
def userreg(request):
    return render(request,"myapp/userreg.html",{})

def insertuser(request):
    tuid=request.POST['tuid']
    tuname=request.POST['tuname']
    us=User(id=tuid,name=tuname)
    us.save()
    return render(request,'myapp/userreg.html',{})

from django.db import connection
from django.http import JsonResponse

def create_user(request):
    try:
        now = datetime.datetime.now()
        with connection.cursor() as cursor:
            # Begin transaction
            cursor.execute('START TRANSACTION')
            # Insert user
            cursor.execute('INSERT INTO user VALUES (%s, %s, %s)', [request.POST['tuid'],request.POST['tuname'],now.strftime('%Y-%m-%d %H:%M:%S.%f')])
            # Commit transaction
            connection.commit()
            return JsonResponse({'success': True})
    except Exception as e:
        # Rollback transaction on error
        connection.rollback()
        return JsonResponse({'error': str(e)}, status=500)
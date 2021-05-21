""" File app project used in excel """

#from pathlib import Path

from django.shortcuts import render
#from tablib import Dataset

from .models import File
from django.contrib import messages


def load(request):
    """ load the file """
    return render(request, 'file/upload.html')


def upload(request):
    """ upload the csv file"""
    if request.method == 'POST':
        file = request.FILES['myfile']
        # print(file)
        # print(file.readlines())
        if not file.name.endswith('.csv'):
            messages.info(request, 'wrong format')
            return render(request, 'file/upload.html')

        file = file.readlines()
        file = file[1:]
        for each in file:
            file1 = each.decode('UTF-8').split(',')
            print((file1))
            File.objects.get_or_create(name=file1[0], email=file1[1], phone=file1[2])
            return render(request, 'file/result.html', {'file': file1})

    return render(request, 'file/upload.html')


def all_objects(request):
    """ show all the data """
    all = File.objects.all()
    return render(request, 'file/all_list.html', {'all': all})

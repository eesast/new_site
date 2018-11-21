from django.shortcuts import render
from django.http import JsonResponse

from os import listdir,path

# Create your views here.
LECTURE_DIR = '../files/'

def directory(request):
	return JsonResponse({'dir':listdir(LECTURE_DIR)})

def subdirectory(request,subdir):
	dir = path.join(LECTURE_DIR,subdir)
	return JsonResponse({'dir':listdir(dir)})

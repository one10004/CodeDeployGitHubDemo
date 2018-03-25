from django.shortcuts import render
from django.http import HttpResponse
import os
from subprocess import call
# Create your views here.

def index(request):
	return render(request,'elections/index.html')


def gitwatch(request, address):
	address = 'https://github.com/' + address
	os.chdir('~')
	call('git clone ' + address + '.git')
	words = address.split('/')
	length = len(words)
	os.chdir('~/' + words[length-1])
	call('python3 home/ubuntu/gitinspector/gitinspector.py -F html > home/ubuntu/CodeDeployGitHubDemo/elections/templates/elections/statistics.html')
	return render(request, 'elections/statistics.html')
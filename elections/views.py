from django.shortcuts import render
from django.http import HttpResponse
import os
# Create your views here.

def index(request):
	return render(request,'elections/index.html')


def gitwatch(request, address):
	address = 'https://github.com/' + address
	os.chdir('/home/ubuntu')
	os.system('git clone ' + address + '.git')
	words = address.split('/')
	length = len(words)
	os.chdir('/home/ubuntu/' + words[length-1])
	os.system('python3 /home/ubuntu/gitinspector/gitinspector.py -F html > /home/ubuntu/CodeDeployGitHubDemo/elections/templates/elections/statistics.html')
	return render(request, 'elections/statistics.html')
from django.shortcuts import render
from dbtest.models import *
from django.http import HttpResponse

'''
Views to be written:
	user_detail - show user info
		contact
		name
	organization_detail - show organization info
		name
	organization_job_index - list organizations jobs
		list accepted/requested jobs
		for requested, link to 'accept job'
	job_detail - show job info
		creator, name, description
		link to user profile

	create user - create a User
	create job - create a Job
	add_member - add User to Organization 'members' field
	accept_job - add Organization to to Job 'accepted' field
	organization_search

	front page
	user login - login page for users

todo
	use get_object_or_404 for database lookups
'''

def user_detail(request,user_id):
	user = User.objects.get(id=user_id)
	return render(request, 'dbtest/user_detail.html',{'user': user})

def organization_detail(request,organization_id):
	organization = Organization.objects.get(id=organization_id)
	return render(request, 'dbtest/organization_detail.html',{'organization': organization})

def organization_job_index(request,organization_id):
	organization = Organization.objects.get(id=organization_id)
	return render(request, 'dbtest/organization_job_index.html',{'organization': organization})

def job_detail(request,job_id):
	job = Job.objects.get(id=job_id)
	return render(request, 'dbtest/job_detail.html',{'job': job})



def create_user(request):
	if request.method == 'POST':
		try:
			username = request.POST['user']
			password = request.POST['password']
		except KeyError:
			#input error message
			return render(request, 'dbtest/create_user.html', {'error':"There are incorrect fields"})
		else:
			#confirmation message
			return render(request,'dbtest/create_user.html', {'username':username})
	
	else:
		return render(request, 'dbtest/create_user.html')

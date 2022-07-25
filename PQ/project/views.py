from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == "POST":
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account Was Created'+ user)
				return redirect('login')
		context = {'form':form}
		return render(request, 'projects/register.html', context)


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:


		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)


			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')
				context = {}
				return render(request, 'projects/login.html', context)
		context = {}
		return render(request, 'projects/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def home(request):
	project = projects.objects.all()
	bid = bids.objects.all()

	# project = projects.objects.filter(Project_Manager=request.user)
	total_project = project.filter(status='On-Going').count()
	total_Under_Estimation = bid.filter(Are_you_Interest='True').count()

	context = {'project': project, 'total_project': total_project, 'total_Under_Estimation':total_Under_Estimation}

	return render(request, 'projects/dashboard.html', context)
def updateProject(request, pk):

	project = projects.objects.get(id=pk)
	form = ProjctForm(instance=project)

	if request.method == 'POST':
		form = ProjctForm(request.POST, instance=project)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'projects/order_form.html', context)

@login_required(login_url='login')
def bid(request):
	bid = bids.objects.all()
	# project = projects.objects.filter(Project_Manager=request.user)
	total_bid = bid.filter(File_downloaded='True').count()
	total_Under_Estimation = bid.filter(Are_you_Interest='True').count()
	total_Failed_To_Submit = bid.filter(Failed_To_Submit='True').count()
	total_WIN = bid.filter(WIN='True').count()

	context = {'bid': bid, 'total_bid': total_bid ,'total_Under_Estimation':total_Under_Estimation,'total_Failed_To_Submit':total_Failed_To_Submit,'total_WIN':total_WIN }
	#context = {'bid': bid}

	return render(request, 'projects/bid.html', context)


def userPage(request):
	context = {}
	return render(request,'projects/user.html',context)





@login_required(login_url='login')
def createProject(request):
	form = ProjctForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = ProjctForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'projects/order_form.html', context)

def createbid(request):
	form = BidForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = BidForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'projects/bid_form.html', context)




def updateBid(request, pk):
	bid = bids.objects.get(id=pk)
	form = BidForm(instance=bid)

	if request.method == 'POST':
		form = BidForm(request.POST, instance=bid)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'projects/bid_form.html', context)

def BOQ(request):
	boq = bid_BOQ.objects.all()
	context = {'boq': boq}

	return render(request, 'projects/BOQ_List1.html', context)
def createbid_BOQ(request):
	form = bid_BOQ_fORM()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = bid_BOQ_fORM(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'projects/BOQ_form.html', context)

def updateBOQ(request, pk):
	bid = bid_BOQ.objects.get(id=pk)
	form = bid_BOQ_fORM(instance=bid)

	if request.method == 'POST':
		form = bid_BOQ_fORM(request.POST, instance=bid)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'projects/BOQ_List1.html', context)



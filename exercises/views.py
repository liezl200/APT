from django.shortcuts import render, render_to_response, RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def home(request):
	return render_to_response("home.html", 
		locals(), 
		context_instance=RequestContext(request))

def dailyExercises(request):
	exercise_list = ['E1', 'E2', 'E3', 'E4', 'E5']
	#put one element of data onto each page
	paginator = Paginator(exercise_list, 1)
	page = request.GET.get('page')

	try:
		exercises = paginator.page(page)
	except PageNotAnInteger:
		#if page is not an integer, deliver first page.
		exercises = paginator.page(1)
	except EmptyPage:
		#if page is out of range (e.g. 9999), deliver last page of results.
		exercises = paginator.page(paginator.num_pages)

	patientExerciseData = Movement(patientExerciseData)

	return render_to_response('dashboard.html', {"exercises": exercises})


from django.shortcuts import render

# Create your views here.
def index(request):
	context = {

	}
	return render(request, "home/index.html", context)

def about(request):
	context = {

	}
	return render(request, "home/about.html", context)


def list(request):
		context = {
		"object_list": home.objects.all()
		}
		return render(request, "home/list.html", context)
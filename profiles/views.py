from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from profiles.models import Profile
from profiles.forms import ProfileForm

# Create your views here.
def index(request):
	#print(request.session.get('first_name','Unknown')) #Getter
	context = locals()
	template = 'index.html'
	return render(request,template,context)

def about(request):
	context = locals()
	template = 'about.html'
	return render(request,template,context)
def userProfile(request):
	#Profile = Profile.objects.get(user=request.user)
	title = Profile.objects.all()
	template = 'core/profile.html'
	return render(request,template,{"title":title})

def model_profile_upload(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'model_profile_upload.html', {
        'form': form
    })

def faq(request):
	context = locals()
	template = 'faq.html'
	return render(request,template,context)

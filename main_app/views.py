from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import HttpResponse

from django.http import HttpResponse, HttpResponseRedirect

from .models import Child
from .models import Daily_Activity
from django.contrib.auth.forms import UserCreationForm
from .forms import Daily_ActivityForm, ChildForm
# Create your views here.
from django.contrib.auth import login

# bring in decorator
from django.contrib.auth.decorators import login_required

# attempt form
from django.forms.models import model_to_dict

class ChildCreate(CreateView):
  model = Child
#   fields = '__all__'
  success_url = '/children'

class ChildUpdate(UpdateView):
  model = Child
  fields = ['image', 'name', 'age', 'gender', 'address', 'pcp', 'bio']

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    return HttpResponseRedirect('/children/' + str(self.object.pk))


class ChildDelete(DeleteView):
  model = Child
  success_url = '/children'




def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


@login_required()
def children_index(request):
    children = Child.objects.all()
    return render(request, 'children/index.html', { 'children' : children })

@login_required()
def children_new(request):
  # create new instance of cat form filled with submitted values or nothing
  # if this is a request.GET get request this will be none.
  # if the form was posted and valid
  child_form = ChildForm(request.POST or None)  
  if request.POST and child_form.is_valid():
    new_child = child_form.save(commit=False)
    new_child.user = request.user
    new_child.save()
    # redirect to index
    return redirect('index')
  else:
    # this handles a GET request
    # render the page with the new cat form
    return render(request, 'children/new.html', { 'child_form': child_form })


#refactor to custom update to use @login_required decorator
@login_required
def children_update(request, pk):
  if request.POST:
    print('its an update request')
    # get the original cat
    our_child = Child.objects.get(id=pk)
    # update the values
    our_child.image = request.POST.get('image')
    our_child.name = request.POST.get('name')
    our_child.age = request.POST.get('age')
    our_child.gender = request.POST.get('gender')
    our_child.address = request.POST.get('address')
    our_child.pcp = request.POST.get('pcp')
    our_child.bio = request.POST.get('bio')
    our_child.save()
    return redirect('children')

  # this is for the GET request
  child = Child.objects.get(id=pk)
  childform = ChildForm(initial=model_to_dict(child)) 
  return render(request, 'children/child_form.html', { 'form': childform })


@login_required()
def children_show(request, child_id):
    # we get access to that child_id variable
    # query for the specific child clicked
    child = Child.objects.get(id=child_id)
    # lets make a Daily_ActivityForm
    daily_ActivityForm = Daily_ActivityForm()
    print(child.daily_activity_set.all)
    return render(request, 'children/show.html', { 
      'child': child,
     'daily_ActivityForm': daily_ActivityForm
    })


@login_required()
def add_dailyActivities(request, pk):
  # this time we are passing the data from our request in that form
  form = Daily_ActivityForm(request.POST)
  # validate form.is_valid built in
  if form.is_valid():
    # don't save yet!! First lets add out child_id
    new_activity = form.save(commit=False)
    new_activity.child_id = pk
    # child been added we can save
    new_activity.save()
  return redirect('children_show', child_id = pk)    

def sign_up(request):
  error_message= ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      # ok user created log them in
      login(request, user)
      return redirect('index')
    else:
      error_message='That was a no go. Invalid signup'
  # this will run after if it's not a POST or it was invalid
  form = UserCreationForm()
  return render(request, 'registration/signup.html', {
    'form': form,
    'error_message': error_message
  })  


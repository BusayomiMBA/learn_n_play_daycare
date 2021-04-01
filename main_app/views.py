from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import HttpResponse

from django.http import HttpResponse, HttpResponseRedirect

from .models import Child
from .models import Daily_Activity
from django.contrib.auth.forms import UserCreationForm
from .forms import Daily_ActivityForm, ChildForm
# Create your views here.

# attempt form
from django.forms.models import model_to_dict

class ChildCreate(CreateView):
  model = Child
  fields = '__all__'
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



def children_index(request):
    children = Child.objects.all()
    return render(request, 'children/index.html', { 'children' : children })

# def children_show(request, child_id):
#     # we get access to that child_id variable
#     # query for the specific child clicked
#     child = Child.objects.get(id=child_id)
#     # lets make a Daily_ActivityForm
#     daily_ActivityForm = Daily_ActivityForm()
#     return render(request, 'children/show.html', { 
#       'child': child,
#      'daily_ActivityForm': daily_ActivityForm
#     })

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
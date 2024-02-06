from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import taskform
# Create your views here.
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView,DeleteView
class tasklistview(ListView):
    model = Task
    template_name = 'form.html'
    context_object_name = 'task'

class taskdetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')


    def get_success_url(self):
        return reverse_lazy("todoapp:detail_view", kwargs={'pk': self.object.id})


class taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:list_view')


def add(request):
    task=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        todo=Task(name=name,priority=priority,date=date)
        todo.save();
    return render(request,'form.html',{'task':task})
def delete(request,id):
    t=Task.objects.get(id=id)
    if request.method=='POST':
        t.delete();
        return redirect('/')
    return render(request,'delete.html',{'t':t})
def update(request,taskid):
    ta=Task.objects.get(id=taskid)
    f=taskform(request.POST or None,instance=ta)
    if f.is_valid():
        f.save();
        return redirect('/')
    return render(request,'edit.html',{'ta':ta,'f':f})
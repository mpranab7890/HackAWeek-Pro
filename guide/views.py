from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import RegistrationForm, ServiceForm ,ReviewForm
from django.contrib import messages
from .models import UserServices, Review
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import DetailView
# from annoying.decorators import render_to

from django.shortcuts import render_to_response
from django.template import RequestContext


from django.forms.models import inlineformset_factory
def home(request):
     return render(request , 'guide/index.html')

def register(request):

     if request.method=='POST':
          form = RegistrationForm(request.POST)
          if form.is_valid():
               form.save()
               username = form.cleaned_data.get('username')
               messages.success(request, f'Your account has created you can now log in!')
               return redirect('login')

     else:
          form=RegistrationForm()
     return render(request, 'guide/register.html', {'form':form})

@login_required
def dashboard(request):
     context = {
          'posts': UserServices.objects.all
     }
     return render(request , 'guide/dashboard.html' , context)

@login_required
def setService(request):
     u = UserServices.objects.get(user=request.user)
     if request.method=='POST':
          # data = request.POST.copy()
          # data.update({'user': request.user.pk })
          s_form = ServiceForm( request.POST , request.FILES , instance = u)
          if s_form.is_valid():
               # s_form.user = request.user
               s_form.save()
               # x.user = request.user
               # x.save()
               return redirect('dashboard')
     else:
          s_form = ServiceForm(instance = u)
     return render(request , 'guide/service.html', {'s_form':s_form})

@login_required
def Profile(request):
     return render(request , 'guide/profile.html')

# class UserServicesDetailView(DetailView):
#      template_name = "guide/posts.html"

#      model = UserServices
     
#      form_class = ReviewForm
#      success_url = '/dashboard/'

#      def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.save()
#         return super().form_valid(form)
     # p = Review.objects.get(posts = post.id)
     #      if request.method=='POST':
     #           r_form = ReviewForm( request.POST , request.FILES , instance = p)
     #           if r_form.is_valid():
     #                r_form.save()
     #                      return redirect('posts')
     #           else:
     #                r_form = ReviewForm(instance = p)


# @render_to('guide/posts.html')
# def commentView(request):
#      if request.method=='POST':
#                r_form = ReviewForm( request.POST )
#                if r_form.is_valid():
#                     r_form.save()
#                     return redirect('posts')
#                else:
#                     r_form = ReviewForm()

def DetailView(request,pk):
     # post = get_object_or_404(UserServices, slug=slug)
     post = UserServices.objects.get(pk=pk)
     return render(request ,'guide/posts.html', {'post': post})
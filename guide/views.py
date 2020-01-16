from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import RegistrationForm, ServiceForm ,ReviewForm, BookForm
from django.contrib import messages
from .models import UserServices, Review
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.conf import settings
from django.core.mail import send_mail


# from annoying.decorators import render_to

# from django.shortcuts import render_to_response
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
@login_required
def DetailView(request,pk):
     # post = get_object_or_404(UserServices, slug=slug)
     post = UserServices.objects.get(pk=pk)
     
     if request.method=='POST':
          r_form = ReviewForm( request.POST )
          if r_form.is_valid():
               x=r_form.save(commit=False)
               x.posts = post
               x.author = request.user.username
               x.save()
               
               return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
     else:
          r_form = ReviewForm()

     reviews = Review.objects.filter(posts = post)

     return render(request ,'guide/posts.html', {
          'post':post,
          'form': r_form,
          'reviews':reviews,
     })

@login_required
def homestayView(request):
     posts = UserServices.objects.filter(type_of_service = 'Homestay')
     return render(request , 'guide/homestay.html', {'posts':posts})

@login_required
def transportView(request):
     posts = UserServices.objects.filter(type_of_service = 'Transportation')
     return render(request , 'guide/transport.html', {'posts':posts})

@login_required
def hotelView(request):
     posts = UserServices.objects.filter(type_of_service = 'Hotel')
     return render(request , 'guide/hotel.html', {'posts':posts})

@login_required
def travelagencyView(request):
     posts = UserServices.objects.filter(type_of_service = 'Travel Agency')
     return render(request , 'guide/travel.html', {'posts':posts})

@login_required
def bookView(request,pk):
     post = UserServices.objects.get(pk=pk)
     if request.method=='POST':
          form = BookForm( request.POST )
          if form.is_valid():
               data = form.cleaned_data
               date1 = str(data['date'])
          subject = 'Thank you for registering to our site'
          
          u = request.user.first_name
          e= request.user.email
          message = 'Hello Miss '+post.user.first_name+'. '+'Mr. '+ u + ' wants to book '+ post.name_of_service + ' for ' + date1 + '. Please contact him through Namaste webapp or through his email '+ e + ". Thank you for using Namaste." 
          
         
          email_from = settings.EMAIL_HOST_USER
          recipient_list = [post.user.email]
          send_mail( subject, message, email_from, recipient_list )
          return redirect('dashboard')

     
     else:
          form = BookForm()


     return render(request, 'guide/book.html', {'form': form, 'post':post})
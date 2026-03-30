from django.shortcuts import render
import logging
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib import messages
from allpg.forms import CustomUserCreationForm, ContactForm

User = get_user_model()

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

                                                    #  backend area starting from here
                                                    #  backend area starting from here
                                                    #  backend area starting from here
                                                    #  backend area starting from here

def contact(request):
      if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info(f"Contact form submitted and saved: {form.cleaned_data}")
            messages.success(request, 'Thank you for contacting us! We will get back to you shortly.')
            return redirect('contact')
        else:
            logger.warning(f"Contact form invalid: {form.errors}")
      else:
       form = ContactForm()
      return render(request, "contact.html", {'form': form})
      return render(request, 'contact.html')
                                            
                                            #  login section starts!!

def login_view(request):
    logger.info(f"Login view called. Method: {request.method}")
    if request.method == 'POST':
        username_or_email = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username_or_email, password=password)
        if user is None:
            try:
                user_obj = User.objects.get(email=username_or_email)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                pass
        logger.info(f"Authentication for {username_or_email}: {user}")
        if user is not None:
            login(request, user)
            messages.success(request, f'Login successful! Welcome back {user.username}!')
            logger.info(f"Login successful for user: {username_or_email}, redirecting to index")
            return redirect('index')
        else:
            logger.warning(f"Login failed for user: {username_or_email}")
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')
                          
                                                # login section end

                                                # logout section starts!!
def logout_view(request):
    logout(request)
    return redirect('index')

                                                # logout section end

                                                # signup section starts!!


def signup(request):
    logger.info(f"Signup view called. Method: {request.method}")
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            logger.info(f"User created: {username}, logging in directly")
            
            login(request, user)
            messages.success(request, f'Account created successfully! Welcome to REVO {username}!')
            logger.info(f"Signup successful for user: {username}, redirecting to index")
            return redirect('index')
        else:
            logger.warning(f"Signup form invalid: {form.errors}")
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'signup_form.html', {'form': form})

                                                    #    signup section end!!
    







                                                    #  Backend area ending here!!
                                                    #  Backend area ending here!!
                                                    #  Backend area ending here!!
                                                    #  Backend area ending here!!


def singlepg(request):
    return render(request, 'singlepg.html')

def staticpg(request):
    return render(request, 'staticpg.html')

def multipg(request):
    return render(request, 'multipg.html')

def threedpg(request):
    return render(request, '3d design.html')

def static1_formula(request):
    return render(request, 'static1_formula.html')

def static2_story(request):
    return render(request, 'static2_story.html')

def static3_contact(request):
    return render(request, 'static3_contact.html')

def chatbot_view(request):
       return render(request, 'chatbot.html')

def multiplepg(request):
    return render(request, 'multiplepg.html')

def chatbot(request):
    return render(request, 'chatbot.html')



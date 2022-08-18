from ast import Return
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import *
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import *
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
# from djangoUpload.forms import UploadForm
from django.contrib.auth.decorators import login_required
from django. views. decorators. csrf import csrf_exempt
# ---------EMAIL VER. IMPORTS BELOW
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
# ---------EMAIL VER. IMPORTS END


class UserList(ListView):
    # specify the model for list view
    model = User

# HOME FUNCTION


@login_required(login_url='Login')
def Home(request):
    videoall = Video_Files.objects.all()
    return render(request, "home.html", context={"videoall": videoall})


# SIGN UP FUNCTION


def SignUpView(request):
    if request.method == "POST":
        Full_Name = request.POST['userfullname']
        Email = request.POST['emailaddress']
        Password = request.POST['password']
        new_user = User_Main(Full_Name=Full_Name,
                             Email=Email, Password=Password)
        new_user.save()
        return redirect("Validation")
    return render(request=request, template_name="signup2.html")


# LOGIN FUNCTION
@csrf_exempt
def Login_page(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            Email = request.POST.get('Email')
            Password = request.POST.get('Password')
            user = authenticate(
                request, email=Email, password=Password)
            if request.user.is_authenticated:
                form.save()
                login(request, user)
                return redirect("Home")
            else:
                messages.error(
                    request, "Login Unsuccessful: Enter Correct Details.")
                return redirect("Login")
        else:
            messages.error(
                request, "Login Unsuccessful: Form Is Invalid. [Try Confirming Your Email Address")
            return redirect("Login")
    return render(request=request, template_name="login.html", context={"login_form": form})


# LOGOUT FUNCTION


def Logout_user(request):
    logout(request)
    messages.success(request, "LOGOUT successful.")
    return redirect('Login')


def Watch(request):
    return render(request=request, template_name="watchpage.html")


# VALIDATION IMAGES FUNCTION

def Validate_id(request):
    data = Validation.objects.all()
    form = ValidateForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('Login')
        messages.success(
            request, "ID pictures Uploaded, Proceed to Login Now")

    else:
        form = ValidateForm()
    return render(request, "validateid.html", context={"ValidateForm": form})


# VALIDATION 2 SCHOOL ID AND EMAIL
def Validation2(request):
    form = ValidateForm2(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "School Email Submitted.")
            return redirect("Validate")

    return render(request=request, template_name="validation2.html", context={"validation2_form": form})
    # return render(request, "validation2.html")


# ---


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


# -----
# VIDEO UPLOAD FUNCTION


@csrf_exempt
@login_required(login_url='Login')
def Video_Upload(request):
    form = VideoForm(request.POST, request.FILES)
    videoall = Video_Files.objects.all()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Upload successful.")
            return redirect("Home")
    else:
        # form = VideoForm()
        print("done")
    return render(request=request, template_name=("video.html"), context={"video_form": form})

    # def _upload_file_view(request):


# Library functio below

def Library(request):
    videoall = Video_Files.objects.all()
    return render(request, "library.html", context={"videoall": videoall})


# COMMENT FUNCTION
@login_required(login_url='Login')
def Comment(request):

    if request.method == "POST":
        print('This is a POST document')

    form = CommentForm(request.POST or None)
    if form.is_valid():
        Comment = form.save()
        messages.success(request, "Comment successful.")
        return redirect("Home")
        messages.error(
            request, "Unsuccessful Commenting.")
    return render(request=request, template_name="comment.html", context={"comment_form": form})


# EMAIL REDIRECTION FUNCTON PAGE
@csrf_exempt
def emailPage(request):
    return render(request, "email.html")

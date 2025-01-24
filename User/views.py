from django.shortcuts import render, redirect

from SnapForge import settings


# Create your views here.

def index(request):
    return render(request, "Index.html", {})


def img_creation(request):
    return render(request, "Img_creation.html", {})


def signup(request):
    return render(request, "SignUp.html", {})


def login(request):
    return redirect("/Index")


from django.core.mail import send_mail
import random


def sendotp(request):
    if request.method == "POST":
        otp = random.randint(1000, 9999)

        e = request.POST['email']

        subject = 'Your SnapForge Portal OTP'
        message = 'Dear ' + e + ', you have attempted to login in the SnapForge Portal.\n\nUse OTP: ' + str(otp) + '\n\nNote: Do not share the OTP with anyone else. '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e, ]

        send_mail(subject, message, email_from, recipient_list)
        print("-=-=-=-=-=-=-=-=-=-  Email has been sent successfully...")

    return render(request, "Login.html", {})

# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# def show(request):
#     if request.method == "POST":
#
#         im = request.FILES['img']
#
#         img = mpimg.imread(im)
#
#         plt.imshow(img)
#         plt.axis('off')
#         plt.show()

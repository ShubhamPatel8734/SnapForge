from django.shortcuts import render, redirect

from SnapForge.settings import BASE_DIR
from User.models import *
from pymongo.errors import *

from SnapForge import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.

def index(request):

    fs = FileSystemStorage()
    file_url = fs.url('coder_boy.jpg')
    print("file_url :-", file_url)

    return render(request, "Index.html", {"file_url": file_url})


def img_creation(request):
    if request.method == "POST":

        # If HTML_form contains  enctype="multipart/form-data" then:-
        Left = request.FILES['left']
        Right = request.FILES['right']
        Front = request.FILES['front']
        Back = request.FILES['back']

        # If HTML_form   Not contains   enctype="multipart/form-data" then:-
        # Left = request.FILES.get('left')
        # Right = request.FILES.get('right')
        # Front = request.FILES.get('front')
        # Back = request.FILES.get('back')

        fs = FileSystemStorage(location=settings.MEDIA_ROOT)

        if Left and Right and Front and Back:
            Left_path = fs.save(Left.name, Left)
            Right_path = fs.save(Right.name, Right)
            Front_path = fs.save(Front.name, Front)
            Back_path = fs.save(Back.name, Back)

            Left_name = fs.get_valid_name(Left_path)
            Right_name = fs.get_valid_name(Right_path)
            Front_name = fs.get_valid_name(Front_path)
            Back_name = fs.get_valid_name(Back_path)

            records = {
                "left_img": Left_name,
                "right_img": Right_name,
                "Front_img": Front_name,
                "Back_img": Back_name,
                "user_email": "pshubham8734@gmail.com"
            }
            images_collection.insert_one(records)
            print(f":::::::::::::::::::  Left_name : {Left_name} \n:::::::::::::::::::  Right_name : {Right_name} \n:::::::::::::::::::  Front_name : {Front_name} \n:::::::::::::::::::  Back_name : {Back_name}")
            return redirect("/Index")

    return render(request, "Img_creation.html", {})


def signup(request):
    if request.method == "POST":

        name = request.POST['user_name']
        email = request.POST['user_email']

        records = {
            "user_name": name,
            "user_email": email
        }
        print("Form Data :", records)

        try:
            user_collection.insert_one(records)
            return render(request, "Login.html", {})
        except DuplicateKeyError:
            err_msg = "The email address is already registered. Please use a different email."
            print("-+-+-+-+-+-+-+-+-+-+-+- :- ", err_msg)
            return render(request, "SignUp.html", {"error": err_msg})
        except Exception as e:
            print("-=-=-=-=-=-=-=-=-=-=-=- Somthing want wrong :- ", e)
            err_msg = "An unexpected error occurred. Please try again."
            return render(request, "SighUp.html", {"error": err_msg})

    return render(request, "SignUp.html", {})


def login(request):
    if request.method == 'POST':

        email = request.POST['user_email']
        otp = request.POST['otp']

        print("+-+-+-+-+-+ Email from Send OTP Form :-", email)
        user = user_collection.find_one({"user_email": email})

        # print("User details :- ", user)

        if user:
            if user.get("otp") == otp:
                print("*=*=*=*=*=*=*=*=*=*=*=* :- login successfully..")
                return redirect("/Index")
            else:
                print("+-+-+-+-+-+-+-+-+-+-+-+ :- OTP is incorrect.")
                return render(request, "Login.html", {"visibility": 'block', "email": email, "error": "Invalid OTP."})

    return render(request, "Login.html", {})


from django.core.mail import send_mail
import random


def sendotp(request):
    if request.method == 'POST':
        otp = random.randint(1000, 9999)

        email = request.POST['user_email']

        print("*=*=*=*=*=*=* otp:- ",otp,"email:- ",email)

        user = user_collection.update_one(
            {"user_email": email},  # Filter: Match the email
            {"$set": {"otp": str(otp)}}  # Update: Add or update the OTP field
        )

        if user.matched_count == 0:
            err_msg = "Email not found. Please SignUp before requesting an OTP."
            print("-=-=-=-=-=-=-=-", err_msg)
            return render(request, "SignUp.html", {"error": err_msg})

        subject = 'Your SnapForge Portal OTP'
        message = 'Dear user, you have attempted to login in the SnapForge Portal.\n\nUse OTP: ' + str(otp) + '\n\nNote: Do not share the OTP with anyone else. '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]

        # send_mail(subject, message, email_from, recipient_list)
        print("+=+=+=+=+=+=+=+=+=+  " + email + "  +=+=+=+  Email has been sent successfully...")

        print(f"*=*=*=*=*=*=*=*=*=*=*=*  OTP {otp} successfully added to the collection for email {email}")

    return render(request, "Login.html", {"visibility": 'block', "email": email})

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

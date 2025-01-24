from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return render(request, "index.html", {})


def img_creation(request):
    return render(request, "input.html", {})


def signup(request):
    return render(request, "SignUp.html", {})


def login(request):
    return redirect("/")


def sendotp(request):
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


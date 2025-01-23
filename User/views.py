from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "input.html", {})


def login(request):
    return render(request, "Login.html", {})


def sendotp(request):
    return render(request, "Validate_OTP.html", {})


def validateotp(request):
    return render(request, "input.html")



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


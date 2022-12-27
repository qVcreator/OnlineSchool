from django.shortcuts import render


# Create your views here.
def main_window(req):
    return render(req, 'course/main.html')

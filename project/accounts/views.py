from django.shortcuts import render, HttpResponse
from django.views import View

class Register(View):
    """
        Register page for user using view
    """

    def get(self, request):

        return HttpResponse("Register page")
class Login(View):
    """
        Login page for user using view
    """

    def get(self, request):

        return HttpResponse("Login page")

class Logout(View):
    """
        Logout page for user using view
    """

    def get(self, request):

        return HttpResponse("Logout page")

from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth import login, logout,update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.contrib.auth.forms import SetPasswordForm

from . import serializers
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


# for sending mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.

# class UserRegistrationView(FormView):
#     template_name = 'accounts/user_registration.html'
#     form_class = UserRegistrationForm
#     success_url = reverse_lazy('home')

#     def form_valid(self,form):
#         user = form.save() 
#         login(self.request, user)
#         return super().form_valid(form)
    
# class UserLoginView(LoginView):
#     template_name = 'accounts/user_login.html'
#     def get_success_url(self):
#         return reverse_lazy('home')
    
# class UserLogoutView(LogoutView):
#     def get_success_url(self):
#         if self.request.user.is_authenticated:
#             logout(self.request)
#         return reverse_lazy('home')

class UserRegistrationApiView(APIView):
    serializer_class = serializers.RegistrationSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            token = default_token_generator.make_token(user)
            print("token ", token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print("uid ", uid)
            confirm_link = f"http://127.0.0.1:8000/accounts/active/{uid}/{token}/"
            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
            
            email = EmailMultiAlternatives(email_subject , '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response("Check your mail for confirmation")
        return Response(serializer.errors)

    

def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None 
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')
    

class UserLoginApiView(APIView):
    def post(self,request):
        serializer = serializers.UserLoginSerializer(data = self.request.data)
        if(serializer.is_valid()):
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)

            if(user):
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key,'user_id':user.id})
            else:
                return Response({'error':"Invalid Credentials"})
        
        return Response(serializer.errors)




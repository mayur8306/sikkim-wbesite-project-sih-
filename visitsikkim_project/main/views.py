


# from django.shortcuts import render, redirect
# from .models import Monastery
# from django.http import JsonResponse
# import os
# from django.contrib import messages
# from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
# from django.contrib.auth import login
# from django.contrib.auth import logout
# import requests
# from django.conf import settings
# from django.http import JsonResponse
# import json


# def index(request):
#     return render(request, 'index.html')

# def archives(request):
#     return render(request, 'archives.html')

# def tour(request):
#     return render(request, 'tour.html')

# def interactive(request):
#     return render(request, 'interactive.html')

# def manuscripts(request):
#     return render(request, 'manuscipts.html')

# def murals(request):
#     return render(request, 'murals.html')

# # Create your views here.
# def tour(request):
#     monasteries = Monastery.objects.all()
#     return render(request, "tour.html", {"monasteries": monasteries})


    







# # --- ADD THESE IMPORTS TO THE TOP OF YOUR main/views.py FILE ---
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.conf import settings # Needed to access the API key
# import requests # Needed to make the HTTP POST request

# # -----------------------------------------------------------------

# @csrf_exempt
# def ask_gemini(request):
#     """
#     Handles the chatbot's API requests, calls the Gemini model, 
#     and returns a JSON response.
#     """
#     # Get the question from the frontend
#     question = request.GET.get("q", "")
    
#     if not question:
#         # Changed status code to 400 for a bad request
#         return JsonResponse({"error": "No question provided"}, status=400)
    
#     # Get your secret key from settings
#     # Ensure you set GEMINI_API_KEY in your settings.py
#     api_key = getattr(settings, 'GEMINI_API_KEY', None)
    
#     if not api_key:
#         return JsonResponse({"error": "API key not configured"}, status=500)
    
#     # Prepare the request to Gemini API
#     url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
    
#     # System prompt for Sikkim tour guide
#     system_prompt = """You are a friendly and expert tour guide for Sikkim, India. Your name is SikkimBot.
#     Your ONLY purpose is to help users plan their trips to Sikkim.
#     - You MUST refuse to answer any questions not related to Sikkim tourism, travel, culture, monasteries, or trip planning.
#     - When a user asks for a travel plan, provide a detailed, day-by-day itinerary.
#     - Include suggestions for accommodations, transportation, and local food.
#     - Provide estimated costs for different parts of the plan.
#     - Do not use markdown in your response."""
    
#     # The data we send to Gemini
#     payload = {
#         "contents": [{
#             "parts": [{
#                 "text": question
#             }]
#         }],
#         "config": {
#             "systemInstruction": system_prompt 
#         }
#     }
    
#     try:
#         # Make the API call
#         response = requests.post(
#             f"{url}?key={api_key}",
#             headers={"Content-Type": "application/json"},
#             json=payload
#         )
#         response.raise_for_status() # Raises an exception for bad status codes (4xx or 5xx)
        
#         # Return the answer to the frontend
#         return JsonResponse(response.json())
        
#     except requests.exceptions.RequestException as e:
#         # Return a 500 status code if the API request itself fails
#         return JsonResponse({"error": f"API request failed: {str(e)}"}, status=500)




# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             login(request, user)
#             messages.success(request, f"Welcome back, {user.username}!")
#             return redirect('index')  # Redirect to homepage after login
#         else:
#             messages.error(request, "Invalid username or password.")
#             return render(request, 'login.html')
            
#     return render(request, 'login.html')


# def user_signup(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         password_confirm = request.POST.get('password_confirm')

#         # --- Validations ---
#         if password != password_confirm:
#             messages.error(request, "Passwords do not match.")
#             return render(request, 'signup.html')
        
#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username is already taken.")
#             return render(request, 'signup.html')

#         if User.objects.filter(email=email).exists():
#             messages.error(request, "An account with this email already exists.")
#             return render(request, 'signup.html')
            
#         # Create the new user
#         user = User.objects.create_user(username=username, email=email, password=password)
#         user.save()
        
#         # Log the user in immediately after signing up
#         login(request, user)
#         messages.success(request, f"Account created successfully! Welcome, {user.username}.")
#         return redirect('index')

#     return render(request, 'signup.html')


# def user_logout(request):
#     logout(request)
#     messages.info(request, "You have been logged out.")
#     return redirect('index')





# #signup
# def user_signup(request):
#     if request.method == "POST":
#         # Get data from the form
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         password2 = request.POST['password2']

#         # Basic validation
#         if password != password2:
#             messages.error(request, 'Passwords do not match.')
#             return render(request, 'main/signup.html')

#         if User.objects.filter(username=username).exists():
#             messages.error(request, 'Username is already taken.')
#             return render(request, 'main/signup.html')
        
#         if User.objects.filter(email=email).exists():
#             messages.error(request, 'Email is already registered.')
#             return render(request, 'main/signup.html')

#         # Create a new user
#         user = User.objects.create_user(username=username, email=email, password=password)
#         user.save()
        
#         # Display a success message and redirect to the login page
#         messages.success(request, 'Account created successfully! You can now log in.')
#         return redirect('user_login')  # Replace with the name of your login URL

#     # Handle the GET request to display the form
#     return render(request, 'main/signup.html')


# def user_logout(request):
#     logout(request)
#     messages.success(request, 'Logged out successfully.')
#     return redirect('index')  # or redirect to your home page



# # In main/views.py

# def cultural_calendar(request):
#     return render(request, 'cultural_calendar.html')

# # In main/views.py

# def booking_options(request):
#     return render(request, 'booking_options.html')


# # Travel & Stay
# def travel_and_stay(request):
#     return render(request, 'travel_and_stay.html')







from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Monastery
import requests

# ----------------- MAIN PAGES -----------------
def index(request):
    return render(request, 'index.html')

def archives(request):
    return render(request, 'archives.html')

def tour(request):
    monasteries = Monastery.objects.all()
    return render(request, "tour.html", {"monasteries": monasteries})

def interactive(request):
    return render(request, 'interactive.html')

def manuscripts(request):
    return render(request, 'manuscipts.html')

def murals(request):
    return render(request, 'murals.html')

def cultural_calendar(request):
    return render(request, 'cultural_calendar.html')

def book_experience(request):
    return render(request, 'book_an_experience.html')

def travel_and_stay(request):
    return render(request, 'travel_and_stay.html')


# ----------------- CHATBOT ENDPOINT -----------------
@csrf_exempt
def ask_gemini(request):
    """
    Handles the chatbot's API requests, calls the Gemini model,
    and returns a JSON response to the frontend.
    """
    question = request.GET.get("q", "").strip()

    if not question:
        return JsonResponse({"error": "No question provided"}, status=400)

    api_key = getattr(settings, 'GEMINI_API_KEY', None)
    if not api_key:
        return JsonResponse({"error": "API key not configured"}, status=500)

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"

    system_prompt = (
        "You are a friendly and expert tour guide for Sikkim, India. Your name is SikkimBot. "
        "Your ONLY purpose is to help users plan their trips to Sikkim. "
        "You MUST refuse to answer any questions not related to Sikkim tourism, culture, monasteries, "
        "or travel planning. When a user asks for a travel plan, provide a detailed day-by-day itinerary, "
        "including accommodations, transportation, local food, and estimated costs. Do not use markdown."
    )

    payload = {
        "contents": [{
            "role": "user",
            "parts": [{"text": f"{system_prompt}\nUser: {question}"}]
        }]
    }

    try:
        response = requests.post(
            f"{url}?key={api_key}",
            headers={"Content-Type": "application/json"},
            json=payload
        )
        response.raise_for_status()
        return JsonResponse(response.json())

    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": f"API request failed: {str(e)}"}, status=500)


# ----------------- USER AUTH -----------------
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')


def user_signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            return render(request, 'signup.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        login(request, user)
        messages.success(request, f"Account created successfully! Welcome, {user.username}.")
        return redirect('index')

    return render(request, 'signup.html')


def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('index')

def about(request):
    return render(request, 'about_us.html')
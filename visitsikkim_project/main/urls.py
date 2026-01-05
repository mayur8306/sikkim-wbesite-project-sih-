from django.urls import path
from . import views

urlpatterns = [
    # --- Main Pages ---
    path('', views.index, name="index"),
    path('archives/', views.archives, name="archives"),
    path('tour/', views.tour, name="tour"),
    path('interactive/', views.interactive, name="interactive"),
    path('manuscripts/', views.manuscripts, name="manuscripts"),
    path('murals/', views.murals, name="murals"),

    # --- Chatbot API Endpoint ---
    path('ask/', views.ask_gemini, name='ask_gemini'),

    # --- User Authentication ---
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),

    # --- Other Pages ---
    path('cultural/', views.cultural_calendar, name='cultural_calendar'),
    path('booking/', views.book_experience, name='book_experience'),
    path('travel-stay/', views.travel_and_stay, name='travel_and_stay'),
    path('about/', views.about, name='about'),
]

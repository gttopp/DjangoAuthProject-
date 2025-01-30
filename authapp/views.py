# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout


# def home(request):
#         return render(request, "index.html")


# def login(request):
#  if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")

#         user = authenticate(request, username=username, password=password)
#         if user:
#                 login(user)
#                 return redirect("authapp:home")
#         messages.error(request, "Invalid username or password")
#         return redirect(request, "authapp:login")

# def register(request):
#         return render(request, "register.html")

from django.shortcuts import render
from pytube import YouTube
from pytube.exceptions import VideoUnavailable

# Define the view for the downloader
def download_video(request):
    video_url = ''
    download_link = ''
    error = ''
    
    if request.method == "POST":
        video_url = request.POST.get("url", "")
        try:
            # Fetch the video using Pytube
            yt = YouTube(video_url)
            
            # You can choose a specific stream (video/audio quality)
            stream = yt.streams.filter(progressive=True, file_extension="mp4").first()
            download_link = stream.url
        except VideoUnavailable:
            error = "The video is unavailable or invalid."
        except Exception as e:
            error = f"An error occurred: {e}"
    
    return render(request, 'downloader/download.html', {'download_link': download_link, 'error': error, 'video_url': video_url})
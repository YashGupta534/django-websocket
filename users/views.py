from django.shortcuts import render, redirect, reverse
import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

# Create your views here.

from django.views.generic.base import TemplateView

# class IndexView(TemplateView):
#     template_name = "index.html"

class HomeView(TemplateView):
    template_name = "home.html"

async def websocket_view(socket):
    await socket.accept()
    await socket.send_text('hello')
    await socket.close()

def index_view(request):
    # return redirect(reverse('/index'))
    return render(request, 'index.html')
from django.shortcuts import render
import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

# Create your views here.

from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"
    
async def websocket_view(socket):
    logging.DEBUG('Before Accept')
    print('Before Accept')
    await socket.accept()
    print('Before Send')
    logging.DEBUG('Before Send')
    await socket.send_text('hello')
    print('Before Close')
    logging.DEBUG('Before Close')
    await socket.close()
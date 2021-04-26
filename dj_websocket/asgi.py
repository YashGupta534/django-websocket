"""
ASGI config for dj_websocket project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

# import os, django

# from django.core.asgi import get_asgi_application
# # from  import get_asgi_application
# from websocket.middleware import websockets

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_websocket.settings')

# django.setup()
# application = get_asgi_application()
# application = websockets(application)

import os

from django.core.asgi import get_asgi_application
from websocket.websocket import websocket_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_websocket.settings')

django_application = get_asgi_application()

async def application(scope, receive, send):
    if scope['type'] == 'http':
        await django_application(scope, receive, send)
    elif scope['type'] == 'websocket':
        await websocket_application(scope, receive, send)
    else:
        raise NotImplementedError(f"Unknown scope type {scope['type']}")

# # websocket.py
# async def websocket_application(scope, receive, send):

#     while True:
#         event = await receive()

#         if event['type'] == 'websocket.connect':
#                 await send({
#                     'type': 'websocket.accept'
#                 })
            
#         if event['type'] == 'websocket.disconnect':
#             break
        
#         if event['type'] == 'websocket.receive':
#             if event['text'] == 'ping':
#                 await send({
#                     'type': 'websocket.send',
#                     'text': 'pong!'
#                 })
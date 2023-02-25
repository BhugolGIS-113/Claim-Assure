# routing.py
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from PreAuth.consumers import LatestUploadsConsumer

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/latest-uploads/', LatestUploadsConsumer.as_asgi()),
    ]),
})

# consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from django.core.serializers import serialize
from .models import PersonalInfo

class LatestUploadsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        # Fetch latest 5 uploads from database
        latest_uploads = PersonalInfo.objects.order_by('-NHPMID')[:5]
        serialized_uploads = serialize('json', latest_uploads)
        await self.send(text_data=json.dumps({'latest_uploads': serialized_uploads}))

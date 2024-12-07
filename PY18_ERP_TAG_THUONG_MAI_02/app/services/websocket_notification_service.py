import asyncio
import websockets

class WebSocketNotificationService:
    def __init__(self):
        self.clients = set()
    
    async def register(self, websocket):
        self.clients.add(websocket)
    
    async def unregister(self, websocket):
        self.clients.remove(websocket)
    
    async def send_notification(self, message):
        # Send the notification to all connected clients
        if self.clients:
            await asyncio.wait([client.send(message) for client in self.clients])

# Usage (in a server or async event loop):
notification_service = WebSocketNotificationService()

async def handler(websocket, path):
    await notification_service.register(websocket)
    try:
        while True:
            message = await websocket.recv()
            print(f"Received message: {message}")
    finally:
        await notification_service.unregister(websocket)

# Start the WebSocket server
start_server = websockets.serve(handler, "localhost", 6789)

# Run the event loop
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

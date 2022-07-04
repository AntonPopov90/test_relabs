from fastapi import FastAPI, WebSocket, Request
from fastapi.templating import Jinja2Templates
import json

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse('first_page.html', {"request": request})


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    count = 1
    await websocket.accept()

    while True:
        data = await websocket.receive_text()
        message = json.loads(data)
        message['count'] = count
        await websocket.send_text(json.dumps(message))
        count += 1

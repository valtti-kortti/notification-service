from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from services.email_service import sendMessage

app = FastAPI()
app.mount("/media", StaticFiles(directory="media"), name="media")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def main(request: Request) -> None:
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/send")
async def sendMessageEmail(email: str = Form(...), message: str = Form()):
    try:
        sendMessage(email, message)
        return {"status": "Сообщение отправлено"}
    except Exception as e:
        return {"status": "Ошибка отправки"}

import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv
import os

load_dotenv()

login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")


def sendMessage(email: str, message: str) -> None:
    msg = EmailMessage()
    msg.set_content(message)
    msg["Subject"] = "Уведомление"
    msg["From"] = login
    msg["To"] = email

    # Используем SMTP с TLS (порт 587)
    with smtplib.SMTP("smtp.mail.ru", 587) as server:
        server.starttls()  # Включаем шифрование
        server.login(login, password)
        server.send_message(msg)
from pydantic import BaseModel

class Notification(BaseModel):
    email: str
    telegram: str
    message: str
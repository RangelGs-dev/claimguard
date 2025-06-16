from pydantic import BaseModel

class MensagemSchema(BaseModel):
    From: str
    To: str
    Body: str
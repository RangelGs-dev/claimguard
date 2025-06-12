from fastapi import FastAPI, Form
from fastapi.responses import PlainTextResponse
from twilio.rest import Client
from claimguard.settings import Settings

app = FastAPI()
settings = Settings()

account_sid = settings.ACCOUNT_SID
auth_token = settings.AUTH_TOKEN
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
  content_variables='{"1":"12/1","2":"3pm"}',
  to='whatsapp:+559391627229'
)


@app.post('/webhook')
def receber_mensagem_whatsapp(From: str = Form(...), Body: str = Form(...)):
    print(f"Mensagem de {From}: {Body}")
    return PlainTextResponse("Recebido com sucesso!", status_code=200)

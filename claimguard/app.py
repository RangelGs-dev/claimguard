from contextlib import asynccontextmanager

from fastapi import FastAPI, Form
from fastapi.responses import PlainTextResponse
from claimguard.scheduler import configura_agenda


@asynccontextmanager
async def ciclo_de_vida(app: FastAPI):
    scheduler = configura_agenda()
    yield
    scheduler.shutdown()


app = FastAPI(lifespan=ciclo_de_vida)

@app.post('/webhook')
def receber_mensagem_whatsapp(From: str = Form(...), Body: str = Form(...)):
    print(f"Mensagem de {From}: {Body}")
    return PlainTextResponse("Recebido com sucesso!", status_code=200)

from datetime import date

from claimguard.settings import Settings
from sqlalchemy import func, select
# from sqlalchemy.orm import Session

from claimguard.database import get_session_job
from claimguard.models import Autorizacao
from twilio.rest import Client

settings = Settings()

account_sid = settings.ACCOUNT_SID
auth_token = settings.AUTH_TOKEN
client = Client(account_sid, auth_token)

def envia_mensagem():
    with get_session_job() as session:
        autorizacoes = session.scalars(
            select(Autorizacao).where(
                func.date(Autorizacao.data_solicitacao) == date.today()
            )       
        ).all()

    if autorizacoes:
        for transacao in autorizacoes:
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
                content_variables='{"1":"12/1","2":"3pm"}',
                to=f"whatsapp:+5593{transacao.celular}"
            )
            print(message.sid)
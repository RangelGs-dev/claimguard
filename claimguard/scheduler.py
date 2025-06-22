from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from claimguard.job_send_message import envia_mensagem


def configura_agenda():
    scheduler = BackgroundScheduler()
    trigger = CronTrigger(hour=1, minute=27)
    scheduler.add_job(envia_mensagem, trigger)
    scheduler.start()

    return scheduler

    
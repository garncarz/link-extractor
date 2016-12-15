from celery import Celery


app = Celery(
    'extractor',
    include=['extractor.tasks'],
)

app.config_from_object('extractor.settings')

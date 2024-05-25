from django.dispatch import receiver
from simple_history.models import HistoricalRecords
from simple_history.signals import pre_create_historical_record

@receiver(pre_create_historical_record)
def pre_create_historical_record_callback(sender, **kwargs):
    history_instance = kwargs['history_instance']
    request = getattr(HistoricalRecords.thread, 'request', None)
    if request:
        history_instance.ip_address = request.META.get('REMOTE_ADDR', '127.0.0.1')
    else:
        history_instance.ip_address = '127.0.0.1'
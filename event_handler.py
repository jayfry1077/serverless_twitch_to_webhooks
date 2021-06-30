from aws_lambda_powertools.utilities import parameters
from aws_lambda_powertools import Logger
import importlib


logger = Logger(service='twitch-event-handler')


def main(event, context):

    subscription_type = event['subscription']['type'].replace('.', '_')
    module = importlib.import_module(f'events.{subscription_type}')
    event_class = getattr(module, subscription_type)
    event_instance = event_class(event)

    event_instance.execute()
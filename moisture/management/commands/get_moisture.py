from django.core.management.base import BaseCommand, CommandError
from moisture.models import MoistureLevel
import RPi.GPIO as GPIO


class Command(BaseCommand):
    help = "Grabs moisture level and saves in DB"

    def handle(self, *args, **options):
        GPIO.setmode(GPIO.BCM)
        channel = 17
        GPIO.setup(channel, GPIO.IN)

        if GPIO.input(channel):
            saturated = False
        else:
            saturated = True
        MoistureLevel.objects.create(saturated=saturated)
        print(f"Saturated: {saturated}")

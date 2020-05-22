import datetime
import random

from django.core.management.base import BaseCommand

from rupesh.models import rupi


class Command(BaseCommand):
    help = "Save randomly generated stock record values."

    def get_date(self):
        # Naively generating a random date
        day = random.randint(1,28)
        month = random.randint(1, 12)
        year = random.randint(2017, 2020)
        return datetime.date(year, month,day)
    def handle(self, *args, **options):
        records = []
        name =["Egon Spengler","Glinda Southgood"]
        tz = ["America/Los_Angeles", "Asia/Kolkata"]
        for _ in range(10):
            kwargs = {
                'name':random.choice(name),
                'tz':random.choice(tz),
                'start_time': self.get_date(),
                'end_time': self.get_date(),
                'start_times':self.get_date(),
                'end_times':self.get_date()
            }
            record = rupi(**kwargs)
            records.append(record)
        rupi.objects.bulk_create(records)
        self.stdout.write(self.style.SUCCESS('Stock records saved successfully.'))
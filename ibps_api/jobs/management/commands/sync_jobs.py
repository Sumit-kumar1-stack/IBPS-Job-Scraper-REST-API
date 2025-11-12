import pandas as pd
from django.core.management.base import BaseCommand
from jobs.models import Job
from pathlib import Path

class Command(BaseCommand):
    help = "Sync scraped IBPS jobs from CSV into the database."

    def handle(self, *args, **kwargs):
        csv_path = Path(__file__).resolve().parents[3] / "scraper" / "outputs" / "ibps_jobs.csv"

        if not csv_path.exists():
            self.stdout.write(self.style.ERROR(f"❌ CSV file not found at {csv_path}"))
            return

        df = pd.read_csv(csv_path)

        added_count = 0
        for _, row in df.iterrows():
            job, created = Job.objects.get_or_create(
                title=row.get("Job Title", "N/A"),
                defaults={
                    "link": row.get("Link", ""),
                    "location": "N/A",  # not scraped currently
                    "publish_date": None,
                },
            )
            if created:
                added_count += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Imported {added_count} new job(s)"))

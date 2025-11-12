import os
import json
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ibps_api.settings")
django.setup()

from ibps_jobs.models import Job

# Path to your JSON file
json_path = r"C:\Users\sumit\ibps_suite\scraper\outputs\ibps_jobs.json"

with open(json_path, "r", encoding="utf-8") as f:
    jobs = json.load(f)

count = 0
for job in jobs:
    title = job.get("Job Title", "N/A")
    link = job.get("Link", "")
    posted_date = None  # since "Publish Date" is "N/A"
    
    Job.objects.get_or_create(
        title=title,
        link=link,
        posted_date=posted_date
    )
    count += 1

print(f"✅ Imported {count} jobs successfully!")

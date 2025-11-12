# 🏦 IBPS Job Scraper & REST API

This project is a **Django REST Framework (DRF)** based web application that scrapes **latest job notifications from the IBPS (Institute of Banking Personnel Selection)** official website and provides them through a secure **REST API**.  
It is designed to automate the process of fetching, storing, and serving job data, which can later be used by mobile apps, dashboards, or other job-related platforms.

---

## 🔍 Project Overview

The main idea of this project is to:
1. **Scrape job listings** (title, link, and publish date) from the official IBPS website.  
2. **Store those listings in a database** using Django ORM.  
3. **Expose the job data through REST API endpoints** for authenticated users.

This ensures that every time IBPS updates new recruitment notifications, the scraper can fetch them and update the backend automatically.

---

## ⚙️ Tech Stack Used

- **Python** – core programming language  
- **Django** – web framework  
- **Django REST Framework (DRF)** – for building APIs  
- **SQLite** – lightweight database  
- **BeautifulSoup (bs4)** – for web scraping HTML content  
- **Requests** – for making HTTP requests  
- **Token Authentication** – for secure API access  

---

## 🚀 Features

✅ Scrapes job data (title, link, date) directly from IBPS official site  
✅ Automatically stores scraped jobs into a database  
✅ REST API endpoint (`/api/jobs/`) to fetch job listings  
✅ Token-based authentication for API access  
✅ Easy to extend — can be customized to scrape other websites too  
✅ Clean, modular, and production-ready Django setup  

---

## 🧩 Project Structure

ibps_suite/
├── ibps_api/
│ ├── settings.py # Django project configuration
│ ├── urls.py # URL routing for API
│ ├── wsgi.py # WSGI entry point
│ └── ...
├── ibps_jobs/
│ ├── models.py # Job model definition
│ ├── views.py # API views using DRF
│ ├── serializers.py # Converts data to JSON
│ ├── urls.py # Job-related API routes
│ └── ...
├── scraper/
│ ├── ibps_scraper.py # Scraping script for IBPS website
│ └── outputs/
│ └── ibps_jobs.json # JSON output file from scraper
├── load_scraped_jobs.py # Script to load JSON data into Django DB
└── db.sqlite3 # SQLite database

yaml
Copy code

---

## ⚡ How It Works (Step by Step)

### 1️⃣ Scraping Data  
The **scraper script** (`ibps_scraper.py`) visits the official [IBPS website](https://www.ibps.in) and extracts job titles, links, and publish dates.  
It saves the scraped output into a JSON file (`ibps_jobs.json`) inside the `scraper/outputs` folder.

Example JSON:
json
[
  {
    "Job Title": "CRP Clerical cadre",
    "Location": "All India",
    "Publish Date": "N/A",
    "Link": "https://www.ibps.in/index.php/clerical-cadre"
  }
]
2️⃣ Importing into Database
Once the data is scraped, it is loaded into the database using the load_scraped_jobs.py script:

bash
Copy code
python load_scraped_jobs.py
This reads the JSON and creates records in the Job model in Django.

3️⃣ Exposing Data through API
The Django REST Framework exposes an authenticated API endpoint:

ruby
Copy code
GET http://127.0.0.1:8000/api/jobs/
Only users with a valid Token can access it.
The API returns a JSON response like this:

json
Copy code
[
  {
    "id": 1,
    "title": "CRP Clerical cadre",
    "link": "https://www.ibps.in/index.php/clerical-cadre",
    "posted_date": null
  }
]
🧱 Django Model Example
python
Copy code
class Job(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    posted_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
🔐 Authentication Setup
The API uses Token Authentication:

Each user has a unique token.

You must send this token with your request headers.

Example using PowerShell or cURL:

bash
Copy code
curl -Method GET http://127.0.0.1:8000/api/jobs/ `
  -Headers @{ "Authorization" = "Token your_generated_token" }
🧰 How to Run This Project Locally
1️⃣ Clone the repository
bash
Copy code
git clone https://github.com/Sumit-kumar1-stack/IBPS-Job-Scraper-REST-API.git
cd IBPS-Job-Scraper-REST-API
2️⃣ Create and activate virtual environment
bash
Copy code
python -m venv venv
venv\Scripts\activate
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run database migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate
5️⃣ Create a superuser
bash
Copy code
python manage.py createsuperuser
6️⃣ Run the scraper and import jobs
bash
Copy code
python scraper/ibps_scraper.py
python load_scraped_jobs.py
7️⃣ Start the Django server
bash
Copy code
python manage.py runserver
8️⃣ Access API
Visit: http://127.0.0.1:8000/api/jobs/
Use your authentication token to view the job list.

🧠 How to Explain in Interviews
“I built a Django REST API that scrapes real job postings from the official IBPS recruitment site.
It uses Python’s BeautifulSoup to collect job data, saves it in JSON, then loads it into a Django database.
Using Django REST Framework, I created API endpoints to expose these job details securely with token authentication.
The project can easily be extended to scrape other government job portals as well by updating the scraper logic.”

🌐 Future Scope
Add automated daily scraping using CRON jobs.

Extend scraper for multiple government job websites.

Add a frontend dashboard using React or Streamlit.

Deploy on cloud (AWS, Render, or Vercel).

👨‍💻 Author
Sumit Kumar
📧 Email: your.email@example.com
🔗 GitHub: https://github.com/Sumit-kumar1-stack

🏁 Conclusion
This project demonstrates end-to-end automation — from web scraping to database management and REST API development.
It’s a great example of combining Python, Django, and REST principles to build scalable, real-world automation tools.


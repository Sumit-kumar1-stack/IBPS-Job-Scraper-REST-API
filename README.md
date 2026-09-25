# 🏦 IBPS Job Scraper & REST API

> A Django REST Framework backend that collects IBPS recruitment notices, stores structured job data, and exposes authenticated REST endpoints for downstream applications.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-Backend-092E20?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django%20REST%20Framework-API-A30000)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Web%20Scraping-4B8BBE)

## Overview

This project demonstrates an end-to-end data pipeline:

```text
IBPS website
    │
    ▼
BeautifulSoup scraper
    │
    ▼
Structured JSON
    │
    ▼
Django ORM
    │
    ▼
Authenticated REST API
    │
    ▼
Web / mobile / dashboard consumers
```

It is useful as a compact example of web scraping, backend development, database persistence, API design, and token-based authentication.

## ✨ Features

- Scrapes recruitment notices from the official IBPS website
- Extracts job title, source link, and available publication metadata
- Stores imported data using Django ORM
- Exposes job records through Django REST Framework
- Protects API access with token authentication
- Separates scraping, persistence, and API concerns
- Can be extended to additional recruitment sources

## 🧰 Tech Stack

| Area | Technology |
|---|---|
| Language | Python |
| Backend | Django |
| API | Django REST Framework |
| Scraping | BeautifulSoup, Requests |
| Database | SQLite for local development |
| Authentication | DRF token authentication |

## 📂 Project Structure

```text
.
├── ibps_api/              # Django project configuration
├── ibps_jobs/             # Models, serializers, views, routes
├── scraper/
│   ├── ibps_scraper.py    # Scraping logic
│   └── outputs/           # Scraper output
├── load_scraped_jobs.py   # Imports scraped records into Django
├── manage.py
└── requirements.txt
```

## 🚀 Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/Sumit-kumar1-stack/IBPS-Job-Scraper-REST-API.git
cd IBPS-Job-Scraper-REST-API
```

### 2. Create and activate a virtual environment

**Windows**

```bat
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Create an admin user

```bash
python manage.py createsuperuser
```

### 6. Run the scraper and import the data

```bash
python scraper/ibps_scraper.py
python load_scraped_jobs.py
```

### 7. Start Django

```bash
python manage.py runserver
```

The local API is available at:

```text
http://127.0.0.1:8000/api/jobs/
```

## 🔐 Authentication

The API uses DRF token authentication. Send the token in the `Authorization` header:

```text
Authorization: Token <your-token>
```

Do not commit real tokens, passwords, or production secrets.

## 📦 Example Response

```json
[
  {
    "id": 1,
    "title": "CRP Clerical Cadre",
    "link": "https://www.ibps.in/",
    "posted_date": null
  }
]
```

## 💡 Engineering Concepts Demonstrated

- Web scraping and HTML parsing
- Data normalization
- Django ORM persistence
- REST API design
- Authentication
- Separation of concerns
- Extensible ingestion architecture

## 🛣️ Possible Extensions

- Scheduled scraping with Celery, cron, or a managed scheduler
- Duplicate-detection / idempotent imports
- PostgreSQL for production deployment
- Source-health monitoring and scraper alerts
- Pagination, filtering, and search
- Multiple recruitment-source adapters
- CI tests for parser behavior

## ⚠️ Responsible Scraping

External websites can change structure and usage policies over time. Before running automated collection at scale, review the target site's current terms, robots guidance, request-rate expectations, and applicable policies. Use conservative request rates and avoid unnecessary load.

## 🤝 Contributing

Issues and pull requests are welcome. Good contribution areas include parser resilience, tests, additional source adapters, API filtering, deployment, and observability.

## 👤 Author

**Sumit Kumar**  
GitHub: https://github.com/Sumit-kumar1-stack

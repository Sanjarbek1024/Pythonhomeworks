import requests
from bs4 import BeautifulSoup
import sqlite3
import csv
from datetime import datetime

# URL of the website to scrape
URL = "https://realpython.github.io/fake-jobs"

# Database connection
DB_FILE = "jobs.db"


def scrape_jobs():
    """Scrape job listings from the website and return a list of job dictionaries."""
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []
    job_elements = soup.find_all("div", class_="card-content")
    for job_element in job_elements:
        job_title = job_element.find("h2", class_="title").text.strip()
        company_name = job_element.find("h3", class_="subtitle").text.strip()
        location = job_element.find("p", class_="location").text.strip()
        job_description = job_element.find("div", class_="content").text.strip()
        application_link = job_element.find("a", text="Apply")["href"]

        jobs.append({
            "job_title": job_title,
            "company_name": company_name,
            "location": location,
            "job_description": job_description,
            "application_link": application_link
        })
    return jobs


def initialize_database():
    """Create the jobs table in SQLite if it does not already exist."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_title TEXT NOT NULL,
            company_name TEXT NOT NULL,
            location TEXT NOT NULL,
            job_description TEXT,
            application_link TEXT,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE (job_title, company_name, location)
        )
    """)

    conn.commit()
    conn.close()


def insert_or_update_jobs(jobs):
    """Insert new job listings or update existing ones in the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    for job in jobs:
        cursor.execute("""
            INSERT INTO jobs (job_title, company_name, location, job_description, application_link)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(job_title, company_name, location) 
            DO UPDATE SET 
                job_description=excluded.job_description,
                application_link=excluded.application_link,
                last_updated=CURRENT_TIMESTAMP
        """, (job["job_title"], job["company_name"], job["location"],
              job["job_description"], job["application_link"]))

    conn.commit()
    conn.close()


def filter_jobs(location=None, company_name=None):
    """Retrieve filtered job listings by location or company name."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    query = "SELECT * FROM jobs WHERE 1=1"
    params = []

    if location:
        query += " AND location = ?"
        params.append(location)
    if company_name:
        query += " AND company_name = ?"
        params.append(company_name)

    cursor.execute(query, params)
    jobs = cursor.fetchall()

    conn.close()
    return jobs


def export_to_csv(jobs, filename):
    """Export filtered job listings to a CSV file."""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company Name", "Location", "Job Description", "Application Link", "Last Updated"])
        writer.writerows(jobs)


def main():
    # Step 1: Initialize the database
    initialize_database()

    # Step 2: Scrape jobs
    jobs = scrape_jobs()

    # Step 3: Insert or update jobs in the database
    insert_or_update_jobs(jobs)

    # Step 4: Filter and export jobs
    print("Available Filters:")
    print("1. Filter by Location")
    print("2. Filter by Company Name")
    print("3. Export All Jobs")

    choice = input("Enter your choice (1/2/3): ").strip()
    filtered_jobs = []

    if choice == "1":
        location = input("Enter location to filter: ").strip()
        filtered_jobs = filter_jobs(location=location)
    elif choice == "2":
        company_name = input("Enter company name to filter: ").strip()
        filtered_jobs = filter_jobs(company_name=company_name)
    elif choice == "3":
        filtered_jobs = filter_jobs()

    if filtered_jobs:
        filename = f"filtered_jobs_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
        export_to_csv(filtered_jobs, filename)
        print(f"Jobs exported to {filename}")
    else:
        print("No jobs found for the selected filter.")


if __name__ == "__main__":
    main()

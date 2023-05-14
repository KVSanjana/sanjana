import requests
from bs4 import BeautifulSoup
import json


def scrape_job_postings():
    url = "https://www.cermati.com/karir"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    print(soup,"000")
    departments = soup.select("department")
    print(departments,"aa")
    job_data = {"test":"test val"}
    print(departments, "11")
    for department in departments:
        department_name = department.text
        department_url = department["href"]
        jobs = get_jobs_from_department(department_url)
        job_data[department_name] = jobs
    print(job_data)
    with open("job_openings.json", "w") as json_file:
        json.dump(job_data, json_file, indent=4)

    print("Job data has been scraped and saved to job_openings.json.")


def get_jobs_from_department(department_url):
    response = requests.get(department_url)
    soup = BeautifulSoup(response.content, "html.parser")
    job_elements = soup.select(".job-post")
    jobs = []

    for job_element in job_elements:
        title = job_element.select_one(".job-title").text
        location = job_element.select_one(".job-location").text
        posted_by = job_element.select_one(".job-postedby").text

        description_elements = job_element.select(".job-description p")
        description = [element.text for element in description_elements]

        qualification_elements = job_element.select(".job-qualification li")
        qualification = [element.text for element in qualification_elements]

        job = {
            "title": title,
            "location": location,
            "description": description,
            "qualification": qualification,
            "posted by": posted_by
        }
        jobs.append(job)
    print(jobs, "22")
    return jobs


print("33")

scrape_job_postings()

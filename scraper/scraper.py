# scraper/scraper.py
import requests
from bs4 import BeautifulSoup
import logging
import json
import os

logger = logging.getLogger(__name__)

DATA_LAKE_DIR = os.getenv('DATA_LAKE_DIR', './data_lake')
if not os.path.exists(DATA_LAKE_DIR):
    os.makedirs(DATA_LAKE_DIR)

def save_data(source_name, data):
    filename = os.path.join(DATA_LAKE_DIR, f"{source_name}.json")
    with open(filename, 'w') as f:
        json.dump(data, f)
    logger.info(f"Data saved for {source_name} at {filename}")

def scrape_openfda():
    url = "https://api.fda.gov/drug/drugsfda.json?limit=100"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        save_data("openfda", data)
        return data
    except Exception as e:
        logger.error(f"Error scraping openfda: {e}")
        return None

def scrape_clinical_trials():
    url = "https://clinicaltrials.gov/api/v2/studies?fmt=json&max_rnk=100"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        save_data("clinical_trials", data)
        return data
    except Exception as e:
        logger.error(f"Error scraping clinical trials: {e}")
        return None

def scrape_mayoclinic_drugs():
    url = "https://www.mayoclinic.org/drugs-supplements"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        drugs = []
        for item in soup.find_all("a", href=True):
            if "/drugs-supplements/" in item['href']:
                drugs.append({"name": item.text.strip(), "url": item['href']})
        save_data("mayoclinic_drugs", drugs)
        return drugs
    except Exception as e:
        logger.error(f"Error scraping mayoclinic drugs: {e}")
        return None

def scrape_mayoclinic_diseases():
    url = "https://www.mayoclinic.org/diseases-conditions"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        diseases = []
        for item in soup.find_all("a", href=True):
            if "/diseases-conditions/" in item['href']:
                diseases.append({"name": item.text.strip(), "url": item['href']})
        save_data("mayoclinic_diseases", diseases)
        return diseases
    except Exception as e:
        logger.error(f"Error scraping mayoclinic diseases: {e}")
        return None

def scrape_mayoclinic_symptoms():
    url = "https://www.mayoclinic.org/symptoms"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        symptoms = []
        for item in soup.find_all("a", href=True):
            if "/symptoms/" in item['href']:
                symptoms.append({"name": item.text.strip(), "url": item['href']})
        save_data("mayoclinic_symptoms", symptoms)
        return symptoms
    except Exception as e:
        logger.error(f"Error scraping mayoclinic symptoms: {e}")
        return None

def scrape_drugs_com_otc():
    url = "https://www.drugs.com/otc/"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        otc_drugs = []
        for item in soup.find_all("a", href=True):
            if "/otc/" in item['href']:
                otc_drugs.append({"name": item.text.strip(), "url": item['href']})
        save_data("drugs_com_otc", otc_drugs)
        return otc_drugs
    except Exception as e:
        logger.error(f"Error scraping drugs.com otc: {e}")
        return None

def scrape_medlineplus():
    url = "https://medlineplus.gov/druginformation.html"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        drugs_info = []
        for item in soup.find_all("a", href=True):
            if "druginformation" in item['href']:
                drugs_info.append({"name": item.text.strip(), "url": item['href']})
        save_data("medlineplus", drugs_info)
        return drugs_info
    except Exception as e:
        logger.error(f"Error scraping medlineplus: {e}")
        return None

def scrape_dailymed():
    # Example: scraping drug names and classes from DailyMed API endpoints
    drugnames_url = "https://www.dailymed.nlm.nih.gov/dailymed/webservices-help/v2/drugnames_api.cfm?output=json"
    drugclasses_url = "https://www.dailymed.nlm.nih.gov/dailymed/webservices-help/v2/drugclasses_api.cfm?output=json"
    try:
        response_names = requests.get(drugnames_url, timeout=10)
        response_names.raise_for_status()
        names_data = response_names.json()

        response_classes = requests.get(drugclasses_url, timeout=10)
        response_classes.raise_for_status()
        classes_data = response_classes.json()

        combined = {"drugnames": names_data, "drugclasses": classes_data}
        save_data("dailymed", combined)
        return combined
    except Exception as e:
        logger.error(f"Error scraping dailymed: {e}")
        return None

def scrape_webmd():
    url = "https://www.webmd.com/drugs/2/index"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        drugs = []
        for item in soup.find_all("a", href=True):
            if "/drugs/" in item['href']:
                drugs.append({"name": item.text.strip(), "url": item['href']})
        save_data("webmd", drugs)
        return drugs
    except Exception as e:
        logger.error(f"Error scraping webmd: {e}")
        return None

def scrape_imaging():
    # For CT scans and MRI images, we scrape an example imaging site (e.g., Radiopaedia)
    url = "https://radiopaedia.org/articles"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        imaging_cases = []
        for item in soup.find_all("a", href=True):
            if "/cases/" in item['href']:
                imaging_cases.append({"title": item.text.strip(), "url": item['href']})
        save_data("imaging", imaging_cases)
        return imaging_cases
    except Exception as e:
        logger.error(f"Error scraping imaging cases: {e}")
        return None

if __name__ == "__main__":
    # For testing individual scrapers
    scrape_openfda()
    scrape_clinical_trials()
    scrape_mayoclinic_drugs()
    scrape_mayoclinic_diseases()
    scrape_mayoclinic_symptoms()
    scrape_drugs_com_otc()
    scrape_medlineplus()
    scrape_dailymed()
    scrape_webmd()
    scrape_imaging()

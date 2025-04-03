# scraper/scheduler.py
from apscheduler.schedulers.blocking import BlockingScheduler
import logging
from scraper import scraper

logger = logging.getLogger(__name__)

def scheduled_scrape():
    logger.info("Starting scheduled scraping tasks")
    scraper.scrape_openfda()
    scraper.scrape_clinical_trials()
    scraper.scrape_mayoclinic_drugs()
    scraper.scrape_mayoclinic_diseases()
    scraper.scrape_mayoclinic_symptoms()
    scraper.scrape_drugs_com_otc()
    scraper.scrape_medlineplus()
    scraper.scrape_dailymed()
    scraper.scrape_webmd()
    scraper.scrape_imaging()
    logger.info("Scheduled scraping tasks completed")

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    # Schedule to run every day at 2 AM
    scheduler.add_job(scheduled_scrape, 'cron', hour=2)
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

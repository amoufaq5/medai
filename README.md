# Medical AI Diagnostic System

## Overview
This project implements a multi-microservice Medical AI Diagnostic System that:
- Scrapes data from various sources (openFDA, clinicaltrials.gov, drugs.com, medlineplus, dailymed, WebMD, etc.).
- Preprocesses and annotates multimodal data (text, CT scans, MRI images, blood tests).
- Trains a TensorFlow-based multimodal diagnosis model.
- Implements a custom dialogue system incorporating ASMETHOD, ENCORE, and SIT DOWN SIR frameworks.
- Provides a Flask-based chatbot interface with day (white & blue) and night (black & red) themes.

## Architecture
- **Scraper:** Collects data from APIs and web pages using `requests` and BeautifulSoup, scheduled with APScheduler.
- **Preprocessing:** Cleans and annotates textual data and processes imaging data using OpenCV and TensorFlow.
- **Training:** Builds and trains a multimodal neural network.
- **Dialogue:** Implements a custom dialogue system to interpret user input and generate diagnostic responses.
- **API:** A Flask application providing a RESTful endpoint and a web interface for user interaction.
- **Utils:** Centralized logging and utility functions.

## Setup and Installation

1. **Clone the repository:**

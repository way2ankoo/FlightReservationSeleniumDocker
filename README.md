# Python Selenium Test Framework

This repository contains a Python Selenium test framework using pytest and Selenium Grid with Docker.

## Prerequisites

- Python 3.6+
- Docker
- Docker Compose

## Setup

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   
2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   (selenium, pytest, pytest-dependency & pytest-html)

3. **Pull below docker images:**

   ```bash
   selenium/hub
   selenium/node-chrome
   selenium/node-firefox
   
4. **Use docker-compose.yml and spin-up containers to start Selenium Grid:**
   
   ```bash
   docker-compose up
   docker-compose up -d

5. **Run your test:**

   ```bash
   pytest tests/

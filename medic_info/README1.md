# Week 7 Project: Ethiopian Medical Businesses Data Warehouse

## Project Overview

This project aims to build a data warehouse for Ethiopian medical businesses, integrating object detection capabilities using YOLO (You Only Look Once) and developing ETL/ELT pipelines. The project involves scraping data from Telegram channels, performing object detection on collected images, and exposing the collected data through a FastAPI application.

## Table of Contents

- [Objectives](#objectives)
- [Project Structure](#project-structure)
- [Tasks](#tasks)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)

## Objectives

- Scrape data from public Telegram channels related to Ethiopian medical businesses.
- Perform object detection on images collected from Telegram channels.
- Store the detection results in a PostgreSQL database.
- Expose the collected data via a REST API using FastAPI.

## Project Structure

## Tasks

### Task 1: Data Scraping
- Develop a data scraping pipeline to extract data from public Telegram channels related to Ethiopian medical businesses.
- Use Python packages such as Telethon, Beautiful Soup, Scrapy, and Selenium for scraping.
- Collect images for object detection from channels like Chemed and Lobelia for Cosmetics.

### Task 2: Data Cleaning and Transformation
- Clean and transform the scraped data using two CSV files.
- Prepare the data for analysis and storage.

### Task 3: Object Detection Using YOLO
- Set up the environment and install necessary dependencies for YOLO.
- Download the YOLO model and perform object detection on the scraped images.
- Extract relevant detection results (bounding box coordinates, confidence scores, class labels) and store them in the database.

### Task 4: Expose Collected Data Using FastAPI
- Create a FastAPI application to expose the collected data via API endpoints.
- Implement CRUD operations for managing detection records in the database.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd my_project

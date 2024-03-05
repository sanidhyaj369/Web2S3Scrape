# importing the necessary libraries
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import boto3

# Function to scrape website and return data
def scrape_website(url):

    # Sending GET request to the URL
    response = requests.get(url)

    # Checking if request was successfull
    if response.status_code == 200:
        # Parsing the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extracting the relevant data
        jobs = soup.find_all('li', class_ = "clearfix job-bx wht-shd-bx")

        # Creating a dictonary to store data
        data = {'Company Name': [], 'Skills': [], 'Experience': [], 'Location': [], 'More Info': []}

        for job in jobs:
            company_name = job.find('h3', class_ = "joblist-comp-name").text.strip().title()
            skills = job.find('span', class_ = "srp-skills").text.replace(' ','').strip()
            experience = job.find('li').text.removeprefix("card_travel")
            location = job.find('span').text
            more_info = job.header.h2.a['href']
            data['Company Name'].append(company_name)
            data['Skills'].append(skills)
            data['Experience'].append(experience)
            data['Location'].append(location)
            data['More Info'].append(more_info)

        # Creating a dataframe from dictonary
        df = pd.DataFrame.from_dict(data)
        return df 
    
    else: 
        print("Failed to retrieve data from the website.")
        return None
    

# Function to export dataframe to CSV and uploading it to AWS S3 bucket
def export_to_s3(df, bucket_name, file_name, region_name='ap-south-1'):
    
    # Exporting the dataframe to CSV
    df.to_csv(file_name, index=False)
    os.path.join(os.getcwd(), file_name)

    # Initializing the S3 client with specified region
    s3 = boto3.client('s3', region_name=region_name)

    # Creating the S3 bucket and uploading file in bucket
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region_name})

    s3.upload_file(file_name, bucket_name, file_name)
    print(f"{file_name} uploaded to S3 bucket {bucket_name}.")
    

# URL of the website to scrape
url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation="
    
# Name of the AWS S3 bucket
bucket_name = 'web-scrapping-unique123'
    
# File name for CSV
file_name = 'Python_Jobs.csv'
    
# Scraping the website and storing the data in DataFrame
data = scrape_website(url)

# Exporting the data to CSV file and uploading it to AWS S3 bucket
if data is not None:
    export_to_s3(data, bucket_name, file_name)

Purpose:
The purpose of this script is to scrape job listings related to Python from a specific website (timesjobs.com), store the scraped data into a DataFrame, and then export that DataFrame into a CSV file. Additionally, it uploads this CSV file to an AWS S3 bucket using boto3.

Libraries Used:
- os: Provides a portable way of using operating system-dependent functionality.
- requests: Used to send HTTP requests to the website and fetch its content.
- BeautifulSoup (from bs4): Used for parsing HTML content fetched from the website.
- pandas: Used for creating and manipulating data in a DataFrame.
- boto3: AWS SDK for Python. Used for interacting with AWS services like S3.

Functions:
1. scrape_website(url):
- This function takes a URL as input, sends a GET request to that URL. If the request is successful (status code 200), it parses the HTML content using BeautifulSoup.
- It then extracts relevant job information such as company name, skills required, experience level, location, and more info link from the HTML based on the provided class.
- This information is stored in a dictionary and then converted to a DataFrame.
- Finally, the DataFrame containing job information is returned.

2. export_to_s3(df, bucket_name, file_name, region_name='ap-south-1'):
- This function takes a DataFrame (df), an AWS S3 bucket name (bucket_name), a file name for CSV (file_name), and an optional AWS region name (region_name).
- It exports the DataFrame to a CSV file.
- Initializes an S3 client and creates an S3 bucket in the specified region.
- Uploads the CSV file to the specified S3 bucket.
- Finally, it prints a message confirming the successful upload.

Main Execution:
- Defines the URL of the website to scrape for Python jobs.
- Specifies the name of the AWS S3 bucket to upload the data.
- Defines the file name for the CSV file.
- Calls the scrape_website() function to scrape job data from the website.
- If the scraping operation is successful (data is not None), it calls the export_to_s3() function to export the data to a CSV file and upload it to the specified S3 bucket.

Note:
- Ensure that you have necessary permissions set up for accessing AWS S3.
- Install required libraries (requests, beautifulsoup4, pandas, boto3) using pip before running the code.
- Make sure to replace 'web-scrapping-unique123' with your own S3 bucket name and adjust the region accordingly.
- Also, verify the HTML structure of the target website in case any changes have been made, as this code relies heavily on it for scraping job information.
import re
from datetime import datetime
import feedparser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class JobFeedProcessor:
    def __init__(self, rss_feed_url):
        self.rss_feed_url = rss_feed_url
        self.entries = []

    def fetch_rss_data(self):
        feed = feedparser.parse(self.rss_feed_url)
        self.entries = feed.entries

    def process_entries(self):
        # Define the desired skills
        desired_skills = ['Databricks Platform', 'Big Data', 'Data Science' 'Terraform', 'AWS Glue,', 'AWS','Amazon Web Services',
                           'Spark', 'PySpark', 'Python', 'SQL Server', 'Apache Spark', 'ETL Pipeline', 'AWS S3']

        # Get today's date in the format "Month Day, Year"
        today_date = datetime.now().strftime('%B %d, %Y')

        # Initialize an empty string to store the email content
        email_content = ""

        for entry in self.entries:
            title = entry.title 
            url = entry.link
            description = entry.description

            # Clean up the description (remove HTML tags)
            cleaned_description = re.sub(r'<.*?>', '', description)

            skills = re.findall(r'<b>Skills</b>:\s*(.*?)(?=<|$)', description)

            # Extract the "Posted On" date from the description
            posted_date_match = re.search(r'Posted On: ([A-Za-z]+ \d{1,2}, \d{4})', cleaned_description)
            
            if posted_date_match:
                # Extract the posted date from the match
                posted_date = posted_date_match.group(1).strip()

                # Check if the posted date matches today's date
                if posted_date == today_date:
                    # Check if skills are found
                    if skills: 
                        skills_list = [skill.strip() for skill in skills[0].split(',')]

                        # Check if any of the desired skills are present in the skills list
                        relevant_skills = [skill for skill in skills_list if skill in desired_skills]

                        if relevant_skills:
                            # Append job details to the email content
                            email_content += f"Title: {title}\n"
                            email_content += f"URL: {url}\n"
                            email_content += f"Description: {cleaned_description}\n"
                            email_content += f"Relevant Skills: {relevant_skills}\n\n"
                    else: 
                        email_content += "No Skills Found\n"
            else:
                email_content += "Posted date not found\n"

        return email_content

# Function to send email
def send_email(email_content):
    # Email configuration
    sender_email = "enmanuelm385@gmail.com"
    receiver_email = "emadera@emanalyticsllc.com"
    password = "twnd mvwn muqh vvgv"
    
    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Job Entries for Today"
    
    # Add email content
    message.attach(MIMEText(email_content, "plain"))
    
    # Connect to SMTP server and send email
    # Connect to Google SMTP server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
# RSS Feed URL

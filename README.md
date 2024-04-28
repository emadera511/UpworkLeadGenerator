# Generating Leads From Upwork 

This program will generate the leads from upwork below is the psudocode of the program: 

Class JobFeedProcessor:
    Constructor:
        Initialize rss_feed_url
        Initialize entries as an empty list

    Method fetch_rss_data():
        Parse the RSS feed from rss_feed_url using feedparser
        Store the parsed entries in the entries list

    Method process_entries():
        Define desired_skills list
        Get today's date in the format "Month Day, Year"

        For each entry in entries:
            Extract title, url, and description from the entry
            Clean up the description (remove HTML tags)

            Extract skills from the description using regular expressions

            Extract the "Posted On" date from the description using regular expressions
            If "Posted On" date is found:
                Extract and clean the posted date
                If the posted date matches today's date:
                    If skills are found:
                        Extract and clean the skills list
                        Check if any of the desired skills are present in the skills list
                        If relevant skills are found:
                            Print title, URL, description, and relevant skills
                    Else:
                        Print "No Skills Found"
            Else:
                Print "Posted date not found"

# Define the RSS Feed URL
rss_feed_url = "https://www.upwork.com/ab/feed/jobs/rss?paging=0-10&q=databricks&sort=recency&api_params=1&securityToken=868c62fc648e2665016beca66dc2546eb419edf5d2a8d41c4bef71ae6f7e70f99c8f6a574f9e410182edf286da8d6261c24090c402fea9a97f9a7e0cc6d0349d&userUid=1734205641781354496&orgUid=1734205641781354497"

# Create an instance of JobFeedProcessor
job_processor = JobFeedProcessor(rss_feed_url)

# Fetch and process the RSS data
job_processor.fetch_rss_data()
job_processor.process_entries()

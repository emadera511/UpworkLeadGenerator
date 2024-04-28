from LeadGenerator.JobGenerator import JobFeedProcessor, send_email

jobs = {
    'Data Analysis': 'https://www.upwork.com/ab/feed/jobs/rss?paging=0-10&q=data%20analyst&sort=recency&api_params=1&securityToken=868c62fc648e2665016beca66dc2546eb419edf5d2a8d41c4bef71ae6f7e70f99c8f6a574f9e410182edf286da8d6261c24090c402fea9a97f9a7e0cc6d0349d&userUid=1734205641781354496&orgUid=1734205641781354497', 
    'Data Engineer': 'https://www.upwork.com/ab/feed/jobs/rss?paging=0-10&q=data%20Engineer&sort=recency&api_params=1&securityToken=868c62fc648e2665016beca66dc2546eb419edf5d2a8d41c4bef71ae6f7e70f99c8f6a574f9e410182edf286da8d6261c24090c402fea9a97f9a7e0cc6d0349d&userUid=1734205641781354496&orgUid=1734205641781354497',
    'SQL Developer': 'https://www.upwork.com/ab/feed/jobs/rss?paging=0-10&q=sql%20server%20dba&sort=recency&api_params=1&securityToken=868c62fc648e2665016beca66dc2546eb419edf5d2a8d41c4bef71ae6f7e70f99c8f6a574f9e410182edf286da8d6261c24090c402fea9a97f9a7e0cc6d0349d&userUid=1734205641781354496&orgUid=1734205641781354497'
}

for job, url in jobs.items(): 
    print(url)
    # Create an instance of JobFeedProcessor
    job_processor = JobFeedProcessor(url)

    # Fetch the RSS data
    job_processor.fetch_rss_data()

    # Process the entries and get email content
    email_content = job_processor.process_entries()

    send_email(email_content, job)

   
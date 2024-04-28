from LeadGenerator.JobGenerator import JobFeedProcessor, send_email

rss_feed_url = ["https://www.upwork.com/ab/feed/jobs/rss?category2_uid=531770282580668420&paging=0-10&q=aws&sort=recency&api_params=1&securityToken=868c62fc648e2665016beca66dc2546eb419edf5d2a8d41c4bef71ae6f7e70f99c8f6a574f9e410182edf286da8d6261c24090c402fea9a97f9a7e0cc6d0349d&userUid=1734205641781354496&orgUid=1734205641781354497", "https://www.upwork.com/ab/feed/jobs/rss?category2_uid=531770282580668420&paging=0-10&q=databricks&sort=recency&api_params=1&securityToken=868c62fc648e2665016beca66dc2546eb419edf5d2a8d41c4bef71ae6f7e70f99c8f6a574f9e410182edf286da8d6261c24090c402fea9a97f9a7e0cc6d0349d&userUid=1734205641781354496&orgUid=1734205641781354497"]
# ["https://www.upwork.com/ab/feed/jobs/rss?paging=0-10&q=databricks&sort=recency&api_params=1&securityToken=868c62fc648e2665016beca66dc2546eb419edf5d2a8d41c4bef71ae6f7e70f99c8f6a574f9e410182edf286da8d6261c24090c402fea9a97f9a7e0cc6d0349d&userUid=1734205641781354496&orgUid=1734205641781354497",
# "https://www.upwork.com/ab/feed/jobs/rss?paging=0-10&q=sql%20developer&sort=recency&api_params=1&securityToken=868c62fc648e2665016beca66dc2546eb419edf5d2a8d41c4bef71ae6f7e70f99c8f6a574f9e410182edf286da8d6261c24090c402fea9a97f9a7e0cc6d0349d&userUid=1734205641781354496&orgUid=1734205641781354497"
# ]

for url in rss_feed_url: 
    print(url)
    # Create an instance of JobFeedProcessor
    job_processor = JobFeedProcessor(url)

    # Fetch the RSS data
    job_processor.fetch_rss_data()

    # Process the entries and get email content
    email_content = job_processor.process_entries()

    send_email(email_content)

   
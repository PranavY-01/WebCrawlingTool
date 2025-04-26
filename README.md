# WebCrawlingTool
I developed my own GUI based web crawling tool to do web crawling using python.

Purpose:
Web crawling tools, also known as web spiders or bots, are automated programs that systematically explore the internet, following links and extracting information from websites.
	1.Indexing for Search Engines:
		1.Search engines like Google use web crawlers to discover, index, and rank web pages. 
		2.These crawlers follow links between web pages to build a comprehensive index of the internet. 
		3.The index is then used to provide relevant search results to users. 
	2.Data Extraction and Scraping:
		1.Web crawlers can be used to extract specific data from web pages, such as prices, product information, or news articles.
		2.This extracted data can be used for various purposes, including e-commerce, market research, or data analysis. 
	3.Monitoring and Automation:
		1.Web crawlers can be used to monitor websites for changes or new content.
		2.They can automate tasks like updating databases or sending notifications when new information is found. 
	4.Content Aggregation and RSS Feeds:
		1.Web crawlers can be used to gather content from different websites and aggregate it into a single feed.
		2.This can be used for creating news aggregators, RSS feeds, or other content-driven websites. 
	5.SEO and Website Optimization:
		1.Web crawlers help search engines understand the content and structure of a website.
		2.Website owners can use this knowledge to optimize their sites for better search engine rankings. 
	
How it works:
1.Type the website URL inside the box.
2.Enter how many pages you want. (Default: 5)
3.Enter the file name and filepath location where you want to save.
4.Click o the "Start Crawl" button.
5.It crawls the given page and the internal url pages. 
6.Saves URL and parameters data in your desired file in .csv extension automatically.

Advantages:
1.Recursive: It crawls inside linked pages too (not just the homepage).
2.Same domain only: Won’t accidentally crawl other domains (Facebook, Google, etc).
3.Depth control: You can control how deep it should go.
4.Error handling:Friendly popup error messages to correct the user to give valid input (like valid webpages, valid number of pages, valid file name & location).

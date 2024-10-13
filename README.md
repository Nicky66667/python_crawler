# Python Spider Learning Resources

This repository contains learning resources for beginners to learn how to create web crawlers (spiders) in Python. 
The materials include examples of fetching web page data and filtering information from it.

All notes and explanations can be found in `note.md`.

## Contents

1. **learn_urllib.py** and **learn_requests.py**  
   These scripts provide simple examples of how to request the HTML source from websites using the `urllib` and `requests` libraries.

2. **crawl_douban.py**  
   This is a practical example of web scraping from the Douban website. It demonstrates how to:
   - Fetch data from the Douban Top 250 movies page.
   - Filter information such as movie titles, release years, ratings, and review counts using regex.
   - Print information and store it in a CSV file (`data_douban.csv`).

## How to Run

All programs can be executed by running:

```bash
python <script_name>.py

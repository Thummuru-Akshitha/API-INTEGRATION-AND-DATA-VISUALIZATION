# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*: CODETECH IT SOLUTIONS

*NAME*: THUMMURU AKSHITHA

*INTERN ID*: CT06WR252

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 6 WEEKS

*MENTOR*: NEELA SANTOSH

*DESCRIPTION OF  API-INTEGRATION-AND-DATA-VISUALIZATION*:
This Python program is designed to fetch the latest top news headlines from India using the NewsAPI and then present the information both in text format and visually through a horizontal bar chart. It combines the use of APIs, basic data handling, and data visualization techniques to create a small but functional project that touches multiple important concepts in programming.
1. Libraries Used
The program uses three important Python libraries:
requests:
This is used to make HTTP requests to the NewsAPI service. It allows the program to retrieve live data from the web.
matplotlib.pyplot:
A popular plotting library used here for creating a bar chart of the news sources and the number of articles fetched from each.
collections.Counter:
Used to count how many articles came from each news source efficiently.
These libraries make the program powerful without writing complex code from scratch.
2. Connecting to the NewsAPI
The program starts by requiring a valid API key from NewsAPI.org.
An API key is essentially a password that authorizes a user to access the service.
Once the API key is provided, the program builds a URL endpoint to fetch top news headlines for the country code in (India).
The URL format used:
bash
Copy code
https://newsapi.org/v2/top-headlines?country=in&apiKey=YOUR_API_KEY
It then uses the requests.get(url) function to send a request to NewsAPI's servers and gets the news articles in a JSON format.
3. Checking the API Response
After making the request, it is important to check if the response is successful.
The program checks:
If response.status_code == 200 (which means HTTP OK),
If data['status'] == 'ok' (which is NewsAPI's way of saying the request succeeded).
If both are true, it proceeds. Otherwise, it prints an error message showing what went wrong (e.g., "Invalid API Key", "Rate limit exceeded", etc.).
4. Displaying Top 5 Headlines
Once the articles are successfully fetched:
The program prints the first 5 news headlines along with the name of their source (such as "Times of India", "NDTV", etc.).
It uses Python’s enumerate function to number them neatly from 1 to 5.
This part gives the user a quick view of the trending news without needing to open any news website.
5. Analyzing the News Sources
After listing the top 5 headlines, the program focuses on analyzing the sources:
It extracts all source names from the articles.
It uses the Counter class from the collections module to count how many articles each source contributed.
The data is sorted in descending order — the source with the most articles appears first.
This gives a sense of which news organizations are most active or dominant among the top headlines.
6. Plotting the Data
Finally, the program creates a horizontal bar chart using matplotlib:
The y-axis contains the names of news sources.
The x-axis represents the number of articles contributed by each source.
The most active source appears at the top (using plt.gca().invert_yaxis()).
The chart is styled with:
A custom color (teal) for the bars,
Proper labels and a title,
tight_layout() to avoid overlaps.
This visualization allows users to instantly understand the distribution of news across different sources.

Why Is This Program Useful?
Real-World Data: It shows how you can connect to real-world APIs and fetch live data dynamically.
Practical API Skills: Working with APIs is an essential modern development skill.
Data Parsing: It teaches how to handle and parse complex JSON data.
Data Analysis and Visualization: It introduces basic techniques for analyzing and visualizing data to make it understandable quickly.
Automation: Instead of manually visiting multiple websites, you automate the gathering of news in a few seconds.
Potential Extensions
This simple project can be extended in many ways, such as:
Allowing users to input a keyword (e.g., "sports", "technology") to fetch topic-specific news.
Fetching headlines for different countries.
Scheduling the script to run automatically and save the results to a file.
Adding error handling for empty fields or unexpected server errors.
Making a small GUI (Graphical User Interface) to make it even more user-friendly.

Conclusion
Overall, this program is a compact, real-world Python project that brings together web APIs, data processing, and visualization into one easy-to-understand flow.
It is a great starting point for beginners who want to move beyond simple console programs and start working with live web data and basic visual analytics.








# Step 1: Import necessary libraries
import requests
import matplotlib.pyplot as plt
from collections import Counter

# Step 2: Add your NewsAPI Key here
API_KEY = 'a7934b18e0c94d4695b70e9befe53d46'  

# Step 3: Define the API endpoint
url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}"

# Step 4: Send the GET request to NewsAPI
response = requests.get(url)
data = response.json()

# Step 5: Check if the request was successful
if response.status_code == 200 and data.get('status') == 'ok':
    articles = data.get('articles', [])

    if not articles:
        print("No news articles found.")
    else:
        print("\nTop 5 Headlines:\n" + "-" * 30)
        for i, article in enumerate(articles[:5], 1):
            title = article.get('title', 'No Title')
            source = article.get('source', {}).get('name', 'Unknown Source')
            print(f"{i}. {title} ({source})")

        # Step 6: Count the number of articles per source
        sources = [article.get('source', {}).get('name', 'Unknown Source') for article in articles]
        source_counts = Counter(sources)

        # Step 7: Prepare data for plotting
        sorted_sources = source_counts.most_common()
        labels = [source for source, _ in sorted_sources]
        counts = [count for _, count in sorted_sources]

        # Step 8: Plot the data
        plt.figure(figsize=(10, 6))
        plt.barh(labels, counts, color='teal')
        plt.xlabel("Number of Articles")
        plt.title("News Sources and Article Counts")
        plt.gca().invert_yaxis()  # Show most articles at the top
        plt.tight_layout()
        plt.show()

else:
    print("Error fetching news:", data.get("message", "Unknown error"))

import requests
import json
import xmltodict

# Define the arXiv API endpoint and search parameters
ARXIV_API = "http://export.arxiv.org/api/query"
KEYWORDS = "machine learning, AI, deep learning"

# Fetch papers from arXiv API
def fetch_papers():
    params = {
        "search_query": f"all:{KEYWORDS}",
        "start": 0,
        "max_results": 10,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    response = requests.get(ARXIV_API, params=params)
    if response.status_code == 200:
        # Parse XML response to JSON-like dictionary
        return xmltodict.parse(response.text)
    else:
        print("Failed to fetch papers.")
        return None

# Save fetched papers to a JSON file
def save_papers(data):
    with open("papers.json", "w") as file:
        json.dump(data, file, indent=4)

# Main execution
if __name__ == "__main__":
    papers = fetch_papers()
    if papers:
        save_papers(papers)
        print("Papers fetched and saved successfully.")
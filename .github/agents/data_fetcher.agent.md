---
agent_type: data_fetcher
model: gpt-4
tools:
  - arxiv_api
---

# Data Fetcher Agent

## Purpose
This agent is responsible for fetching the latest arXiv papers based on user-defined keywords.

## Tasks
1. Query the arXiv API with specified keywords.
2. Parse the response to extract paper details (title, authors, abstract, PDF link).
3. Save the data in a structured format (e.g., JSON).
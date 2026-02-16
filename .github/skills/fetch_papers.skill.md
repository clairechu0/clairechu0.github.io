---
skill_name: fetch_papers
description: Queries the arXiv API for papers matching keywords and formats the response.
---

# Fetch Papers Skill

## Purpose
This skill queries the arXiv API for papers matching user-defined keywords and formats the response for further processing.

## Steps
1. Accept keywords as input.
2. Query the arXiv API.
3. Parse the response to extract relevant details (title, authors, abstract, PDF link).
4. Return the data in JSON format.
---
agent_type: data_updater
model: gpt-4
tools:
  - git
  - html_editor
---

# Data Updater Agent

## Purpose
This agent updates the paper list on the website and triggers the GitHub Actions workflow for auto-updates.

## Tasks
1. Update the HTML file with new paper data.
2. Ensure proper formatting and styling of the updated content.
3. Commit and push changes to the repository.
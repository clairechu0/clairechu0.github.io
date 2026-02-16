import json

# Load papers from JSON file
def load_papers():
    with open("papers.json", "r") as file:
        return json.load(file)

# Update the HTML file with paper data
def update_html(papers):
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paper Listing</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Latest arXiv Papers</h1>
        <nav>
            <ul>
                <li><a href="index.html">Home</a></li>
                <li><a href="pacman.html">Play Pacman</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section>
            <h2>Paper Feed</h2>
            <ul>
    """

    for entry in papers['feed']['entry']:
        title = entry['title']
        pdf_url = next(link['@href'] for link in entry['link'] if link['@rel'] == 'related' and link['@type'] == 'application/pdf')
        authors = [author['name'] for author in entry['author']]
        html_content += f"<li><a href='{pdf_url}'>{title}</a> by {', '.join(authors)}</li>"

    html_content += """
            </ul>
        </section>
    </main>
    <footer>
        <p>&copy; 2026 My Personal Website</p>
    </footer>
</body>
</html>
"""

    with open("papers.html", "w") as file:
        file.write(html_content)

# Main execution
if __name__ == "__main__":
    papers = load_papers()
    update_html(papers)
    print("papers.html updated successfully.")
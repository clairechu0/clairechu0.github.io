# Project Plan: Personal Website with Data Pipeline

## **Project Overview**
The goal is to create a "Personal Website" that includes a terminal-based copilot to orchestrate a data pipeline. The website will feature:
1. **Paper Listing**: Display the latest arXiv papers based on user-defined keywords.
2. **Paper Details**: Each paper entry will include the title, authors, abstract, and a direct link to the PDF.
3. **Auto-Update**: The paper list will refresh automatically every midnight using GitHub Actions.
4. **Homepage Link**: A link to this page will be added to the homepage.
5. **Page Design**: The page will be styled for readability and user engagement.

---

## **Plan Components**

### **1. Directory Structure**
- **Agents**: `.github/agents/`
  - Define agents responsible for orchestrating the data pipeline.
- **Skills**: `.github/skills/`
  - Define reusable skills for agents to perform specific tasks.
- **Prompts**: `.github/prompts/`
  - Define prompts to guide agents in executing their tasks.

---

### **2. Agent Design**
Agents will be defined in `.agent.md` files with YAML front matter specifying:
- **Agent Type**: Define the role of the agent (e.g., data fetcher, updater).
- **Model**: Specify the AI model used.
- **Tools**: List tools required for the agent's tasks.

**Agents to Create**:
1. **Data Fetcher Agent**:
   - Fetches the latest arXiv papers based on keywords.
   - Stores the data in a structured format (e.g., JSON).
2. **Data Updater Agent**:
   - Updates the paper list on the website.
   - Triggers the GitHub Actions workflow for auto-updates.
3. **Page Designer Agent**:
   - Generates HTML and CSS for the paper listing page.
   - Ensures the page is linked to the homepage.

---

### **3. Skills Design**
Skills will be modular and reusable, defined in `.skill.md` files. Examples:
1. **Fetch Papers Skill**:
   - Queries the arXiv API for papers matching keywords.
   - Parses and formats the response.
2. **Update Website Skill**:
   - Updates the HTML file with new paper data.
   - Ensures proper formatting and styling.
3. **Trigger Workflow Skill**:
   - Initiates the GitHub Actions workflow for auto-updates.
4. **HTML Styling Skill**:
   - Applies consistent styling to the webpage.

---

### **4. Prompt Design**
Prompts will guide agents in their tasks, defined in `.prompt.md` files. Examples:
1. **Fetch Papers Prompt**:
   - "Fetch the latest arXiv papers matching the following keywords: [keywords]. Format the response as JSON."
2. **Update Website Prompt**:
   - "Update the HTML file with the following paper data: [data]. Ensure the page is styled consistently."
3. **Trigger Workflow Prompt**:
   - "Trigger the GitHub Actions workflow to refresh the paper list."
4. **HTML Styling Prompt**:
   - "Apply the following CSS styles to the webpage: [styles]."

---

### **5. Coding Style Instructions**
- **General**:
  - Follow best practices for modular and reusable code.
  - Use clear and concise comments.
  - Ensure all files are well-documented.
- **HTML**:
  - Use semantic HTML5 elements.
  - Ensure accessibility (e.g., alt text for images, ARIA roles).
  - Optimize for responsive design.

---

### **6. GitHub Actions Workflow**
- Schedule the workflow to run every midnight.
- Steps:
  1. Fetch the latest arXiv papers.
  2. Update the HTML file with new data.
  3. Commit and push changes to the repository.

---

### **7. Deployment**
- Confirm the GitHub account and repository for deployment.
- Example: `clairechu0/clairechu0.github.io`.

---

### **8. Additional Requirements**
- Follow the format for Copilot CLI:
  - Agents must use `.agent.md` file extensions.
  - Include YAML front matter specifying agent type, model, and tools.
  - Refer to the official documentation: https://code.visualstudio.com/docs/copilot/customization/custom-agents.

---

### **9. Homepage Design**
- The homepage will serve as the central hub for the website.
- It will include:
  - A brief introduction about the website and its purpose.
  - A navigation menu linking to the paper listing page and the Pacman page.
  - A visually appealing layout with responsive design.

---

### **10. Pacman Page**
- The Pacman page will feature an interactive Pacman game.
- Key features:
  - A playable Pacman game embedded directly on the page.
  - Instructions for how to play the game.
  - A link back to the homepage for easy navigation.
- Design considerations:
  - Ensure the game is responsive and works on both desktop and mobile devices.
  - Style the page to match the overall theme of the website.
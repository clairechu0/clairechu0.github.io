# clairechu0.github.io

## Agentic Programming and Workflow: From Planning to Implementation

This project leveraged agentic programming and workflow automation to move from high-level planning to concrete implementation. The process was structured as follows:

### 1. Planning with plan_prompt
- The process began with a detailed `plan_prompt.md`, outlining the requirements for the personal website, Pac-Man game, and auto-updating arXiv paper feed.
- The prompt specified the need for modular agents, skills, and prompts, as well as coding and HTML style guidelines.
- The plan emphasized using Copilot CLI and agentic workflows for automation and reproducibility.

### 2. Agent and Skill Design
- Agents were defined in `.agent.md` files, each with a clear role (e.g., data fetcher, updater, page designer).
- Skills were modularized in `.skill.md` files, enabling agents to perform tasks like fetching arXiv data, updating HTML, and triggering workflows.
- Prompts in `.prompt.md` files guided agents in executing their tasks, ensuring consistency and clarity.

### 3. Workflow Automation
- GitHub Actions workflows were created to automate the nightly update of the papers page, using Python scripts to fetch and process data.
- The workflow was triggered on a schedule, running scripts to fetch new arXiv papers, update the JSON and HTML, and commit changes automatically.
- This ensured the site remained up-to-date with minimal manual intervention.

### 4. Scripted Implementation
- Python scripts (e.g., `update_papers.py`) were developed to transform raw arXiv data into a styled, interactive HTML page.
- JavaScript and HTML were generated and refined using Copilot CLI, guided by prompts and feedback from the agentic plan.
- The modular structure allowed for easy updates and debugging, as each component (prompt, skill, script) could be improved independently.

### 5. Iterative Refinement
- Throughout the process, prompts and skills were adjusted based on testing and user feedback.
- The agentic approach enabled rapid iteration, as changes to prompts or skills could be quickly propagated through the workflow.
- This resulted in a robust, maintainable, and extensible project architecture.

---

**Summary:**
Agentic programming and workflow automation, starting from a comprehensive plan prompt, enabled a seamless transition from requirements to implementation. By modularizing logic into agents, skills, and prompts, and automating updates with workflows and scripts, the project achieved both flexibility and reliability.


## Case Study: Using AI Copilot to Build a Personal Website

This report is a case-study tutorial on how to use AI Copilot and Copilot CLI to solve three core problems in building a modern personal website:

1. **Homepage Design and Navigation**
2. **Valentine's Pac-Man Game Implementation**
3. **Auto-Updating arXiv Paper Listing Page**

---

### 1. Homepage Design and Navigation

- **AI Tools Used:** GitHub Copilot, Copilot CLI
- **Prompt Design:**
	- Started with a high-level prompt: "Create a modern homepage with navigation links to Pac-Man and Papers pages."
	- Iteratively refined prompts to add hero sections, feature cards, and responsive design.
- **Copilot CLI Workflow:**
	- Used Copilot CLI to generate and edit `index.html` and CSS.
	- Adjusted HTML structure and styles based on Copilot suggestions and live preview.
- **Adjustments:**
	- Enhanced navigation, added visual polish, and ensured accessibility.

---

### 2. Valentine's Pac-Man Game Implementation

- **AI Tools Used:** GitHub Copilot, Copilot CLI
- **Prompt Design:**
	- Initial prompt: "Build a Pac-Man game with a Valentine's theme, including a maze, ghosts, power-up rose, and heart projectiles."
	- Refined prompts to specify maze logic, wall collision, ghost AI, and keyboard controls.
- **Copilot CLI Workflow:**
	- Used Copilot CLI to create and iteratively improve `pacman.html`.
	- Adjusted maze layout, wall logic, and ghost movement based on playtesting and Copilot feedback.
	- Ensured arrow keys do not scroll the page and ghosts cannot cross walls.
- **Adjustments:**
	- Redesigned maze to avoid closed boxes, improved gameplay, and added visual effects.

---

### 3. Auto-Updating arXiv Paper Listing Page

- **AI Tools Used:** GitHub Copilot, Copilot CLI, GitHub Actions
- **Prompt Design:**
	- Prompted Copilot to create a professional, card-based papers page with search/filter and all required metadata.
	- Designed prompts for Python scripts to fetch and update arXiv data (`update_papers.py`).
	- Specified requirements for a visible last-updated timestamp and auto-update workflow.
- **Copilot CLI Workflow:**
	- Used Copilot CLI to edit `papers.html`, add dynamic JS, and style the page.
	- Created and refined GitHub Actions workflow for nightly updates.
	- Used Copilot to generate and update Python scripts for HTML generation.
- **Adjustments:**
	- Improved card layout, search UX, and timestamp visibility based on feedback.

---

### Summary of Copilot CLI Usage

- **File Creation & Editing:** Used Copilot CLI to create and iteratively edit HTML, CSS, JS, and Python files.
- **Prompt Engineering:** Designed and refined prompts to guide Copilot in generating code, fixing bugs, and improving UX.
- **Automation:** Leveraged Copilot to scaffold and debug GitHub Actions workflows for automated updates.
- **Debugging:** Used Copilot CLI to quickly identify and resolve issues in logic, layout, and interactivity.

This project demonstrates how AI Copilot and Copilot CLI can accelerate web development, automate repetitive tasks, and enable rapid prototyping and iteration for complex, multi-component sites.
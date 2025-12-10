# 📄 Tailored Resume Generator

The Tailored Resume Generator is a command-line interface (CLI) application that uses the Google Gemini API to produce **seven distinct, tailored resume versions** from a single source document and a set of strategic user answers.

This tool is designed for senior professionals (Manager/Architect/Principal tracks) in the Semiconductor, Embedded Systems, and High-Performance Infrastructure domains who need multiple, context-specific resumes quickly.

---

## ✨ Features

* **API Key Management:** Securely manages the `GEMINI_API_KEY` using a local `.env` file and includes validation checks.
* **Targeted Output:** Generates a single, organized HTML document containing seven specific resumes (Startup-focus, Established-focus, Managerial, Architect, and Distinguished blends).
* **Modular Versioning:** Implements a dynamic versioning system (`MAJOR.MINOR.PATCH`) by aggregating version data and changelog history from all core Python modules.
* **Low-Cost Generation:** Uses the efficient `gemini-2.5-flash` model for high-volume, structured generation to stay within free-tier limits.

## 🚀 Getting Started

Follow these steps to clone the repository, install dependencies, and run the application.

### 1. Prerequisites

You must have the following installed on your system:

* **Python 3.8+**
* **A Google Gemini API Key** (Obtain one from [Google AI Studio](https://aistudio.google.com/app/apikey))

### 2. Installation

1.  **Clone the Repository (or download the source files):**
    ```bash
    git clone [https://github.com/sgscaffidi3/resume_generator.git](https://github.com/sgscaffidi3/resume_generator.git)
    cd resume_generator
    ```

2.  **Create a Python Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You will need to create a `requirements.txt` file containing the packages below if you don't have one.)*
    
    > **`requirements.txt` content:**
    > ```
    > google-genai
    > python-dotenv
    > ```

---

## 💻 Usage

The application is run via the main entry script, `cli.py`.

### A. Run the Resume Generation Flow

The first time you run the script, it will automatically launch the **Setup Flow** to prompt you for and validate your `GEMINI_API_KEY`.

1.  **Execute the main application:**
    ```bash
    python cli.py
    ```
2.  **Input Key:** If prompted, enter your Gemini API Key. The script will save it to the local `.env` file and test its validity.
3.  **Generation:** Once the key is validated, the script connects to the API and generates the content.
4.  **Output:** The final, structured HTML output is saved to:
    `tailored_resumes_output.html`

### B. Checking the Application Version

Use the `--version` flag to display the comprehensive version details, including the application version (calculated from all modules) and the specific version and changelog of each component.

```bash
python cli.py --version
```

### C. Gemini Instance
https://gemini.google.com/app/23d1c8c1e9eadd59

### D. Conversation
https://gemini.google.com/share/b91b4b91f3d6


# Solar Data Discovery — Week 0

## Project Overview

This project is part of the **Solar Data Discovery Challenge**, focusing on analyzing solar farm datasets from **Benin, Sierra Leone, and Togo**.  
The purpose of **Week 0** is to set up the project environment, version control, automation workflow, and prepare datasets for upcoming exploratory data analysis (EDA) and dashboard development.

### Key Objectives

- Set up Python environment and required dependencies  
- Implement **GitHub version control** (branching strategy, commits, repo organization)  
- Create **CI/CD pipeline** using GitHub Actions  
- Document setup instructions and structure  
- Prepare datasets for incoming analysis

---

## Environment Setup

Follow these steps to set up the project on your local machine.

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/MekdelawitGebre/solar-challenge-week0.git

cd solar-challenge-week0
```

### 2️⃣ Create a Python Virtual Environment

```sh
python -m venv .venv
```

### 3️⃣ Activate the Environment

**Windows (PowerShell):**
```sh
.\.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```sh
.\.venv\Scriptsctivate.bat
```

**macOS / Linux:**
```sh
source .venv/bin/activate
```

### 4️⃣ Upgrade pip (optional but recommended)

```sh
python -m pip install --upgrade pip
```

### 5️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

### 6️⃣ Verify Installation

```sh
python --version
pip list
```

✅ Your environment is now ready for notebooks, Python scripts, and dashboard development.

---

## CI/CD Setup (GitHub Actions)

This project uses **GitHub Actions** for continuous integration.

- Workflow file: `.github/workflows/ci.yml`
- Triggered on: `push` and `pull_request`
- Steps performed:
  - Check out repository
  - Set up Python **3.11**
  - Install dependencies
  - Run basic validation (e.g., Python version test)

### Example: Run CI steps locally 

```sh
# Activate venv
.\.venv\Scripts\Activate.ps1

# Run simple test (temporary for Week 0)
python --version
```

The CI ensures every contributor runs the project in a consistent and reproducible environment.

---


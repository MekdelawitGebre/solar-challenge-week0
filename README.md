# Solar Data Discovery — Week 0

## Project Overview

This project is part of the **Solar Data Discovery Challenge**, focusing on analyzing solar farm datasets from **Benin, Sierra Leone, and Togo**.
The purpose of **Week 0** is to set up the project environment, version control, automation workflow, perform initial data exploration, and develop an interactive dashboard.

**Deployed Dashboard:** [Solar Dashboard Insights](https://solar-dashboard-insight.streamlit.app/)

---

## Key Objectives

* Set up Python environment and required dependencies
* Implement **GitHub version control** (branching strategy, commits, repo organization)
* Create **CI/CD pipeline** using GitHub Actions
* Document setup instructions and project structure
* Prepare datasets for exploratory data analysis (EDA) and dashboard development
* Design and deploy a **Streamlit interactive dashboard**

---

## Environment Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/MekdelawitGebre/solar-challenge-week0.git
cd solar-challenge-week0
```

### 2️⃣ Create a Python Virtual Environment

```bash
python -m venv .venv
```

### 3️⃣ Activate the Environment

**Windows (PowerShell):**

```bash
.\.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**

```bash
.\.venv\Scripts\activate.bat
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### 4️⃣ Upgrade pip (optional but recommended)

```bash
python -m pip install --upgrade pip
```

### 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 6️⃣ Verify Installation

```bash
python --version
pip list
```

Your environment is now ready for notebooks, Python scripts, and dashboard development.

---

## Tasks Completed

### Task 1 — Git & Environment Setup 

* Initialized GitHub repo and created `setup-task` branch
* Added `.gitignore` (including `data/`), `requirements.txt`, and GitHub Actions workflow
* Merged setup-task into `main`

### Task 2 — Data Profiling, Cleaning & EDA 

* Created EDA notebooks for each country (`benin_eda.ipynb`, etc.)
* Performed:

  * Summary statistics, missing-value report, outlier detection
  * Cleaning: drop or impute missing/incorrect values
  * Time-series analysis and visualizations (GHI, DNI, DHI, Tamb)
  * Correlation heatmaps, scatter plots, histograms, bubble charts
* Exported cleaned datasets locally (ignored in Git)

### Task 3 — Cross-Country Comparison 

* Created `compare-countries` branch
* Loaded all three cleaned datasets
* Compared metrics (GHI, DNI, DHI) with:

  * Side-by-side boxplots
  * Summary table (mean, median, standard deviation)
  * ANOVA/Kruskal–Wallis tests
* Added key observations and optional bar chart ranking countries by GHI

### Bonus — Interactive Dashboard (Streamlit) 

* Created `dashboard-dev` branch
* Developed `app/main.py` with:

  * Country selection widget
  * Upload CSV feature
  * GHI boxplots
  * Top regions table
* Developed `app/utils.py` with reusable functions:

  * `load_uploaded_data()`
  * `plot_ghi_boxplot()`
  * `compare_countries_barplot()`
* Deployed on Streamlit Community Cloud: [https://solar-dashboard-insight.streamlit.app/](https://solar-dashboard-insight.streamlit.app/)
* Ensured `data/` folder is ignored in Git

---

## How to Run the Dashboard Locally

1. Activate virtual environment:

```bash
.\.venv\Scripts\Activate.ps1
```

2. Run Streamlit app:

```bash
streamlit run app/main.py
```

3. Upload your country CSVs through the dashboard interface and explore insights interactively.



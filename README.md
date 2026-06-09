# 📊 Applied Plotting, Charting & Data Representation in Python

**Completed by Kankon Mondal**  
*University of Michigan (Coursera)*

<div align="center">
  <img src="https://img.shields.io/badge/Specialization-Applied%20Data%20Science%20with%20Python-blue?style=for-the-badge&logo=python&logoColor=white" alt="Specialization">
  <img src="https://img.shields.io/badge/Verified%20Certificate-3RBFUF5AD9NI-success?style=for-the-badge&logo=coursera" alt="Certificate Badge">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" alt="Status">
</div>

---

## 🌟 Overview & Philosophy

This repository contains my comprehensive coursework, lectures, coding notebooks, and visual projects for the **Applied Plotting, Charting & Data Representation in Python** course by the University of Michigan on Coursera.

The core philosophy of this work revolves around:
1. **Visual Integrity (Alberto Cairo)**: Ensuring representations are truthful, functional, beautiful, and insightful. Avoiding "graphics lies" such as truncated axes, deceptive dimensions, and hidden context.
2. **Dejunking Charts (Edward Tufte)**: Maximizing the **data-ink ratio** by systematically stripping away non-data ink (heavy gridlines, unnecessary spines, decorative borders, redundant labels) to let the data speak clearly.

---

## 🏆 Verified Completion Certificate

Below is my verified completion certificate from the University of Michigan & Coursera.

<div align="center">
  <a href="https://coursera.org/verify/3RBFUF5AD9NI" target="_blank" rel="noopener noreferrer">
    <img src="https://s3.amazonaws.com/coursera_assets/meta_images/generated/CERTIFICATE_LANDING_PAGE/CERTIFICATE_LANDING_PAGE~3RBFUF5AD9NI/CERTIFICATE_LANDING_PAGE~3RBFUF5AD9NI.jpeg" alt="Applied Plotting, Charting & Data Representation Certificate" width="650" style="border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.15);">
    <br>
    <sub><em>Click the image to view the verified certificate page on Coursera.</em></sub>
  </a>
</div>

---

## 🗺️ Curriculum Progress

| Module | Core Focus | Key Assignment / Project |
| :--- | :--- | :--- |
| **[Module 01: Principles of Info Visualization](./Module-01/README.md)** | Theoretical foundations, graphical integrity & Cairo's framework | [Assignment.ipynb](./Module-01/02-Assignments/Assignment.ipynb) (Misleading Visual Critique) |
| **[Module 02: Basic Charting & Dejunking](./Module-02/README.md)** | Matplotlib architecture layers & Edward Tufte's data-ink ratio | [assignment2.ipynb](./Module-02/02-Assignments/assignment2.ipynb) (Ann Arbor Temperature Records) |
| **[Module 03: Charting Fundamentals & Interactivity](./Module-03/README.md)** | Subplots layout, statistical plots & dynamic mouse event handlers | [assignment3.ipynb](./Module-03/02-Assignments/assignment3.ipynb) (Ferreira Interactive Confidence Intervals) |
| **[Module 04: Applied Visualizations & Project](./Module-04/README.md)** | Pandas/Seaborn statistical APIs, Folium geographical mapping | [assignment4.ipynb](./Module-04/02-Project/assignment4.ipynb) (Atmospheric CO2 & Temperature Correlation) |

---

## 🛠️ Technology Stack & Libraries

<div align="left">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/Matplotlib-Plotting%20Engine-F5793A?style=for-the-badge&logo=python&logoColor=white" alt="Matplotlib">
  <img src="https://img.shields.io/badge/Seaborn-Statistical%20Plots-4D72B0?style=for-the-badge&logo=python&logoColor=white" alt="Seaborn">
  <img src="https://img.shields.io/badge/Folium-Geographical%20Maps-77AA33?style=for-the-badge&logo=leaflet&logoColor=white" alt="Folium">
</div>

---

## 🚀 Setup & Execution Guide

To set up the workspace, install all course dependencies, and execute the visualization notebooks or scripts locally:

### 1. Clone the Repository
```bash
git clone https://github.com/KankonNil007/Applied-Python-Data-Visualization.git
cd Applied-Python-Data-Visualization
```

### 2. Create and Activate a Virtual Environment (Recommended)
* **Windows (PowerShell)**:
  ```powershell
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  ```
* **macOS / Linux**:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 3. Install Requirements
Install all core libraries (Matplotlib, Seaborn, Pandas, Folium, Jupyter, etc.) using [requirements.txt](./requirements.txt):
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Running the Notebooks & Scripts
* **Jupyter Notebooks**: Open the Jupyter environment to run any `.ipynb` file:
  ```bash
  jupyter notebook
  ```
* **Python Scripts**: Run standalone scripts directly in your terminal:
  * **Module 02**: `python Module-02/02-Assignments/assignment2.py`
  * **Module 03**: `python Module-03/02-Assignments/assignment3.py`

---

## 📁 Repository Structure

```text
Applied-Python-Data-Visualization/
├── Module-01/
│   ├── 01-Principles-of-Information-Visualization/
│   │   └── README.md
│   └── 02-Assignments/
│       └── Assignment.ipynb
│
├── Module-02/
│   ├── 01-Basic-Charting/
│   │   ├── 01-Basic-Matplotlib.ipynb
│   │   ├── 02-Scatter-Plots.ipynb
│   │   ├── 03-Line-Plots.ipynb
│   │   ├── 04-Bar-Charts.ipynb
│   │   ├── 05-Dejunkfying-a-Plot.ipynb
│   │   └── test.png
│   └── 02-Assignments/
│       ├── assets/
│       │   ├── BinSize_d400.csv
│       │   ├── chris_sketch.png
│       │   └── fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv
│       ├── assignment2.ipynb
│       ├── assignment2.py
│       ├── assignment2_plot.png
│       └── map.html
│
├── Module-03/
│   ├── 01-Charting-Fundamentals/
│   │   ├── assets/
│   │   │   ├── iris.csv
│   │   │   ├── nyc-hourly-traffic.csv
│   │   │   └── wipeout.csv
│   │   ├── 01-Subplots.ipynb
│   │   ├── 02-Histograms.ipynb
│   │   ├── 03-Boxplots.ipynb
│   │   ├── 04-Heatmaps.ipynb
│   │   ├── 05-Animations.ipynb
│   │   └── 06-Widget-Demonstration.ipynb
│   └── 02-Assignments/
│       ├── assets/
│       │   ├── Assignment3Fig1.png
│       │   └── Assignment3Fig2c.png
│       ├── 01-Practice_Assignment.ipynb
│       ├── 01-Practice_Assignment.py
│       ├── assignment3.ipynb
│       └── assignment3.py
│
└── Module-04/
    ├── 01-Applied-Visualizations/
    │   ├── assets/
    │   │   ├── iris.csv
    │   │   ├── map.png
    │   │   └── wipeout.csv
    │   ├── 01-Plotting-with-Pandas.ipynb
    │   ├── 02-Seaborn.ipynb
    │   ├── 03-Mapping-and-Geographical-Investigations.ipynb
    │   ├── map.html
    │   └── map2.html
    └── 02-Project/
        ├── Example/
        │   └── Assignment4_example.pdf
        ├── assignment4.ipynb
        └── climate_change_correlation.png
```

---

## 📜 Ethical Note & License

This repository is shared for educational and reference purposes to showcase the application of data representation principles in Python. If you are currently taking the University of Michigan's Applied Plotting course, please respect the Coursera Honor Code and do not copy these solutions directly. 

This project is licensed under the [MIT License](LICENSE).

---
**Created with care by [Kankon Mondal](https://github.com/KankonNil007)**

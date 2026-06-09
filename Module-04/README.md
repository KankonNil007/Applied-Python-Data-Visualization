# 🗺️ Module 04: Applied Visualizations & Custom Climatology Project

This module explores advanced statistical plotting ecosystems (Pandas built-in APIs, Seaborn) and Leaflet-based geographical mapping libraries (Folium). It culminates in a self-driven, peer-reviewed final data science project investigating climatological correlations.

<div align="center">
  <img src="https://img.shields.io/badge/Data%20Analysis-Seaborn-4D72B0?style=for-the-badge&logo=python" alt="Seaborn">
  <img src="https://img.shields.io/badge/Geographical-Folium-77AA33?style=for-the-badge&logo=leaflet" alt="Folium">
  <img src="https://img.shields.io/badge/Project-Climatology-blue?style=for-the-badge" alt="Project">
</div>

---

## 🎯 Learning Objectives & Key Concepts

* **Pandas Plotting API**: Accessing standard visualization methods directly from pandas DataFrames (`df.plot()`) and utilizing built-in style sheets (`plt.style.use()`).
* **Seaborn Statistical Plots**:
  * Visualizing probability densities using Kernel Density Estimation (KDE) and violin plots.
  * Performing multi-variable analysis using pairwise correlation grids (`sns.pairplot()`) and joint marginal distribution views.
  * Fitting linear relationships visually using regression charts (`sns.regplot()`).
* **Folium Mapping Engine**:
  * Initializing interactive Leaflet tiles, setting zoom configurations, and dropping map pins.
  * Importing GPS/fit files ([wipeout.csv](./01-Applied-Visualizations/assets/wipeout.csv)), computing coordinate angles, and drawing line pathways to map bike trails.
  * Exporting dynamic visualizations to standalone HTML components.

---

## 📂 Directory Layout

```text
Module-04/
├── 01-Applied-Visualizations/               # Lecture Notebooks on Pandas, Seaborn, & Maps
│   ├── assets/                              # Data and reference image assets
│   │   ├── iris.csv                         # Iris flower dataset
│   │   ├── map.png                          # Map layout snapshot
│   │   └── wipeout.csv                      # Cyclist workout track coordinate file
│   ├── 01-Plotting-with-Pandas.ipynb
│   ├── 02-Seaborn.ipynb
│   ├── 03-Mapping-and-Geographical-Investigations.ipynb
│   ├── map.html                             # Output simple map HTML
│   └── map2.html                            # Output advanced trajectory map HTML
└── 02-Project/                              # Self-driven climatology research project
    ├── Example/
    │   └── Assignment4_example.pdf         # Project instructions and rules
    ├── assignment4.ipynb                    # Project data cleaning and analysis notebook
    └── climate_change_correlation.png       # Final publication-grade dual-axis plot
```

---

## 📓 Lecture Notebooks Breakdown

### 📁 01-Applied-Visualizations/

#### 1. [01-Plotting-with-Pandas.ipynb](./01-Applied-Visualizations/01-Plotting-with-Pandas.ipynb)
* **Goal**: Build visualizations directly from Pandas DataFrames.
* **Concepts**:
  * Exploring Matplotlib style configurations (`plt.style.available`) and loading specific templates (e.g. `plt.style.use("seaborn-v0_8-colorblind")`).
  * Creating basic plots directly from data data structures: line charts, scatter plots (`df.plot.scatter()`), and bar charts (`df.plot.bar()`).
  * Visualizing statistical data using kernel density estimations, box plots, and hexagonal binning overlays.

#### 2. [02-Seaborn.ipynb](./01-Applied-Visualizations/02-Seaborn.ipynb)
* **Goal**: Create advanced statistical graphics using Seaborn.
* **Concepts**:
  * Designing histograms, stacked bar layouts, and smooth density charts.
  * Generating scatter matrices (`sns.pairplot()`) to instantly analyze correlations between columns.
  * Visualizing categorical splits using boxplots, swarm plots, and violin charts.
  * Charting trendlines and regression confidence bounds using `sns.regplot()`.

#### 3. [03-Mapping-and-Geographical-Investigations.ipynb](./01-Applied-Visualizations/03-Mapping-and-Geographical-Investigations.ipynb)
* **Goal**: Build Leaflet-based interactive maps in Python.
* **Concepts**:
  * Loading athlete workout files ([wipeout.csv](./01-Applied-Visualizations/assets/wipeout.csv)) containing latitude, longitude, and speed.
  * Converting raw measurements (GPS coordinates stored as integers) into degrees.
  * Initializing maps (`folium.Map`), overlaying paths (`folium.PolyLine`), and setting custom markers with popups to display athlete speed at specific markers.
  * Exporting projects to interactive HTML maps: [map.html](./01-Applied-Visualizations/map.html) and [map2.html](./01-Applied-Visualizations/map2.html).

---

## 📝 Final Project Details

### 📁 02-Project/

#### 📓 [assignment4.ipynb](./02-Project/assignment4.ipynb)
* **Research Question**: *Is there a visual correlation between global atmospheric carbon dioxide levels and global land-ocean temperature anomalies from 1959 to the present?*
* **Datasets Cleaned**:
  1. **Atmospheric Carbon Dioxide**: NOAA Mauna Loa dataset (monthly average parts-per-million).
  2. **Land-Ocean Temperature Anomalies**: NASA GISTEMP dataset (deviations from 1951-1980 base period).
* **Data Processing Pipeline**:
  * Load NOAA dataset, clean missing values (encoded as -99.99), and calculate annual CO2 averages.
  * Clean NASA GISTEMP dataframe, unpack monthly anomaly values, and compute annual average anomalies.
  * Merge datasets on year coordinates, covering 1959 to 2025.
* **Visualization Features**:
  * **Dual Y-Axis Sync**: Plot CO2 levels (left axis, ppm) as a clean line plot, and Temperature anomalies (right axis, °C) as a vertical bar chart.
  * **High-Fidelity Styling**: Select a soft color palette (blue bars for anomalies, dark grey line for CO2), remove heavy borders, and add gridlines to ensure readability.
  * **Annotation**: Label key milestones (e.g. crossing 400 ppm CO2) directly on the chart.
* **Output Image**: [climate_change_correlation.png](./02-Project/climate_change_correlation.png)

#### 🎨 [Example/Assignment4_example.pdf](./02-Project/Example/Assignment4_example.pdf)
* The official coursework project rubric, outlining criteria for exploratory question formulation, clean data fetching, and visual presentation.

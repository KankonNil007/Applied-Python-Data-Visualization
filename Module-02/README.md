# 📊 Module 02: Basic Charting & Edward Tufte's Dejunking Principles

This module covers the practical implementation of core chart types using Python's Matplotlib library and introduces the concept of maximizing the data-ink ratio as advocated by Edward Tufte.

<div align="center">
  <img src="https://img.shields.io/badge/Matplotlib-OO%20API-orange?style=for-the-badge&logo=python" alt="Matplotlib">
  <img src="https://img.shields.io/badge/Aesthetic-Edward%20Tufte-blue?style=for-the-badge" alt="Tufte">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" alt="Status">
</div>

---

## 🎯 Learning Objectives & Key Concepts

* **Matplotlib Architecture**:
  * **Backend Layer**: Coordinates the rendering to output devices/formats (e.g. `FigureCanvasAgg` for raster PNG output).
  * **Artist Layer**: Handles the figure layout elements (Figures, Axes, Spines, Ticks, Labels).
  * **Scripting Layer (`pyplot`)**: Simplifies interaction by maintaining states, retrieving current axes (`plt.gca()`), and figures (`plt.gcf()`).
* **Core Plots**: Line plots, scatter plots, horizontal and vertical bar charts.
* **Edward Tufte's Data-Ink Ratio**: Minimizing visual clutter ("chartjunk") by removing borders, ticks, unnecessary legends, and gridlines to focus solely on high-value data ink.

---

## 📂 Directory Layout

```text
Module-02/
├── 01-Basic-Charting/       # Lecture Notebooks on Matplotlib scripting & layouts
│   ├── 01-Basic-Matplotlib.ipynb
│   ├── 02-Scatter-Plots.ipynb
│   ├── 03-Line-Plots.ipynb
│   ├── 04-Bar-Charts.ipynb
│   ├── 05-Dejunkfying-a-Plot.ipynb
│   └── test.png
└── 02-Assignments/          # Ann Arbor daily climate records assignment
    ├── assets/
    │   ├── BinSize_d400.csv
    │   ├── chris_sketch.png
    │   └── fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv
    ├── assignment2.ipynb
    ├── assignment2.py
    ├── assignment2_plot.png
    └── map.html
```

---

## 📓 Lecture Notebooks Breakdown

### 📁 01-Basic-Charting/

#### 1. [01-Basic-Matplotlib.ipynb](./01-Basic-Charting/01-Basic-Matplotlib.ipynb)
* **Goal**: Understand the design architecture of Matplotlib.
* **Concepts**:
  * Switching backends (`mpl.get_backend()`).
  * Creating a figure canvas programmatically using the Artist layer: importing `FigureCanvasAgg` and `Figure`, drawing elements, and saving to [test.png](./01-Basic-Charting/test.png).
  * Finding current figures and axes using `plt.gcf()` and `plt.gca()`.
  * Basic point plotting (`plt.plot(3, 2, '.')`).

#### 2. [02-Scatter-Plots.ipynb](./01-Basic-Charting/02-Scatter-Plots.ipynb)
* **Goal**: Implement scatter plots and coordinate manipulations.
* **Concepts**:
  * Drawing scatter plots using `plt.scatter(x, y)`.
  * Passing color vectors to highlight specific data points (e.g. coloring the last point red).
  * Using Python's `zip` generator to bundle coordinate sequences and unpacking them using `*zip`.
  * Customizing markers, labels, legends, and axis boundaries.

#### 3. [03-Line-Plots.ipynb](./01-Basic-Charting/03-Line-Plots.ipynb)
* **Goal**: Construct line charts and fill between boundaries.
* **Concepts**:
  * Charting continuous variables and mathematical functions (e.g., quadratic curves $y = x^2$).
  * Specifying formatting shortcuts (e.g., `'-o'` for lines with circular markers, `'--r'` for dashed red lines).
  * Shading areas between coordinates using `plt.gca().fill_between(x, y1, y2, facecolor='grey', alpha=0.25)` to represent data ranges.

#### 4. [04-Bar-Charts.ipynb](./01-Basic-Charting/04-Bar-Charts.ipynb)
* **Goal**: Model categorical counts using vertical and horizontal bars.
* **Concepts**:
  * Designing standard bar charts (`plt.bar`) and horizontal bar charts (`plt.barh`).
  * Specifying variable widths, adjusting bar positioning, and adding standard error bars (`yerr`).
  * Stacking multiple categories and rendering stacked charts.

#### 5. [05-Dejunkfying-a-Plot.ipynb](./01-Basic-Charting/05-Dejunkfying-a-Plot.ipynb)
* **Goal**: Apply Edward Tufte's core design rules to a standard visual.
* **Concepts**:
  * Starting with a default heavy-border popularity bar chart of programming languages.
  * **Step-by-Step Dejunking Process**:
    1. Remove all figure borders (spines) by setting `spine.set_visible(False)`.
    2. Eliminate y-axis ticks and labels to remove visual weight.
    3. Calculate text positions and overlay popularity percentages directly inside/above the bars.
    4. Transition from high-contrast primary colors to soft, cohesive tones (e.g., slate grey with a highlighted blue bar for Python).

---

## 📝 Assignment Details

### 📁 02-Assignments/

#### 📓 [assignment2.ipynb](./02-Assignments/assignment2.ipynb) / [assignment2.py](./02-Assignments/assignment2.py)
* **Goal**: Build a publication-quality daily temperature record chart for stations near Ann Arbor, Michigan (2005-2015).
* **Data Pipeline**:
  1. Load station data from CSV containing maximum/minimum temperatures.
  2. Filter out leap-year days (February 29) to keep standard 365-day tracking.
  3. Group daily data from 2005 to 2014 by day-of-year to extract the record max and record min bounds.
  4. Identify days in 2015 where the temperature exceeded the historical 10-year record high or fell below the 10-year record low.
* **Visualization Styling**:
  * Plot the 2005-2014 minimum and maximum records as boundary lines, shading the envelope in between with a light grey color.
  * Scatter plot the 2015 breaking highs as vivid red dots, and breaking lows as blue dots.
  * Apply Tufte's dejunking: remove the top and right spines, simplify tick labels, and add a descriptive title.
* **Output Image**: [assignment2_plot.png](./02-Assignments/assignment2_plot.png)

#### 🌐 [map.html](./02-Assignments/map.html)
* An interactive geographical mapping component built using Folium, visualizing the locations of the weather stations near Ann Arbor that provided the temperature dataset.

#### 🎨 [chris_sketch.png](./02-Assignments/assets/chris_sketch.png)
* The reference wireframe designed by course instructor Christopher Brooks outlining the structural requirements of the temperature anomaly plot.

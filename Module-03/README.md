# 📈 Module 03: Charting Fundamentals & Interactivity

This module dives into advanced layout structuring, statistical distribution charting, real-time animation engines, and custom interactive event-driven interfaces in Matplotlib.

<div align="center">
  <img src="https://img.shields.io/badge/Layout-GridSpec-blue?style=for-the-badge" alt="GridSpec">
  <img src="https://img.shields.io/badge/Interactive-Event%20Handlers-orange?style=for-the-badge" alt="Interactivity">
  <img src="https://img.shields.io/badge/Statistics-Confidence%20Intervals-green?style=for-the-badge" alt="Statistics">
</div>

---

## 🎯 Learning Objectives & Key Concepts

* **Subplots & Layouts**: Managing multi-axis figure grids, sharing coordinate axes to sync scaling, and defining custom grids using Matplotlib's `GridSpec` engine.
* **Statistical Representations**:
  * **Histograms**: Analyzing sample distributions, frequency densities, and mapping marginal distributions on scatter plots.
  * **Boxplots**: Visualizing distributions through medians, quartiles (IQR), whiskers, and outliers.
  * **Heatmaps**: Plotting 2D density matrices to map frequency across two independent variables.
* **Interactivity & Widgets**:
  * Capturing mouse events (`button_press_event`) to trigger user-driven recalculations.
  * Creating real-time animations with `FuncAnimation`.
  * Using IPython widgets (`ipywidgets`) for sliders, selectors, and dropdown controls.

---

## 📂 Directory Layout

```text
Module-03/
├── 01-Charting-Fundamentals/        # Lecture Notebooks on stats plots & interaction
│   ├── assets/                      # CSV datasets
│   │   ├── iris.csv                 # Iris flower dimensions
│   │   ├── nyc-hourly-traffic.csv   # Hourly traffic volume data
│   │   └── wipeout.csv              # Workout geographical GPS coordinates
│   ├── 01-Subplots.ipynb
│   ├── 02-Histograms.ipynb
│   ├── 03-Boxplots.ipynb
│   ├── 04-Heatmaps.ipynb
│   ├── 05-Animations.ipynb
│   └── 06-Widget-Demonstration.ipynb
└── 02-Assignments/                  # Assignments and practice exercises
    ├── assets/                      # Reference visual layouts
    │   ├── Assignment3Fig1.png
    │   └── Assignment3Fig2c.png
    ├── 01-Practice_Assignment.ipynb # Statistics practice notebook
    ├── 01-Practice_Assignment.py    # Statistics practice script
    ├── assignment3.ipynb            # Interactive confidence interval notebook
    └── assignment3.py               # Interactive confidence interval script
```

---

## 📓 Lecture Notebooks Breakdown

### 📁 01-Charting-Fundamentals/

#### 1. [01-Subplots.ipynb](./01-Charting-Fundamentals/01-Subplots.ipynb)
* **Goal**: Build custom multi-pane visual layouts.
* **Concepts**:
  * Creating grid-based layouts using `plt.subplot(rows, cols, index)`.
  * Sharing x-axes and y-axes to keep scaling consistent across plots.
  * Using `GridSpec` to span plots across multiple rows/columns (e.g. side-by-side marginal plots).

#### 2. [02-Histograms.ipynb](./01-Charting-Fundamentals/02-Histograms.ipynb)
* **Goal**: Chart frequency distributions.
* **Concepts**:
  * Generating 1D histograms using `plt.hist()` and custom bin frequencies.
  * Visualizing random normal, random, and gamma distributions.
  * Mapping a scatter plot of coordinates alongside its marginal histograms using `GridSpec`.

#### 3. [03-Boxplots.ipynb](./01-Charting-Fundamentals/03-Boxplots.ipynb)
* **Goal**: Render box-and-whisker plots for comparative analysis.
* **Concepts**:
  * Plotting distributions using `plt.boxplot()`.
  * Explaining components: the median line, the Interquartile Range box ($IQR = Q_3 - Q_1$), whiskers ($1.5 \times IQR$), and individual outlier points.
  * Comparing normal, random, and skewed gamma samples side-by-side.

#### 4. [04-Heatmaps.ipynb](./01-Charting-Fundamentals/04-Heatmaps.ipynb)
* **Goal**: Construct 2D density maps.
* **Concepts**:
  * Loading NYC hourly traffic data ([nyc-hourly-traffic.csv](./01-Charting-Fundamentals/assets/nyc-hourly-traffic.csv)).
  * Aggregating traffic volume by day-of-week and hour-of-day.
  * Rendering heatmaps using 2D histograms (`plt.hist2d()`) and matrix visualizers (`plt.imshow()`) to find peak commuting windows.

#### 5. [05-Animations.ipynb](./01-Charting-Fundamentals/05-Animations.ipynb)
* **Goal**: Design dynamic simulations.
* **Concepts**:
  * Using `matplotlib.animation.FuncAnimation` to run frame-based update loops.
  * Developing an update function that appends new random samples to a growing dataset and updates the plot canvas dynamically.

#### 6. [06-Widget-Demonstration.ipynb](./01-Charting-Fundamentals/06-Widget-Demonstration.ipynb)
* **Goal**: Integrate interactive dashboard controls.
* **Concepts**:
  * Utilizing `ipywidgets.interact` to build UI overlays.
  * Binding widgets (sliders, dropdowns) to python visualization functions to dynamically filter datasets and refresh charts.

---

## 📝 Assignment Details

### 📁 02-Assignments/

#### 📓 [assignment3.ipynb](./02-Assignments/assignment3.ipynb) / [assignment3.py](./02-Assignments/assignment3.py)
* **Goal**: Build an interactive data visualization dashboard displaying sample means and standard error confidence intervals (Ferreira framework).
* **Statistical Logic**:
  * Compute the mean ($\bar{x}$) and standard error ($yerr$) for four distinct years (1992-1995) from a sample dataset.
  * Construct a bar chart showing the mean values with 95% confidence intervals ($1.96 \times yerr$) rendered as error whiskers.
* **Interactive Design**:
  * Capture user mouse clicks on the y-axis coordinate of the chart using `fig.canvas.mpl_connect('button_press_event', onclick)`.
  * Draw a horizontal reference line at the clicked y-coordinate ($Y$).
  * Dynamically evaluate each year's sample mean and margin of error against the threshold. Recalculate the probability $P(\mu > Y)$ that the true population mean lies above the selected line.
  * Automatically color-code each year's bar using a divergent colormap (`RdBu_r`), mapping full blue to values safely above the line, full red to values safely below, and neutral white to values that overlap.

#### 📓 [01-Practice_Assignment.ipynb](./02-Assignments/01-Practice_Assignment.ipynb) / [01-Practice_Assignment.py](./02-Assignments/01-Practice_Assignment.py)
* Practical scripting exercise focused on basic sampling procedures, density rendering, and histogram alignments.

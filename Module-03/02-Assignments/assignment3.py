import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize

# 1. Setup the data exactly as defined in the assignment instructions
np.random.seed(12345)
df = pd.DataFrame([np.random.normal(32000, 200000, 3650), 
                   np.random.normal(43000, 100000, 3650), 
                   np.random.normal(43500, 140000, 3650), 
                   np.random.normal(48000, 70000, 3650)], 
                  index=[1992, 1993, 1994, 1995])

# Calculate statistics for each year
# Calculate the sample mean (center points of our bars)
means = df.mean(axis=1)
stds = df.std(axis=1)
n = df.shape[1]
# Calculate the Standard Error (SE) of the sample mean: SE = std_dev / sqrt(sample_size)
se = stds / np.sqrt(n)

# 95% confidence interval half-width: z = 1.96 (for sample size 3650)
# Calculate the 95% Confidence Interval half-width using z = 1.96
yerr = 1.96 * se
years = df.index.astype(str)

# 2. Probability mapping calculation
# P(Mean > Y) = standard normal CDF((Mean - Y) / SE)
# Compute statistical probabilities: P(true mean > Y-threshold)
# Uses normal cumulative density function (CDF) to find probability ranges
def get_probabilities(y_val):
    try:
        from scipy.stats import norm
        return norm.cdf((means - y_val) / se)
    except ImportError:
        # Fallback using standard library math.erf if scipy is not installed
        z = (means - y_val) / se
        # CDF of standard normal is 0.5 * (1 + erf(z / sqrt(2)))
        return 0.5 * (1 + np.vectorize(math.erf)(z / np.sqrt(2)))

# Initial reference value
y_interest = 40000.0
probs = get_probabilities(y_interest)

# 3. Setup the visualization
fig, ax = plt.subplots(figsize=(10, 6.5))
fig.canvas.manager.set_window_title('Assignment 3: Custom Visualization')

# Select divergent colormap (Blue -> White -> Red reversed, so Red means above, Blue means below)
# Select a divergent colormap (RdBu_r: Red-White-Blue reversed)
# Red indicates probability closer to 1 (value safely above threshold)
# Blue indicates probability closer to 0 (value safely below threshold)
# White represents ~0.5 probability (overlapping confidence range)
cap = plt.colormaps.get_cmap('RdBu_r')
cmap = cap
norm = Normalize(vmin=0, vmax=1)

# Plot the bars with error bars (95% CI)
bars = ax.bar(years, means, yerr=yerr, capsize=10,
              edgecolor='#2c3e50', linewidth=1.2, color=[cmap(p) for p in probs],
              error_kw=dict(ecolor='#2c3e50', elinewidth=2, capthick=1.5))

# Draw initial horizontal line at the reference value
hline = ax.axhline(y_interest, color='#e74c3c', linestyle='--', linewidth=2, zorder=5)

# Place text next to the line (aligned slightly left of the first bar)
y_text = ax.text(-0.4, y_interest, f' Y = {y_interest:.0f} ', color='#e74c3c', weight='bold',
                 fontsize=10, va='center', ha='right',
                 bbox=dict(facecolor='white', edgecolor='#e74c3c', boxstyle='round,pad=0.2', alpha=0.95, zorder=6))

# Add probability text labels above each bar
bar_texts = []
for i in range(len(years)):
    val = probs[i] * 100
    txt = ax.text(i, means.iloc[i] + yerr.iloc[i] + 1200, f'{val:.1f}%\nProb > Y',
                  ha='center', va='bottom', fontsize=9, color='#2c3e50', weight='bold')
    bar_texts.append(txt)

# Aesthetics
ax.set_title("Building a Custom Visualization (Ferreira et al. 2014)\nInteractive Mean Comparison relative to Y-Value", 
             fontsize=13, pad=15, weight='bold', color='#2c3e50')
ax.set_xlabel("Year", fontsize=11, labelpad=10, weight='semibold', color='#2c3e50')
ax.set_ylabel("Mean Value & 95% Confidence Interval", fontsize=11, labelpad=10, weight='semibold', color='#2c3e50')
ax.grid(True, axis='y', linestyle='--', alpha=0.5)
ax.set_axisbelow(True)

# Adjust y limits to make space for the label texts above bars
y_min, y_max = ax.get_ylim()
ax.set_ylim(0, y_max + 5000)

# Add horizontal colorbar
sm = cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax, orientation='horizontal', pad=0.18, aspect=45)
cbar.set_label('Confidence level of Year Mean being above selected Y ($P(\\mu > Y)$)', 
               fontsize=10, weight='semibold', color='#2c3e50', labelpad=8)
cbar.set_ticks([0, 0.25, 0.5, 0.75, 1])
cbar.set_ticklabels(['0.0\n(Certainly Below Y)', '0.25', '0.5\n(Mean = Y)', '0.75', '1.0\n(Certainly Above Y)'])
cbar.ax.tick_params(labelsize=8)

# 4. Define interactive event handler
def onclick(event):
    # Ensure the click was inside the main axes
    if event.inaxes != ax:
        return
        
    y_val = event.ydata
    
    # Recalculate probabilities for new y value
    new_probs = get_probabilities(y_val)
    
    # Dynamically update the color of the bars
    for idx, bar in enumerate(bars):
        bar.set_facecolor(cmap(new_probs[idx]))
        
    # Update position and label of the horizontal line
    hline.set_ydata([y_val, y_val])
    y_text.set_position((-0.4, y_val))
    y_text.set_text(f' Y = {y_val:.0f} ')
    
    # Update the probability texts above each bar
    for idx, txt in enumerate(bar_texts):
        val = new_probs[idx] * 100
        txt.set_text(f'{val:.1f}%\nProb > Y')
        
    fig.canvas.draw_idle()

# Connect the click event to the handler
# Bind mouse button clicks to the interactive callback function
fig.canvas.mpl_connect('button_press_event', onclick)

# Add instructional prompt at the bottom of the figure
fig.text(0.5, 0.02, "Click anywhere on the plot area to adjust the reference value Y", 
         ha='center', fontsize=9.5, style='italic', color='#555555', weight='semibold')

plt.tight_layout()
plt.show()

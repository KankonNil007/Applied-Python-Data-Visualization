"""
Assignment 2 - Data Visualization
Applied Plotting, Charting & Data Representation in Python
University of Michigan

This script reproduces the daily temperature record analysis and visualization
completed in assignment2.ipynb. It processes weather station data for the Ann Arbor,
Michigan region to compare 2005-2014 temperature records against anomalies in 2015.
"""

import folium
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# Part 1: Station Location Map (Folium)
# ==========================================
print("Step 0: Generating station locations map...")

# Get the location information for this dataset
bins_df = pd.read_csv('assets/BinSize_d400.csv')
station_locations = bins_df[bins_df['hash'] == 'fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89']

# Get longitude and latitude to plot
lons = station_locations['LONGITUDE'].tolist()
lats = station_locations['LATITUDE'].tolist()

# Plot on a folium map and save as map.html
my_map = folium.Map(location=[lats[0], lons[0]], height=500, zoom_start=9)
for lat, lon in zip(lats, lons):
    folium.Marker([lat, lon]).add_to(my_map)

my_map.save("map.html")
print("Map successfully saved to 'map.html'.")


# ==========================================
# Step 1: Load and Transform Temperature Data
# ==========================================
print("\nStep 1: Loading and transforming dataset...")

# Load raw temperature dataset
df = pd.read_csv('assets/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')

# Transform Data_Value column from tenths of degrees C to degrees Celsius
df['Data_Value'] = df['Data_Value'] / 10.0

# Extract TMAX and TMIN rows into separate DataFrames (~80,000 entries each)
tmax_df = df[df['Element'] == 'TMAX'].copy()
tmin_df = df[df['Element'] == 'TMIN'].copy()

print(f"tmax_df entries: {tmax_df.shape[0]}")
print(f"tmin_df entries: {tmin_df.shape[0]}")


# ==========================================
# Step 2: Handle Leap Years and Group Daily Records
# ==========================================
print("\nStep 2: Processing daily station records (excluding leap days)...")

# Drop records for February 29th (leap days) to align with standard 365-day year
tmax_df = tmax_df[~tmax_df['Date'].str.endswith('-02-29')]
tmin_df = tmin_df[~tmin_df['Date'].str.endswith('-02-29')]

# Create a DataFrame of maximum and minimum temperature by date across all weather stations
max_temp_by_date = tmax_df.groupby('Date')['Data_Value'].max().reset_index()
min_temp_by_date = tmin_df.groupby('Date')['Data_Value'].min().reset_index()

# Ensure exactly 4015 observations are present (11 years * 365 days)
print(f"max_temp_by_date records (expected 4015): {max_temp_by_date.shape[0]}")
print(f"min_temp_by_date records (expected 4015): {min_temp_by_date.shape[0]}")


# ==========================================
# Step 3: Segment Decade (2005-2014) vs. 2015
# ==========================================
print("\nStep 3: Calculating daily bounds and segmenting 2015...")

# Convert Date column to datetime to easily extract Year and Month-Day
max_temp_by_date['Date'] = pd.to_datetime(max_temp_by_date['Date'])
min_temp_by_date['Date'] = pd.to_datetime(min_temp_by_date['Date'])

max_temp_by_date['Year'] = max_temp_by_date['Date'].dt.year
max_temp_by_date['Month_Day'] = max_temp_by_date['Date'].dt.strftime('%m-%d')

min_temp_by_date['Year'] = min_temp_by_date['Date'].dt.year
min_temp_by_date['Month_Day'] = min_temp_by_date['Date'].dt.strftime('%m-%d')

# Filter for the 2005-2014 decade
max_05_14 = max_temp_by_date[max_temp_by_date['Year'] < 2015]
min_05_14 = min_temp_by_date[min_temp_by_date['Year'] < 2015]

# Group by Month_Day to find the record high and low for each day of the year over the decade
decade_max = max_05_14.groupby('Month_Day')['Data_Value'].max().reset_index()
decade_min = min_05_14.groupby('Month_Day')['Data_Value'].min().reset_index()

# Calculate the minimum and maximum values for the year 2015
max_2015 = max_temp_by_date[max_temp_by_date['Year'] == 2015].groupby('Month_Day')['Data_Value'].max().reset_index()
min_2015 = min_temp_by_date[min_temp_by_date['Year'] == 2015].groupby('Month_Day')['Data_Value'].min().reset_index()

print(f"decade_max records (expected 365): {decade_max.shape[0]}")
print(f"decade_min records (expected 365): {decade_min.shape[0]}")
print(f"max_2015 records (expected 365): {max_2015.shape[0]}")
print(f"min_2015 records (expected 365): {min_2015.shape[0]}")


# ==========================================
# Step 4: Identify Anomalies and Plot
# ==========================================
print("\nStep 4: Identifying anomalies and generating matplotlib visualization...")

# Identify 2015 temperatures that broke the 10-year records
broken_high = max_2015[max_2015['Data_Value'] > decade_max['Data_Value']]
broken_low = min_2015[min_2015['Data_Value'] < decade_min['Data_Value']]

print(f"2015 record high-breaking days: {len(broken_high)}")
print(f"2015 record low-breaking days: {len(broken_low)}")

# Set figure size for high readability
plt.figure(figsize=(10, 6))

# Plot historical record lines (2005-2014)
plt.plot(decade_max['Data_Value'], color='#fc8d59', alpha=0.8, linewidth=1.5, label='Record High (2005-2014)')
plt.plot(decade_min['Data_Value'], color='#91bfdb', alpha=0.8, linewidth=1.5, label='Record Low (2005-2014)')

# Shade the historical envelope area
plt.gca().fill_between(range(365), 
                       decade_min['Data_Value'], 
                       decade_max['Data_Value'], 
                       facecolor='#e0e0e0', 
                       alpha=0.4)

# Overlay 2015 record-breaking scatter points
plt.scatter(broken_high.index, broken_high['Data_Value'], color='#d73027', s=25, label='2015 Record High Broken', zorder=10)
plt.scatter(broken_low.index, broken_low['Data_Value'], color='#4575b4', s=25, label='2015 Record Low Broken', zorder=10)

# Title and labels
plt.title('Daily Temperature Records (2005-2014) vs. Record-Breaking 2015 Temperatures\n(Ann Arbor, Michigan, USA)', 
          fontsize=12, fontweight='bold', pad=15, color='#333333')
plt.ylabel('Temperature (°C)', fontsize=10, labelpad=8, color='#333333')

# Format calendar months as x-axis ticks
month_starts = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.xticks(month_starts, month_names, fontsize=9, color='#555555')
plt.yticks(fontsize=9, color='#555555')

plt.xlim(0, 365)

# Tufte-style design: Remove chart junk (top and right spines) and mute remaining borders
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_color('#cccccc')
plt.gca().spines['bottom'].set_color('#cccccc')

# Legend placed below the visual without a border
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.18), ncol=4, frameon=False, fontsize=9)

# Adjust layout and save the visualization
plt.tight_layout()
plt.savefig('assignment2_plot.png', dpi=300, bbox_inches='tight')
print("Successfully generated and saved plot to 'assignment2_plot.png'.")

# Show the plot
plt.show()

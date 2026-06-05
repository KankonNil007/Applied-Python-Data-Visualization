#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Practice Assignment: Understanding Distributions Through Sampling

This script simulates and animates sampling from four probability distributions:
- Normal Distribution
- Gamma Distribution
- Exponential Distribution
- Uniform Distribution

It provides:
1. A static plot visualization (matching Cell 1 of the notebook).
2. An interactive dashboard using matplotlib widgets for parameterized distribution
   sampling animations (matching the bonus goal in Cell 2 of the notebook).

Usage:
    python 01-Practice_Assignment.py         # Runs the interactive animator dashboard
    python 01-Practice_Assignment.py --static # Runs the static visualization plot
"""

import sys
import argparse
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button

# Global variables for animation data and state
x1, x2, x3, x4 = None, None, None, None
anim = None
is_paused = False
updating_sliders = False

# Plot configurations
titles = ['Normal Distribution', 'Gamma Distribution', 'Exponential Distribution', 'Uniform Distribution']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#9467bd']


def run_static_plot():
    """Generates and displays a static plot of the distributions."""
    print("Generating static plot...")
    # Generate 10,000 samples from the normal, gamma, exponential, and uniform distributions
    x1_val = np.random.normal(-2.5, 1, 10000)
    x2_val = np.random.gamma(2, 1.5, 10000)
    x3_val = np.random.exponential(2, 10000) + 7
    x4_val = np.random.uniform(14, 20, 10000)

    # Plot the histograms
    plt.figure(figsize=(9, 4))
    plt.hist(x1_val, density=True, bins=20, alpha=0.5, color=colors[0], label='x1 Normal')
    plt.hist(x2_val, density=True, bins=20, alpha=0.5, color=colors[1], label='x2 Gamma')
    plt.hist(x3_val, density=True, bins=20, alpha=0.5, color=colors[2], label='x3 Exponential')
    plt.hist(x4_val, density=True, bins=20, alpha=0.5, color=colors[3], label='x4 Uniform')
    plt.axis([-7, 21, 0, 0.6])

    plt.text(x1_val.mean() - 1.5, 0.5, 'x1\nNormal', color='#0f4c75', fontweight='bold')
    plt.text(x2_val.mean() - 1.5, 0.5, 'x2\nGamma', color='#c25c0e', fontweight='bold')
    plt.text(x3_val.mean() - 1.5, 0.5, 'x3\nExponential', color='#1e5f1e', fontweight='bold')
    plt.text(x4_val.mean() - 1.5, 0.5, 'x4\nUniform', color='#5e3f85', fontweight='bold')
    
    plt.title("Static Distributions Sampling Visualization", fontsize=12, pad=10)
    plt.xlabel("Value")
    plt.ylabel("Probability Density")
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()


def init_datasets(slider_samples, slider_norm_mean, slider_norm_std, slider_gamma_shape, slider_gamma_scale,
                  slider_exp_scale, slider_exp_offset, slider_unif_low, slider_unif_high):
    """Initializes the four datasets based on the current slider configurations."""
    global x1, x2, x3, x4
    n_max = int(slider_samples.val)
    
    # Generate maximum required samples based on current slider parameters
    x1 = np.random.normal(slider_norm_mean.val, slider_norm_std.val, n_max)
    x2 = np.random.gamma(slider_gamma_shape.val, slider_gamma_scale.val, n_max)
    x3 = np.random.exponential(slider_exp_scale.val, n_max) + slider_exp_offset.val
    
    # Ensure uniform low is strictly less than uniform high
    low = slider_unif_low.val
    high = slider_unif_high.val
    if high <= low:
        high = low + 0.1
    x4 = np.random.uniform(low, high, n_max)


def run_interactive_dashboard():
    """Initializes and runs the interactive animation dashboard with matplotlib widgets."""
    global anim, is_paused, updating_sliders
    print("Launching interactive animator dashboard...")
    print("Note: Two windows will open - one for the visualization and one for control sliders.")
    
    # Create the figures
    fig_plots, axs = plt.subplots(2, 2, figsize=(10, 8))
    axs = axs.ravel()
    fig_plots.canvas.manager.set_window_title('Distribution Animations')
    
    fig_ctrl = plt.figure("Distribution Parameters", figsize=(9, 6.5))
    fig_ctrl.patch.set_facecolor('#f0f0f0')

    # Add descriptive text headers to control panel
    fig_ctrl.text(0.15, 0.93, "Normal Distribution (x1)", fontsize=11, weight='bold', color=colors[0])
    fig_ctrl.text(0.60, 0.93, "Gamma Distribution (x2)", fontsize=11, weight='bold', color=colors[1])
    
    fig_ctrl.text(0.15, 0.62, "Exponential Distribution (x3)", fontsize=11, weight='bold', color=colors[2])
    fig_ctrl.text(0.60, 0.62, "Uniform Distribution (x4)", fontsize=11, weight='bold', color=colors[3])
    
    fig_ctrl.text(0.15, 0.31, "Animation Configurations", fontsize=11, weight='bold', color='#333333')

    # Slider positioning layouts
    # Column 1 & 2 X coordinates and width
    c1_x, c2_x, width = 0.15, 0.60, 0.28
    
    # Axes definition
    ax_norm_mean = fig_ctrl.add_axes([c1_x, 0.85, width, 0.03])
    ax_norm_std  = fig_ctrl.add_axes([c1_x, 0.79, width, 0.03])
    
    ax_gamma_shape = fig_ctrl.add_axes([c2_x, 0.85, width, 0.03])
    ax_gamma_scale = fig_ctrl.add_axes([c2_x, 0.79, width, 0.03])
    
    ax_exp_scale  = fig_ctrl.add_axes([c1_x, 0.54, width, 0.03])
    ax_exp_offset = fig_ctrl.add_axes([c1_x, 0.48, width, 0.03])
    
    ax_unif_low  = fig_ctrl.add_axes([c2_x, 0.54, width, 0.03])
    ax_unif_high = fig_ctrl.add_axes([c2_x, 0.48, width, 0.03])
    
    ax_samples = fig_ctrl.add_axes([c1_x, 0.23, width, 0.03])
    ax_speed   = fig_ctrl.add_axes([c2_x, 0.23, width, 0.03])

    # Instantiate sliders
    slider_norm_mean = Slider(ax_norm_mean, 'Mean', -10.0, 10.0, valinit=-2.5, color=colors[0])
    slider_norm_std  = Slider(ax_norm_std, 'Std Dev', 0.1, 5.0, valinit=1.0, color=colors[0])
    
    slider_gamma_shape = Slider(ax_gamma_shape, 'Shape', 0.5, 10.0, valinit=2.0, color=colors[1])
    slider_gamma_scale = Slider(ax_gamma_scale, 'Scale', 0.1, 5.0, valinit=1.5, color=colors[1])
    
    slider_exp_scale  = Slider(ax_exp_scale, 'Scale', 0.1, 10.0, valinit=2.0, color=colors[2])
    slider_exp_offset = Slider(ax_exp_offset, 'Offset', 0.0, 15.0, valinit=7.0, color=colors[2])
    
    slider_unif_low  = Slider(ax_unif_low, 'Low', 5.0, 25.0, valinit=14.0, color=colors[3])
    slider_unif_high = Slider(ax_unif_high, 'High', 10.0, 30.0, valinit=20.0, color=colors[3])
    
    slider_samples = Slider(ax_samples, 'Max Samples', 100, 1000, valinit=500, valstep=50, color='#555555')
    slider_speed   = Slider(ax_speed, 'Speed (ms)', 20, 200, valinit=50, valstep=10, color='#555555')

    # Style labels/values
    for slider in [slider_norm_mean, slider_norm_std, slider_gamma_shape, slider_gamma_scale,
                   slider_exp_scale, slider_exp_offset, slider_unif_low, slider_unif_high,
                   slider_samples, slider_speed]:
        slider.label.set_fontsize(9)
        slider.valtext.set_fontsize(9)

    # Initialize datasets based on initial values
    init_datasets(slider_samples, slider_norm_mean, slider_norm_std, slider_gamma_shape, slider_gamma_scale,
                  slider_exp_scale, slider_exp_offset, slider_unif_low, slider_unif_high)

    def update(frame):
        """Update callback function for FuncAnimation."""
        if x1 is None:
            return
            
        for i in range(4):
            axs[i].clear()
            
            # Determine dynamic ranges and bins based on current widget parameters
            if i == 0:
                data = x1[:frame]
                mu, sigma = slider_norm_mean.val, slider_norm_std.val
                xlim = (mu - 4 * sigma, mu + 4 * sigma)
                ylim = (0, 1.2 / (sigma * np.sqrt(2 * np.pi)))
                bins = np.linspace(xlim[0], xlim[1], 30)
            elif i == 1:
                data = x2[:frame]
                shape, scale = slider_gamma_shape.val, slider_gamma_scale.val
                xlim = (0, shape * scale + 4 * np.sqrt(shape) * scale)
                if shape > 1:
                    peak = ((shape - 1)**(shape - 1) * np.exp(1 - shape)) / (scale * math.gamma(shape))
                else:
                    peak = 1.0 / scale
                ylim = (0, max(peak * 1.2, 0.2))
                bins = np.linspace(xlim[0], xlim[1], 30)
            elif i == 2:
                data = x3[:frame]
                scale, offset = slider_exp_scale.val, slider_exp_offset.val
                xlim = (offset, offset + 4 * scale)
                ylim = (0, 1.2 / scale)
                bins = np.linspace(xlim[0], xlim[1], 30)
            else:
                data = x4[:frame]
                low, high = slider_unif_low.val, slider_unif_high.val
                if high <= low:
                    high = low + 0.1
                xlim = (low - 0.5, high + 0.5)
                ylim = (0, 1.2 / (high - low))
                bins = np.linspace(low, high, 30)
                
            # Draw the histogram
            axs[i].hist(data, bins=bins, density=True, color=colors[i], alpha=0.6, edgecolor='black', linewidth=0.5)
            axs[i].set_xlim(xlim)
            axs[i].set_ylim(ylim)
            axs[i].set_title(f'{titles[i]} (n={frame})', fontsize=10, weight='bold')
            axs[i].set_ylabel('Probability Density', fontsize=8)
            axs[i].set_xlabel('Value', fontsize=8)
            axs[i].grid(True, linestyle='--', alpha=0.3)
            axs[i].tick_params(labelsize=8)
            
        fig_plots.tight_layout()

    def restart_anim(val=None):
        """Restarts/Re-initializes the matplotlib FuncAnimation object."""
        global anim, is_paused
        
        # Stop existing animation if one is active
        if anim is not None:
            try:
                anim.event_source.stop()
            except Exception:
                pass
                
        n_max = int(slider_samples.val)
        interval = int(slider_speed.val)
        
        # Generate frame steps from 100 to N
        frame_steps = np.arange(100, n_max + 1, max(1, (n_max - 100) // 40))
        
        # Reset pauses
        is_paused = False
        btn_pause.label.set_text("Pause")
        
        anim = animation.FuncAnimation(
            fig_plots, 
            update, 
            frames=frame_steps, 
            interval=interval, 
            cache_frame_data=False,
            repeat=True, 
            repeat_delay=1000
        )
        fig_plots.canvas.draw_idle()

    # Event handlers for slider changes
    def on_parameter_change(val):
        """Callback for distribution parameter slider movements."""
        global updating_sliders
        if updating_sliders:
            return
            
        updating_sliders = True
        try:
            # Enforce Low < High constraint for Uniform distribution
            if slider_unif_low.val >= slider_unif_high.val:
                slider_unif_high.set_val(slider_unif_low.val + 0.5)
        finally:
            updating_sliders = False
            
        init_datasets(slider_samples, slider_norm_mean, slider_norm_std, slider_gamma_shape, slider_gamma_scale,
                      slider_exp_scale, slider_exp_offset, slider_unif_low, slider_unif_high)
        # We do not need to restart the entire animation loop;
        # updating the global datasets (x1, x2, x3, x4) is enough
        # and runs incredibly smoothly without lagging.

    def on_structure_change(val):
        """Callback for structure changes like Max Samples or animation speed/interval."""
        init_datasets(slider_samples, slider_norm_mean, slider_norm_std, slider_gamma_shape, slider_gamma_scale,
                      slider_exp_scale, slider_exp_offset, slider_unif_low, slider_unif_high)
        restart_anim()

    # Register slider updates
    for slider in [slider_norm_mean, slider_norm_std, slider_gamma_shape, slider_gamma_scale,
                   slider_exp_scale, slider_exp_offset, slider_unif_low, slider_unif_high]:
        slider.on_changed(on_parameter_change)
        
    slider_samples.on_changed(on_structure_change)
    slider_speed.on_changed(on_structure_change)

    # Add Action Buttons
    ax_pause = fig_ctrl.add_axes([0.33, 0.05, 0.14, 0.06])
    btn_pause = Button(ax_pause, 'Pause', color='#e0e0e0', hovercolor='#d0d0d0')
    
    ax_reset = fig_ctrl.add_axes([0.53, 0.05, 0.14, 0.06])
    btn_reset = Button(ax_reset, 'Reset All', color='#e0e0e0', hovercolor='#d0d0d0')

    # Button Event handlers
    def toggle_pause(event):
        global is_paused
        if is_paused:
            anim.resume()
            btn_pause.label.set_text("Pause")
            is_paused = False
        else:
            anim.pause()
            btn_pause.label.set_text("Play")
            is_paused = True
        fig_ctrl.canvas.draw_idle()

    def reset_sliders(event):
        global updating_sliders
        updating_sliders = True
        try:
            slider_norm_mean.reset()
            slider_norm_std.reset()
            slider_gamma_shape.reset()
            slider_gamma_scale.reset()
            slider_exp_scale.reset()
            slider_exp_offset.reset()
            slider_unif_low.reset()
            slider_unif_high.reset()
            slider_samples.reset()
            slider_speed.reset()
        finally:
            updating_sliders = False
            
        init_datasets(slider_samples, slider_norm_mean, slider_norm_std, slider_gamma_shape, slider_gamma_scale,
                      slider_exp_scale, slider_exp_offset, slider_unif_low, slider_unif_high)
        restart_anim()

    btn_pause.on_clicked(toggle_pause)
    btn_reset.on_clicked(reset_sliders)

    # Launch initial animation loop
    restart_anim()
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Visualize distributions through sampling.")
    parser.add_argument('--static', action='store_true', help="Show the simple static histogram plot")
    args = parser.parse_args()

    if args.static:
        run_static_plot()
    else:
        run_interactive_dashboard()

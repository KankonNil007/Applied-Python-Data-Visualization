# 📚 Principles of Information Visualization (Theory & Critique)

This folder contains the theoretical foundations and reading guides for Module 01, focusing on the cognitive science, integrity guidelines, and critical evaluation techniques of information design.

<div align="center">
  <img src="https://img.shields.io/badge/Focus-Graphical%20Integrity-blue?style=for-the-badge" alt="Focus">
  <img src="https://img.shields.io/badge/Standard-Tufte%20%26%20Cairo-orange?style=for-the-badge" alt="Standards">
</div>

---

## 📖 Key Theoretical Frameworks

This submodule explores two of the most influential frameworks in modern data visualization:

### 1. Alberto Cairo's Core Dimensions
A visual graphic must be evaluated along four interconnected dimensions to ensure it serves as an effective tool for visual discovery:
* **Truthful**: Accurate representation of the data without geometry manipulation or cherry-picking.
* **Functional**: Designed to support specific analytical questions, making patterns easy to identify.
* **Beautiful**: Visually engaging, clean typography, harmonious colors, and appropriate visual hierarchy.
* **Insightful**: Revealing patterns or relationships that would otherwise remain hidden in raw tabular data.

### 2. Edward Tufte's Graphical Integrity
* **The Lie Factor**: The size of the effect shown in a graphic divided by the actual size of the effect in the data. A Lie Factor $> 1$ indicates distortion.
  $$\text{Lie Factor} = \frac{\text{Size of effect shown in graphic}}{\text{Size of effect in data}}$$
* **Data-Ink Ratio**: Maximizing the ratio of data-ink (ink directly representing data variations) to total ink used in the graphic.
* **Integrity Rules**:
  * Clear, detailed, and thorough labeling should be used to defeat graphical distortion and ambiguity.
  * Write out explanations of the data directly on the graphic itself.
  * Show data variation, not design variation.

---

## 🚫 The Three Mechanisms of Chart Deception

According to Cairo's *Graphics Lies, Misleading Visuals*, visual designers often deceive viewers (intentionally or unintentionally) through three primary mechanisms:

| Mechanism | Description | Example Flaws |
| :--- | :--- | :--- |
| **1. Hiding Data** | Omiting critical background context, historical trend data, or key comparison groups. | • Showing a single year spike while omitting a 10-year downward trend.<br>• Cherry-picking specific starting points for a timeline. |
| **2. Cluttering** | Overwhelming the viewer with excessive visual junk or chart decorations. | • Heavy, high-contrast grids.<br>• Redundant legends and decorative 3D bars.<br>• Complex patterns that obscure readability. |
| **3. Incorrect Representation** | Using incorrect visual geometry, inappropriate scales, or misleading axes. | • **Truncated Y-Axes**: Starting the vertical axis above zero on a bar chart.<br>• **Area Scaling**: Doubling a circle's radius (which increases area by $4\times$) to represent a $2\times$ data increase. |

---

## 🧩 Visual Critiquing Framework

When reviewing any data visualization in this course, I use the following checklist:
1. **Identify the source and context**: Who made it? What was the medium and publication date? Who was the intended audience?
2. **Deconstruct the visual encoding**: What coordinates, colors, areas, and shapes are mapped to the numbers?
3. **Verify the scales**: Are the scales linear, logarithmic, or categorical? Do the y-axes start at zero where required?
4. **Determine the Lie Factor**: Does the graphic's geometry visually match the underlying mathematical proportions?
5. **Suggest improvements**: How can this chart be redesigned using Edward Tufte's dejunking principles to represent the data truthfully?

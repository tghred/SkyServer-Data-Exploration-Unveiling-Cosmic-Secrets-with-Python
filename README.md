# 🌌 SkyServer Data Exploration: Unveiling Cosmic Secrets with Python

[![Kaggle](https://img.shields.io/badge/Kaggle-Notebook-blue?style=flat&logo=kaggle)](YOUR_KAGGLE_LINK_HERE)
[![Python](https://img.shields.io/badge/Python-3.8+-yellow?style=flat&logo=python)](https://www.python.org)

> "An exploratory data analysis (EDA) and time-series journey into the Sloan Digital Sky Survey (SDSS) dataset, where tabular astronomical rows transform into breathing stars, cosmic expansions, and stellar explosions."

---

## 📌 Project Overview

This project bridges the gap between **Data Engineering** and **Observational Astrophysics**. Using a subset of 10,000 observations from the **SkyServer (SDSS)**, this repository uncovers how statistical filters and time-series analysis can identify rare stellar events and map the geometry of our universe right from a computer screen.

### 🔍 Key Discoveries
* **The 6,750 Universe:** Out of 6,750 unique celestial objects, the vast majority were captured as static snapshots to build a 3D cosmic map.
* **The Dynamic 5:** By leveraging statistical aggregation (`value_counts()`), 5 heavily monitored objects were isolated to reconstruct their temporal behavior across years.
* **Stellar Phenomena Uncovered:**
  * **The Cepheid Variable Candidate:** A star displaying smooth, periodic pulsations—the cosmic yardstick.
  * **The Sudden Nova:** Capturing a dramatic, sudden spike in brightness followed by a sharp fading back into the dark.
  * **The Cosmic Ruler (Redshift):** Linking astronomical velocity to distance, separating our Milky Way neighbors from distant expanding galaxies.

---

### 📊 Dataset 

The dataset used in this project is sourced from Kaggle: [SDSS SkyServer Dataset](https://www.kaggle.com/datasets/muhakabartay/sloan-digital-sky-survey-dr16).

## 📊 Visualizing the Cosmic Symphony

Using `Matplotlib` with shared axes grid configurations, the project generates a 2x2 comparison plot of light curves (`r`-magnitude over time) for the top four most observed objects:

![Stellar Light Curves](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgiGkoPRxMph2BkCAQcNINCgNUhR3HtT5Bs5GWUNNyFNhuiV52I_nVSDdV_BKRpw5GjUWicLjK2Dk6ipES-JxPXw4X2G15IelFXbGqIWryKt9D2PJlAgLEYMN8_AiGlCQteWOQAu177JBH8XTiEG5dG9TJjOOTqi-TAZtToBPFIFnZFrOIuhGCdFxEFtta_/s1280/79289.jpg)

*Note: The Y-axis is inverted in accordance with astronomical magnitude conventions (lower values = higher brightness).*

---

## 🧬 Understanding the Features (The Astronomical Blueprint)

The analysis heavily relies on the **ugriz optical filters**:
* **$u$ (Ultraviolet) & $g$ (Green):** Measuring high-temperature, young stellar energy.
* **$r$ (Red) & $i, z$ (Infrared):** Tracing cooler, older stars and cutting through interstellar dust lanes.
* **Redshift ($z$):** Measuring the stretching of light waves to calculate how fast an object is moving away from us due to cosmic expansion.

---

## 🚀 Getting Started

### Prerequisites

## 💾 Dataset
The project utilizes the standard `Skyserver.csv` output containing spatial coordinates, magnitudes, MJD (Modified Julian Date), and spectroscopic redshift attributes.
## 🔮 Future Roadmap (In the Pipeline)
- [ ] **Lomb-Scargle Periodogram:** Extracting the exact mathematical pulsation period of the Cepheid variable candidate.
- [ ] **Color-Magnitude Diagram (CMD):** Plotting all 6,750 unique objects using ($u - r$) colors to replicate the observational Hertzsprung-Russell (HR) diagram.
- [ ] **Photometric Redshift Prediction:** Training a Machine Learning Regressor to predict cosmological distance using only the five optical filters.

## 📝 Blog Post
A detailed, narrative-driven article explaining the physics and data engineering behind this project can be found in Arabic on my science blog [**Sarmady Sci (سرمدي)**](YOUR_BLOG_LINK_HERE).

## 👩‍💻 Author
* **Taghred Salah Ashry** - *Computer Engineer & Scientific Illustrator*
* Find me on [LinkedIn](https://www.linkedin.com/in/taghred-salah-952611146/) | [Kaggle](https://www.kaggle.com/taghredsalah199)

---
*"We are all in the gutter, but some of us are looking at the stars." — Oscar Wilde*

## 🚀 Quick Run
Clone the repository and run the main notebook:

```bash
git clone [https://github.com/YOUR_USERNAME/skyserver-astronomy-eda.git](https://github.com/YOUR_USERNAME/skyserver-astronomy-eda.git)
cd skyserver-astronomy-eda




pip install pandas matplotlib numpy



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Citation & Attribution
If you use this data pipeline, code, or methodology in your academic research, papers, or projects, please provide proper attribution by citing this repository:

```text
Ashry, T. S. (2026). SkyServer Data Exploration & Pipeline. GitHub repository:
 [https://github.com/tghred/SkyServer-Data-Exploration-Unveiling-Cosmic-Secrets-with-Python/blob/main/README.md]


```text
MIT License

Copyright (c) 2026 Taghred Salah Ashry

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


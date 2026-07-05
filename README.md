
# 🌌 SkyServer Data Exploration: Unveiling Cosmic Secrets with Python

[![Kaggle](https://img.shields.io/badge/Kaggle-Notebook-blue?style=flat&logo=kaggle)](YOUR_KAGGLE_LINK_HERE)
[![Python](https://img.shields.io/badge/Python-3.8+-yellow?style=flat&logo=python)](https://www.python.org)

> "An exploratory data analysis (EDA) and time-series journey into the Sloan Digital Sky Survey (SDSS) dataset, where tabular astronomical rows transform into breathing stars, cosmic expansions, and stellar eclipses."

---

## 📌 Project Overview

This project bridges the gap between **Data Engineering** and **Observational Astrophysics**. Using a subset of observations from the **SkyServer (SDSS)**, this repository uncovers how statistical filters, data cleaning, and time-series analysis can isolate rare stellar systems and map the geometry of our universe right from a computer screen.

### 🔍 Key Discoveries
* **The Static Universe:** Out of thousands of unique celestial objects, the vast majority were captured as static snapshots to map large-scale cosmic structures.
* **The Dynamic 5:** By leveraging statistical aggregation (`value_counts()`), heavily monitored objects were isolated to reconstruct their temporal behavior across years.
* **Stellar Phenomena Uncovered:**
  * **The Eclipsing Binary Star System:** A spectacular find—two co-orbiting stars crossing paths. The light curve displays a periodic deep drop in brightness as one star mechanically blocks the light of its companion.
  * **The Cosmic Ruler (Redshift):** Linking astronomical velocity to distance. The binary candidate shows a spectroscopic redshift ($z \approx 0$), proving it is a dynamic stellar neighbor residing deep within our own Milky Way, obeying Keplerian orbital mechanics rather than cosmic expansion.
  * **The Sudden Nova Candidate:** Capturing a dramatic, sudden spike in brightness followed by a sharp fading back into the dark.

---

## 📊 Visualizing the Cosmic Symphony

Using `Matplotlib` with shared axes grid configurations, the project generates a 2x2 comparison plot of light curves (`r`-magnitude over time) for the top most observed objects, showcasing the regular dips of the eclipsing binary:

![Stellar Light Curves](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgiGkoPRxMph2BkCAQcNINCgNUhR3HtT5Bs5GWUNNyFNhuiV52I_nVSDdV_BKRpw5GjUWicLjK2Dk6ipES-JxPXw4X2G15IelFXbGqIWryKt9D2PJlAgLEYMN8_AiGlCQteWOQAu177JBH8XTiEG5dG9TJjOOTqi-TAZtToBPFIFnZFrOIuhGCdFxEFtta_/s1280/79289.jpg)

*Note: The Y-axis is inverted in accordance with astronomical magnitude conventions (lower values = higher brightness).*

---

## 🧬 Understanding the Features (The Astronomical Blueprint)

The analysis heavily relies on the **ugriz optical filters** and spectroscopic attributes:
* **$u$ (Ultraviolet) & $g$ (Green):** Measuring high-temperature, young stellar energy.
* **$r$ (Red) & $i, z$ (Infrared):** Tracing cooler, older stars and cutting through interstellar dust lanes.
* **Redshift ($z$):** Measuring the stretching of light waves. Used here as a cosmic gatekeeper to separate expanding extragalactic objects from local galactic stars ($z \approx 0$).

---

## 💾 Dataset
The project utilizes the standard `Skyserver.csv` output containing spatial coordinates, magnitudes, MJD (Modified Julian Date), and spectroscopic redshift attributes sourced from Kaggle: [SDSS SkyServer Dataset](https://www.kaggle.com/datasets/muhakabartay/sloan-digital-sky-survey-dr16).

---

## 🚀 Getting Started

### Prerequisites
You need Python 3.8+ and the following data science libraries installed:
```bash
pip install pandas matplotlib numpy

```

### Quick Run

Clone the repository and run the main notebook:

```bash
git clone [https://github.com/YOUR_USERNAME/skyserver-astronomy-eda.git](https://github.com/YOUR_USERNAME/skyserver-astronomy-eda.git)
cd skyserver-astronomy-eda
jupyter notebook

```

---

## 🔮 Future Roadmap (In the Pipeline)

* [ ] **Orbital Modeling:** Applying Kepler's Third Law to approximate the mass ratio and distance between the two co-orbiting stars in the binary system.
* [ ] **Color-Magnitude Diagram (CMD):** Plotting unique objects using ($u - r$) colors to replicate the observational Hertzsprung-Russell (HR) diagram.
* [ ] **Photometric Redshift Prediction:** Training a Machine Learning Regressor to predict cosmological distance using only the five optical filters.

---

## 📝 Blog Post

A detailed, narrative-driven article explaining the physics and data engineering behind this project can be found in Arabic on my science blog **[Sarmady Sci (سرمدي العلمي)](https://www.google.com/search?q=YOUR_BLOG_LINK_HERE)**.

## 👩‍💻 Author

* **Taghred Salah Ashry** - *Data Engineer, Scientific Illustrator & Astronomy Enthusiast*
* Find me on [LinkedIn](https://www.linkedin.com/in/taghred-salah-952611146/) | [Kaggle](https://www.kaggle.com/taghredsalah199)

---

*"We are all in the gutter, but some of us are looking at the stars." — Oscar Wilde*

---

## 📄 License

This project is licensed under the MIT License - see below for details.

### Citation & Attribution

If you use this data pipeline, code, or methodology in your academic research, papers, or projects, please provide proper attribution by citing this repository:

```text
Ashry, T. S. (2026). SkyServer Data Exploration & Pipeline. GitHub repository: [https://github.com/tghred/SkyServer-Data-Exploration](https://github.com/tghred/SkyServer-Data-Exploration).

```

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


```

```

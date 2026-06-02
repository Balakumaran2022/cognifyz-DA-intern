# Cognifyz Data Analysis Internship Solutions

This repository contains professional, insight-driven Python solutions for all 11 tasks across **Levels 1, 2, and 3** of the Cognifyz Data Analysis Internship.

Each solution is designed to:
1. Perform robust statistical and qualitative computations on the provided `Dataset .csv`.
2. Output clean, human-readable tabular data and analytical summaries to the console.
3. Handle special characters (UTF-8 encoding) to prevent command prompt crashes.
4. Export high-resolution, premium visualizations (`.png` plots with custom modern palettes) saved directly in the respective level folders.

---

## 📂 Repository Structure

```
COGNIFYZ/
├── Level 1/
│   ├── task1_top_cuisines.py         # Top most common cuisines & percentages
│   ├── task1_top_cuisines.png        # Bar chart of top cuisines
│   ├── task2_city_analysis.py        # Restaurant volume vs. rating per city
│   ├── task2_city_analysis.png       # Dual-axis volume and rating chart
│   ├── task3_price_distribution.py   # Distribution of restaurant price ranges
│   ├── task3_price_distribution.png  # Percentage distribution bar chart
│   ├── task4_online_delivery.py      # Delivery availability vs. restaurant rating
│   └── task4_online_delivery.png     # Donut & bar chart comparison
├── Level 2/
│   ├── task1_restaurant_ratings.py   # Aggregate rating distribution & votes
│   ├── task1_restaurant_ratings.png  # Ratings distribution histogram & ranges
│   ├── task2_cuisine_combinations.py # Most common cuisine combos vs. global rating
│   ├── task2_cuisine_combinations.png# Counts & average ratings comparison
│   ├── task3_geographic_analysis.py  # Spatial clustering of restaurants
│   ├── task3_geographic_analysis.png # K-Means cluster map & NCR hotspot map
│   ├── task4_restaurant_chains.py    # Outlets volume, ratings & popularity
│   └── task4_restaurant_chains.png   # Outlets count vs. total votes charts
├── Level 3/
│   ├── task1_restaurant_reviews.py   # Review keyword analysis & length vs. rating
│   ├── task1_restaurant_reviews.png  # Word frequency & length vs. rating charts
│   ├── task2_votes_analysis.py       # Extremes of voting & votes-rating correlation
│   ├── task2_votes_analysis.png      # Regression/scatter plot of votes vs. rating
│   ├── task3_price_vs_services.py    # Price ranges vs. online delivery & table booking
│   └── task3_price_vs_services.png   # Multi-variable stacked availability chart
├── Dataset .csv                      # Underlying raw dataset
├── Data Analysis.pdf                 # Internship task definitions
└── README.md                         # Project documentation
```

---

## 🚀 How to Run the Solutions

Make sure you have the required libraries installed:
```bash
pip install pandas matplotlib seaborn scikit-learn
```

Run any script directly from the root workspace directory. Examples:
```bash
python "Level 1/task1_top_cuisines.py"
python "Level 2/task3_geographic_analysis.py"
python "Level 3/task2_votes_analysis.py"
```

---

## 📊 Analytical Insights and Findings

### 📍 Level 1 Summary

* **Task 1: Top Cuisines**
  * **Top 3 Cuisines**: North Indian (41.46%), Chinese (28.64%), and Fast Food (20.79%).
  * *Insight*: North Indian and Chinese dominate nearly 70% of the dataset's culinary landscape.

* **Task 2: City Analysis**
  * **Volume Leader**: New Delhi is the largest market, hosting 5,473 restaurants.
  * **Rating Leaders**: **Inner City** is the absolute highest (4.90 rating across 2 outlets). Among cities with significant volume (min 10 restaurants), **London** scores highest with a **4.54/5.0** average rating.

* **Task 3: Price Distribution**
  * **Breakdown**: Low Price Range (46.53%), Medium (32.59%), High (14.74%), and Very High (6.14%).
  * *Insight*: Nearly 80% of the restaurants are positioned as budget-to-mid-range dining options.

* **Task 4: Online Delivery Impact**
  * **Availability**: 25.66% offer online delivery; 74.34% do not.
  * **Rating Impact**: Restaurants offering online delivery have an average rating of **3.25**, compared to **2.47** for those without (+0.78 rating points higher).

---

### 📍 Level 2 Summary

* **Task 1: Ratings and Votes**
  * **Most Common Range**: **3.0 - 3.5** rating (26.20% of restaurants). 
  * **Averages**: Overall average votes per restaurant stands at **156.91**.

* **Task 2: Cuisine Combinations**
  * **Most Common**: "North Indian" (936 outlets), "North Indian, Chinese" (511 outlets).
  * *Insight*: While single-category North Indian has a lower average rating (1.67), combination pairings like **North Indian & Mughlai** (2.89) and **Cafes** (2.89) outperform the global dataset average of **2.67**.

* **Task 3: Geographic Clustering**
  * **Primary Global Hubs**: K-Means clustering successfully separated three main geographical hotspots:
    1. **India Hub (Agra/NCR)**: 8,379 restaurants (92.6% of coordinates).
    2. **USA Hub**: 438 restaurants (4.8%).
    3. **UK/Europe Hub**: 235 restaurants (2.6%).
  * *Insight*: Zoom-in analysis of the NCR hotspot reveals higher-rated restaurants clustered strongly around major city centers/hubs.

* **Task 4: Chains Analysis**
  * **Largest Chains**: Cafe Coffee Day (83 outlets) and Domino's Pizza (79 outlets).
  * **Popularity Leader**: **Barbeque Nation** dominates in votes (28,142 total votes across 26 outlets) and holds a premium rating of **4.35 / 5.0**.

---

### 📍 Level 3 Summary

* **Task 1: Review Sentiment & Length**
  * **Positive Keywords**: "Good" (3,179 occurrences), "Very" (1,079 occurrences), "Excellent" (301 occurrences).
  * **Negative Keywords**: "Average" (3,737 occurrences), "Poor" (186 occurrences).
  * *Insight*: Text review length has a **negative correlation (-0.48)** with the rating. This mathematically proves that unrated/average ratings have longer descriptors (like "Not rated" or "Average") compared to simple high descriptors ("Good", "Excellent").

* **Task 2: Votes and Ratings Correlation**
  * **Correlation Coefficient**: **0.3137** (Moderate positive correlation).
  * *Insight*: Higher-rated restaurants attract exponentially higher voter turnout. The absolute highest voted restaurant in the dataset is **Toit** (Bangalore) with **10,934 votes** and an outstanding **4.8/5.0** rating.

* **Task 3: Service Availability vs. Price Range**
  * *Insight*: Higher-priced restaurants are substantially more likely to offer services.
    * **Table Booking**: Rises from a mere **0.02%** in the budget tier to **46.76%** in the premium tier (strong correlation: **0.4718**).
    * **Online Delivery**: Peaks in the mid-range tier (**41.31%** for Price Range 2) and drops to **9.04%** in the premium tier, showing that luxury dining places prioritize dine-in over home deliveries.

---

*Solutions implemented and verified by Antigravity, Advanced Agentic Coding Assistant.*

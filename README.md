# 📊 Restaurant Industry Data Analysis & Visualization Portfolio

This repository contains professional, insight-driven Python solutions for all 11 analytical tasks across the three progression levels of the **Cognifyz Data Analysis Internship**. Using standard data science libraries (Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn), these solutions extract deep business intelligence from a global restaurant dataset of over 9,500 outlets.

---

## 📂 Repository File Structure
```bash
├── Level 1/
│   ├── task1_top_cuisines.py         # Cuisine frequency & percentage analysis
│   ├── task1_top_cuisines.png        # Visualization: Horizontal bar chart
│   ├── task2_city_analysis.py        # Regional volume vs. rating mapping
│   ├── task2_city_analysis.png       # Visualization: Dual-axis chart
│   ├── task3_price_distribution.py   # Price tier volume segmenting
│   ├── task3_price_distribution.png  # Visualization: Distribution bar chart
│   ├── task4_online_delivery.py      # Delivery availability vs. rating impact
│   └── task4_online_delivery.png     # Visualization: Donut & bar charts
├── Level 2/
│   ├── task1_restaurant_ratings.py   # Aggregate rating distribution & votes analysis
│   ├── task1_restaurant_ratings.png  # Visualization: Histogram & distribution range
│   ├── task2_cuisine_combinations.py # Common cuisine pairings vs. average rating
│   ├── task2_cuisine_combinations.png# Visualization: Combined count and rating bars
│   ├── task3_geographic_analysis.py  # Spatial clustering of restaurants (K-Means)
│   ├── task3_geographic_analysis.png # Visualization: Cluster scatter plots
│   ├── task4_restaurant_chains.py    # Outlets volume, ratings & brand popularity
│   └── task4_restaurant_chains.png   # Visualization: Outlets count vs. total votes
├── Level 3/
│   ├── task1_restaurant_reviews.py   # Review text keyword search & review length correlation
│   ├── task1_restaurant_reviews.png  # Visualization: Word frequency & scatter plot
│   ├── task2_votes_analysis.py       # Voting distribution & votes-rating correlation
│   ├── task2_votes_analysis.png      # Visualization: Regression scatter plot
│   ├── task3_price_vs_services.py    # Service availability across price range tiers
│   └── task3_price_vs_services.png   # Visualization: Multi-variable stacked bar chart
├── Dataset .csv                      # Underlying raw CSV dataset
├── Data Analysis.pdf                 # Internship task specifications
└── README.md                         # Project documentation
```

---

## 💻 Installation & Environment Setup

Follow these steps to run the Python scripts locally:

### 1. Prerequisites
Ensure you have [Python 3.8+](https://www.python.org/) installed.

### 2. Install Required Libraries
Install the necessary analytical and graphing libraries using pip:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

### 3. Run the Scripts
Execute the scripts from the root directory of the workspace to ensure correct relative paths for loading the dataset:
```bash
# Level 1 Examples
python "Level 1/task1_top_cuisines.py"
python "Level 1/task4_online_delivery.py"

# Level 2 Examples
python "Level 2/task3_geographic_analysis.py"

# Level 3 Examples
python "Level 3/task2_votes_analysis.py"
```

---

## 📈 Analytical Insights & Findings

### 📍 Level 1: Market Fundamentals
* **Task 1: Top Cuisines**
  - **Dominant Flavors**: The top three cuisines in the dataset are **North Indian** (41.46%), **Chinese** (28.64%), and **Fast Food** (20.79%).
  - *Insight*: Over 70% of the restaurants feature North Indian or Chinese offerings, showing high market saturation for these categories.
* **Task 2: City Analysis**
  - **Volume Leader**: New Delhi represents the largest regional market, containing 5,473 restaurants.
  - **Rating Leaders**: Among cities with significant volume (minimum 10 outlets), **London** scores highest with an outstanding average rating of **4.54/5.0**.
* **Task 3: Price Tier Distribution**
  - **Distribution**: Low Price Range (46.53%), Medium (32.59%), High (14.74%), and Very High (6.14%).
  - *Insight*: Approximately 80% of the market targets budget-to-mid-range consumers.
* **Task 4: Online Delivery Impact**
  - **Availability**: Only 25.66% of restaurants offer online delivery.
  - **Rating Impact**: Restaurants offering online delivery have an average rating of **3.25**, compared to **2.47** for those without (+0.78 rating difference).

---

### 📍 Level 2: Advanced Groupings & Spatial Data
* **Task 1: Rating Ranges & Votes**
  - **Most Common Rating**: The **3.0 - 3.5** rating range represents the largest segment (26.20% of restaurants). 
  - **Voter Turnout**: The overall average number of votes per restaurant is **156.91**.
* **Task 2: Cuisine Combinations**
  - **Most Popular Pairings**: Single-cuisine "North Indian" (936 outlets) and "North Indian, Chinese" combo (511 outlets) are the most frequent.
  - *Insight*: While single-category North Indian holds a lower average rating (1.67), combinations like **North Indian & Mughlai** (2.89) outperform the global dataset average of **2.67**.
* **Task 3: Spatial Clustering (K-Means)**
  - **Global Hotspots**: K-Means clustering identified three geographical hubs:
    1. **India Hub (NCR)**: 8,379 restaurants (92.6% of coordinates).
    2. **USA Hub**: 438 restaurants (4.8%).
    3. **UK/Europe Hub**: 235 restaurants (2.6%).
  - *Insight*: Within the Indian NCR hotspot, high-rated restaurants form dense clusters in central urban business districts.
* **Task 4: Restaurant Chains**
  - **Largest Chains**: Cafe Coffee Day (83 outlets) and Domino's Pizza (79 outlets).
  - **Popularity & Rating Leader**: **Barbeque Nation** leads in votes (28,142 total votes across 26 outlets) with a high average rating of **4.35 / 5.0**.

---

### 📍 Level 3: Text Mining, Correlation & Services Mapping
* **Task 1: Sentiment & Review Length Analysis**
  - **Sentiment Keywords**: "Good" (3,179 occurrences) and "Very" (1,079 occurrences) dominate positive feedback. "Average" (3,737 occurrences) represents the most common neutral feedback.
  - *Insight*: A **negative correlation (-0.48)** exists between review length and rating. Unrated or average listings contain longer placeholders (like "Not rated"), while high ratings feature concise, positive descriptors (like "Excellent", "Good").
* **Task 2: Voting & Rating Correlation**
  - **Correlation Coefficient**: **0.3137** (Moderate positive correlation).
  - *Insight*: Outlets with higher ratings receive significantly more votes. **Toit** (Bangalore) has the highest voter turnout in the dataset (**10,934 votes** with a **4.8/5.0** rating).
* **Task 3: Service Availability by Price Range**
  - *Insight*: Premium restaurants are much more likely to offer services:
    - **Table Booking**: Rises from **0.02%** in the budget tier to **46.76%** in the premium tier (strong positive correlation of **0.4718**).
    - **Online Delivery**: Peaks in the mid-range tier (**41.31%** for Price Range 2) and drops to **9.04%** in the premium tier, showing that luxury dining options prioritize dine-in experiences over delivery.

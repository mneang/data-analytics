# Retail Performance Dashboard

The **Retail Performance Dashboard** is a comprehensive analytical tool that transforms raw retail data into actionable insights. Designed to answer real-world business questions, this project highlights my ability to merge technical expertise with a passion for solving problems and inspiring others through data.

---

## **Project Overview**

This dashboard empowers decision-makers by providing key insights into **sales**, **profit**, **profit margin**, and **return rates** across **regions, time periods, and product categories**. Built using **Tableau** for visualization and **Python** for data preparation, it showcases my ability to extract meaningful insights and present them in a clear, interactive, and business-focused manner.

### **Key Business Questions Addressed**
1. Which regions generate the most revenue and profit?
2. Which product categories drive success, and where are liabilities hiding?
3. How do trends in sales and profit evolve over time?
4. Where can we reduce inefficiencies, such as high return rates?

This dashboard combines **clarity over complexity** and ensures insights are just one click away.

---

## **Features**

### **Dynamic Interactivity**
- **Metric Selector**: Toggle between **Sales** and **Profit** dynamically across all visualizations.
- **Filters**: Drill down into specific **regions**, **date ranges**, and **categories** for a tailored analysis.

### **Key Visualizations**
1. **KPIs**: A high-level snapshot of Sales, Profit, Profit Margin, and Return Rates.
2. **Geographic Insights**: Map and bar chart to explore state and regional performance.
3. **Trends Over Time**: A line chart to uncover seasonal patterns and temporal changes.
4. **Product Performance**: A heatmap showcasing category and sub-category performance.
5. **Operational Efficiency**: A bar chart highlighting return rates by category with drill-down capabilities.

### **Dashboard in Action**
Explore the interactive dashboard on Tableau Public:  
[👉 **Retail Performance Dashboard**](https://public.tableau.com/app/profile/mikey.neang/viz/retail-superstore-analysis/Dashboard)



---

## **Key Insights**

### **1. Regional Performance**
- **West Region** dominates in sales and profit, while the **South Region** underperforms.
- State-level insights show California as the top performer.

### **2. Product Categories**
- **Office Supplies** maintain steady revenue but suffer from the highest return rates (~1.6%).
- **Storage Products** are driving disproportionate returns within Office Supplies.

### **3. Temporal Trends**
- Sales and profit peak in **Q4**, highlighting strong seasonality.

---

## **Recommendations**

1. **Double Down on High-Performing Regions**:
   - Invest in marketing and operations in the West and East regions to capitalize on success.
2. **Reduce Return Rates**:
   - Investigate product quality or customer expectations in high-return categories, especially Storage.
3. **Leverage Seasonality**:
   - Plan promotions and inventory for **Q4** to maximize profit during peak demand.

---

## **Data Model and Technology**

### **Technology Stack**
- **Tableau**: For interactive visualizations and dashboards.
- **Python**: For data cleaning and preparation.

### **Data Sources**
1. **Orders**: Sales, profit, and customer details.
2. **Returns**: Return rates by product category and region.
3. **People**: Customer segmentation information.

### **Entity-Relationship Diagram (ERD)**
The data preparation process is built on a relational model, flattened into a single table for efficiency in Tableau.  
![retail-superstore-analysis](https://github.com/user-attachments/assets/5f781eef-8fea-48da-949b-60c66d4e0714)




## **Data Preparation: Using the Python Script**

The `clean_data.py` script prepares the dataset by merging, cleaning, and transforming raw data into a format optimized for Tableau.

### **Prerequisites**
- Python 3.7+ installed on your system.
- Required libraries: listed in the `requirements.txt` file.

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-url
   cd your-repo-directory
   ```
   
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

### **Running the Script**
1. Place the raw data files (`orders.csv`, `returns.csv`, `people.csv`) in the same directory as `clean_data.py`.
  
2. Run the script using the following command:
   ```bash
   python clean_data.py
   ```
   
3. The cleaned dataset (`cleaned_data.csv`) will be generated in the same directory, ready for use in Tableau.

4. Verify the output:
   - Open the `cleaned_data.csv` file to ensure the structure matches the expected columns and values.
   - Confirm that merged fields (e.g., `return_rate`, `profit_margin`) are correctly calculated.

5. Use the cleaned data:
   - Import `cleaned_data.csv` into Tableau to build or update the dashboard.

---

## **How to Use the Dashboard**

1. **Metric Selector**:
   - Switch dynamically between **Sales** and **Profit** across all visualizations using the dropdown filter.
2. **Filters**:
   - Narrow insights by applying filters for **Region** or **Date Range** to focus on specific areas or time periods.
3. **Interactivity**:
   - Click on map areas, bar chart regions, or category heatmap sections to drill deeper into the details and see relationships between data points.

---

## **Caveats and Assumptions**

- The dataset covers **2014–2017** and may not reflect current retail trends or behaviors.
- **Return rates** are based on unit counts and not weighted by sales revenue.
- **Profit margin** excludes operational overhead and external costs beyond direct sales and returns.

---

## **Files in Repository**

1. `clean_data.py`:
   - A Python script for merging, cleaning, and preparing the raw datasets for analysis.
2. `cleaned_data.csv`:
   - The final processed data file used in Tableau for building the dashboard.
3. `requirements.txt`:
   - A list of Python libraries required to run the `clean_data.py` script.
4. `Retail Performance Dashboard.twbx`:
   - The Tableau packaged workbook containing all visualizations and interactivity.
5. Screenshots and GIFs:
   - Visual media showing dashboard components and filter interactivity.

---

## **Closing Statement**

This project reflects my **passion** for data analytics and storytelling. By transforming raw data into actionable insights, I demonstrate the ability to solve real-world business problems while inspiring others to see the power of data. Each aspect of this dashboard was thoughtfully designed to answer critical questions with clarity and precision.

I look forward to bringing the same enthusiasm, dedication, and expertise to your team.

# **Supply Chain Optimization: Optimizing Supplier Lead Times and Inventory Management**

---

## **1. Background**

Efficient supply chain management is critical to ensuring smooth operations and minimizing delays. This project aims to analyze and optimize supplier performance and inventory management for better decision-making. By analyzing supplier lead times and current inventory levels, this project identifies key areas for improvement, which will help businesses avoid stockouts and improve supplier reliability.

---

## **2. Technology Architecture Overview**

- **Tools**: Python (pandas, matplotlib), Jupyter Notebook, GitHub.
- **Workflow**: Data cleaning, analysis, and visualization to identify key supply chain inefficiencies.

---

## **3. Executive Summary**

- **Problem**: 
  Supplier delays and low inventory levels can disrupt the entire supply chain, leading to production delays or stockouts. Identifying suppliers with long lead times and products that are nearing their reorder points can help businesses take preemptive actions to optimize supply chain performance.

- **Key Insights**:
  1. **Supplier B and Supplier E** have lead times significantly above the acceptable threshold, increasing the risk of delayed deliveries.
  2. **Supplier D's inventory** is dangerously close to its reorder point, signaling a potential stockout if immediate restocking actions are not taken.

- **Actionable Recommendations**:
  - **Supplier Performance**: Initiate discussions with Supplier B and Supplier E to either improve lead times or seek alternative suppliers.
  - **Inventory Management**: Implement automated reorder triggers for Supplier D to prevent future stockouts and improve inventory efficiency.

---

## **4. Key Insights and Recommendations**

- **Supplier Lead Times**: Supplier B and Supplier E have lead times exceeding 10 days, increasing the risk of delivery delays.  
   **Recommendation**: Collaborate with procurement teams to address performance issues or consider renegotiating contracts with these suppliers.

- **Inventory Levels**: Supplier D’s inventory is nearing the reorder point, indicating a need for immediate restocking to prevent stockouts.  
   **Recommendation**: Implement automated reorder triggers to prevent stockouts in the future.

**Visualizations**:
- Supplier Lead Times Chart:
  
  ![supplierleadtimes](https://github.com/user-attachments/assets/19b41e0e-d0dc-421e-825a-0054576d6768)

- Inventory Levels vs. Reorder Points Chart:

  ![reorder_point_chart](https://github.com/user-attachments/assets/7f63709d-5a47-460f-acd0-77f094a8fd2a)

---

## **5. Caveats and Assumptions**

1. **Dataset**: The analysis is based on a mock dataset, which assumes consistent supplier performance over time. Real-world supplier performance may vary due to market conditions, demand fluctuations, or logistical issues.
   
2. **Thresholds**: Lead times above 10 days were considered "long" for the purpose of this analysis, but industry-specific thresholds may differ based on product type or market needs.
   
3. **Data Availability**: This analysis is based on the data available, but additional data (e.g., cost data, supplier reliability history) could improve the recommendations.

---

## **6. How to Run This Project**

To reproduce this analysis, follow these steps:

1. **Clone this repository**:
   ```bash
   git clone https://github.com/mneang/supply-chain-optimization.git
   cd supply-chain-optimization
   
2. **Install dependencies**: Make sure you have Python installed, then run:

   ```bash
   pip install -r requirements.txt

3. **Run the Jupyter Notebook**: Open the Jupyter Notebook file and follow the step-by-step analysis:

   ```bash
   jupyter notebook Optimizing_Supplier_Lead_Times_and_Inventory_Management.ipynb

---

## 7. Conclusion

This project highlights the importance of monitoring supplier performance and inventory management to avoid delays and stockouts in the supply chain. By using data analysis and visualization tools, businesses can proactively address potential risks and maintain smooth operations. 

The analysis demonstrates how data-driven decisions, such as improving lead times or setting automated reorder points, can drive operational improvements. This project serves as an example of how analytics can be applied to supply chain challenges to generate meaningful business insights.

# ✅ PROJECT-08

In this project, a complete data engineering solution was developed on the Azure platform, focusing on Olympic data analysis. The goal was to demonstrate how best practices and tools can be applied to transform large volumes of information into strategic insights. The process covers everything from **data ingestion and storage**, using scalable services like **Azure Data Lake**, to **transformation and modeling**, employing **Azure Databricks** to ensure quality and efficiency.  

Additionally, **orchestration and automation** techniques are implemented, ensuring continuous updates in the data flow, as well as **security** measures such as access control and encryption to protect the information. The project's final outcome consists of data analysis through **Azure Synapse Analytics**, where SQL queries are used to explore and interpret the data, extracting relevant insights about Olympic sports.  

This project serves as a practical and structured guide for professionals interested in developing complete data engineering solutions on **Azure**, covering everything from extraction to advanced data analysis, with a focus on scalability, efficiency, and security.

![archtecture_project_14](https://github.com/user-attachments/assets/d4390eff-dde7-4d51-84f9-154b9006010e)

Keywords: Olympic Gamges, Data Analysis, Data Engineering, ETL/ELT, Azure, Data Lake, Databricks, Synapse Analytics, SQL, Pyspark.


# ✅ PROCESS

The project began with the **ingestion of raw data** from a GitHub repository, using **Azure Data Factory** to develop a **structured ETL pipeline** with two layers: **"raw_data"**, where data was stored without modifications, and **"transformed_data"**, which contains processed and analysis-ready data. Storage was handled using **Azure Data Lake Storage Gen2**, ensuring scalability and security. 

<img width="1187" alt="Screenshot 2025-03-13 at 11 27 25" src="https://github.com/user-attachments/assets/a70484c6-782f-4a26-a541-c9330a476e7b" />

The **data transformation and cleaning** process was conducted in **Azure Databricks**, where corrections were applied to standardize and optimize the datasets. The **"Athletes"** and **"Coaches"** tables had their names formatted to a consistent standard, while the **"Teams"** dataset underwent adjustments, including the **removal of the "TeamName" column**, which contained redundant data compared to the **"Country"** column. The **"Gender"** and **"Medals"** datasets required no modifications, as they were already consistent.

With the data properly structured, **Azure Synapse Analytics** was used to perform **exploratory SQL queries**, enabling an in-depth analysis of the transformed data. This process allowed the identification of **patterns and strategic insights** into Olympic sports, providing detailed information on athlete distribution, country performance, and the relationships between teams and medal achievements.

# ✅ CONCLUSION

The statistical analysis in **Azure Synapse Analytics** revealed significant patterns in athlete participation, coach distribution, and the relationship between teams and medals. The **0.89 correlation** between athletes and coaches indicates that countries with large delegations tend to have more coaches, although this relationship varies depending on investment and logistics. Additionally, some countries demonstrated high technical efficiency, winning more medals with fewer coaches.  

The relationship between teams and medals showed a **0.88 correlation**, confirming that countries investing in team sports increase their chances of success. One country with **48 teams** won **58 medals**, whereas a country without teams earned only **3 medals** in individual sports, highlighting the impact of collective participation.  

The gender analysis showed a balanced participation, with **5,432 women (48%)** and **5,884 men (52%)**. Some sports, such as **3x3 Basketball and Archery**, exhibit perfect gender equity, while others, like **Artistic Swimming**, are exclusively female, demonstrating the need for more inclusive policies.

![Screenshot 2025-02-12 at 21 03 20](https://github.com/user-attachments/assets/bfdcce22-64cf-4d96-8e15-9034ec29dd5f)

The **0.69 correlation** between coaches and medals indicates that while a higher number of coaches is associated with better performance, other factors such as sports infrastructure and individual talent are equally important. One country with **35 coaches won 58 medals**, whereas another, with no registered coaches, earned **2 medals**, reinforcing that specialization can compensate for a lower number of trainers.  

This project demonstrated how **data engineering on Azure** can provide valuable insights for sports, aiding in strategic decision-making and improving delegation performance. In addition to tabular analysis, Synapse enabled graphical visualization of the data, facilitating interpretation. Although the entire process could have been conducted exclusively in **Synapse Analytics**, the goal was to integrate different **Azure Cloud** frameworks, showcasing a complete and scalable **ETL pipeline**.


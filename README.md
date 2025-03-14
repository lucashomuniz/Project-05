# ✅ PROJECT-08

In this project, a complete data engineering solution was developed on the Azure platform, focusing on Olympic data analysis. The goal was to demonstrate how best practices and tools can be applied to transform large volumes of information into strategic insights. The process covers everything from **data ingestion and storage**, using scalable services like **Azure Data Lake**, to **transformation and modeling**, employing **Azure Databricks** to ensure quality and efficiency.  

Additionally, **orchestration and automation** techniques are implemented, ensuring continuous updates in the data flow, as well as **security** measures such as access control and encryption to protect the information. The project's final outcome consists of data analysis through **Azure Synapse Analytics**, where SQL queries are used to explore and interpret the data, extracting relevant insights about Olympic sports.  

This project serves as a practical and structured guide for professionals interested in developing complete data engineering solutions on **Azure**, covering everything from extraction to advanced data analysis, with a focus on scalability, efficiency, and security.

![archtecture_project_14](https://github.com/user-attachments/assets/d4390eff-dde7-4d51-84f9-154b9006010e)

Keywords: Olympic Gamges, Data Analysis, Data Engineering, ETL/ELT, Azure, Data Lake, Databricks, Synapse Analytics, SQL, Pyspark.


# ✅ PROCESS

The project began with the **ingestion of raw data** from a GitHub repository, using **Azure Data Factory** to develop a **structured ETL pipeline** with two layers: **"raw_data"**, where data was stored without modifications, and **"transformed_data"**, which contains processed and analysis-ready data. Storage was handled using **Azure Data Lake Storage Gen2**, ensuring scalability and security. 

![Screen Recording 2025-03-13 at 21 02 59](https://github.com/user-attachments/assets/09595f9f-a731-4d4d-91dd-b16d5206a90c)

The **data transformation and cleaning** process was conducted in **Azure Databricks**, where corrections were applied to standardize and optimize the datasets. The **"Athletes"** and **"Coaches"** tables had their names formatted to a consistent standard, while the **"Teams"** dataset underwent adjustments, including the **removal of the "TeamName" column**, which contained redundant data compared to the **"Country"** column. The **"Gender"** and **"Medals"** datasets required no modifications, as they were already consistent. Com isso as tabelas transformadas foram salvas via linguagem **PySpark** no **Databricks**, em uma pasta do **Azure Data Lake Storage Gen2** chamada **"transformed_data"**, completando o ciclo entre raw data e transformeed data.

![Screen Recording 2025-03-13 at 21 07 01](https://github.com/user-attachments/assets/4ba1fbb2-af94-4c98-8dd0-335c41a3d591)

With the data properly structured, **Azure Synapse Analytics** was used to perform **exploratory SQL queries**, enabling an in-depth analysis of the transformed data. This process allowed the identification of **patterns and strategic insights** into Olympic sports, providing detailed information on athlete distribution, country performance, and the relationships between teams and medal achievements.

![Screen Recording 2025-03-14 at 15 08 07](https://github.com/user-attachments/assets/d963a113-4821-4b7d-9a1d-4fa3fc6d3c53)

# ✅ CONCLUSION

The statistical analysis in **Azure Synapse Analytics** revealed significant patterns in athlete participation, coach distribution, and the relationship between medals, atlhetes, teams, coaches and gender. At first, the gender analysis showed a balanced participation, with **5,432 women (48%)** and **5,884 men (52%)**. Some sports, such as **3x3 Basketball and Archery**, exhibit perfect gender equity, while others, like **Artistic Swimming**, are exclusively female, demonstrating the need for more inclusive policies.

This project demonstrated how **data engineering on Azure** can provide valuable insights for sports, aiding in strategic decision-making and improving delegation performance. In addition to tabular analysis, Synapse enabled graphical visualization of the data, facilitating interpretation. Although the entire process could have been conducted exclusively in **Synapse Analytics**, the goal was to integrate different **Azure Cloud** frameworks, showcasing a complete and scalable **ETL pipeline**.


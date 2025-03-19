# ✅ PROJECT-05

In this project, a complete data engineering solution was developed on the Azure platform, focusing on Olympic data analysis. The goal was to demonstrate how best practices and tools can be applied to transform large volumes of information into strategic insights. The process covers everything from **data ingestion and storage**, using scalable services like **Azure Data Lake**, to **transformation and modeling**, employing **Azure Databricks** to ensure quality and efficiency.  

Additionally, **orchestration and automation** techniques are implemented, ensuring continuous updates in the data flow, as well as **security** measures such as access control and encryption to protect the information. The project's final outcome consists of data analysis through **Azure Synapse Analytics**, where SQL queries are used to explore and interpret the data, extracting relevant insights about Olympic sports.  

This project serves as a practical and structured guide for professionals interested in developing complete data engineering solutions on **Azure**, covering everything from extraction to advanced data analysis, with a focus on scalability, efficiency, and security.

![412657060-d4390eff-dde7-4d51-84f9-154b9006010e](https://github.com/user-attachments/assets/ec749b9a-de75-4942-ac7c-eeeb6c9c5d75)

Keywords: Olympic Gamges, Data Analysis, Data Engineering, ETL/ELT, Azure, Data Lake, Databricks, Synapse Analytics, SQL, Pyspark.

# ✅ PROCESS

The project began with the **ingestion of raw data** from a GitHub repository, using **Azure Data Factory** to develop a **structured ETL pipeline** with two layers: **"raw_data"**, where data was stored without modifications, and **"transformed_data"**, which contains processed and analysis-ready data. Storage was handled using **Azure Data Lake Storage Gen2**, ensuring scalability and security. 

![Screen Recording 2025-03-13 at 21 02 59](https://github.com/user-attachments/assets/09595f9f-a731-4d4d-91dd-b16d5206a90c)

The **data transformation and cleaning** process was conducted in **Azure Databricks**, where corrections were applied to standardize and optimize the datasets. The **"Athletes"** and **"Coaches"** tables had their names formatted to a consistent standard, while the **"Teams"** dataset underwent adjustments, including the **removal of the "TeamName" column**, which contained redundant data compared to the **"Country"** column. The **"Gender"** and **"Medals"** datasets required no modifications, as they were already consistent. Com isso as tabelas transformadas foram salvas via linguagem **PySpark** no **Databricks**, em uma pasta do **Azure Data Lake Storage Gen2** chamada **"transformed_data"**, completando o ciclo entre raw data e transformeed data.

![Screen Recording 2025-03-13 at 21 07 01](https://github.com/user-attachments/assets/4ba1fbb2-af94-4c98-8dd0-335c41a3d591)

With the data properly structured, **Azure Synapse Analytics** was used to perform **exploratory SQL queries**, enabling a deep analysis of the transformed dataset. This process revealed **patterns and strategic insights** into Olympic sports, including athlete distribution, country performance, and the relationships between teams, coaches, and medal achievements. By leveraging **SQL-based analytics**, it was possible to uncover trends such as the correlation between delegation size and medal count, variations in gender representation across sports, and the potential impact of coaching staff on performance.  

Beyond validating existing assumptions about Olympic success factors, the analysis also highlighted **new hypotheses** for further exploration, such as the influence of sports infrastructure and investment on medal counts. The scalability and performance of **Synapse Analytics** allowed for rapid data exploration, ensuring that insights were both actionable and valuable for guiding strategic decisions in sports management and policy-making.

![Screen Recording 2025-03-14 at 15 08 07](https://github.com/user-attachments/assets/d963a113-4821-4b7d-9a1d-4fa3fc6d3c53)

# ✅ CONCLUSION

The Descriptive Analytics in **Azure Synapse Analytics** revealed significant patterns in athlete participation, coach distribution, and the relationship between medals, atlhetes, teams, coaches and gender. At first, the gender analysis showed a balanced participation, with **5,432 women (48%)** and **5,884 men (52%)**. Some sports, such as **3x3 Basketball and Archery**, exhibit perfect gender equity, while others, like **Artistic Swimming**, are exclusively female, demonstrating the need for more inclusive policies.

In the frist analysis, the chart bellow illustrates the relationship between the number of athletes sent by the 15 countries with the largest Olympic delegations and the total medals each country earned. In general, larger delegations tend to win more medals, although notable exceptions exist. For instance, China, despite having fewer athletes compared to some other nations, achieved a higher medal count. This demonstrates clearly that the number of athletes alone is not the only determining factor for Olympic success. Other factors such as technical quality, sports infrastructure, and investments in training are also crucial. To further validate this relationship, detailed statistical tests would be required. Nonetheless, this initial analysis already highlights the significant role played by the combination of athlete quantity and technical quality in achieving success at major international competitions.

![Screen Recording 2025-03-16 at 11 27 32](https://github.com/user-attachments/assets/4141c361-f377-45f6-b6c4-328de391fe3f)

The chart presented highlights the relationship between the number of sports disciplines contested and the total medals earned by the top 15 participating countries at the Olympic Games. It is observed that the number of disciplines contested among these leading countries is relatively similar, with minor variations. However, despite this similarity, there is considerable variation in the total medals achieved, indicating that the number of disciplines alone does not determine a country's sporting success. This observation suggests a potentially low correlation between the number of disciplines contested and total medal count among the top countries analyzed. Nevertheless, to statistically confirm this relationship, further analyses such as correlation coefficients and hypothesis testing would be required. Such tests could clarify the significance of other factors, like investment in sports infrastructure, training quality, and technical preparation, that may strongly influence overall team performance.

![Screen Recording 2025-03-16 at 11 46 09](https://github.com/user-attachments/assets/d1005acf-8058-4d6c-987d-63b70f1ee177)

The third analysis, which examines the 15 countries with the highest number of coaches, reveals a seemingly weak relationship between the number of coaches and the total medals won by each country. For example, South Africa and ROC both have approximately 12 coaches, yet ROC achieved a remarkable 71 medals, while South Africa secured only 3. Similarly, Spain has nearly as many coaches as the United States but obtained significantly fewer medals. These examples clearly indicate that, although there may be a general trend linking more coaches to higher medal counts, this relationship is weak. Additional factors, such as the quality of training, sports infrastructure, and investment levels, likely play a more decisive role in Olympic success. To statistically confirm the strength and validity of this relationship, more rigorous tests, such as correlation coefficients or hypothesis testing, would be necessary.

![Screen Recording 2025-03-16 at 11 59 06](https://github.com/user-attachments/assets/828e3282-a3ff-450a-8200-d6f72abab1e9)

This project demonstrated how **data engineering on Azure** can provide valuable insights for sports, aiding in strategic decision-making and improving delegation performance. In addition to tabular analysis, Synapse enabled graphical visualization of the data, facilitating interpretation. Although the entire process could have been conducted exclusively in **Synapse Analytics**, the goal was to integrate different **Azure Cloud** frameworks, showcasing a complete and scalable **ETL pipeline**.


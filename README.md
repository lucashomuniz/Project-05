# ✅ PROJECT-05

In this project, we perform a comprehensive **analysis** of **socioeconomic** data to gain deeper insights into the **business environment**. We investigate regional, city-level, and national differences, assessing how various **indicators** influence **customer purchasing decisions** and how shifts in the **scenario** may affect **corporate strategies**. Leveraging **exploratory analysis** on real, **publicly available** data, we address **data cleaning** challenges to ensure high-quality outcomes and adopt a strategy of reorganizing data perspectives for more meaningful insights. Finally, we answer five **business** questions through relevant **graphs** and **statistics**. Before addressing these questions, we must understand what each **dataset variable** represents. We then load the data, identify issues, **clean** and **transform** it, and conclude by providing answers through **graphs** and **statistics**.
 
Keywords: R Language, Data Analysis, Statistics, dplyr, ggplot2, Data Munging, Data Exploration, Analysis Socioeconomic, Data Driven Culture, Business Problems.

# ✅ PROCESS

**Correlation** analysis measures the strength and direction of a **linear** relationship between two **variables**. A relationship is **linear** if its **scatterplot** shows a straight-line pattern. When the slope rises, it indicates a **positive** relationship; when it declines, it indicates a **negative** relationship. **Correlations** can be **perfect**, **moderate**, **weak**, or **unrelated**. Importantly, **correlation**—the link between two **events**—does not imply a **causal relationship**. While **correlation** may provide clues for potential causes or areas worth further exploration, concluding **causation** from **correlation** alone is a **logical fallacy**. Naturally, any true **causal relationship** must exhibit **correlation**, but one should not automatically assume **causation** without rigorous validation.

It is essential to conduct further **investigation** when different **scenarios** arise in a **correlation** study. In one scenario, **variable x** may genuinely **cause** **variable y**. Conversely, **variable y** could be the **cause** of **variable x**. Another possibility is that a third **variable** exerts **influence** on both **variable x** and **variable y**, or there may be a **combination** of these factors at play. Additionally, the **correlation** might simply be a **coincidence**, indicating that two **events** occur simultaneously without any direct **causal** connection. In **scientific** contexts, employing a **large sample** can mitigate the likelihood of such coincidental findings and strengthen the validity of any **conclusions**.

# ✅ CONCLUSION

> Question 1: Does the increase in per capita GDP of a country positively affect the life expectancy of citizens at birth? What is the correlation between these two variables?

As **Gross Domestic Product (GDP) per capita** increases, a concurrent rise in **life expectancy** is often observed. In many cases, countries with higher **GDP per capita** also exhibit higher **life expectancy**. However, this **relationship** does not imply direct **causality**, as more in-depth **mathematical** and **statistical** analyses are necessary to confirm a cause-and-effect link. According to the **cor.test** function, there is an approximate +85% correlation, indicating a **strong positive correlation** between these variables. This information clarifies the overall association between **GDP per capita** and **life expectancy**, while recognizing that additional factors may influence this **complex** interaction.

![image](https://github.com/lucashomuniz/Project-7/assets/123151332/1d458130-0c84-4e14-83e5-38aa79523ad4)

> Question 2: Is there a correlation between the scale of life and the general public's awareness of corruption in business and government? What is the correlation between these two variables?

There is a trend suggesting that, as **quality of life** increases, **corruption** levels tend to decrease. This phenomenon is often seen in countries with greater **economic prosperity**, potentially influenced by factors like a more **educated** population, higher **purchasing power**, and broader **access to information**. It is essential to note that this association does not imply a direct **causal relationship**, as deeper analysis is required to establish causality. Still, a **cor.test** yields a correlation of approximately **-46%**, indicating a **moderate negative correlation**. This suggests that higher **quality of life** generally aligns with lower **corruption** levels, although various **contextual** and **country-specific** factors may also shape these outcomes.

![image](https://github.com/lucashomuniz/Project-7/assets/123151332/1a158fcc-a6b8-4a53-a911-a6a1a965ebd6)

> Question 3: Does increasing the scale of life have an effect on average happiness among the general public? What is the correlation between the two variables?

As **quality of life** improves, a positive effect on **emotions** and **happiness** is observed. There is a significant **correlation** between rising **quality of life** and the prevalence of more **positive emotions**. This relationship can be attributed to various factors, such as satisfaction with important life aspects, access to resources and opportunities, and the **emotional stability** afforded by favorable living conditions. However, it is crucial to note that this association does not establish a direct **causal relationship**, as other influences can affect an individual’s **emotions** and **happiness**. Using the **cor.test** function, the observed **correlation** is approximately **57%**, indicating a **moderate positive correlation**. In general, as **quality of life** increases, there is a tendency for **positive emotions** and **happiness** to rise. Nonetheless, it is important to recognize that **happiness** is multifaceted and shaped by numerous **individual** and **contextual** factors.

![image](https://github.com/lucashomuniz/Project-7/assets/123151332/fff9c54e-76e5-43f5-9fc2-8b191ad086a3)

> Question 4: Does the country with the lowest social support index have the highest perception of corruption in relation to companies and the country's government?

There is an apparent **association** between the **lowest level of social support** in a country and a heightened **perception of corruption**. Here, **social support** refers to **government** measures aimed at assisting the population. When **social support** is low, the **government** presumably invests fewer **public policies** to help its citizens. A **corruption** indicator reached **84%**, suggesting that individuals receive limited **assistance** and may suspect active **government corruption**. However, it is important to note the challenge of **analysis** for this particular country due to **limited data**. The generated **graph** reveals few **data points**, making it difficult to draw robust conclusions about the **relationship** between these **data** and the country in question.

When performing a **correlation** coefficient analysis, a value of **-49%** is observed, indicating a **moderate negative correlation**. This suggests a potential link between **low social support** and the perception of **high corruption**, though it is essential to consider other **variables** and **contextual** factors that may influence this **relationship**. In summary, the preliminary analysis indicates a possible association between **reduced government assistance** and **high corruption** perception, but further **in-depth** studies and consideration of additional **socioeconomic** and **political** factors are required for a more comprehensive understanding.

![image](https://github.com/lucashomuniz/Project-7/assets/123151332/13ccf588-9eb5-41f3-9ef8-21057204d661)

# ✅ SOURCE

https://data.world/laurel/world-happiness-report-data![image](https://github.com/lucashomuniz/Project-7/assets/123151332/d514791b-82c5-43da-ae45-a373462c07a8)

# ✅ PROJECT-14

Nesse projeto, foi desenvolvida uma solução completa de engenharia de dados na plataforma Azure, com foco na análise de dados olímpicos. O objetivo foi demonstrar como as melhores práticas e ferramentas podem ser aplicadas para transformar grandes volumes de informações em insights estratégicos. O processo abrange desde a **ingestão e armazenamento dos dados**, utilizando serviços escaláveis como o **Azure Data Lake**, até a **transformação e modelagem**, empregando o **Azure Databricks** para garantir qualidade e eficiência.  

Além disso, são implementadas técnicas de **orquestração e automação**, assegurando atualizações contínuas no fluxo de dados, bem como medidas de **segurança**, como controle de acesso e criptografia, garantindo a proteção das informações. O resultado final do projeto consiste na análise dos dados por meio do **Azure Synapse Analytics**, onde consultas SQL são utilizadas para explorar e interpretar os dados, extraindo insights relevantes sobre os esportes olímpicos.  

Esse projeto se estabelece como um guia prático e estruturado para profissionais interessados em desenvolver soluções completas de engenharia de dados no **Azure**, abordando desde a extração até a análise avançada dos dados, com foco em escalabilidade, eficiência e segurança.

Keywords: Olympic Gamges, Data Analysis, Data Engineering, ETL/ELT, Azure, Data Lake, Databricks, Synapse Analytics, SQL, Pyspark.

![archtecture_project_14](https://github.com/user-attachments/assets/d4390eff-dde7-4d51-84f9-154b9006010e)

# ✅ PROCESS

O projeto iniciou com a **ingestão de dados brutos** de um repositório no GitHub, utilizando o **Azure Data Factory** para desenvolver um **pipeline de ETL** estruturado em duas camadas: **"raw_data"**, onde os dados foram armazenados sem modificações, e **"transformed_data"**, que contém os dados processados e prontos para análise. O armazenamento foi realizado no **Azure Data Lake Storage Gen2**, garantindo escalabilidade e segurança.  

A **transformação e limpeza dos dados** foi conduzida no **Azure Databricks**, onde foram aplicadas correções para padronizar e otimizar as bases. As tabelas **"Athletes"** e **"Coaches"** tiveram seus nomes formatados para um padrão único, enquanto a base **"Teams"** passou por ajustes, incluindo a **remoção da coluna "TeamName"**, que apresentava dados redundantes em relação à coluna **"Country"**. As bases **"Gender"** e **"Medals"** não necessitaram modificações, pois estavam consistentes.  

![Screenshot 2025-02-12 at 20 57 54](https://github.com/user-attachments/assets/4f80067f-a02b-46e3-b0d0-9356d63abaca)

Com os dados devidamente estruturados, o **Azure Synapse Analytics** foi utilizado para realizar **consultas SQL exploratórias**, permitindo a análise aprofundada dos dados transformados. Esse processo possibilitou a identificação de **padrões e insights estratégicos** sobre os esportes olímpicos, fornecendo informações detalhadas sobre a distribuição de atletas, desempenho por país e relações entre equipes e conquistas de medalhas.

# ✅ CONCLUSION

A análise estatística no **Azure Synapse Analytics** revelou padrões significativos na participação de atletas, distribuição de técnicos e relação entre equipes e medalhas. A correlação de **0.89** entre atletas e técnicos indica que países com grandes delegações tendem a ter mais treinadores, embora essa relação varie conforme investimentos e logística. Além disso, alguns países demonstraram alta eficiência técnica, conquistando mais medalhas com menos treinadores.  

A relação entre equipes e medalhas apresentou uma correlação de **0.88**, confirmando que países que investem em esportes coletivos ampliam suas chances de sucesso. O país com **48 equipes** conquistou **58 medalhas**, enquanto um país sem equipes obteve apenas **3 medalhas** em esportes individuais, evidenciando o impacto da participação coletiva.  

A análise de gênero mostrou uma participação equilibrada, com **5.432 mulheres (48%)** e **5.884 homens (52%)**. Algumas modalidades, como **3x3 Basketball e Tiro com Arco**, apresentam equidade perfeita, enquanto outras, como **Natação Artística**, são exclusivamente femininas, demonstrando a necessidade de políticas mais inclusivas.  

A correlação de **0.69** entre técnicos e medalhas indica que, embora um maior número de treinadores esteja associado a melhores desempenhos, outros fatores, como infraestrutura esportiva e talento individual, são igualmente importantes. Um país com **35 técnicos conquistou 58 medalhas**, enquanto outro, sem técnicos registrados, obteve **2 medalhas**, reforçando que a especialização pode compensar a menor quantidade de treinadores.  

O projeto demonstrou como a **engenharia de dados no Azure** pode fornecer insights valiosos para o esporte, auxiliando na tomada de decisões estratégicas e no aprimoramento do desempenho das delegações. Além da análise tabular, o Synapse permitiu a visualização gráfica dos dados, facilitando sua interpretação. Embora todo o processo pudesse ter sido realizado exclusivamente no **Synapse Analytics**, a proposta foi integrar diferentes frameworks do **Azure Cloud**, demonstrando um pipeline de ETL completo e escalável.



# PARAMETERS 1

from pyspark.sql.functions import col
from pyspark.sql.types import IntegerType, DoubleType, BooleanType, DateType

#################################################################################

# PARAMETERS 2

# Unmount the directory if it is already mounted
dbutils.fs.unmount("/mnt/project14")

# Define the configurations
configs = {
    "fs.azure.account.auth.type": "OAuth",
    "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
    "fs.azure.account.oauth2.client.id": "?",
    "fs.azure.account.oauth2.client.secret": '?',
    "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/?/oauth2/token"
}

# Mount the directory
dbutils.fs.mount(
    source="abfss://?@?.dfs.core.windows.net", 
    mount_point="/mnt/project14",
    extra_configs=configs
)

#################################################################################

#%fs
#ls "/mnt/project14"

#################################################################################

# PARAMETERS 3

athletes = spark.read.format("csv").option("header","true").option("inferSchema","true").load("dbfs:/mnt/project14/raw_data/athletes.csv")
coaches = spark.read.format("csv").option("header","true").option("inferSchema","true").load("dbfs:/mnt/project14/raw_data/coaches.csv")
gender = spark.read.format("csv").option("header","true").option("inferSchema","true").load("dbfs:/mnt/project14/raw_data/gender.csv")
medals = spark.read.format("csv").option("header","true").option("inferSchema","true").load("dbfs:/mnt/project14/raw_data/medals.csv")
teams = spark.read.format("csv").option("header","true").option("inferSchema","true").load("dbfs:/mnt/project14/raw_data/teams.csv")

#################################################################################

# TRANSFORMATION ATHLETES

from pyspark.sql.functions import col, split, concat_ws, initcap, expr

# Separar os nomes em uma array
athletes_transformed = athletes.withColumn("name_parts", split(col("PersonName"), " "))

# Concatenar corretamente o nome no formato "ÚltimoNome, PrimeiroNome1 PrimeiroNome2..."
athletes_transformed = athletes_transformed.withColumn("PersonName",
expr("concat_ws(', ', name_parts[size(name_parts)-1], array_join(slice(name_parts, 1, size(name_parts)-1), ' '))"))

# Aplicar Title Case (Primeira letra maiúscula, restante minúscula)
athletes_transformed = athletes_transformed.withColumn("PersonName", initcap(col("PersonName")))

# Remover a coluna auxiliar "name_parts"
athletes_transformed = athletes_transformed.drop("name_parts")

# Convert Spark DataFrame to Pandas DataFrame
athletes_transformed = athletes_transformed.toPandas()

# Salvar dataframe no Data Lake Gen 2
athletes_transformed.to_csv("/dbfs/mnt/project14/trans_data/athletes.csv", index=False)

# Mostrar o dataframe
display(athletes_transformed)

#################################################################################

# TRANSFORMATION COACHES

from pyspark.sql.functions import col, split, concat_ws, initcap, expr

# Separar os nomes em uma array
coaches_transformed = coaches.withColumn("name_parts", split(col("Name"), " "))

# Concatenar corretamente o nome no formato "ÚltimoNome, PrimeiroNome1 PrimeiroNome2..."
coaches_transformed = coaches_transformed.withColumn("Name",
expr("concat_ws(', ', name_parts[size(name_parts)-1], array_join(slice(name_parts, 1, size(name_parts)-1), ' '))"))

# Aplicar Title Case (Primeira letra maiúscula, restante minúscula)
coaches_transformed = coaches_transformed.withColumn("Name", initcap(col("Name")))

# Remover a coluna auxiliar "name_parts"
coaches_transformed = coaches_transformed.drop("name_parts")

# Convert Spark DataFrame to Pandas DataFrame
coaches_transformed = coaches_transformed.toPandas()

# Salvar dataframe no Data Lake Gen 2
coaches_transformed.to_csv("/dbfs/mnt/project14/trans_data/coaches.csv", index=False)

# Mostrar o dataframe
display(coaches_transformed)

#################################################################################

# TRANSFORMATION GENDER

from pyspark.sql.functions import col, rank, expr
from pyspark.sql.window import Window

# Convert Spark DataFrame to Pandas DataFrame
gender_transformed = gender.toPandas()

# Salvar dataframe no Data Lake Gen 2
gender_transformed.to_csv("/dbfs/mnt/project14/trans_data/gender.csv", index=False)

# Mostrar o dataframe
display(gender_transformed)

#################################################################################

# TRANSFORMATION TEAMS

# Remover a coluna "TeamName"
teams_transformed = teams.drop("TeamName")

# Convert Spark DataFrame to Pandas DataFrame
teams_transformed = teams_transformed.toPandas()

# Salvar dataframe no Data Lake Gen 2
teams_transformed.to_csv("/dbfs/mnt/project14/trans_data/teams.csv", index=False)

# Mostrar o dataframe
display(teams_transformed)

#################################################################################

# TRANSFORMATION MEDALS

from pyspark.sql.window import Window
from pyspark.sql.functions import col, rank

# Convert Spark DataFrame to Pandas DataFrame
medals_transformed = medals.toPandas()

# Salvar dataframe no Data Lake Gen 2
medals_transformed.to_csv("/dbfs/mnt/project14/trans_data/medals.csv", index=False)

# Mostrar o dataframe
display(medals_transformed)



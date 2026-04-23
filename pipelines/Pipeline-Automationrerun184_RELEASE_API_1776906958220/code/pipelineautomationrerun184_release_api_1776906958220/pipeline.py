from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipelineautomationrerun184_release_api_1776906958220.config.ConfigStore import *
from pipelineautomationrerun184_release_api_1776906958220.functions import *
from prophecy.utils import *
from pipelineautomationrerun184_release_api_1776906958220.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Project_Automationrerun184_python_RELEASE_API_1776906958220_dataSet = Project_Automationrerun184_python_RELEASE_API_1776906958220_dataSet(
        spark
    )
    df_select_customer_details = select_customer_details(
        spark, 
        df_Project_Automationrerun184_python_RELEASE_API_1776906958220_dataSet
    )

def main():
    spark = SparkSession.builder\
                .enableHiveSupport()\
                .appName("Pipeline-Automationrerun184_RELEASE_API_1776906958220")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Pipeline-Automationrerun184_RELEASE_API_1776906958220")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(
        spark = spark,
        pipelineId = "pipelines/Pipeline-Automationrerun184_RELEASE_API_1776906958220",
        config = Config
    )(
        pipeline
    )

if __name__ == "__main__":
    main()

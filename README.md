# Data-Engineering---ETL-Data-Pipelines-with-Bash-and-Airflow

#### ETL (extration, transform and loading) process enable organizations to leverage the power of their data to provide information, intelligence and actionable insights into the organization's processes.
ETL data pipelines allows for the curation of data from multiple sources, transform the data into some other formats or structure and then use the transformed data for other other downstream applications. The data can also be loaded onto a repository for some other purpose. With ETL, organizations can easily track and govern their entire data transformation and application processes. 

Apache AIrflow is an ETL platform that can be programmatically used to set up pipelines or workflows for data ETL applications. This tutorial highlights how to set up ETL data pipelines using Airflow and Bash (BashOperator). The tutorial completely solves the final ETL assessment segment in the Coursera's IBM Data Pipeline with Shell, Airflow and Kafka (https://www.coursera.org/learn/etl-and-data-pipelines-shell-airflow-kafka/home/module/1) course

## PROJECT OVERVIEW
You are to play the role of a data engineer at a data analytics consulting company. You have been assigned a project to decongest the national highways by analyzing the road traffic data from different toll plazas. Each highway is operated by a different toll operator with a different IT setups. The IT setups uses different file formats. 

You are to curate the data from their different respective formats and store it in a single file. You are also required to develop an Apache Airflow DAG (Direct Acyclic Graph) that will do the following:
    - Extract data from a csv file
    - Extract data from a tsv file
    - Extract data from a fixed-width file
    - Transform the data
    - Load the transformed data into the staging area

You can download the data using curl or wget from: .....


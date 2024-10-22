# Data-Engineering---ETL-Data-Pipelines-with-Bash-and-Airflow

#### ETL (extration, transform and loading) process enable organizations to leverage the power of their data to provide information, intelligence and actionable insights into the organization's processes.
ETL data pipelines allows for the curation of data from multiple sources, transform the data into some other formats or structure and then use the transformed data for other other downstream applications. The data can also be loaded onto a repository for some other purpose. With ETL, organizations can easily track and govern their entire data transformation and application processes. 

Apache AIrflow is an ETL platform that can be programmatically used to set up pipelines or workflows for data ETL applications. This tutorial highlights how to set up ETL data pipelines using Airflow and Bash (BashOperator). The tutorial completely solves the final ETL assessment segment in the Coursera's IBM Data Pipeline with Shell, Airflow and Kafka (https://www.coursera.org/learn/etl-and-data-pipelines-shell-airflow-kafka/home/module/1) course.

## PROJECT OVERVIEW
You are to play the role of a data engineer at a data analytics consulting company. You have been assigned a project to decongest the national highways by analyzing the road traffic data from different toll plazas. Each highway is operated by a different toll operator with a different IT setups. The IT setups uses different file formats. 

You are to curate the data from their different respective formats and store it in a single file. You are also required to develop an Apache Airflow DAG (Direct Acyclic Graph) that will do the following:
* Extract data from a csv file
* Extract data from a tsv file
* Extract data from a fixed-width file
* Transform the data
* Load the transformed data into the staging area

## Apache Airflow Installation

Detailed information regarding Apache Airflow installation on Ubuntu, CentOS or WSL on Windows could be found here: https://github.com/apache/airflow . However, a concise summary regarding the installation of Airflow is provided below.

To install Apache Airflow:

* $ pip install apache-airflow  (use pip3 if pip did not work)

Then, initialize the Airflow backend:

* $ airflow db init

Start the web server on port 6060 or any other desired port:

* $ airflow webserver -p 6060

  Start the Airflow scheduler:

* $ airflow scheduler

The Airflow web server can now be accessed at: http://localhost:6060

## Project Setup and Procedure
To complete the ETL project, first set up the Airflow home from your command line. Use the following command:

* $ export AIRFLOW_HOME= /home/project/airflow

Create a directory structure for the project's data staging area
* $ sudo mkdir -p /home/project/airflow/dags/staging

Grant read, write and execute permission to users in the project's directory:

* $ sudo chmod -R 777 /home/project/airflow/dags/staging

Use curl or wget to download the project data: 

* $ wget -P /home/project/airflow/dags https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz

In case the IBM link for the project no longer works, the data (tolldata.tgz) has been downloaded and included as part of this tutorial repository. 

From the command line, create the 'ETL_toll_data.py'

* $ touch ETL_toll_data.py

To edit and add the tutorial code, open the 'ETL_toll_data.py' using nano:

* $ nano ETL_toll_data.py

## See the project's repository for the complete tutorial code in 'ETL_toll_data.py'

You can also see snapshots of each of the ETL tasks taken from the CLI. 

### Define DAG arguments

![dag_args](https://github.com/user-attachments/assets/9d445c72-cb83-4a32-abf8-161d9d0fce39)

### Define the DAG

![dag_definition](https://github.com/user-attachments/assets/ce331cb2-37a0-44d9-b999-04242e907c4a)

### Unzip the project's data

![unzip_data](https://github.com/user-attachments/assets/e68fbe34-cc81-4e62-99a5-fbfac1cc588f)

### Create a task to extract data from CSV file

![extract_data_from_csv](https://github.com/user-attachments/assets/55747261-3e62-491f-afec-bc449a1d7b45)

### Create a task to extract data from TSV file

![extract_data_from_tsv](https://github.com/user-attachments/assets/fdb75a3c-549c-4133-9674-0dfe30d7ca70)

### Create a task to extract data from fixed width file

![extract_data_from_fixed_width](https://github.com/user-attachments/assets/c5345c18-adf6-4931-a234-107df9633bd7)

### Create a task to consolidate data

![consolidate_data](https://github.com/user-attachments/assets/f612d27f-7758-476d-a3ac-66bcdeee5917)

### Create a task to transform the data

![transform](https://github.com/user-attachments/assets/88c2dd1b-b73b-4e1c-b36d-1da8517a76fa)

### Create a task to define the Airflow task pipeline

![task_pipeline](https://github.com/user-attachments/assets/04519770-d588-4c50-9063-3fdeb4908d6e)

### To submit the DAG, it is sufficient to use the command: 'airflow dags trigger ETL_toll_data' as shown below:

![submit_dag](https://github.com/user-attachments/assets/97862774-24c9-4cf6-80ec-09ee2d39aafd)























#Import Libraries

from datetime import timedelta
# Import the DAG object. We will need this to instantiate a DAG
from airflow import DAG
# Import Operators. We will need this to write tasks. It could be either BashOperator or PythonOperator #depending on preference or need
from airflow.operators.bash_operator import BashOperator
# For scheduling the DAG runs
from airflow.utils.dates import days_ago
# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization



#Define DAG Arguments

# Here, default arguments such as your name, email, delay time before retries in case your any of your 
# DAGs fails; etc. 
default_args = {
    'owner ': 'your name',
    'start_date': days_ago(0),   # start today
    'email': ['your_email@email_domain.com'],
    'email_on_failure': True,
    'email_on_retry': True',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG

dag = DAG(
    #Name (ID) of the DAG
    'ETL_toll_data',      
     default_args=default_args,
     description='Apache Airflow Final ETL',
     schedule_interval=timedelta(days=1),
)


# Unzip data to a location ('datahouse' in this case)
# Use the 'tar -xvzf' argument (where -x: extract file from archive, -z: use gzip compression to extract the archive, -v: be verbose, display the progress and the file list, -f: specifies the input file (e.g., .tgz file) 
# Unzip the data into the staging file from the dags file. Altenatively, you can unzip it directly into the dags file 

unzip_data = BashOperator(
    task_id='unzip_data',
    bash_commands='tar -xvzf /home/project/airflow/dags/staging/tolldata.tgz -C /home/project/airflow/dags/',
    
    dag=dag,
)



# Create a task to extract data from CSV file

# The task is to extract the following columns: ‘Rowid’, ‘Timestamp’, ‘Anonymized Vehicle number’, ‘Number’, and ‘Vehicle Type’ from ‘vehicle-data.csv’ (part of the ‘tollgate.tgz’ dataset); and save them into ‘new_vehicle_data.csv’ file.

### Some background discussion regarding this task
# We can extract a specific column/field from a delimited text file, by mentioning the delimiter using the -d option, or the field number using the -f option.
# Suppose the /etc/passwd is a “:” delimited file, the command below will extract usernames (the first field) from /etc/passwd.

# cut -d":" -f1 /etc/passwd

#The command below will extract multiple fields 1st, 3rd, and 6th (username, userid, and home directory) #from /etc/passwd.

#cut -d":" -f1,3,6 /etc/passwd

# Task code
extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command='cut -d"," -f1-4 vehicle-data.csv > csv_data.csv',
    dag=dag,
)


# Extract data from tollplaza-data.tsv and load it onto tsv_data.csv
# An alternative bash command for this task is to use: "cut -f "Number of axles","Tollplaza id","Tollplaza code" /home/project/airflow/dags/tollplaza-data.tsv > /home/project/airflow/dags/tsv_data.csv"
extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command='tr "\t" "," < tollplaza-data.tsv | cut -d"," -f5,6,7 > tsv_data.csv',
    dag=dag,
)


# Extract fixed width data and save it onto another file.  

extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command='cut -c1-3,7-9 /home/project/airflow/dags/payment-data.txt > /home/project/airflow/dags/fixed_width_data.csv',
    dag=dag,
)


#Copy all data from csv_data.csv, tsv_data.csv, fixed_width_data.csv and paste into extracted_data.csv 
consolidate_data = BashOperator(
    task_id='consolidate_data',  
    bash_command='paste csv_data.csv tsv_data.csv fixed_width_data.csv > extracted_data.csv',
    dag=dag,
)


# Transform data in extracted_data.csv from lower case to upper case, and save it onto transformed_data.csv
transform_data = BashOperator(
    task_id='transform_data',  
    bash_command='tr  "[A-Z]" "[a-z]"  < extracted_data.csv > transformed_data.csv',
    dag=dag,
)


# Define the Airflow task pipeline
unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data
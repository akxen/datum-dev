"""Collect nemweb current report data"""

import os

import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import timedelta

from scripts.update_database import update_database


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": airflow.utils.dates.days_ago(1),
    "email": [os.environ['EMAIL']],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(seconds=30),
}

dag = DAG("reports", default_args=default_args,
          schedule_interval='1-59/5 * * * *', catchup=False)

t1 = BashOperator(
    task_id="download_data",
    bash_command="/usr/local/airflow/dags/scripts/download_data.sh ",
    dag=dag)

t2 = PythonOperator(
    task_id='update_dispatch_scada',
    python_callable=update_database,
    op_kwargs={'table': 'dispatch_scada'},
    dag=dag,
)

t3 = PythonOperator(
    task_id='update_dispatch_report_case_solution',
    python_callable=update_database,
    op_kwargs={'table': 'dispatch_report_case_solution'},
    dag=dag,
)

t4 = PythonOperator(
    task_id='update_dispatch_report_region_solution',
    python_callable=update_database,
    op_kwargs={'table': 'dispatch_report_region_solution'},
    dag=dag,
)

t5 = PythonOperator(
    task_id='update_dispatch_report_interconnector_solution',
    python_callable=update_database,
    op_kwargs={'table': 'dispatch_report_interconnector_solution'},
    dag=dag,
)

t6 = PythonOperator(
    task_id='update_dispatch_report_constraint_solution',
    python_callable=update_database,
    op_kwargs={'table': 'dispatch_report_constraint_solution'},
    dag=dag,
)

t7 = PythonOperator(
    task_id='update_p5_case_solution',
    python_callable=update_database,
    op_kwargs={'table': 'p5_case_solution'},
    dag=dag,
)

t8 = PythonOperator(
    task_id='update_p5_region_solution',
    python_callable=update_database,
    op_kwargs={'table': 'p5_region_solution'},
    dag=dag,
)

t9 = PythonOperator(
    task_id='update_p5_interconnector_solution',
    python_callable=update_database,
    op_kwargs={'table': 'p5_interconnector_solution'},
    dag=dag,
)

t10 = PythonOperator(
    task_id='update_p5_constraint_solution',
    python_callable=update_database,
    op_kwargs={'table': 'p5_constraint_solution'},
    dag=dag,
)

t1 >> [t2, t3, t4, t5, t6, t7, t8, t9, t10]

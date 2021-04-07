wget -r --no-parent -A html http://nemweb.com.au/Reports/CURRENT/Dispatch_SCADA/ -P /usr/local/airflow/data
wget -r --no-parent -nc http://nemweb.com.au/Reports/CURRENT/Dispatch_SCADA/ -P /usr/local/airflow/data

wget -r --no-parent -A html http://nemweb.com.au/Reports/CURRENT/Dispatch_Reports/ -P /usr/local/airflow/data
wget -r --no-parent -nc http://nemweb.com.au/Reports/CURRENT/Dispatch_Reports/ -P /usr/local/airflow/data

wget -r --no-parent -A html http://nemweb.com.au/Reports/CURRENT/P5_Reports/ -P /usr/local/airflow/data
wget -r --no-parent -nc http://nemweb.com.au/Reports/CURRENT/P5_Reports/ -P /usr/local/airflow/data
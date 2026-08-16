## simple math operation task we will perform
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator  



def start_number(**context):
    context["ti"].xcom_push(key="current_value",value=10)
    print("starting number is 10")

def add_num(**context):
    current_value=context["ti"].xcom_pull(key="current_value",task_ids="t1")
    new_value=current_value +5
    context["ti"].xcom_push(key="current_value",value=new_value)
    print(f"Add 5:{current_value}+5={new_value}")
    
def mul_num(**context):
    current_val=context["ti"].xcom_pull(key="current_value",task_ids="t2")
    new_val=current_val*2
    context["ti"].xcom_push(key="current_value",value=new_val)
    print(f"Mul 2:{current_val}*2={new_val}")
    
    
def sub_num(**context):
    current_val=context["ti"].xcom_pull(key="current_value",task_ids="t3")
    new_val=current_val - 3
    context["ti"].xcom_push(key="current_value",value=new_val)
    print(f"Sub 3:{current_val}-3={new_val}")
    
    
    
def square_num(**context):
    current_val=context["ti"].xcom_pull(key="current_value",task_ids="t4")
    new_val=current_val*current_val
    context["ti"].xcom_push(key="current_value",value=new_val)
    print(f"Square :{current_val}*{current_val}={new_val}")
    
    
    
with DAG(
    dag_id="maths_sequence_dag",
    start_date=datetime(2025, 4, 22), 
    schedule='@weekly',
    catchup=False
) as dag:
    
    start_task = PythonOperator(
        task_id="t1",
        python_callable=start_number
        # Removed provide_context line from here
    )
    
    add_five_task = PythonOperator(
        task_id="t2",
        python_callable=add_num
        # Removed provide_context line from here
    )
    
    mul_2_task = PythonOperator(
        task_id="t3",
        python_callable=mul_num
    )
    
    sub_3_task = PythonOperator(
        task_id="t4",
        python_callable=sub_num
    )
    
    square_num_task = PythonOperator(
        task_id="t5",
        python_callable=square_num
    )
    
    start_task >> add_five_task >> mul_2_task >> sub_3_task >> square_num_task

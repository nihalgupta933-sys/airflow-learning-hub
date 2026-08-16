
from datetime import datetime
from airflow import DAG
from airflow.decorators import  task 

with DAG(
    dag_id="maths_taskflow_sequence_dag",
    start_date=datetime(2025, 4, 22),
    schedule='@weekly',
    catchup=False
)as dag:


    @task
    def start_number():
        initial_value=10
        print(f"starting number is {initial_value}")
        return initial_value 

    @task
    def add_five(number):
        new_value = number + 5
        print(f"Add 5: {number} + 5 = {new_value}")
        return new_value

    @task
    def mul_num(number):
        new_val = number * 2
        print(f"Mul 2: {number} * 2 = {new_val}")
        return new_val

    @task
    def sub_num(number):
        new_val = number - 3
        print(f"Sub 3: {number} - 3 = {new_val}")
        return new_val

    @task
    def square_num(number):
        new_val = number * number
        print(f"Square: {number} * {number} = {new_val}")
        return new_val

    start_value=start_number()
    added_value=add_five(start_value)
    mul_value=mul_num(added_value)
    sub_value=sub_num(mul_value)
    square_value=square_num(sub_value)
    
    

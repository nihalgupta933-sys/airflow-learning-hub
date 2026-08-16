# My First Apache Airflow Project 🚀

Hi! Welcome to my repository. I am a beginner learning Data Engineering. This is my very first project where I built and orchestrated **3 simple data pipelines (DAGs)** using the **Astronomer CLI** and **Docker Desktop**.

*⚠️ **Note:** Due to local system upload constraints, some project configuration folders did not upload completely, but all core code and pipelines run perfectly as shown below!*

---

## 🛠️ Tech Stack Used
* **Orchestrator:** Apache Airflow
* **Environment Management:** Astronomer CLI (Astro)
* **Containerization:** Docker Desktop
* **Language:** Python

---

## 💡 My Core Pipelines (DAGs)

1. **`maths_sequence_dag`**
   - Built using traditional `PythonOperator` tasks.
   - Runs tasks in a simple linear sequence (`t1 >> t2 >> t3 >> t4`).
2. **`maths_taskflow_sequence_dag`**
   - Built using the modern `@task` decorator syntax (**TaskFlow API**).
   - Easily passes data outputs directly between functions.
3. **`ml_pipeline`**
   - Simulates a basic Machine Learning workflow.
   - Moves step-by-step: `preprocess_task` ➡️ `train_task` ➡️ `evaluate_task`.

---

## 📊 Project Execution Screenshots

Here is the visual proof that everything runs successfully in my local setup environment:

### 1. Starting the Project via Astro CLI
Running `astro dev start` in my VS Code terminal to spin up local containers.
![Astro Dev Start](./ss/Screenshot%202026-08-16%20202019.png)

### 2. Docker Desktop Containers Running
Showing my Airflow scheduler, webserver, database, and triggerer instances running smoothly.
![Docker Desktop Setup](./ss/Screenshot%202026-08-16%20202112.png)
)

### 3. Airflow Main Dashboard Overview
My main UI console tracking execution histories for all three custom DAG workflows.
![Airflow Dashboard](./ss/Screenshot%202026-08-16%20202112.png)

### 4. Traditional Sequence Dag Graph View
Looking at the execution status logs of my first task `t1` in the math pipeline.
![Maths Sequence DAG](./ss/Screenshot%202026-08-16%20204801.png)

### 5. Modern Taskflow Graph View
Tracking clean functional parameter pipelines (`start_number` ➡️ `add_five` ➡️ `mul_num` ➡️ `sub_num`).
![Taskflow Graph](./ss/Screenshot%202026-08-16%20204935.png)

### 6. Machine Learning Workflow Run Logs
Verifying data preprocessing stage logs inside my modular machine learning pipeline visualization graph.
![ML Pipeline Logs](./ss/Screenshot%202026-08-16%20202222.png)

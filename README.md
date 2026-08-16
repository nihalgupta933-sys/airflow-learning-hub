# My First Apache Airflow Project 🚀

Hi! Welcome to my repository. I am a beginner learning Data Engineering. This is my very first project where I built and orchestrated **3 simple data pipelines (DAGs)** using the **Astronomer CLI** and **Docker Desktop**.

*⚠️ **Note:** Due to local system upload constraints, some project configuration folders did not upload completely, but all core pipeline code runs perfectly as shown below.*

---

## 🛠️ Tech Stack Used
* **Orchestration Engine:** Apache Airflow
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
   - Passes data outputs seamlessly between functional tasks.
3. **`ml_pipeline`**
   - Simulates a basic Machine Learning lifecycle workflow.
   - Moves step-by-step: `preprocess_task` ➡️ `train_task` ➡️ `evaluate_task`.

---

## 📊 Project Execution Screenshots

Here is the exact visual proof of my application workflows running step-by-step in my local environment:

### 1. Project Initialization via Astro CLI
Running `astro dev start` in the terminal to compile local runtime dependencies.
![Astro Dev Start](./ss/Screenshot%202026-08-16%20202019.png)

### 2. Airflow Web Server Dashboard Overview
My main UI console view tracking the status and histories of all three custom pipelines.
![Airflow Dashboard](./ss/Screenshot%202026-08-16%20202112.png)

### 3. Docker Desktop Services Layout
Showing my background metadata database, webserver, and scheduler running smoothly.
![Docker Desktop Setup](./ss/Screenshot%202026-08-16%20204742.png)

### 4. Machine Learning Workflow Graph Views
Verifying successful step execution runs inside the simulated machine learning pipeline.
![ML Pipeline Logs](./ss/Screenshot%202026-08-16%20204801.png)

### 5. Traditional Sequence Graph Logs
Looking closely at execution log details for my sequential python operator tasks.
![Maths Sequence DAG](./ss/Screenshot%202026-08-16%20204903.png)

### 6. Modern Taskflow Graph Verification
Tracking clean parameter flows through the decorated task mapping graph engine.
![Taskflow Graph](./ss/Screenshot%202026-08-16%20204935.png)

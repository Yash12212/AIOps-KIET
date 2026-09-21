# 📋 AIOps Mid-Sem Exam — Ultimate Command Cheatsheet

Print/save this. Everything is grouped by tool, ordered by "most likely to need first."

---

## 1. GIT & GITHUB (your graded artifact — master this)

```bash
# --- Setup (once) ---
git config --global user.name "Your Name"
git config --global user.email "you@email.com"

# --- Start ---
git clone https://github.com/USER/REPO.git     # copy repo to machine
cd REPO
git init                                       # OR: start fresh repo in current folder
git remote add origin https://github.com/USER/REPO.git

# --- The daily loop (memorize these 4) ---
git status                                     # what changed?
git add .                                      # stage everything (or: git add file.py)
git commit -m "Checkpoint 1: description"      # save snapshot
git push                                       # send to GitHub

# --- Sync ---
git pull                                       # get latest from GitHub
git pull origin main
git pull origin main --allow-unrelated-histories   # FIX: push rejected because repo had README
git pull --rebase origin main                  # FIX: "fetch first / non-fast-forward"

# --- History & undo ---
git log --oneline                              # see commit list (checkpoint proof!)
git restore file.py                            # discard my changes to a file
git reset --soft HEAD~1                        # undo last commit, KEEP changes
git reset --hard HEAD~1                        # undo last commit, DELETE changes (careful)

# --- Branches & merge ---
git branch                                     # list branches
git branch feature-x                           # create branch
git switch feature-x                           # go to branch (or: git checkout feature-x)
git switch -c feature-x                        # create + go in one step
git merge feature-x                            # merge feature-x INTO current branch
git merge --abort                              # panic button: cancel a bad merge
git branch -d feature-x                        # delete branch after merge

# --- CONFLICT resolution (3 steps, no panic) ---
# 1. Open files with <<<<<<< markers, edit to keep correct code
git add .
git commit -m "Resolve merge conflict"

# --- Tags (optional checkpoint markers) ---
git tag checkpoint-1
git push --tags

# --- GitHub CLI (if installed) ---
gh auth status
gh pr create --fill                            # open pull request from terminal
gh pr merge                                    # merge it
```

**Web-UI equivalents:** New branch / Pull request / Merge button / Actions tab — all doable with mouse if CLI feels risky.

---

## 2. GITHUB CODESPACES & ACTIONS

```bash
# Codespaces = browser VS Code. Create: repo page → green "Code" → Codespaces tab → Create
Ctrl + `                    # open terminal inside Codespaces
Ctrl + Shift + V            # paste in terminal
# Ports tab → forward port (8080, 5000...) → make Public if needed
# Bottom-left / notification: "Sign in to GitHub" → DO IT (else Actions won't work)

# Actions: repo → Actions tab → see green/red runs → click → re-run if failed
gh run list
gh run view --log-failed
```

Minimal workflow file `.github/workflows/ci.yml`:
```yaml
name: CI
on: push
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.10' }
      - run: pip install -r requirements.txt
      - run: python q1_anomaly.py
```

---

## 3. KAFKA

```bash
# --- Start cluster (2 terminals, from kafka folder) ---
bin/zookeeper-server-start.sh config/zookeeper.properties      # terminal 1
bin/kafka-server-start.sh config/server.properties             # terminal 2

# --- Topics ---
bin/kafka-topics.sh --create --topic server_metrics \
    --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
bin/kafka-topics.sh --list --bootstrap-server localhost:9092
bin/kafka-topics.sh --describe --topic server_metrics --bootstrap-server localhost:9092

# --- Manual test (no Python needed) ---
bin/kafka-console-producer.sh --topic server_metrics --bootstrap-server localhost:9092
bin/kafka-console-consumer.sh --topic server_metrics --bootstrap-server localhost:9092 --from-beginning

# --- Stop ---
bin/kafka-server-stop.sh
bin/zookeeper-server-stop.sh
```

Docker shortcut (if Docker available instead of binaries):
```bash
docker run -d --name kafka -p 9092:9092 \
  -e KAFKA_CFG_NODE_ID=0 -e KAFKA_CFG_PROCESS_ROLES=controller,broker \
  -e KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093 \
  -e KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 \
  -e KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER \
  -e KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=0@localhost:9093 \
  bitnami/kafka:3.7
```

Python core lines (memorize shape):
```python
from kafka import KafkaProducer, KafkaConsumer
import json
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))
producer.send('server_metrics', {"server_id":"s1","cpu_usage":85})

consumer = KafkaConsumer('server_metrics', bootstrap_servers='localhost:9092',
                         auto_offset_reset='earliest',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))
for msg in consumer: print(msg.value)
```

---

## 4. AIRFLOW

```bash
pip install apache-airflow
export AIRFLOW_HOME=~/airflow

# --- Easiest: everything at once (prints admin password!) ---
airflow standalone            # UI at http://localhost:8080 (user: admin)

# --- OR manual ---
airflow db migrate            # init database (old versions: airflow db init)
airflow users create --username admin --password admin --firstname A \
    --lastname B --role Admin --email a@b.com
airflow webserver --port 8080   # terminal 1
airflow scheduler               # terminal 2

# --- Validate DAG without running server (exam lifesaver) ---
python dags/my_dag.py                                  # syntax check
airflow dags list                                      # is my DAG visible?
airflow dags show aiops_workflow                       # structure
airflow tasks list aiops_workflow                      # my 4 tasks?
airflow tasks test aiops_workflow collect_metrics 2023-01-01   # run ONE task
airflow dags trigger aiops_workflow                    # run whole DAG
airflow dags state aiops_workflow                      # success/failed?
```
DAG skeleton (memorize):
```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

with DAG('aiops_workflow', start_date=datetime(2023,1,1),
         schedule_interval=None, catchup=False) as dag:
    t1 = PythonOperator(task_id='collect_metrics', python_callable=collect_metrics)
    t2 = PythonOperator(task_id='process_metrics', python_callable=process_metrics)
    t1 >> t2
```

---

## 5. SPARK / PySpark

```bash
pip install pyspark
pyspark                                  # interactive shell
spark-submit job.py                      # run script
spark-submit --master "local[*]" job.py  # run using all local cores
```
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("aiops").getOrCreate()
df = spark.read.csv("data.csv", header=True, inferSchema=True)
df.show(5); df.printSchema(); df.count()
df.filter(df.cpu_usage > 80).show()
df.groupBy("server_id").avg("cpu_usage").show()
df.write.mode("overwrite").csv("output/")
spark.stop()
```

---

## 6. PYTHON ENV & PACKAGES

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
deactivate
pip install -r requirements.txt
pip install pandas matplotlib kafka-python pyspark apache-airflow mlflow
pip freeze > requirements.txt    # SAVE your deps (commit this!)
python script.py
```

---

## 7. MLflow & DVC (Unit 2 quick hits)

```bash
# MLflow
mlflow ui --port 5000            # view experiments
# python: mlflow.set_experiment("exp"); mlflow.log_param("k",v);
#         mlflow.log_metric("acc",0.9); mlflow.sklearn.log_model(model,"model")

# DVC
dvc init
dvc add data/raw/logs.csv        # tracks dataset
git add .dvc .gitignore data/raw/logs.csv.dvc
git commit -m "Checkpoint: version dataset with DVC"
```

---

## 8. AZURE CLI (Cloud Shell — reads only until deny lifted)

```bash
az login
az account show -o table
az group create --name rg-exam --location eastus
az group delete --name rg-exam --yes --no-wait
az provider register --namespace Microsoft.CloudShell
# Cloud Shell paste = Shift+Insert ; session is EPHEMERAL (nothing persists)
```

---

## 9. LINUX SURVIVAL (you'll use these constantly)

```bash
ls -la          cd folder        pwd             cat file.txt
head -5 f       tail -20 f       tail -f log     wc -l file
grep "ERROR" logs.txt            grep -c "ERROR" logs.txt
mkdir -p a/b    cp a b           mv a b          rm -rf folder
chmod +x run.sh                  ./run.sh
ps aux | grep python             kill -9 PID
curl http://localhost:8000/health                # test an API endpoint
echo $PATH      export X=1       clear           history
Ctrl+C stop program   Ctrl+L clear screen   Ctrl+Z suspend   bg resume
nohup python app.py &            # run in background, survives terminal close
```

---

## 10. DOCKER / K8s (low chance mid-sem, 60 seconds to know)

```bash
docker build -t mymodel .
docker run -p 8000:8000 mymodel
docker ps        docker images        docker logs <id>
kubectl apply -f deploy.yaml    kubectl get pods    kubectl logs <pod>
```

---

## 🎯 Exam-Day Order of Operations (tape this to your brain)

1. Read sheet → create **public** repo → commit #1 (structure).
2. Open Codespaces → **sign in to GitHub** → venv + `pip install -r requirements.txt`.
3. Azure steps → Cloud Shell (Bash, "No storage account required").
4. Code one checkpoint → **test it** → `git add` → `git commit -m "Checkpoint N: ..."` → `git push`. Repeat.
5. Save outputs/graphs as files (`plt.savefig('graph.png')`) and **commit them** — graders see evidence without running code.
6. Something broken? Screenshot error, note assumption in README, commit, move on.
7. End: README with checkpoint table → verify repo public → submit link.

Good luck Monday — you've rehearsed more of this than most of your class already. 🍀
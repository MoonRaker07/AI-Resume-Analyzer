import pandas as pd

skills = {

    "Programming": [
        "Python","Java","C","C++","C#","Go","Rust","Scala",
        "Kotlin","Swift","R","MATLAB","Julia","PHP","Ruby",
        "Perl","Dart","TypeScript","JavaScript","Shell","Bash",
        "PowerShell","Objective-C","VB.NET"
    ],

    "Frontend": [
        "HTML","CSS","JavaScript","React","Angular","Vue",
        "Next.js","Bootstrap","Tailwind CSS","Redux",
        "jQuery","SASS"
    ],

    "Backend": [
        "Node.js","Express","Django","Flask","FastAPI",
        "Spring","Spring Boot","Laravel","ASP.NET",
        "REST API","GraphQL","gRPC","JWT","OAuth",
        "Microservices"
    ],

    "AI/ML": [
        "Machine Learning","Deep Learning","Artificial Intelligence",
        "TensorFlow","PyTorch","Scikit-learn","Keras",
        "OpenCV","NLTK","spaCy","Transformers",
        "Hugging Face","LangChain","LlamaIndex",
        "LLM","RAG","Computer Vision","NLP",
        "GAN","CNN","RNN","LSTM","BERT","GPT",
        "XGBoost","LightGBM","CatBoost",
        "Reinforcement Learning","Feature Engineering",
        "Model Deployment","MLOps"
    ],

    "Data Science": [
        "Pandas","NumPy","SciPy","Matplotlib","Seaborn",
        "Plotly","Power BI","Tableau","Excel",
        "Statistics","Data Analysis","Data Mining",
        "Data Visualization","EDA","A/B Testing",
        "Regression","Classification","Clustering",
        "Forecasting","Time Series"
    ],

    "Database": [
        "MySQL","PostgreSQL","MongoDB","Redis","SQLite",
        "Oracle","Cassandra","Neo4j","Firebase",
        "DynamoDB","Redshift","Snowflake"
    ],

    "Cloud": [
        "AWS","Azure","GCP","Docker","Kubernetes",
        "Terraform","Jenkins","GitHub Actions",
        "CloudFormation","Linux","Nginx","Apache"
    ],

    "Big Data": [
        "Hadoop","Spark","Kafka","Hive","Airflow",
        "Apache Beam","Flink","Databricks","ETL"
    ],

    "DevOps": [
        "Git","GitHub","GitLab","CI/CD",
        "Ansible","Helm","Prometheus","Grafana"
    ],

    "Mobile": [
        "Android","iOS","Flutter",
        "React Native","Xamarin"
    ],

    "Cybersecurity": [
        "Wireshark","Burp Suite","Metasploit",
        "Nmap","OWASP","Kali Linux",
        "Penetration Testing"
    ],

    "Tools": [
        "VS Code","Jupyter Notebook","PyCharm",
        "Postman","Figma","Canva"
    ]
}

rows = []

for category, skill_list in skills.items():
    for skill in skill_list:
        rows.append([category, skill])

df = pd.DataFrame(rows, columns=["Category", "Skill"])

df.to_csv("data/skills.csv", index=False)

print(df.head())
print(f"\nTotal Skills: {len(df)}")
print("\nskills.csv generated successfully!")
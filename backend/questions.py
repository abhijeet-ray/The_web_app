import random

class InterviewQuestionProvider:
    def __init__(self):
        # Define profiles and levels 
        self.profiles = ['DevOps', 'Software Engineer', 'Data Scientist']
        self.levels = ['Entry', 'Mid', 'Senior']  # Changed 'Experienced' to 'Senior'
        self.LEVEL_QUESTIONS = {'Entry': 10, 'Mid': 15, 'Senior': 20}  # Updated key
        self.NUM_SETS = 3
        
        # Initialize question sets for all profiles and levels 
        self.question_sets = {}
        self._initialize_question_sets()

    def _initialize_question_sets(self):
        """Initialize question sets with real interview questions for each profile and level."""
        # DevOps Questions 
        devops_questions = {
            'Entry': {
                1: [
                    "What is DevOps and how does it benefit software development?",
                    "Explain the difference between Continuous Integration and Continuous Deployment.",
                    "What is a Docker container and how does it work?",
                    "How do you check the status of a service in Linux?",
                    "What is the purpose of a version control system like Git?",
                    "What is Infrastructure as Code (IaC)?",
                    "How would you restart a service using systemd?",
                    "What does the command 'chmod 755 file.txt' do?",
                    "What is a pipeline in the context of CI/CD?",
                    "How do you list all running processes in Linux?"
                ],
                2: [
                    "What is the role of a DevOps engineer?",
                    "What is the difference between a virtual machine and a container?",
                    "How do you pull a specific branch from a Git repository?",
                    "What is the purpose of a load balancer?",
                    "Explain what a Dockerfile is used for.",
                    "How do you view the last 10 lines of a log file in Linux?",
                    "What is the difference between 'git fetch' and 'git pull'?",
                    "What is a configuration management tool?",
                    "How would you check disk space usage on a Linux server?",
                    "What is the purpose of SSH in DevOps?"
                ],
                3: [
                    "Why is automation important in DevOps?",
                    "What is the difference between Docker and Kubernetes?",
                    "How do you create a new branch in Git?",
                    "What is a reverse proxy and how does it work?",
                    "What does the 'ps' command do in Linux?",
                    "What is a Jenkins pipeline?",
                    "How do you clone a Git repository?",
                    "What is the purpose of monitoring in DevOps?",
                    "How do you find the IP address of a Linux machine?",
                    "What is a shell script and why is it useful?"
                ]
            },
            'Mid': {
                1: [
                    "Explain how you would set up a CI/CD pipeline using Jenkins.",
                    "What are the key components of Kubernetes architecture?",
                    "How do you handle secrets management in a DevOps environment?",
                    "What is the difference between blue-green deployment and canary deployment?",
                    "How do you monitor container performance in Docker?",
                    "What is Ansible and how does it differ from Puppet?",
                    "How would you automate server provisioning using Terraform?",
                    "What is the purpose of a service mesh like Istio?",
                    "How do you troubleshoot a failed deployment?",
                    "What is the difference between 'docker stop' and 'docker kill'?",
                    "How do you scale an application horizontally?",
                    "What is log aggregation and why is it important?",
                    "How do you secure a Docker container?",
                    "What is the role of a reverse proxy in a microservices architecture?",
                    "How do you check network connectivity between two servers?"
                ],
                2: [
                    "How do you implement high availability in a DevOps setup?",
                    "What are the benefits of using Helm with Kubernetes?",
                    "How do you manage Docker images in a registry?",
                    "What is the difference between a StatefulSet and a Deployment in Kubernetes?",
                    "How would you set up monitoring using Prometheus and Grafana?",
                    "What is the purpose of a GitOps workflow?",
                    "How do you handle rollbacks in a CI/CD pipeline?",
                    "What is a sidecar pattern in microservices?",
                    "How do you optimize a Dockerfile for faster builds?",
                    "What is the difference between orchestration and automation?",
                    "How do you use AWS CloudFormation for IaC?",
                    "What is Chaos Engineering and why is it useful?",
                    "How do you debug a Kubernetes pod that keeps crashing?",
                    "What is the purpose of a load balancer health check?",
                    "How do you ensure idempotency in Ansible playbooks?"
                ],
                3: [
                    "How do you configure a multi-stage build in Docker?",
                    "What is the difference between Kubernetes namespaces and contexts?",
                    "How do you implement auto-scaling in AWS?",
                    "What are the advantages of using a container orchestration tool?",
                    "How do you manage dependencies in a CI/CD pipeline?",
                    "What is the role of a proxy server in DevOps?",
                    "How do you use Terraform modules effectively?",
                    "What is the difference between a pod and a node in Kubernetes?",
                    "How do you handle version drift in IaC?",
                    "What is a Kubernetes ingress controller?",
                    "How do you set up a zero-downtime deployment?",
                    "What is the purpose of a liveness probe in Kubernetes?",
                    "How do you analyze logs using ELK stack?",
                    "What is network policy in Kubernetes?",
                    "How do you secure SSH access to a production server?"
                ]
            },
            'Senior': {
                1: [
                    "Design a CI/CD pipeline for a microservices architecture.",
                    "How do you implement disaster recovery in a Kubernetes cluster?",
                    "What are the trade-offs of using serverless vs. containerized deployments?",
                    "How do you optimize Kubernetes resource limits and requests?",
                    "Explain how to set up a multi-region deployment in AWS.",
                    "What is the role of service discovery in microservices?",
                    "How do you handle stateful applications in Kubernetes?",
                    "What are the best practices for securing a CI/CD pipeline?",
                    "How do you implement a GitOps strategy with ArgoCD?",
                    "What is the difference between eventual consistency and strong consistency?",
                    "How do you troubleshoot network latency in a distributed system?",
                    "What are the challenges of managing hybrid cloud infrastructure?",
                    "How do you use canary releases with Istio?",
                    "What is the purpose of a chaos monkey in resilience testing?",
                    "How do you migrate a monolithic application to microservices?",
                    "What is the role of an API gateway in DevOps?",
                    "How do you ensure compliance with security standards in IaC?",
                    "What is the difference between horizontal and vertical pod autoscaling?",
                    "How do you manage secrets across multiple cloud providers?",
                    "What are the key metrics to monitor in a production Kubernetes cluster?"
                ],
                2: [
                    "How do you architect a zero-trust security model in DevOps?",
                    "What are the considerations for running stateful workloads in Kubernetes?",
                    "How do you implement blue-green deployments at scale?",
                    "What is the role of observability in a DevOps culture?",
                    "How do you optimize Terraform state management in large teams?",
                    "What are the challenges of multi-cloud deployments?",
                    "How do you use AWS EKS for managing containerized applications?",
                    "What is the difference between a service mesh and an API gateway?",
                    "How do you handle database migrations in a CI/CD pipeline?",
                    "What is the impact of container orchestration on application performance?",
                    "How do you design a fault-tolerant system using AWS services?",
                    "What are the best practices for managing Kubernetes RBAC?",
                    "How do you implement a disaster recovery plan for a hybrid cloud?",
                    "What is the role of tracing in microservices debugging?",
                    "How do you automate compliance checks in a DevOps pipeline?",
                    "What are the trade-offs of using Helm charts vs. raw YAML?",
                    "How do you manage resource contention in a Kubernetes cluster?",
                    "What is the purpose of a readiness probe in Kubernetes?",
                    "How do you optimize CI/CD pipeline execution time?",
                    "What are the security implications of using public Docker images?"
                ],
                3: [
                    "How do you design a highly available CI/CD system across regions?",
                    "What are the challenges of managing secrets in a serverless architecture?",
                    "How do you implement a multi-tenant Kubernetes cluster?",
                    "What is the role of a service mesh in traffic management?",
                    "How do you optimize AWS costs in a DevOps environment?",
                    "What are the best practices for managing Kubernetes upgrades?",
                    "How do you use Spinnaker for advanced deployment strategies?",
                    "What is the difference between a circuit breaker and a retry policy?",
                    "How do you handle data consistency in distributed systems?",
                    "What are the benefits of using a service catalog in DevOps?",
                    "How do you implement auto-scaling for a stateful application?",
                    "What is the role of a DevOps engineer in incident response?",
                    "How do you use Terraform to manage multi-environment deployments?",
                    "What are the challenges of monitoring serverless applications?",
                    "How do you design a rollback strategy for a failed Kubernetes deployment?",
                    "What is the impact of network policies on cluster security?",
                    "How do you integrate security scanning into a CI/CD pipeline?",
                    "What are the trade-offs of using managed vs. self-hosted Kubernetes?",
                    "How do you ensure data integrity during a cloud migration?",
                    "What is the role of chaos engineering in production readiness?"
                ]
            }
        }

        # Software Engineer Questions 
        software_engineer_questions = {
            'Entry': {
                1: [
                    "What is the difference between a class and an object?",
                    "Explain what a REST API is.",
                    "How do you reverse a string in Python?",
                    "What is the purpose of unit testing?",
                    "What does 'public static void main' mean in Java?",
                    "How do you handle exceptions in Python?",
                    "What is the difference between '==' and '===' in JavaScript?",
                    "What is a primary key in a database?",
                    "How do you declare a variable in C++?",
                    "What is the purpose of a constructor in a class?"
                ],
                2: [
                    "What is object-oriented programming (OOP)?",
                    "How do you make an HTTP GET request in Python?",
                    "What is the difference between a list and a tuple in Python?",
                    "What is version control and why is it important?",
                    "How do you write a basic SQL SELECT query?",
                    "What is a loop and how does it work?",
                    "What does 'this' keyword refer to in Java?",
                    "How do you comment code in Python?",
                    "What is the difference between stack and heap memory?",
                    "What is an array and how do you access its elements?"
                ],
                3: [
                    "What is polymorphism in programming?",
                    "How do you debug a simple program?",
                    "What is the difference between GET and POST HTTP methods?",
                    "What is a function and how do you define one in Python?",
                    "What is the purpose of a database index?",
                    "How do you sort an array in Java?",
                    "What is encapsulation in OOP?",
                    "How do you handle null values in a program?",
                    "What is a boolean data type?",
                    "What is the difference between a while loop and a for loop?"
                ]
            },
            'Mid': {
                1: [
                    "How do you implement a binary search algorithm?",
                    "What is the difference between monolithic and microservices architecture?",
                    "How do you optimize a SQL query?",
                    "What is dependency injection and how does it work?",
                    "How do you implement multithreading in Java?",
                    "What is the difference between REST and GraphQL?",
                    "How do you handle race conditions in programming?",
                    "What is a design pattern? Give an example.",
                    "How do you secure an API endpoint?",
                    "What is the difference between a shallow copy and a deep copy?",
                    "How do you use Git to resolve merge conflicts?",
                    "What is the purpose of a middleware in a web application?",
                    "How do you implement a queue using two stacks?",
                    "What is the difference between a process and a thread?",
                    "How do you test an API using Postman?"
                ],
                2: [
                    "How do you design a URL shortening service?",
                    "What is the difference between synchronous and asynchronous programming?",
                    "How do you implement a singleton pattern?",
                    "What are the SOLID principles in software design?",
                    "How do you use Docker to containerize an application?",
                    "What is the difference between a hash table and a binary tree?",
                    "How do you handle database transactions?",
                    "What is a lambda function in Python?",
                    "How do you implement caching in a web application?",
                    "What is the difference between Agile and Waterfall methodologies?",
                    "How do you write a recursive function?",
                    "What is the purpose of an ORM like Hibernate?",
                    "How do you profile a Python application for performance?",
                    "What is the difference between TCP and UDP?",
                    "How do you implement a factory pattern?"
                ],
                3: [
                    "How do you design a rate limiter for an API?",
                    "What is event-driven architecture?",
                    "How do you use regular expressions in Python?",
                    "What is the difference between a linked list and an array?",
                    "How do you implement authentication in a REST API?",
                    "What is the purpose of a load balancer in software systems?",
                    "How do you optimize a web application for scalability?",
                    "What is a closure in JavaScript?",
                    "How do you handle memory leaks in a program?",
                    "What is the difference between composition and inheritance?",
                    "How do you use Jenkins for automated testing?",
                    "What is a microservice and how do you deploy one?",
                    "How do you implement a trie data structure?",
                    "What is the purpose of a reverse proxy?",
                    "How do you ensure code quality in a team project?"
                ]
            },
            'Senior': {
                1: [
                    "Design a distributed caching system like Redis.",
                    "How do you handle distributed transactions across microservices?",
                    "What are the challenges of scaling a monolithic application?",
                    "How do you implement a message queue system?",
                    "What is the CAP theorem and how does it apply to databases?",
                    "How do you optimize a system for low latency?",
                    "What are the best practices for API versioning?",
                    "How do you design a fault-tolerant distributed system?",
                    "What is the difference between ACID and BASE properties?",
                    "How do you implement a circuit breaker pattern?",
                    "What are the trade-offs of using NoSQL vs. SQL databases?",
                    "How do you handle concurrent modifications in a database?",
                    "What is the role of a software architect?",
                    "How do you use Kubernetes to deploy a microservices app?",
                    "What is a saga pattern in microservices?",
                    "How do you optimize garbage collection in Java?",
                    "What are the security considerations for a REST API?",
                    "How do you design a system for real-time data processing?",
                    "What is the difference between horizontal and vertical scaling?",
                    "How do you ensure high availability in a software system?"
                ],
                2: [
                    "How do you design a load balancer from scratch?",
                    "What are the challenges of implementing a microservices architecture?",
                    "How do you handle eventual consistency in distributed systems?",
                    "What is the role of observability in software engineering?",
                    "How do you implement a pub/sub system?",
                    "What are the best practices for writing scalable code?",
                    "How do you use AWS Lambda for serverless computing?",
                    "What is the difference between a service mesh and a traditional proxy?",
                    "How do you optimize database indexing for performance?",
                    "What is a distributed lock and how do you implement it?",
                    "How do you design a system for handling millions of requests per second?",
                    "What are the trade-offs of using a message broker like RabbitMQ?",
                    "How do you implement a retry mechanism for failed API calls?",
                    "What is the purpose of a Bloom filter?",
                    "How do you handle schema evolution in a database?",
                    "What are the challenges of debugging distributed systems?",
                    "How do you use GraphQL subscriptions for real-time updates?",
                    "What is the role of chaos engineering in software reliability?",
                    "How do you ensure data integrity in a microservices architecture?",
                    "What are the best practices for managing technical debt?"
                ],
                3: [
                    "How do you design a recommendation system like Netflix?",
                    "What are the considerations for running software in a multi-cloud environment?",
                    "How do you implement a distributed file system?",
                    "What is the role of a service registry in microservices?",
                    "How do you optimize a system for high throughput?",
                    "What are the best practices for managing API gateways?",
                    "How do you use Apache Kafka for event streaming?",
                    "What is the difference between a thread pool and a process pool?",
                    "How do you handle backpressure in a data pipeline?",
                    "What are the benefits of using a hexagonal architecture?",
                    "How do you design a system for GDPR compliance?",
                    "What is the role of a software engineer in incident response?",
                    "How do you implement a content delivery network (CDN)?",
                    "What are the challenges of migrating a legacy system to the cloud?",
                    "How do you use tracing to debug a microservices app?",
                    "What is the impact of network latency on system performance?",
                    "How do you integrate security into the SDLC?",
                    "What are the trade-offs of using a managed database service?",
                    "How do you ensure zero-downtime deployments?",
                    "What is the role of A/B testing in software development?"
                ]
            }
        }

        # Data Science Questions 
        data_scientist_questions = {
            'Entry': {
                1: [
                    "What is the difference between supervised and unsupervised learning?",
                    "How do you calculate the mean of a dataset in Python?",
                    "What is a confusion matrix?",
                    "What is overfitting in machine learning?",
                    "How do you load a CSV file using Pandas?",
                    "What is the purpose of a train-test split?",
                    "What is a p-value in statistics?",
                    "How do you plot a line graph using Matplotlib?",
                    "What is the difference between classification and regression?",
                    "What is a feature in the context of machine learning?"
                ],
                2: [
                    "What is a decision tree and how does it work?",
                    "How do you handle missing values in a dataset?",
                    "What is the purpose of normalization in data preprocessing?",
                    "What is a random forest algorithm?",
                    "How do you compute the standard deviation in Python?",
                    "What is the difference between a bar chart and a histogram?",
                    "What is a correlation coefficient?",
                    "How do you perform a simple linear regression in Python?",
                    "What is the role of a loss function in machine learning?",
                    "What is data cleaning and why is it important?"
                ],
                3: [
                    "What is a k-nearest neighbors (KNN) algorithm?",
                    "How do you select features for a machine learning model?",
                    "What is the difference between precision and recall?",
                    "What is a support vector machine (SVM)?",
                    "How do you create a scatter plot in Python?",
                    "What is the purpose of cross-validation?",
                    "What is a Type I error in statistics?",
                    "How do you encode categorical variables?",
                    "What is the difference between a population and a sample?",
                    "What is exploratory data analysis (EDA)?"
                ]
            },
            'Mid': {
                1: [
                    "How do you implement a logistic regression model in Python?",
                    "What is the difference between bagging and boosting?",
                    "How do you evaluate a clustering algorithm?",
                    "What is principal component analysis (PCA)?",
                    "How do you handle imbalanced datasets?",
                    "What is the difference between L1 and L2 regularization?",
                    "How do you tune hyperparameters in a machine learning model?",
                    "What is a gradient descent algorithm?",
                    "How do you use Scikit-learn to build a model?",
                    "What is the purpose of a ROC curve?",
                    "How do you perform feature scaling?",
                    "What is a time series and how do you analyze it?",
                    "How do you detect outliers in a dataset?",
                    "What is a neural network and how does it work?",
                    "How do you use GridSearchCV for hyperparameter optimization?"
                ],
                2: [
                    "How do you implement a random forest model in Python?",
                    "What is the difference between bias and variance?",
                    "How do you perform k-means clustering?",
                    "What is a Bayesian classifier?",
                    "How do you use cross-validation to prevent overfitting?",
                    "What is the purpose of a validation set?",
                    "How do you interpret an F1 score?",
                    "What is a convolutional neural network (CNN)?",
                    "How do you handle multicollinearity in regression?",
                    "What is the difference between supervised and reinforcement learning?",
                    "How do you visualize high-dimensional data?",
                    "What is an ensemble method in machine learning?",
                    "How do you use TensorFlow to build a simple model?",
                    "What is the role of activation functions in neural networks?",
                    "How do you perform a hypothesis test?"
                ],
                3: [
                    "How do you implement a decision tree in Python?",
                    "What is the difference between batch and stochastic gradient descent?",
                    "How do you evaluate a regression model?",
                    "What is a generative adversarial network (GAN)?",
                    "How do you use feature importance in a model?",
                    "What is the purpose of dimensionality reduction?",
                    "How do you interpret a correlation matrix?",
                    "What is a recurrent neural network (RNN)?",
                    "How do you handle skewed data distributions?",
                    "What is the difference between parametric and non-parametric models?",
                    "How do you deploy a machine learning model using Flask?",
                    "What is the purpose of a learning rate in optimization?",
                    "How do you perform time series forecasting?",
                    "What is a chi-squared test?",
                    "How do you use PCA to reduce dataset dimensions?"
                ]
            },
            'Senior': {
                1: [
                    "How do you design a recommendation system using collaborative filtering?",
                    "What are the challenges of training deep learning models?",
                    "How do you implement a gradient boosting model like XGBoost?",
                    "What is the difference between online and batch learning?",
                    "How do you optimize a neural network for large datasets?",
                    "What is transfer learning and how do you apply it?",
                    "How do you handle concept drift in production models?",
                    "What is the role of attention mechanisms in transformers?",
                    "How do you deploy a machine learning model on AWS?",
                    "What are the trade-offs of using different clustering algorithms?",
                    "How do you interpret SHAP values for model explainability?",
                    "What is the difference between a variational autoencoder and a standard autoencoder?",
                    "How do you optimize hyperparameters at scale?",
                    "What is a Markov chain and how is it used in data science?",
                    "How do you build a pipeline for real-time data processing?",
                    "What are the best practices for model monitoring in production?",
                    "How do you use PySpark for distributed data processing?",
                    "What is the role of regularization in preventing overfitting?",
                    "How do you design an A/B testing framework?",
                    "What are the challenges of working with unstructured data?"
                ],
                2: [
                    "How do you implement a reinforcement learning agent?",
                    "What are the considerations for scaling machine learning models?",
                    "How do you use natural language processing (NLP) for text classification?",
                    "What is the difference between a discriminative and generative model?",
                    "How do you optimize a time series model for accuracy?",
                    "What is the role of embeddings in deep learning?",
                    "How do you handle data drift in a production environment?",
                    "What is a transformer model and how does it work?",
                    "How do you use Kubernetes to deploy ML models?",
                    "What are the best practices for feature engineering?",
                    "How do you implement a custom loss function in TensorFlow?",
                    "What is the difference between PCA and t-SNE?",
                    "How do you design a system for anomaly detection?",
                    "What is the purpose of a hidden Markov model?",
                    "How do you use Apache Airflow for data workflows?",
                    "What are the challenges of interpreting black-box models?",
                    "How do you optimize a model for edge devices?",
                    "What is the role of ensemble techniques in improving accuracy?",
                    "How do you perform causal inference in data science?",
                    "What are the trade-offs of using cloud vs. on-premises ML solutions?"
                ],
                3: [
                    "How do you design a fraud detection system using machine learning?",
                    "What are the challenges of deploying deep learning models in production?",
                    "How do you implement a BERT model for NLP tasks?",
                    "What is the difference between active learning and semi-supervised learning?",
                    "How do you optimize a model for low-latency inference?",
                    "What is the role of GANs in data augmentation?",
                    "How do you handle missing data in a time series?",
                    "What is a self-attention mechanism in deep learning?",
                    "How do you use Docker to containerize a data science workflow?",
                    "What are the best practices for managing large datasets?",
                    "How do you implement a pipeline for automated model retraining?",
                    "What is the difference between hierarchical and k-means clustering?",
                    "How do you design a system for real-time recommendation?",
                    "What is the purpose of a Kalman filter?",
                    "How do you use MLflow for model management?",
                    "What are the challenges of explainable AI in regulated industries?",
                    "How do you optimize a distributed training process?",
                    "What is the role of Bayesian inference in data science?",
                    "How do you integrate data science into a DevOps pipeline?",
                    "What are the trade-offs of using pre-trained vs. custom models?"
                ]
            }
        }

        # Populate question_sets with the defined questions 
        for profile in self.profiles:
            self.question_sets[profile] = {}
            if profile == 'DevOps':
                questions = devops_questions
            elif profile == 'Software Engineer':
                questions = software_engineer_questions
            else:  # Data Science 
                questions = data_scientist_questions
            
            for level in self.levels:
                self.question_sets[profile][level] = {
                    'sets': [questions[level][i] for i in range(1, self.NUM_SETS + 1)],
                    'current_index': 0
                }

    def get_questions(self, profile, level):
        """Return a shuffled set of questions for the given profile and level."""
        if profile not in self.profiles or level not in self.levels:
            return "Invalid profile or level"
        
        level_data = self.question_sets[profile][level]
        current_set = level_data['sets'][level_data['current_index']]
        
        questions = current_set.copy()
        random.shuffle(questions)
        
        level_data['current_index'] = (level_data['current_index'] + 1) % self.NUM_SETS
        
        return questions

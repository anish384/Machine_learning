# Machine Learning

### Machine Learning is everywhere
---
- Like in facebook, twitter, insta they learn the user data and customize their feeds 
- recommondation like app
- self driving cars
---

### ML vs DataMining
---


### Types of Machine Learning
---
#### 1. Supervised Learning
---
Two Types
##### 1. Regression
- Regression is a type of supervised learning used to predict continuous values. It answers questions like "How much?" or "What will be the price?" 
- **Example:** Imagine predicting house prices based on factors like area, number of rooms, and location. These factors (called features) help predict a continuous value (house price).

Some popular algorithms used for regression tasks include:

- Linear Regression: Finds a straight-line relationship between input and output.
- Polynomial Regression: Fits a curve if the data points don't follow a straight line.
- Support Vector Regression (SVR): Works well for non-linear data.
- Decision Trees and Random Forests: Used when relationships between variables are more complex.

---
##### 2. Classification
- Classification is a type of supervised learning used to predict categorical values. It answers questions like "Which category?" or "Is it A or B?"
- Imagine building a system to detect if an email is spam or not spam. The input (email content) is used to classify it into one of two categories (spam or not spam).
- Some popular algorithms used for classification tasks include:

- Logistic Regression: Used for binary classification.
- Decision Trees and Random Forests: Divide data into smaller subsets for classification.
- Support Vector Machines (SVM): Finds a boundary that best separates the categories.
- k-Nearest Neighbors (k-NN): Classifies data based on its neighbors.
- Naive Bayes: Based on probability theory to classify data.

---
#### 2. Unsupervised Learning
---
- Unsupervised learning deals with data that has no labeled output. The goal is to find hidden patterns or structures in the data without predefined labels or categories.
- Common Algorithms:

- K-Means Clustering: Divides the data into a predefined number of clusters by minimizing the distance between data points and the cluster center.
- Hierarchical Clustering: Builds a tree-like structure of clusters by successively merging or splitting clusters.
- DBSCAN (Density-Based Spatial Clustering): Groups together data points that are close to each other in terms of density.
- Principal Component Analysis (PCA): Finds a new set of dimensions (called principal components) that explain most of the variance in the data.
- t-SNE (t-distributed Stochastic Neighbor Embedding): Reduces dimensions while preserving the relationships between data points, often used for visualization.
- Isolation Forest: Detects anomalies by isolating data points that are different from the rest of the data.
- Autoencoders (Neural Networks): Learn to reconstruct data and flag instances with high reconstruction errors as anomalies.
---
#### 3. Reinforcement Learning
---
- Reinforcement Learning (RL) is a type of machine learning where an agent learns to make decisions by interacting with an environment, receiving feedback in the form of rewards or penalties based on its actions.
- Common Algorithms:
- Q-Learning: A model-free algorithm where the agent learns a Q-value (quality) for each state-action pair and updates it based on rewards and future state values.
- Deep Q-Networks (DQN): Combines Q-learning with deep neural networks, allowing the agent to learn from high-dimensional data, like images (used in games like Atari).
- Policy Gradient Methods: Directly learn the policy that the agent should follow by updating it in the direction of higher expected rewards.
- Actor-Critic Methods: Combine value-based and policy-based methods, where the "actor" chooses actions, and the "critic" evaluates how good those actions are.
---


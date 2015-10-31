# Scikit-learn GUI
A simple GUI for doing fast-paced machine learning using Python

To run all tests, install the **nose** Python module, and enter the following command in the root directory of the project:
```
nosetests
```

## Todo List
- [ ] MVC Components
    - [ ] Model Classes
        - [x] Algorithm
        - [x] SupervisedAlgorithm
        - [x] UnsupervisedAlgorithm
        - [ ] RegressionAlgorithm
        - [ ] ExecutionReport
    - [ ] Controller Classes
        - [ ] AlgorithmEngine
        - [x] DataLoader
        - [ ] PreprocessingEngine
        - [ ] Visualizer
    - [ ] View Classes
        - [ ] BaseView
- [ ] Demos
  - [x] Image segmentation demo
  - [x] Command-line GUI
- [x] Loading
    - [x] File formats
      - [x] .arff
      - [x] .csv
      - [x] .xls/.xlsx
  - [x] Generate random Gaussian data w/ labels
  - [x] Download dataset from mldata.org
- [x] Preprocessing data
  - [x] Standardization
  - [x] Normalization of training examples
  - [x] Feature Binarization
  - [x] Remove examples with '?' missing values
  - [x] Imputation of missing values
  - [x] Numerical encoding of categorical features
- [ ] Supervised Learning
  - [ ] Linear & Quadratic Discriminant Analysis
  - [ ] SVMs
  - [ ] Stochastic Gradient Descent
  - [ ] kNN
  - [X] Decision Trees
  - [ ] Ensemble Methods
    - [ ] Bagging
    - [ ] Randomized Trees
    - [ ] AdaBoost
  - [ ] Multiclass and Multilabel Algorithms
  - [ ] Feature Selection
    - [ ] Variance thresholding
    - [ ] Univariate feature selection
  - [ ] Generalized Linear Models
    - [ ] Least Squares
    - [ ] RANSAC
    - [ ] Bayesian
    - [ ] Logistic
    - [ ] Polynomial
  - [ ] Kernel Ridge Regression
- [ ] Unsupervised Learning
  - [ ] Gaussian Mixture Models
    - [ ] GMM
    - [ ] DPGMM
  - [ ] Manifold Learning
  - [ ] Clustering
    - [ ] K-means
    - [ ] Spectral clustering
    - [ ] Hierarchical clustering
    - [ ] DBSCAN
  - [ ] Decomposing signals into components
    - [ ] PCA
    - [ ] ICA
    - [ ] Factor Analysis
  - [ ] Covariance Estimation
  - [ ] Novelty and Outlier Detection
  - [ ] Restricted Boltzmann Machines
- [ ] Model Selection and Evaluation
  - [X] Cross Validation
  - [ ] Grid Search
  - [ ] Prediction Metrics
    - [ ] Classification Metrics
      - [ ] ROC
      - [X] Accuracy Score
      - [X] Confusion Matrix
    - [ ] Regression Metrics
      - [ ] MAE, MSE, R2
    - [ ] Clustering Metrics
      - [ ] Adjusted Rand index
      - [ ] Homogeneity (similarity of items within cluster)
      - [ ] Completeness (same class items all go in one cluster)
  - [ ] Validation Curves
- [ ] Dataset Transformations
  - [ ] Pipelining
  - [ ] Feature Extraction
    - [x] Dictionary Vectorization
  - [ ] Kernel Approximation
- [ ] Visualizations
    - [x] Plotting features (2d, frequency chart, radial plot, etc.)

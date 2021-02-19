# Iterative k-Means clustering on Spark: 

Implement iterative k-means using Spark. Note that we have provided that centroids for you (see below), so you do not need to select the initial centroids (skip Line 2 of Algorithm 1).
P1 has 3 files:
1. data.txt contains the dataset which has 4601 rows and 58 columns. Each row is a document represented as a 58-dimensional vector of features. Each component in the vector
represents the importance of a word in the document. 
2. c1.txt contains k initial cluster centroids. These centroids were chosen by selecting k = 10 random points from the input data.
3. c2.txt contains initial cluster centroids which are as far apart as possible. (You can do this by choosing 1st centroid c1 randomly, and then finding the point c2 that is farthest from c1, then selecting c3 which is farthest from c1 and c2, and so on). 

Set the number of iterations to 20 and the number of clusters k to 10 for all the experiments carried out in this question. Your driver program should ensure that the correct amount of iterations are run.

a. Exploring initialization strategies with Euclidean distance
1. Using the Euclidean distance (refer to Equation 1) as the distance measure, compute the cost function φ(i) (refer to Equation 2) for every iteration i. This means that, for your first iteration, you will be computing the cost function using the initial centroids located in one of the two text files. Run the k-means on data.txt using c1.txt and c2.txt. Generate a graph (line plot) where you plot the cost function φ(i) as a function of the number of iterations i=1..20 for c1.txt and also for c2.txt.
Hint: Note that you do not need to write a separate Spark job to compute φ(i). You should be able to calculate costs while partitioning points into clusters.
2. Is random initialization of k-means using c1.txt better than initialization using c2.txt in terms of cost φ(i)? Explain your reasoning.

b. Exploring initialization strategies with Manhattan distance
1. Using the Manhattan distance metric (refer to Equation 3) as the distance measure, compute the cost function ψ(i) (refer to Equation 4) for every iteration i. This means that,
for your first iteration, you’ll be computing the cost function using the initial centroids located in one of the two text files. Run the k-means on data.txt using c1.txt and c2.txt. Generate a graph where you plot the cost function ψ(i) as a function of the number of iterations i=1..20 for c1.txt and also for c2.txt.
2. Is random initialization of k-means using c1.txt better than initialization using c2.txt in
terms of cost ψ(i)? Explain your reasoning.

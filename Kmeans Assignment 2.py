# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 22:55:08 2019

@author: supriya
"""
import numpy as np
import matplotlib.pyplot as plt
from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local")
sc = SparkContext.getOrCreate(conf=conf)
from scipy.spatial import distance 
dataset_path = 'C:/Users/pratik/Desktop/Big Data Mining/Assignment 2/data.txt'
centroid_set1_path = 'C:/Users/pratik/Desktop/Big Data Mining/Assignment 2/c1.txt'
centroid_set2_path = 'C:/Users/pratik/Desktop/Big Data Mining/Assignment 2/c2.txt'
def kmeans(data,centroids,iterations,eucledian_distance):
    dataset = np.loadtxt(data)
    data = sc.parallelize(dataset)
    centroid_set = np.loadtxt(centroids)
    set1 = sc.parallelize(centroid_set)
    c1 = set1.collect()
    #print('euclidean distance')
    #type(c1[0])
    iterations_set = []
    cost_centroid_new = []
    for i in range(iterations):
        #print("yes")
        """Calculate euclidean or manhattan distance """
        calculate_distance = lambda x: np.array([distance.euclidean(x,y) for y in c1] if (eucledian_distance) else [distance.cityblock(x,y) for y in c1])
        calculate_distance(data.take(1)[0])
        distance_calculate_rdd = data.map(calculate_distance)
        #print(rdd1.take(4600))
        #calculate cost function
        minimum_distance = lambda x: (np.amin(x))**2 if (eucledian_distance) else (np.amin(x))
        minimum_distance_list = distance_calculate_rdd.map(minimum_distance)
        #print(data_min_list.take(1))
        """identify the index of the centroid"""
        min_distance_index = distance_calculate_rdd.map(lambda x: np.argmin(x))
        
        #print(tst.take(1))
        #print(data_min_list.collect())
        print('iteration', i+1,':',minimum_distance_list.sum())
        """find sum of the minimum distance"""
        sum_cost = minimum_distance_list.sum()
        cost_centroid_new.append(sum_cost)
        iterations_set.append(i+1)
        rdd_temp = min_distance_index.zip(data)
        
        #print(rdd_temp.take(1))
        """rdd with the index to centroid and vectors"""
        group_vector_index = rdd_temp.groupByKey().map(lambda x : (x[0], list(x[1])))
        #print(rdd_group.take(1))
        #print("2")
        #print(rdd_group.take(1))
        """recalculate the centroid"""
        c1 = group_vector_index.map(lambda x: np.average(x[1],axis=0))
        #print(c1.take(1))
        c1= c1.collect()
        
     
    plt.plot(iterations_set,cost_centroid_new,marker='*')
    plt.xlabel('iteration')
    plt.ylabel('cost')
    plt.show()

kmeans(dataset_path,centroid_set2_path,20,True)
sc.stop()
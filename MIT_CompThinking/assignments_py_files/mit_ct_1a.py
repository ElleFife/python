# -*- coding: utf-8 -*-
"""MIT_CT_1a.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b951Tuzn7TCylFc6urB18w77QBo99xWJ

#================================
# Part A: Transporting Space Cows
#================================
"""

from google.colab import drive
drive.mount('/content/gdrive/')

#Problem 1 - Loading the cow data

#from ps1_partition import get_partitions
import time

cowdata1 = '/content/gdrive/MyDrive/mit_ct_2016/Assignments/PS1/ps1_cow_data.txt'
cowdata2 = '/content/gdrive/MyDrive/mit_ct_2016/Assignments/PS1/ps1_cow_data_2.txt'

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.
    Parameters:
    filename - the name of the data file as a string
    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    cow_file = open(filename, 'r')
    cow_dict = dict()
    for line in cow_file:
        line_listed = line.split(',')
        line_listed[1] = int(line_listed[1].strip('\n'))
        cow_dict[line_listed[0]] = line_listed[1]
    return cow_dict

#run test

print(load_cows(cowdata1))

# Problem 2
def greedy_cow_transport(cows,limit=10):
  
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    copy_cows = dict(cows)
    trips = list()
    while len(copy_cows) != 0:
        space_left = int(limit)
        trip = list()
        while len(copy_cows) > 0 and space_left >= copy_cows[cow_with_min_weight(copy_cows)]:

            trip.append(cow_with_max_weight(copy_cows))
            space_left -= copy_cows[cow_with_max_weight(copy_cows)]
            copy_cows.pop(cow_with_max_weight(copy_cows))
        trips.append(trip)
    return trips
    
def cow_with_max_weight(cows):
    ''' form a dictionary with cows as a keys and weight as a value
    return key with max value
    '''
    weights = list(cows.values())
    cows_keys = list(cows.keys())
    return cows_keys[weights.index(max(weights))]

def cow_with_min_weight(cows):
    '''the same as max but min'''
    weights = list(cows.values())
    cows_keys = list(cows.keys())
    return cows_keys[weights.index(min(weights))]

print(cow_with_max_weight(load_cows(cowdata1)))
#print(cow_with_min_weight(load_cows(cowdata1))
#print(greedy_cow_transport(load_cows(cowdata1))
greedy_cow_transport(load_cows(cowdata1),9)
#print(len(greedy_cow_transport(load_cows(cowdata1))

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    '''
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:
    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.
    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    '''
    best_trips_exists = False

    for each_set in get_partitions(set(cows.keys())):
        for each_trip in each_set:
            if not can_fit(each_set, limit, cows):
                break
            else: 
                if best_trips_exists == False:
                    best_trips = each_set
                    best_trips_exists = True
                elif len(best_trips) > len(each_set):
                    best_trips = each_set
    return best_trips

def can_fit(trips, limit, cows):
    '''True if every trip of set can fit set of cows, False otherwise'''
    overloaded = False
    for trip in trips:
        weight = int()
        for each in trip:
            weight += cows[each]
        if weight > limit:
            overloaded = True
            break

    if overloaded == True:
        return False
    else: return True

# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.
    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    start = time.time()
    greedy_cow_transport(load_cows(cowdata1))
    end = time.time()
    print('time it takes', end-start,'in sec for greedy algorithm on ps1_cow_data.txt')
    
    start = time.time()
    brute_force_cow_transport(load_cows(cowdata1))
    end = time.time()
    print('time it takes', end-start, 'in sec to brute force ps1_cow_data.txt')

    start = time.time()
    greedy_cow_transport(load_cows(cowdata2))
    end = time.time()
    print('time it takes', end - start,'in sec for greedy algorithm on ps1_cow_data')
    
    start = time.time()
    brute_force_cow_transport(load_cows(cowdata2))
    end = time.time()
    print('time it takes ', end - start, 'in sec to brute force ps1_cow_data')

compare_cow_transport_algorithms()
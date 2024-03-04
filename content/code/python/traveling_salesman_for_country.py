import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist, squareform
from python_tsp.exact import solve_tsp_dynamic_programming
import sys


# Function to calculate distance matrix for a set of locations
def calculate_distance_matrix(locations):
    distance_matrix = pdist(locations, "euclidean")
    distance_matrix = squareform(distance_matrix)
    return distance_matrix


# Function to solve the Traveling Salesman Problem returning the positions in the travel route.
def solve_tsp(distance_matrix):
    permutation, distance = solve_tsp_dynamic_programming(distance_matrix)
    indices = list(range(len(permutation)))
    # Sort the indices based on the values in the randomized array
    sorted_indices = sorted(indices, key=lambda x: permutation[x])
    return sorted_indices


# Read the CSV file into a pandas DataFrame
file_path = "cities.csv"  # Update with your actual file path
df = pd.read_csv(file_path)

country = sys.argv[1]

# Filter DataFrame for the current country
country_df = df[df["Country"] == country].copy()
# Get latitude and longitude for each city in the country
locations = country_df[["Latitude", "Longitude"]].to_numpy()
# Calculate distance matrix
distance_matrix = calculate_distance_matrix(locations)
# Solve TSP using linear_sum_assignment
tsp_solution = solve_tsp(distance_matrix)
# Update the DataFrame with the optimal order
country_df["TSP_Order"] = tsp_solution
country_df.reset_index(drop=True)
# Print the result for the current country
country_df.to_csv(f"{country}.csv")

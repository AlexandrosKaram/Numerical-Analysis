from linear_equation_methods import initialize_matrix, print_matrix
from copy import deepcopy
from statistics import stdev


def create_google_matrix(A, q=0.15):
    """Function that receives Adjacency matrix and creates Google matrix."""
    n = len(A)
    G = initialize_matrix(n)   # Initialize Google matrix with zeros

    for j in range(n):
        nj = sum(A[j][i] for i in range(n))
        for i in range(n):
            G[i][j] = q/n + A[j][i]*(1-q)/nj
    
    return G


def multiply_matrix_with_vector(A, b):
    """Function that multiplies a Matrix with a Vector.
    
    Parameters:
        A (list[list]): The matrix
        b (list): The vector
    
    Returns:
        (list): The new vector
    """
    return [sum(A[i][j] * b[j] for j in range(len(b))) for i in range(len(A))]


def normalize_vector(b):
    """Function to normalize a vector."""
    s = sum(b)
    return [b[i]/s for i in range(len(b))]


def vector_infinity_norm(b):
    return max(abs(b[i]) for i in range(len(b)))


def power_method(A, epsilon = 0.00001, max_iterations = 100):
    """Function that executes the power method.
    
    Parameters:
        A (list[list]): The matrix we want to execute the power method with.
    
    Returns:
        (list): The eigenvector of the maximum eigenvalue.
    """
    b = [1] * len(A[0])  # Base vector of 1's

    # Execute power method
    for i in range(max_iterations):
        b_new = multiply_matrix_with_vector(A, b)
        b_new = normalize_vector(b_new)
        # Check if power method is over
        if (abs(vector_infinity_norm(b) - vector_infinity_norm(b_new)) < epsilon):
            return b
        b = b_new   # Replace old b with the new one
    
    # Surpassed maximum iterations
    print("Power method fails.")
    return None


def print_page_dynamic(G, eigenvector):
    """Helper function that parallel sorts the index of the pages and the page ranks and prints the results."""
    page_index = [i for i in range(len(G))]
    pairs = list(zip(eigenvector, page_index))   # Merge lists to parallel sort
    sorted_pairs = sorted(pairs, key=lambda x: x[0], reverse=True)   # Sort in respect of eigenvector values
    print("\nThese are the most important pages in order:\n")
    for pair in sorted_pairs:
        print(f"\tPage {pair[1]}: {pair[0]:.4f}")


# Main
def main():
    # Αdjacency matrix
    A = [
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
    ]

    # Exercise 4a
    print("\nExercise 4a")
    n = len(A)
    q = 0.15
    for j in range(n):
        nj = sum(A[j][i] for i in range(n))   # Sum of connections to j
        s = 0
        for i in range(n):
            s += q/n + A[j][i]*(1-q)/nj
        if s != 1:   # Sum of j-column not equal to 1
            print("Google matrix is not stochastic.")
            break
    else:   # Loop ended 
        print("Google matrix indeed is stochastic.")

    # Exercise 4b
    print("\nExercise 4b")
    G = create_google_matrix(A)
    eigenvector = power_method(G)   # Calculate the eigenvector by the power method
    print(f"\nAs we can see the Eigenvector is the one we expected:\n{eigenvector}")

    # Check which pages are the most important
    print_page_dynamic(G, eigenvector)

    # Exercise 4c
    print("\nExercise 4c")
    A_2 = [
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    standard_deviation = []

    G_2 = create_google_matrix(A_2)
    eigenvector_2 = power_method(G_2)
    standard_deviation.append(stdev(eigenvector_2))

    # Print new results
    print("\nAfter updating the A matrix, we can now see that the dynamic in the rankings has changed.")
    print_page_dynamic(G_2, eigenvector_2)
    print("\nWe have succesfully shifted the dynamic of 'Page 0' as from the second to last position it is now the most important page.")
    print("That was the result of adding pages pointing the the 'Page 0' but also importantly to 'Page 3' (which is pointing to 'Page 0').")
    print("However, the success of our experiment is also due to the fact that the favored pages of the previous rankings (12, 13, 14) are pointing to our new pages.\n")

    # Exercise 4d
    print("\nExercise 4d")
    print("\nAfter changing q to 0.02 from 0.15 we can see the following differences:\n")
    G_2 = create_google_matrix(A_2, 0.02)
    eigenvector_2 = power_method(G_2)
    standard_deviation.append(stdev(eigenvector_2))
    print_page_dynamic(G_2, eigenvector_2)

    print("\nAfter changing q to 0.6 from 0.02 we can see the following differences:\n")
    G_2 = create_google_matrix(A_2, 0.6)
    eigenvector_2 = power_method(G_2)
    standard_deviation.append(stdev(eigenvector_2))
    print_page_dynamic(G_2, eigenvector_2)

    # Observation
    print("\nFrom the results above and the help of standard deviation we make the following observation.")
    print(f"\tq=0.02, standard deviation={standard_deviation[1]:.4f}")
    print(f"\tq=0.15, standard deviation={standard_deviation[0]:.4f}")
    print(f"\tq=0.6, standard deviation={standard_deviation[2]:.4f}")
    print("The higher the value of 'q' is, the less relevant is the page rank system. This is due to the fact that")
    print("the number of connections each page has gets less important, as there are more chances of randomly selecting")
    print("the page than being led to it by another page.\n")

    # Exercise 4e
    print("\nExercise 4e")
    print("Reminder of page dynamic of our starter matrix.")
    print_page_dynamic(G, eigenvector)
    print("After changing A[7][10] and A[11][10] to '3',")
    A[7][10] = A[11][10] = 3
    G = create_google_matrix(A)
    eigenvector = power_method(G)
    print_page_dynamic(G, eigenvector)
    print("We can clearly see that the 11th page has now surpassed the 10th page's dynamic.")

    # Exercise 4f
    print("\nExercise 4f")
    print("After deleting page 10 (A[9])")
    # Remove page 10
    connections_from_page_10 = A.pop(9)
    print(connections_from_page_10)
    for i in range(len(A)):
        A[i].pop(9)
    
    print_matrix(A)

    G = create_google_matrix(A)
    new_eigenvector = power_method(G)    


# Call main
if __name__ == "__main__":
    main()

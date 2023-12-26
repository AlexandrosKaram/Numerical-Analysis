from linear_equation_methods import print_matrix, round_matrix, initialize_matrix

q = 0.15   # Probability of moving to a page
n = 15   # Total pages


def create_google_matrix(A):
    """Function that receives Adjacency matrix and creates Google matrix."""
    G = initialize_matrix(15)   # Initialize 15x15 Google matrix with zeros

    for j in range(n):
        nj = sum(A[j][i] for i in range(n))
        for i in range(n):
            G[i][j] = q/n + A[j][i]*(1-q)/nj
    
    return G

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
    G = create_google_matrix(A)


# Call main
if __name__ == "__main__":
    main()
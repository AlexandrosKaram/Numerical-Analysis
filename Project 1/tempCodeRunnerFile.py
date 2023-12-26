    page_index = [i for i in range(len(A))]
    pairs = list(zip(eigenvector, page_index))   # Merge lists to sort
    sorted_pairs = sorted(pairs, key=lambda x: x[0], reverse=True)   # Sort in respect of eigenvector values
    print("\nThese are the most important pages in order:")
    for pair in sorted_pairs:
        print(f"Page {pair[1]}: {pair[0]:.4f}")
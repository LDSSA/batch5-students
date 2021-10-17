def reduce_word_vecs(vectors, random_state):
    """
    Returns PCA-reduced word vectors of the input vectors for plotting
    
    Parameters:
        vectors (np.array): Word vectors to be reduced
        random_state (int): random state to use in PCA

    Returns:
        reduced_vecs (np.array): Word vectors reduced to the number of dimensions
                                 suitable for plotting with given random_state
    """
    ### BEGIN SOLUTION
    pca = PCA(n_components=2, random_state=random_state)
    reduced_vecs = pca.fit(vectors)
    reduced_vecs = pca.transform(vectors)
    ### END SOLUTION
    
    return reduced_vecs

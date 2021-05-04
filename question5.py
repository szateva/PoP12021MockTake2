# 13021326

""" Implement a non-fruitful function
trim_matrix(M)
that, given a list M of lists M[0], M[1], . . . , modifies M so that it forms a correct matrix.
The modification should make all of the M[i] of the same length by removing from the
end of each M[i] a number of elements n, such that M[i] is longer than the shortest
list among M[0], M[1], . . . by n. Importing any libraries is NOT allowed.
Indicative test cases:
X = [[1,2,3],[12,13],[21,22,23,24]]
trim_matrix(X)
assert X == [[1,2],[12,13],[21,22]] #must be True
X = [[1,2,3],[12,13,14]]
trim_matrix(X)
assert X == [[1,2,3],[12,13,14]] #must be True
X = [[1,2,3],[12,13,14],[]]
trim_matrix(X)
assert X == [[],[], []] #must be True """

def trim_matrix(M):
    # finding the shortest row:
    shortest = len(M[0])
    for row in range(len(M)):
        if len(M[row]) < shortest:
            shortest = len(M[row])

    for row in range(len(M)):
        if len(M[row]) > shortest:
            del M[row][shortest:]
    return M

# Indicative test cases:
X = [[1,2,3],[12,13],[21,22,23,24]]
trim_matrix(X)
assert X == [[1,2],[12,13],[21,22]] #must be True
X = [[1,2,3],[12,13,14]]
trim_matrix(X)
assert X == [[1,2,3],[12,13,14]] #must be True
X = [[1,2,3],[12,13,14],[]]
trim_matrix(X)
assert X == [[],[], []] #must be True
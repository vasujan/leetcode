#!/usr/bin/python
"""
# Knut Morris Pratt Algorithm

https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
"""

from algo.utils import timer


def kmp_search(S: str, W: str) -> list[int]:
    """
    Search for all occurrences of string W in string S using the Knuth-Morris-Pratt algorithm.

    Find all occurrences of string `W` in string `S` using the KMP string matching algorithm.

    This algorithm works by preprocessing `W` to generate a table
    `T` of size `len(W) + 1`. Each element `T[i]` of the table is
    the length of the longest proper prefix of `W` that is also a
    suffix of `W` at position `i`. The table is used to efficiently
    skip over sections of `S` that cannot match `W`.

    Parameters
    ----------
    S : str
        The string to search in.
    W : str
        The string to search for.

    Returns
    -------
    list[int]
        A list of indices at which `W` is found in `S`, or an empty list if `W` is not found in `S`.

    Examples
    --------
    >>> kmp_search("banana", "ana")
    [1, 3]
    >>> kmp_search("banana", "anb")
    []
    >>> kmp_search("", "ana")
    []
    >>> kmp_search("a", "ana")
    []
    >>> kmp_search("ana", "ana")
    [0]
    """
    j: int = 0  # index in S
    k: int = 0  # index in W
    P: list[int] = list()  # output
    T: list[int] = kmp_table(W)

    while j < len(S):
        # If the current character of S matches the current character of W
        if W[k] == S[j]:
            j += 1
            k += 1
            if k == len(W):
                # Match found, add the index to the output
                P.append(j - k)
                # Reset k to the length of the longest proper prefix of W
                # that is also a suffix of W at position k-1
                k = T[k - 1]
        else:
            # If the current character of S does not match the current character of W
            # reset k to the length of the longest proper prefix of W that is also
            # a suffix of W at position k
            k = T[k]
            if k < 0:
                # If the longest proper prefix of W that is also a suffix of W at
                # position k is empty, increment j to the next character in S
                # and reset k to 0
                j += 1
                k += 1

    return P


def kmp_table(W: str) -> list[int]:
    """
    Preprocesses a string `W` to generate a table `T` that encodes
    information about the longest proper prefix of `W` that is also
    a suffix of W at each position. The table is used by the KMP
    string matching algorithm to efficiently skip over sections of
    a string `S` that cannot match `W`. The table is of size `len(W) + 1`
    and each element `T[i]` is the length of the longest proper prefix
    of `W` that is also a suffix of `W[:i+1]`.
    """
    pos: int = 1  # current position in W
    cnd: int = (
        0  # zero-based index in W of the next character of current candidate string
    )

    T: list[int] = [0] * (len(W) + 1)
    T[0] = -1

    while pos < len(W):
        # If the current character in W matches the candidate string then
        # the length of the longest proper prefix of W that is also a suffix
        # of W[:pos+1] is one more than the value at the current candidate
        # position in the table.
        if W[pos] == W[cnd]:
            T[pos] = cnd + 1
        else:
            # If the current character in W does not match the candidate string
            # then the length of the longest proper prefix of W that is also a
            # suffix of W[:pos+1] is the value at the current candidate position
            # in the table
            T[pos] = cnd
            # we need to find a new candidate string by moving the candidate
            # position in the table to the value at the current candidate
            # position in the table
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = T[cnd]
        # Move on to the next character in W
        pos += 1
        # Move on to the next character in the candidate string
        cnd += 1
    else:
        # The length of the longest proper prefix of W that is also a suffix
        # of W is the value at the last position in the table
        T[pos] = cnd

    return T


if __name__ == "__main__":
    S = "ABC ABCDAB ABCDABCDABDE"
    W = "ABCDABD"
    print(kmp_table(W))
    with timer("kmp_search"):
        print(kmp_search(S, W))

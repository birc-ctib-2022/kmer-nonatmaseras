"""Computing kmers of a string."""


def kmer(x: str, k: int) -> list[str]:
    """
    Computer all k-mers of x.

    >>> kmer('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']

    """
    kmer = [x[i:i+k] for i in range(0,len(x)-k+1)]
    return kmer


def unique_kmers(x: str, k: int) -> list[str]:
    """
    Computer all unique k-mers of x.

    """
    return list(set(kmer(x,k)))

def count_kmers(x: str, k: int) -> dict[str, int]:
    """
    Computer all k-mers of x and count how often they appear.
    

    """
    # get unique kmers
    unique_k = unique_kmers(x,k)
    # get all kmers
    all_kmers = kmer(x,k)
    #dictionary with the unique kmers
    counts =  dict.fromkeys(unique_k,0)
    
    # for to count occurences in all_kmers
    for k in all_kmers:
        counts[k] += 1
    return counts



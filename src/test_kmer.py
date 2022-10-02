# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_
from kmer import (
    kmer,unique_kmers,count_kmers
)


def test_kmer() -> None:
    assert kmer('agtagtcg', 3) ==  ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']



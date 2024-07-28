This is results of third task.

1) For firts text file with pattern that exists in text.

| Name                  | Duration               |
| --------------------- | ---------------------- |
| Python default search | 1.1357000403222628e-05 |
| Rabin-Karp            | 0.007134898000003886   |
| Knuth-Morris-Pratt    | 0.002658536001035827   |
| Boyer-Moore           | 0.00038089499867055565 |

2) For firts text file with pattern that does not exists in text.

| Name                  | Duration               |
| --------------------- | ---------------------- |
| Python default search | 1.0368999937782064e-05 |
| Rabin-Karp            | 0.016306952999002533   |
| Knuth-Morris-Pratt    | 0.0053512180002144305  |
| Boyer-Moore           | 0.0006719459997839294  |

3) For second text file with pattern that exists in text.

| Name                  | Duration               |
| --------------------- | ---------------------- |
| Python default search | 1.570699896547012e-05  |
| Rabin-Karp            | 0.014781926998693962   |
| Knuth-Morris-Pratt    | 0.005871050998393912   |
| Boyer-Moore           | 0.0006985899999563117  |

4) For second text file with pattern that does not exists in text.

| Name                  | Duration               |
| --------------------- | ---------------------- |
| Python default search | 2.0748000679304823e-05 |
| Rabin-Karp            | 0.024135387000569608   |
| Knuth-Morris-Pratt    | 0.010018623999712872   |
| Boyer-Moore           | 0.0012312830003793351  |

The fastest algorithm is Boyer-Moore search for all cases.

The slowest algorithm is Rabin-Karp search for all cases.

Knuth-Morris-Pratt search is faster than Rabin-Karp search but slower than Boyer-Moore search.

Interesting that plain python search beat all other algorithms in all cases. Because this algorith is based on a mix between boyer-moore and horspool algorithms, it is not surprising that it is faster than the other algorithms.

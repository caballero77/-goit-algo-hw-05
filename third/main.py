import timeit
from rabin_karp import rabin_karp_search
from boyer_moore import boyer_moore_search
from kmp import kmp_search


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def test_search(text, pattern, search_func):
    result = -1
    def search(text, pattern):
        nonlocal result
        result = search_func(text, pattern)

    time = timeit.timeit(lambda: search(text, pattern), number=10)
    return result, time


test_cases = [
    ('./text/first.txt', [
        'Пошук стрибками, цей алгоритм від двійкового пошуку відрізняється рухом виключно вперед.',
        'var arrayLength = integers.length;'
    ]),
    ('./text/second.txt', [
        'Випадковим чином обирається контрольна сесія, для якої буде сформовано рекомендацію.',
        'Відображається "стаття 3.txt".'
    ]),
]


search_functions = [
    ('Python search', lambda text, pattern: text.find(pattern)),
    ('Rabin-Karp search', lambda text, pattern: rabin_karp_search(text, pattern)),
    ('Knuth-Morris-Pratt search', lambda text, pattern: kmp_search(text, pattern)),
    ('Boyer-Moore search', lambda text, pattern: boyer_moore_search(text, pattern)),
]

for file_path, patterns in test_cases:
    text = read_file(file_path)
    for pattern in patterns:
        print(f"{file_path:<40} {pattern}")
        for search_name, search in search_functions:
            print(f"{search_name:<40} {test_search(text, pattern, search)}")

# The fastest algorithm is Boyer-Moore search for all cases.
# The slowest algorithm is Rabin-Karp search for all cases.
# Knuth-Morris-Pratt search is faster than Rabin-Karp search but slower than Boyer-Moore search.
# Interesting that plain python search beat all other algorithms in all cases. Because this algorith is based on a mix between boyer-
#    moore and horspool algorithms, it is not surprising that it is faster than the other algorithms.
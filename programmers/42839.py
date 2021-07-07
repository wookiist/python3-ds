# 42839 완전탐색 > 소수 찾기

from itertools import permutations

def solution(numbers):
    answer = 0
    primes = [True for _ in range(10**len(numbers))]
    primes[0], primes[1] = False, False
    for i in range(2, int(len(primes)/2)):
        if primes[i]:
            for j in range(i+i, len(primes), i):
                primes[j] = False

    checked = dict()
    for i in range(1, len(numbers)+1):
        for comb in permutations(numbers, i):
            num = int(''.join(comb))
            if primes[num] and checked.get(num) is None:
                answer += 1
                checked[num] = "ok"
    
    return answer
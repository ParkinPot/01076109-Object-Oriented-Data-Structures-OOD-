def fibonacci(k):
    if k <= 2:
        return 1
    else:
        return fibonacci(k - 1) + fibonacci(k - 2)

def minimum_weight(purity):
    min_w = 1
    for p in range(2, purity+1):
        ck = fibonacci(p-1)
        min_w = (2*min_w + ck + 1) // 2  
    return min_w

memo = {}
def max_weight_recursive(purity, weight):
    if (purity, weight) in memo:
        return memo[(purity, weight)]
    if weight <= 0:
        return -1
    if purity == 1:
        return weight

    ck = fibonacci(purity-1)
    best = -1
    for total in [2*weight - ck, 2*weight + 1 - ck]:
        if total <= 0:
            continue
        for a in range(1, total):
            b = total - a
            left = max_weight_recursive(purity-1, a)
            right = max_weight_recursive(purity-1, b)
            if left != -1 and right != -1:
                best = max(best, left + right)
    memo[(purity, weight)] = best
    return best

def max_total_purity1_weight(purity, weight):
    if purity == 1:
        return weight
    if weight < minimum_weight(purity):
        return max_weight_recursive(purity, weight)
    else:
        return (1 << (purity - 1)) * weight + (1 << (purity - 2)) * (purity - fibonacci(purity + 1))

purity, weight = map(int, input("Purity and Weight needed: ").split())
total_weight = max_total_purity1_weight(purity, weight)

print(f"Total weight of used minerals with Purity 1 : {total_weight}")

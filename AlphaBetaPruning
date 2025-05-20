import math
MAX = 1000
MIN = -1000
def alpha_beta(depth, nodeIndex, maximizingPlayer, values, alpha, beta, targetDepth):
    if depth == targetDepth:
        return values[nodeIndex]
    if maximizingPlayer:
        best = MIN
        for i in range(2):
            val = alpha_beta(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta, targetDepth)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = MAX
        for i in range(2):
            val = alpha_beta(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta, targetDepth)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

if __name__ == "__main__":
    values = [3, 5, 6, 9]
    targetDepth = int(math.log(len(values), 2))  
    print("The optimal value is:", alpha_beta(0, 0, True, values, MIN, MAX, targetDepth))

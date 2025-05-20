import math
MAX = 1000
MIN = -1000
def minimax(depth, nodeIndex, maximizingPlayer, values, targetDepth):
    if depth == targetDepth:
        return values[nodeIndex]
    if maximizingPlayer:
        best = MIN
        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, targetDepth)
            best = max(best, val)
        return best
    else:
        best = MAX
        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, targetDepth)
            best = min(best, val)
        return best
if __name__ == "__main__":
    values = [3, 5, 6, 9]
    targetDepth = int(math.log(len(values), 2))  
    print("The optimal value is:", minimax(0, 0, True, values, targetDepth))


def alpha_beta_pruning(node, depth, alpha, beta, maximizingPlayer):

    if depth == 0 or isinstance(node, int):
        return node

    if maximizingPlayer:
        maxEval = float('-inf')
        for child in node:
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = float('inf')
        for child in node:
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval


game_tree = [
    [3, 5, 14, 8],
    [-2, 5, -1, 7]
]


optimal_value = alpha_beta_pruning(game_tree, 2, float('-inf'), float('inf'), True)
print("The optimal value for the MAX player is:", optimal_value)

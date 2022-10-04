mod_val = 10**9 + 7


# Idea: use table with precomputed number of paths that can lead to certain cell
# Main hypothesis: the number of paths that lead to certain cell equals the sum of 
# values in the cell on the left and the cell above (sinse we only can move right and down)
def dynamic_solution(m, n):
    tbl = [[0] * n for _ in range(m)]
    for i in range(1, m):
        tbl[i][0] = 1
    
    for j in range(1, n):
        tbl[0][j] = 1
    
    for i in range(1, m):
        for j in range(1, n):
            tbl[i][j] = (tbl[i-1][j] % mod_val) + (tbl[i][j-1] % mod_val)
    
    return tbl[m-1][n-1]


# Very slow and inefficient because we need to recompute the number of paths from 
# certain cell multiple times
def recursive_solution(m, n):
    if m == 1 and n == 1:
        return 0
    if (m == 1) or (n == 1):
        return 1
    
    def recursive_f(i, j):
        if i == m or j == n:
            return 1
        else:
            return (recursive_f(i + 1, j) % mod_val) + (recursive_f(i, j + 1) % mod_val)

    res = recursive_f(1, 1)
    return res


def test_function(sol_func, m, n, expected_value):
    obtained_value = sol_func(m, n)
    res = ''
    if expected_value == obtained_value:
        res = 'Passed'
    else:
        res = 'Failed'
    
    print(f'{res}: expected: {expected_value}, obtained: {obtained_value}')


def test_1(sol_func, remark=''):
    m = 3
    n = 3
    expected_value = 6
    
    print(f'--- Test 1 ({remark}) ---')
    test_function(sol_func, m, n, expected_value)


if __name__ == '__main__':
    test_1(dynamic_solution, 'dynamic_solution')
    test_1(recursive_solution, 'recursive_solution')

def solution(W, wt, val, n):
    '''
        Link to the problem: https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/ 

        W: int, max capacity of knapsack,
        n: int, number of items
        wt: list, weights of items
        val: list, values of items

        Dynamic programming approach:
        - for every new item, you consider its possible combinations that sum up to W
        and update those cells which give larger value;
        - in other words, you build a table, with (W+1) rows and (n+1) columns such that
        cell (i, j) corresponds to the max possible value at step j for weight i

        Remark: 
        - maybe one can skip updating cells if the value in the cell which we add to 
        the current value is zero, apart from the case when that cell has weight zero, meaning 
        there is no rest in that cell (it might give some optimization)
    '''

    max_val = 0
    tbl = [[0]*(n+1) for _ in range(W+1)]
    for i in range(n):
        w = wt[i]
        v = val[i]

        ########## longer way ##################
        for j in range(1, W+1):
            tbl[j][i+1] = tbl[j][i]
        if w > W or w == 0:
            continue
        for rest in range(W - w + 1):
            curr_v = v + tbl[rest][i]
            if curr_v > tbl[w+rest][i]: 
                tbl[w+rest][i+1] = curr_v
        
        ########## shorter way #########
        # for j in range(1, W+1):
        #     tbl[j][i+1] = max(tbl[j][i], ((j - w) >= 0) * (tbl[max(0, j-w)][i] + v))
 
    for j in range(1, W+1):
        max_val = max(max_val, tbl[j][n])
    
    return max_val


def test_function(W, wt, val, n, expected_value):
    obtained_value = solution(W, wt, val, n)
    res = ''
    if expected_value == obtained_value:
        res = 'Passed'
    else:
        res = 'Failed'
    
    print(f'{res}: expected: {expected_value}, obtained: {obtained_value}')


def test_1():
    val = [1,2,3]
    wt = [4,5,1]
    W = 4
    n = 3
    expected_value = 3
    print('--- Test 1 ---')
    test_function(W, wt, val, n, expected_value)


if __name__ == '__main__':
    # test_1()
    w = 3
    j = 3
    res = ((j-w) >= 0)
    print(res*4)
    

def solution(items, W, n):
    def get_per_unit_value(elem):
        return elem[0] / elem[1]

    # sort list with key
    sorted_items = sorted(items, key=get_per_unit_value, reverse=True)
    
    curr_W = 0
    curr_V = 0
    
    i = 0
    while i < n:
        v, w = sorted_items[i]
        rest = W - curr_W # free space
        if w < rest:
            curr_W += w
            rest -= w
            curr_V += v
        else:
            curr_V = curr_V + (rest / w) * v
            break
        i+=1
    
    return curr_V


def test_function(items, W, n, expected_value):
    obtained_value = solution(items, W, n)
    res = ''
    if expected_value == obtained_value:
        res = 'Passed'
    else:
        res = 'Failed'
    
    print(f'{res}: expected: {expected_value}, obtained: {obtained_value}')


def test_1():
    items = [(60, 10), (100, 20), (120, 30)]
    W = 50
    n = 3
    expected_value = 240
    
    print('--- Test 1 ---')
    test_function(items, W, n, expected_value)


def test_2():
    items = [(60, 10), (100, 20)]
    W = 50
    n = 2
    expected_value = 160
    
    print('--- Test 2 ---')
    test_function(items, W, n, expected_value)


def test_3():
    items = [(60, 10), (100, 20)]
    W = 50
    n = 2
    expected_value = 160
    
    print('--- Test 3 ---')
    test_function(items, W, n, expected_value)


if __name__ == '__main__':
    test_1()
    test_2()

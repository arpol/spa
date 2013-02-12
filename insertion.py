from burstSettings import EOS

def sort(data, array, depth, L, R):

    def less(a, b):
        d = depth
        while True:
            c1 = data[a + d]
            c2 = data[b + d]
            if c1 < c2:
                return True
            if c2 < c1:
                return False
            if c1 == EOS == c2:
                return False
            d += 1
            
    if len(array) < 2:
        return

    for i in xrange(L + 1, R):
        j = i
        temp = array[i]
        while j > L and less(temp, array[j - 1]):
            array[j] = array[j - 1]
            j -= 1
        array[j] = temp

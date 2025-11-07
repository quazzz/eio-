n,m,q = map(int,input().split())
grid = []
for _ in range(n):
    row = list(map(int,input().split()))
    grid.append(row)

def otsi_reast(i, algus, lopp, size, max_h):
    """Leia suurim j kus grid[i][j + size - 1] <= max_h"""
    if algus > lopp:
        return -1
    result = -1
    while algus <= lopp:
        mid = (algus + lopp) // 2
        if mid + size - 1 >= m:
            lopp = mid - 1
            continue
        mxVal = grid[i][mid + size - 1]
        if mxVal <= max_h:
            result = mid
            algus = mid + 1
        else:
            lopp = mid - 1
    return result

def otsi_veerust(j, algus, lopp, size, min_h):
    """Leia väikseim i kus grid[i + size - 1][j] >= min_h"""
    if algus > lopp:
        return -1
    result = -1
    while algus <= lopp:
        mid = (algus + lopp) // 2
        if mid + size - 1 >= n:
            lopp = mid - 1
            continue
        mnVal = grid[mid + size - 1][j]
        if mnVal >= min_h:
            result = mid
            lopp = mid - 1
        else:
            algus = mid + 1
    return result

def sobib(size, min_h, max_h):
    if size == 0:
        return True
    
    # Strateegia: Proovi sadulameetodit IGAST võimalikust veerust
    for start_j in range(m - size + 1):
        i = 0
        j = start_j
        
        while i < n - size + 1 and j < m - size + 1:
            mnVal = grid[i + size - 1][j]
            mxVal = grid[i][j + size - 1]
            
            if min_h <= mnVal and mxVal <= max_h:
                return True
            
            if mxVal > max_h:
                # Leia kahendotsinguga parem j (väiksem max)
                new_j = otsi_reast(i, 0, j - 1, size, max_h)
                if new_j == -1:
                    break  # Selles reas ei ole enam sobivaid
                j = new_j
            elif mnVal < min_h:
                # Leia kahendotsinguga parem i (suurem min)
                new_i = otsi_veerust(j, i + 1, n - size, size, min_h)
                if new_i == -1:
                    break  # Selles veerus ei ole enam sobivaid
                i = new_i
            else:
                return True
    
    return False

for _ in range(q):
    min_h, max_h = map(int, input().split())
    lo, hi = 0, min(n, m)
    vastus = 0
    
    while lo <= hi:
        mid = (lo + hi) // 2
        if sobib(mid, min_h, max_h):
            vastus = mid
            lo = mid + 1
        else:
            hi = mid - 1
    
    print(vastus)
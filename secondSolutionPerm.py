from collections import Counter
#len(s1) < len(s2)
#s2 count = 1,1
#sliding window has to be length of s1 
#does s1 count = s2 count
s1 = 'ac'
s2 = 'abcee'
def perm(s1, s2):
    if len(s1) > len(s2):
        return False
    
    len_s1 = len(s1)
    s1count = Counter(s1)
    window_count = Counter()

    for i, c in enumerate(s2):
        print(i,c)
        window_count[c] += 1
        print(window_count[c], window_count)

        if i >= len_s1:
            l = s2[i - len_s1]
            if window_count[l] == 1:
                del window_count[l]
            else:
                window_count[l] -= 1
        if window_count == s1count:
            return True
    return False 
print(perm(s1, s2))
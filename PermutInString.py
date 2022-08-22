

def permutation(s1, s2):
    
    if len(s1) > len(s2):
        return False
    s1count = [0] * 26
    s2count = [0] * 26
    for i in range(len(s1)): #we're going to go through s1 and s2 at the same time
        s1count[ord(s1[i]) - ord('a')] += 1 #convert char at i'th index using ord function and subtract from it the ASCII value of 'a'
        # print(s1count)
        s2count[ord(s2[i]) - ord('a')] += 1
        # print(s2count)
    matches = 0
    for i in range(26):
        matches += (1 if s1count[i] == s2count[i] else 0)
        # print(matches)
    l = 0
    for r in range(len(s1), len(s2)):
        # print(r)
        if matches == 26: return True
        index = ord(s2[r]) - ord('a')
        # print(s2[r])
        print(s1count[index])
        s2count[index] += 1
        if s1count[index] == s2count[index]:
            matches += 1
        elif s1count[index] + 1 == s2count[index]:
            matches -= 1

        index = ord(s2[l]) - ord('a')
        s2count[index] -= 1
        if s1count[index] == s2count[index]:
            matches += 1
        elif s1count[index] - 1 == s2count[index]:
            matches -= 1
        l += 1
    return matches == 26
print(permutation('az', 'eiabza'))    
# print(permutation('ab', 'kjashdflka'))

#return true if s2 contains s1 in any order
#if the same characters are involved in any order, it's all good then
#make a window the size of s1 to look at s2
#everytime we're moving r just by 1, we subtract from left by 1: need 2 hashmaps
#-------but there is a better way------- of O(n)
#still 2 hash maps, one for s1 and one for s2
#plus a matches variable that equals the total number of matches between s1 and s2
#
#


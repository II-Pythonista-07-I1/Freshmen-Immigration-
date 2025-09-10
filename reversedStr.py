# Revearsed Str question


def reverseStringV1(s):
    right , left = len(s)-1 , 0
    while left<right:
        s[right] , s[left] = s[left] , s[right]
        right-=1
        left+=1
        
    return s

# OR We can just do this (:

def reverseStringV2(s):
    return s[::-1]

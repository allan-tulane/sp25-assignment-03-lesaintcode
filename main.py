import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED=None):

    if MED is None:
        MED = {}
    
    key = (S, T)

    
    if key in MED:
        return MED[key]
    
    if not S:
        MED[key] = len(T)
    
    elif not T:
        MED[key] = len(S)
    
    elif S[0] == T[0]:
        MED[key] = fast_MED(S[1:], T[1:], MED)
    
    else:
        INS = fast_MED(S, T[1:], MED)
        
        DELETE = fast_MED(S[1:], T, MED)
        
        MED[key] = 1 + min(INS, DELETE)

    
    return MED[key]


def fast_align_MED(S, T):
    memo = {}
    
    fast_MED(S, T, memo)

    i, j = len(S), len(T)
    
    s_aligned, t_aligned = [], []

    while i > 0 or j > 0:
        s_prefix, t_prefix = S[:i], T[:j]
        COST = memo.get((s_prefix, t_prefix), math.inf)

        MAT = i > 0 and j > 0 and S[i - 1] == T[j - 1]
        INS = j > 0 and memo.get((s_prefix, T[:j - 1]), math.inf) + 1 == COST
        DELETE = i > 0 and memo.get((S[:i - 1], t_prefix), math.inf) + 1 == COST

        if MAT:
            s_aligned.insert(0, S[i - 1])
            
            t_aligned.insert(0, T[j - 1])
            
            i -= 1
            
            j -= 1

        
        elif INS:
            s_aligned.insert(0, '-')
            
            t_aligned.insert(0, T[j - 1])
            
            j -= 1

        
        elif DELETE:
            s_aligned.insert(0, S[i - 1])
            
            t_aligned.insert(0, '-')
            
            i -= 1

        
        else:
            s_aligned.insert(0, S[i - 1] if i > 0 else '-')
            
            t_aligned.insert(0, T[j - 1] if j > 0 else '-')
            
            i = max(i - 1, 0)
            
            j = max(j - 1, 0)

    return ''.join(s_aligned), ''.join(t_aligned)


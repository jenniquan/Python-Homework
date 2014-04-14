statement = raw_input ("Insert statement: ")


vowelAll = set ('aeiouAEIOU')
vowelA = set ('aA')
vowelE = set ('eE')
vowelO = set ('iI')
vowelI = set ('oO')
vowelU = set ('uU')
countAll = 0
countA = 0
countE = 0
countI = 0
countO = 0
countU = 0
    
for char in statement:
    if char in vowelAll:
        countAll = countAll + 1
    if char in vowelA:
        countA = countA + 1
    if char in vowelE:
        countE = countE + 1
    if char in vowelI:
        countI = countI + 1
    if char in vowelO:
        countO = countO + 1
    if char in vowelU:
        countU = countU + 1

print "A: ", countA
print "E: ", countE
print "I: ", countI
print "O: ", countO
print "U: ", countU
print "Number of vowels total: ", countAll

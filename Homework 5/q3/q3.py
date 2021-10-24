# q3
def one_away(string1, string2):
    if abs(len(string1) - len(string2)) > 1:
        return False
    elif len(string1) == len(string2):
        return one_away_replace(string1,string2)
    elif len(string1) != len(string2):
        return one_away_diff(string1,string2)

def one_away_replace(string1, string2):
    matches = 0
    for i in range(len(string1)):
        if string1[i] == string2[i]:
            matches += 1
    return matches == len(string1) -1

def one_away_diff(string1, string2):
    matches = 0
    if len(string1) > len(string2):
        for i in range(len(string2)):
            if string2[i] in string1:
                matches += 1
        return matches == len(string2)
    elif len(string1) < len(string2):
        for i in range(len(string1)):
            if string1[i] in string2:
                matches += 1
        return matches == len(string1)   

print(one_away('pale','ple'))
print(one_away('pales','pale'))
print(one_away('pale','bale'))
print(one_away('pale','bake'))

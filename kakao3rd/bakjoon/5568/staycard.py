from itertools import permutations


def solution(n , k , p):
    print(p)
    resList = [''.join(p) for p in permutations(p,2)]
    print(set(resList))
    #print(list(combinations(p, 2)))


    return len(set(resList))


def permutations12(string, step = 0):

    # if we've gotten to the end, print the permutation
    if step == len(string):
        print ("".join(string))

    # everything to the right of step has not been swapped yet
    for i in range(step, len(string)):

        # copy the string (store as array)
        string_copy = [character for character in string]

        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        permutations(string_copy, step + 1)





data = "4,2,1,2,12,1"
testData = data.split(",")
print(solution(int(testData[0]),int(testData[1]),testData[2:6]))

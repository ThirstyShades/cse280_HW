### The following code provides several predicates (is_even, is_natural, and is_palindrome). There are multiple test cases that will determine whether the quantifier proposition is True or False given the specified domain. You need to implement the forall and exists functions. Hint: You will need to loop through all the items in the domain (which is a list) and use the predicate (which is a function) to test all or some of the values in the domain. ###



def is_even(x):
    if x % 2 == 0:
        return("True")
    else: 
        return("False")

def is_natural(x):
    if x == x > 0:
        return("True")
    else: 
        return("False")

def is_palindrome(x):
    if x == x[::-1]:
        return("True")
    else: 
        return("False")

def in_unit_circle(point):
    
    if (point[0]**2 + point[1]**2) <= 1:
        return("True")
    else: 
        return("False")

def forall(predicate, domain):
    print(f"\u2200x ({predicate.__name__}) domain={domain}")
    # Add your code here to return True or False
    #test print("True Test")
    # return(is_even(predicate))
    # if is_even(predicate) == 0:
    #     print("True")
    # else:
    #     print("Flase")
    if is_even(predicate) == True:
        return(True)
    
    else:
        pass
    



def exists(predicate, domain):
    print(f"\u2203x ({predicate.__name__}) domain={domain}")
    # Add your code here to return True or False

numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(forall(is_even,numbers1)) # False
print(exists(is_even,numbers1)) # True
print("================================")
print(forall(is_natural,numbers1)) # True
print(exists(is_natural,numbers1)) # True
print("================================")

numbers2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(forall(is_natural,numbers2)) # False
print(exists(is_natural,numbers2)) # True

print("================================")
words1 = ['civic', 'rotor', 'apple']
print(forall(is_palindrome,words1)) # False
print(exists(is_palindrome,words1)) # True
print("================================")

words2 = ['racecar', 'madam', '123454321']
print(forall(is_palindrome,words2)) # True
print(exists(is_palindrome,words2)) # True
print("================================")

words3 = ['no', 'palindromes', 'here']
print(forall(is_palindrome,words3)) # False
print(exists(is_palindrome,words3)) # False
print("================================")

points1 = [(0.5,0.5), (-1,0), (-0.75,-0.3)]
print(forall(in_unit_circle,points1)) # True
print(exists(in_unit_circle,points1)) # True
print("================================")

points2 = [(0.25,-1), (0.9,1.1), (0.1,-0.1)]
print(forall(in_unit_circle,points2)) # False
print(exists(in_unit_circle,points2)) # True
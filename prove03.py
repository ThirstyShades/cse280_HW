
# Set 1: {n | n ∈ {2, 4, 8, 16}}
Set1 = {n for n in {2, 4, 8, 16}}

# Set 2: {n^2 | n ∈ {-2, -1, 0, 1, 2}}
Set2 = {n**2 for n in {-2, -1, 0, 1, 2}}

# Set 3: {n | n ∈ Z+, n is a factor of 24}
Set3 = {n for n in range(1, 25) if 24 % n == 0}

# Set 4: {n | n ∈ Z, -10 ≤ n ≤ 10, n is odd}
Set4 = {n for n in range(-10, 11) if n % 2 != 0}


# Note that sets do not maintain order so it may vary
print(Set1)
print(Set2)
print(Set3)
print(Set4)
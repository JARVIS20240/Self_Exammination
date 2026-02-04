import numpy as np

"""
🟢 SECTION A — ARRAY CREATION & SHAPE (FOUNDATION)
Q1 Create a NumPy array of shape (6, 4) filled with value -1.

Q2 Create a 1D NumPy array containing 20 equally spaced values between 5 and 50 (inclusive).

Q3 Create a random integer array of shape (5, 3) with values between 100 and 999.
"""
# Q1:
arr_q1 = np.full((6,4), -1)
# print(f"Answer of Q1: \n{arr_q1}")

# Q2:
arr_q2 = np.linspace(5, 50, 20)
# print(f"Answer of Q2: \n{arr_q2}")

# Q3:
arr_q3 = np.random.randint(100, 999, size=(5,3))
# print(f"Answer of Q3: \n{arr_q3}")


"""
🟡 SECTION B — INDEXING, SLICING, AXIS (CORE)
Given:
data = np.array([[12, 45, 78, 34],
                 [56, 23, 89, 90],
                 [67, 88, 21, 45],
                 [90, 55, 60, 72]])

Q4 Extract:
i)      The second row
ii)     The last column
iii)    The sub-matrix:
[[45, 78],
 [23, 89]]

 Q5 Compute:
Column-wise sum
Row-wise mean

Q6 Sort the array:
Column-wise
Row-wise
"""
data = np.array([[12, 45, 78, 34],
                 [56, 23, 89, 90],
                 [67, 88, 21, 45],
                 [90, 55, 60, 72]])

# Q4.1:
print(data[1])

# Q4.2:
print(data[-1])

# Q4.3:
print(data[0:2,1:3])

# Q5:
print(f"Column-wise sum: \n{np.sum(data, axis=0)}") #Column-wise sum axis=0 == Column wise
print(f"Row-wise mean: \n{np.mean(data, axis=1)}")

# Q6:
print(f"Column-wise Sorting: \n{np.sort(data, axis = 0)}")
print(f"Row-wise Sorting: \n{np.sort(data, axis =1)}")

"""
🟠 SECTION C — BOOLEAN MASKING (FAIL HERE = NOT READY)

Q7 From data, extract all values greater than 50.

Q8 Replace all values less than 30 with 0 (modify array).

Q9 Extract values between 40 and 80 (inclusive).
"""
# Q7:
print(data[data > 50])

# Q8:
# replace = data[data < 30] = 0
print(data)

# Q9:
print(data[(data >= 40) & (data <= 80)])

"""
🟠 SECTION D — BROADCASTING & VECTORIZATION
Q10 Given:

salary = np.array([30000, 45000, 50000, 60000])
tax_rate = 10


Calculate net salary after tax using broadcasting.

Q11 Given a matrix (n_samples, n_features), subtract the mean of each feature.

Use this data:
X = np.array([[10, 20, 30],
              [20, 30, 40],
              [30, 40, 50]])
"""
# Q10:
salary = np.array([30000, 45000, 50000, 60000])
tax_rate = 10

net_salary = (salary * tax_rate / 100) + salary
print(net_salary)

# Q11:
X = np.array([[10, 20, 30],
              [20, 30, 40],
              [30, 40, 50]])

feature_mean = X.mean(axis=0)
result = X - feature_mean
print(result)

"""
🔴 SECTION E — RESHAPE, STACK, SORT
Q12 Convert a 1D array of size 24 into a (4, 6) matrix.

Q13 Stack the following vertically:

A = np.random.randint(1, 10, (3, 2))
B = np.random.randint(1, 10, (3, 2))

Q14 Find the index of the maximum value in each column.
"""
# Q12:
arr_q12 = np.random.randint(1, 99, 24)
print(arr_q12.reshape((4,6)))

# Q13:
A = np.random.randint(1, 10, (3, 2))
B = np.random.randint(1, 10, (3, 2))
print(A)
print(B)
stack = np.vstack((A,B))
print(stack)

# Q14:
print(stack.max(axis=0))

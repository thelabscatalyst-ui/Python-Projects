import numpy as np

np.random.seed(42)
a = np.random.choice([1,2,3,4],size = 10, replace= True) #choice 
b = np.random.randint(0,255, (3,4))
c = np.random.randn(3,4) # range is [0,1)

print(c)

a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print (a[0])
print (a[1,0]) # 2 digits means first is row and second is collumn

print (a[-1])
print (a[-1,-1]) # -1 stands for last thing 

# Slicing: [row_start:row_end, col_start:col_end]
print (a[:,:2])
print (a[1:,:])

# Boolean masking reffers to change the matrix with the condition 
mask = (a>2) & (a<9)
print (a[mask])

a = np.arange(1, 13)
print (a.reshape(3,4))
print(a.reshape(-1, 6)) # -1 automatically thinks what size needs to be put up accoridngly
# similarly can happens with rows 

b = a.reshape(3,4)
print(b.flatten())

b = a.reshape(3,4)
print(b.ravel())
print(a)

a = a.reshape(3,4)
print(a)
print (a.T)
print(a.transpose(1,0))

a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print (a[np.newaxis, :])
print (a[:, np.newaxis])
print (np.squeeze(a))

# you need to assume that tehre are tow axises in total = 0,1
# 0 is collumn, and 1 is row

a = np.array([[1,2,3], [4,5,6], [7,8,9]])
b = np.array([[10,11,12], [13,14,15], [16,17,18]])
print (np.stack([a,b], axis = 0)) # stack along the row

a = np.array([[1, 2, 3],
[4, 5, 6]])
# --- Reductions (default: over all elements) ---
np.sum(a) # 21
np.sum(a, axis=0) # Column-wise: [5, 7, 9]
np.sum(a, axis=1) # Row-wise: [6, 15]
np.sum(a, keepdims=True) # Preserve shape: [[21]]
np.mean(a) # 3.5
np.median(a) # 3.5
np.std(a) # Standard deviation
np.var(a) # Variance
np.max(a) # 6
np.min(a) # 1
np.argmax(a) # 5 (index in flattened array)
np.argmax(a, axis=1) # [2, 2] (index of max per row)
np.argmin(a, axis=0) # [0, 0, 0] (index of min per col)
# --- Sorting ---
np.sort(a) # Sort each row ascending
np.sort(a, axis=0) # Sort each column
np.argsort(a) # Indices that would sort the array
np.argsort(a)[::-1] # Reverse sort indices
# --- Unique & counts ---
arr = np.array([1, 2, 2, 3, 3, 3])
np.unique(arr) # [1, 2, 3]
vals, counts = np.unique(arr, return_counts=True) # [1,2,3], [1,2,3]
# --- Cumulative ---
np.cumsum(a) # [1, 3, 6, 10, 15, 21]
np.cumprod(a) # [1, 2, 6, 24, 120, 720]
# --- Percentiles ---
np.percentile(a, 50) # Median
np.percentile(a, [25, 75]) # Q1 and Q3

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print (np.linalg.eig(a))
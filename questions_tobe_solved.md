🔹 Level 1 — Core Python
1. Reverse a string without using slicing
Input
s = "machinelearning"
Expected output
"gninraelgnihcenam"
2. Find the second largest number in a list
Input
nums = [10, 5, 8, 20, 15, 20, 3]
Expected output
15
Consider whether duplicate maximum values should count as the same number.
3. Remove duplicates while maintaining order
Input
nums = [4, 2, 4, 5, 2, 3, 5, 1]
Expected output
[4, 2, 5, 3, 1]
4. Count frequency of each character
Input
s = "machinelearning"
Expected output
{
    'm': 1,
    'a': 1,
    'c': 1,
    'h': 1,
    'i': 2,
    'n': 3,
    'e': 2,
    'l': 1,
    'r': 1,
    'g': 1
}
5. Check if two strings are anagrams
Input
s1 = "listen"
s2 = "silent"
Expected output
True
Test this too:
s1 = "hello"
s2 = "world"
Expected:
False
6. Find the first non-repeating character
Input
s = "aabbcdeeff"
Expected output
c
7. Flatten a nested list
Input
nested = [[1, 2], [3, 4], [5, 6]]
Expected output
[1, 2, 3, 4, 5, 6]
Try this afterward:
nested = [[1, 2], [3, [4, 5]], [6]]
Decide whether your function handles only one level or arbitrarily nested lists.
8. Find common elements in two lists
Input
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
Expected output
[3, 4, 5]
9. Rotate a list by k steps
Input
nums = [1, 2, 3, 4, 5]
k = 2
Expected output
[4, 5, 1, 2, 3]
Assume rotation is to the right.
10. Check if a number is a palindrome
Input
num = 1221
Expected output
True
Another:
num = 1234
Expected:
False
🔹 Level 2 — Intermediate Python
11. Implement your own map()
Input
nums = [1, 2, 3, 4, 5]

function = square
Where conceptually:
square(x) → x * x
Expected output
[1, 4, 9, 16, 25]
12. Implement your own filter()
Input
nums = [1, 2, 3, 4, 5, 6, 7, 8]
Filter condition:
keep numbers divisible by 2
Expected output
[2, 4, 6, 8]
13. Fibonacci generator
Generate the first 10 Fibonacci numbers.
Input

n = 10
Expected output
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
14. Longest substring without repeating characters
Input
s = "abcabcbb"
Expected output
3
One valid longest substring is:
"abc"
15. Group words that are anagrams
Input
words = [
    "eat",
    "tea",
    "tan",
    "ate",
    "nat",
    "bat"
]
Expected output
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
Order of groups doesn't matter.
16. Merge two sorted lists
Input
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
Expected output
[1, 2, 3, 4, 5, 6, 7, 8]
17. Implement LRU Cache
Capacity:
capacity = 2
Operations:
put(1, "A")
put(2, "B")
get(1)
put(3, "C")
get(2)
get(3)
Expected outputs for get() operations
get(1) → "A"
get(2) → -1
get(3) → "C"
Because key 2 becomes the least recently used and gets removed.
18. Find all pairs with given sum
Input
nums = [2, 4, 3, 5, 7, 8, 9]
target = 7
Expected output
[(2, 5), (4, 3)]
Order doesn't matter.
19. Detect cycle in a linked list
Example:
1 → 2 → 3 → 4
        ↑     |
        |_____|
Represent it conceptually as:
1 → 2 → 3 → 4
        ↑       |
        └───────
Expected output
True
Second test:
1 → 2 → 3 → 4 → None
Expected:
False
20. Implement stack using queues
Operations:
push(10)
push(20)
push(30)
pop()
pop()
push(40)
pop()
Expected output
30
20
40
🔹 Level 3 — NumPy
For these, you should actually create the arrays in NumPy rather than manually typing the expected result.
21. Create a 5×5 matrix and normalize it
Input
np.random.seed(42)
matrix = np.random.randint(1, 100, (5, 5))
Your task:
Normalize values between 0 and 1.
Expected property:
minimum = 0
maximum = 1
22. Mean, median and standard deviation
Input
data = np.array([10, 20, 30, 40, 50])
Expected output
Mean = 30
Median = 30
Standard deviation ≈ 14.14
23. Replace negative values with 0
Input
arr = np.array([-5, 3, -2, 8, -10, 4])
Expected output
[0, 3, 0, 8, 0, 4]
24. Compute dot product manually and with NumPy
Input
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
Expected output
32
Because:
1×4 + 2×5 + 3×6 = 32
25. Broadcasting
Input
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

vector = np.array([10, 20, 30])
Add the vector to every row.
Expected output

[
    [11, 22, 33],
    [14, 25, 36],
    [17, 28, 39]
]
🔹 Level 3 — Pandas
For these, create a small DataFrame yourself.
26. Find missing values
Input
data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, None, 30, 28],
    "salary": [50000, 60000, None, 55000]
}
Expected missing values
age       → 1
salary    → 1
name      → 0
27. Fill missing values using mean/median
Using the same dataset:
age = [25, None, 30, 28]
Fill the missing age using the mean.
Expected

Mean = 27.67
So:
[25, 27.67, 30, 28]
28. Group by category and calculate average
Input
data = {
    "department": ["IT", "IT", "HR", "HR", "Sales"],
    "salary": [60000, 70000, 50000, 55000, 65000]
}
Expected output
HR     → 52500
IT     → 65000
Sales  → 65000
29. Find top 5 values
Input
data = {
    "name": ["A", "B", "C", "D", "E", "F"],
    "salary": [50000, 80000, 60000, 95000, 70000, 90000]
}
Expected names
D
F
B
E
C
30. Merge two datasets
Dataset 1
employees = {
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"]
}
Dataset 2
salary = {
    "id": [1, 2, 3],
    "salary": [60000, 70000, 80000]
}
Expected output
id   name      salary
1    Alice     60000
2    Bob       70000
3    Charlie   80000
31. Filter rows using multiple conditions
Input
data = {
    "name": ["A", "B", "C", "D"],
    "age": [22, 30, 25, 35],
    "salary": [40000, 70000, 60000, 90000]
}
Find:
People older than 24 AND salary greater than 50000.
Expected
B
C
D
32. Create a new column based on conditions
Input
salary = [40000, 60000, 80000, 100000]
Create:
salary >= 70000 → "High"
salary < 70000  → "Low"
Expected
Low
Low
High
High
33. Handle duplicate rows
Input
data = {
    "name": ["Alice", "Bob", "Alice", "Charlie", "Bob"],
    "age": [25, 30, 25, 35, 30]
}
Remove duplicates.
Expected

Alice    25
Bob      30
Charlie  35
🔹 Level 4 — ML-Oriented Coding
These are where your Python starts becoming actual ML programming.
34. Linear Regression from scratch
Input
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
The relationship is:
y = 2x
Your model should learn approximately:
weight ≈ 2
bias ≈ 0
35. Implement Gradient Descent
Use:
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
Start with:
weight = 0
learning_rate = 0.01
epochs = 1000
Expected:
weight → approximately 2
36. Calculate MSE
Input
actual = np.array([3, 5, 7, 9])
predicted = np.array([2, 5, 8, 10])
Expected
MSE = 0.75
37. Min-Max normalization
Input
X = np.array([10, 20, 30, 40, 50])
Expected
[0.00, 0.25, 0.50, 0.75, 1.00]
38. Standardization / Z-score
Input
X = np.array([10, 20, 30, 40, 50])
Expected properties:
mean ≈ 0
std ≈ 1
39. Train/test split manually
Input
X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Use:
80% training
20% testing
Expected sizes:
Training = 8
Testing  = 2
40. Accuracy, Precision and Recall
Input
Actual:    [1, 1, 1, 0, 0, 0, 1, 0]
Predicted: [1, 1, 0, 0, 1, 0, 1, 0]
Calculate:
Accuracy
Precision
Recall
F1
Don't look up the formulas initially—try to derive them from TP, TN, FP and FN.
41. KNN from scratch
Training data
X = [
    [1, 1],
    [2, 2],
    [3, 3],
    [8, 8],
    [9, 9],
    [10, 10]
]

y = [
    "A",
    "A",
    "A",
    "B",
    "B",
    "B"
]
Prediction:
new_point = [4, 4]
k = 3
Expected
A
42. Logistic Regression
Use this binary classification dataset:
X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6]
])

y = np.array([
    0,
    0,
    0,
    1,
    1,
    1
])
Train your model and predict:
X_test = np.array([
    [2.5],
    [5.5]
])
Expected predictions approximately:
[0, 1]
43. K-Means clustering
Input
X = np.array([
    [1, 1],
    [1, 2],
    [2, 1],
    [8, 8],
    [9, 8],
    [8, 9]
])
Use:
k = 2
Expected:
Cluster 1 → first 3 points
Cluster 2 → last 3 points
Cluster labels 0 and 1 can be reversed.
🔹 Level 5 — Problem Solving
These are more DSA/interview-focused.
44. Top K frequent elements
Input
nums = [1, 1, 1, 2, 2, 3]
k = 2
Expected
[1, 2]
45. Sliding window maximum
Input
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
Expected
[3, 3, 5, 5, 6, 7]
46. Longest increasing subsequence
Input
nums = [10, 9, 2, 5, 3, 7, 101, 18]
Expected length
4
One valid subsequence:
[2, 3, 7, 101]
47. Minimum window substring
Input
s = "ADOBECODEBANC"
t = "ABC"
Expected
"BANC"
48. Merge intervals
Input
intervals = [
    [1, 3],
    [2, 6],
    [8, 10],
    [9, 12]
]
Expected
[
    [1, 6],
    [8, 12]
]
49. Search in rotated sorted array
Input
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
Expected
4
Because 0 is at index 4.
50. Median of two sorted arrays
Input
nums1 = [1, 3]
nums2 = [2]
Expected
2.0
Second test:
nums1 = [1, 2]
nums2 = [3, 4]
Expected:
2.5
51. Word Break
Input
s = "leetcode"

wordDict = ["leet", "code"]
Expected
True
Second:
s = "catsandog"

wordDict = ["cats", "dog", "sand", "and", "cat"]
Expected:
False
52. Subarray Sum Equals K
Input
nums = [1, 1, 1]
k = 2
Expected
2
53. Design a Rate Limiter
Suppose:
Maximum = 3 requests
Time window = 10 seconds
Requests:
User A → 0 sec
User A → 2 sec
User A → 5 sec
User A → 7 sec
User A → 11 sec
Expected:
0 sec  → Allowed
2 sec  → Allowed
5 sec  → Allowed
7 sec  → Rejected
11 sec → Allowed
🔹 Level 6 — Real ML Questions
These are less about solving a puzzle and more about thinking like an ML engineer.
54. Detect outliers
Input
data = np.array([10, 11, 12, 10, 13, 12, 11, 100])
Find the outlier.
Expected

100
Try solving it using:
Z-score
IQR
55. Handle missing values
Input
data = {
    "age": [22, 25, None, 30, None],
    "salary": [40000, None, 60000, 70000, 80000]
}
Your task:
Decide how to handle the missing values.
Don't just fill everything with zero. Think about what would make sense for an ML dataset.
56. Encode categorical variables
Input
data = {
    "gender": ["Male", "Female", "Female", "Male"],
    "city": ["Adelaide", "Sydney", "Melbourne", "Adelaide"]
}
Task:
Convert categorical features into numerical features suitable for an ML model.
Try:
Label encoding
One-hot encoding
57. Feature scaling pipeline
Input
X = np.array([
    [25, 50000],
    [30, 60000],
    [35, 80000],
    [40, 100000]
])
Features:
Age
Salary
Task:
Build a preprocessing pipeline that scales both features.
Then inspect the transformed data.
58. Evaluate a classification model
Input
y_true =    [1, 1, 1, 0, 0, 0, 1, 0, 1, 0]

y_pred =    [1, 1, 0, 0, 1, 0, 1, 0, 1, 1]
Calculate:
Accuracy
Precision
Recall
F1
Confusion Matrix
ROC-AUC
Then answer:
Is this model good?
Don't judge it using accuracy alone.
59. Handle imbalanced data
Suppose:
Total samples = 10,000

Class 0 = 9,500
Class 1 = 500
Task:
How would you handle this dataset?
Try implementing at least:
class weights
oversampling
undersampling
60. Feature selection
Input
features = [
    "age",
    "salary",
    "height",
    "random_number",
    "years_experience",
    "noise"
]
Suppose your target is:
salary_prediction
Task:
Determine which features are useful and which aren't.
Try:
Correlation
Feature importance
SelectKBest
61. Avoid overfitting
Suppose:
Training accuracy = 99%
Validation accuracy = 72%
Task:
What is happening?
Then implement at least 3 techniques to reduce overfitting.
Examples:

Regularization
Cross-validation
Dropout
Early stopping
Reducing model complexity
62. Build an ML pipeline
Use a dataset like:
X = [
    [22, 40000],
    [25, 50000],
    [30, 60000],
    [35, 80000],
    [40, 100000]
]

y = [0, 0, 0, 1, 1]
Build:
Data
 ↓
Train/Test Split
 ↓
Scaling
 ↓
Model
 ↓
Prediction
 ↓
Evaluation
Use sklearn.
63. Save and load a trained model
Train a simple model:
X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]
Task:
Train model
Save model to disk
Load model
Predict:
[[6]]
Expected:
≈ 12
🎯 How I want you to approach these
Since you said you already have an idea of Python, don't spend weeks relearning syntax.
Do them in this order:

Level 1 → Level 2 → Level 3 → Level 4 → Level 6

You can leave Level 5 for later.

For each problem:

Try it yourself first
Don't immediately search Google/ChatGPT
Get your code working
Then ask: "Can I make this more efficient?"
Think about time and space complexity
Only then look at another solution
For the ML path specifically, Levels 1–4 and 6 are much more valuable to you than grinding 200 LeetCode questions.
If you want to work through them with me, start with Question 1 and send me your code. I'll review it, point out what's good/wrong, and then give you the next question without giving you the answer upfront.

# Python Lab Programs

This repository contains six Python programs covering **Divide and Conquer, Dynamic Programming, Python Packages, Generators, Object-Oriented Programming, Abstraction, Inheritance, Type Hints, and Dataclasses**.

---

## 1. Divide-and-Conquer Merge Sort

### Aim

To implement the Divide-and-Conquer Merge Sort algorithm in Python and analyze its time complexity.

### Description

Merge Sort divides an array into smaller subarrays, sorts them recursively, and then merges the sorted subarrays.

### Input

```text
[38, 27, 43, 3, 9, 82, 10]
```

### Output

```text
Original Array: [38, 27, 43, 3, 9, 82, 10]
Sorted Array: [3, 9, 10, 27, 38, 43, 82]
```

### Complexity

* Best Case: O(n log n)
* Average Case: O(n log n)
* Worst Case: O(n log n)
* Space Complexity: O(n)

### Key Concept

**Divide and Conquer**

---

## 2. Dynamic Programming 0/1 Knapsack

### Aim

To implement the Dynamic Programming solution for the 0/1 Knapsack problem and analyze its time and space complexity.

### Description

The 0/1 Knapsack problem selects items with given weights and values so that the total weight does not exceed the capacity while maximizing the total value.

Each item can either be selected once or not selected.

### Input

```text
Weights  = [2, 3, 4, 5]
Values   = [3, 4, 5, 6]
Capacity = 5
```

### Output

```text
Maximum Value: 7
```

### Complexity

* Time Complexity: O(n × W)
* Space Complexity: O(n × W)

where:

* `n` = number of items
* `W` = maximum capacity

### Key Concept

**Dynamic Programming**

---

## 3. Stack and Queue Using Type Hints and Dataclasses

### Aim

To develop a reusable Python package implementing Stack and Queue using type hints and dataclasses.

### Description

This program implements two commonly used data structures:

* Stack
* Queue

The implementation uses:

* Dataclasses
* Generic types
* Type hints
* Python packages

### Stack Operations

```text
push()
pop()
peek()
is_empty()
```

### Queue Operations

```text
enqueue()
dequeue()
front()
is_empty()
```

### Example Output

```text
Stack Top: 30
Stack Pop: 30
Queue Front: A
Queue Dequeue: A
```

### Complexity

#### Stack

* Push: O(1)
* Pop: O(1)
* Peek: O(1)

#### Queue

* Enqueue: O(1)
* Dequeue: O(n)
* Front: O(1)

### Key Concepts

**Packages, Dataclasses, Generics and Type Hints**

---

## 4. List-Based and Generator-Based Processing

### Aim

To compare list-based processing and generator-based processing for a large dataset in terms of execution time and memory usage.

### Description

The program processes one million numbers using:

1. A list
2. A generator

Memory usage is measured using `tracemalloc`, while execution time is measured using `time.perf_counter()`.

### Input

```text
Dataset Size = 1,000,000
```

### Output

```text
List Result: 333332833333500000
Generator Result: 333332833333500000
```

The exact execution time and memory usage depend on the computer.

### Comparison

| Feature       | List                 | Generator                   |
| ------------- | -------------------- | --------------------------- |
| Memory Usage  | Higher               | Lower                       |
| Data Storage  | Stores all values    | Produces values when needed |
| Processing    | Immediate            | Lazy                        |
| Large Dataset | More memory required | More memory efficient       |

### Key Concept

**Generators and Lazy Evaluation**

---

## 5. Banking Management System

### Aim

To develop a Banking Management System demonstrating inheritance and abstraction with full type hints.

### Description

The program creates an abstract `BankAccount` class and derives:

* `SavingsAccount`
* `CurrentAccount`

The system supports:

* Deposit
* Withdrawal
* Balance display
* Interest calculation

### Example Input

```text
Savings Account
Initial Balance = 10000
Deposit = 2000
Withdrawal = 1000
Interest Rate = 4%

Current Account
Balance = 15000
Interest Rate = 2%
```

### Output

```text
Savings Account
Account Number: 101
Holder Name: Surya
Balance: 11000
Interest: 440.0

Current Account
Account Number: 102
Holder Name: Ramya
Balance: 15000
Interest: 300.0
```

### Concepts Demonstrated

* Abstraction
* Inheritance
* Polymorphism
* Type Hints
* Dataclasses
* Abstract Classes

### Key Concept

**Object-Oriented Programming**

---

## 6. Student Data Model Using Dataclass and Traditional Class

### Aim

To implement a Student data model using dataclasses and compare it with a traditional class implementation.

### Description

The program implements the same Student data model using:

1. Traditional Python class
2. Python dataclass

The student contains:

```text
Name
Roll Number
Marks
```

### Output

```text
Traditional Class:
Surya 101 85.5

Dataclass:
Ramya 102 91.5

Dataclass Object:
Student(name='Rahul', roll_no=102, marks=91.5)
```

### Comparison

| Feature                  | Traditional Class | Dataclass               |
| ------------------------ | ----------------- | ----------------------- |
| Constructor              | Manually written  | Automatically generated |
| `__repr__()`             | Manual            | Automatically generated |
| `__eq__()`               | Manual            | Automatically generated |
| Boilerplate Code         | More              | Less                    |
| Suitable for Data Models | Yes               | Very suitable           |

### Key Concept

**Dataclasses and Object-Oriented Programming**

---

# Technologies Used

* Python 3
* Type Hints
* Dataclasses
* Generics
* Abstract Base Classes
* Dynamic Programming
* Divide and Conquer
* Generators
* Object-Oriented Programming

---

# Concepts Covered

| Program           | Main Concept                   |
| ----------------- | ------------------------------ |
| Merge Sort        | Divide and Conquer             |
| 0/1 Knapsack      | Dynamic Programming            |
| Stack & Queue     | Data Structures & Packages     |
| List vs Generator | Generators & Memory Management |
| Banking System    | Abstraction & Inheritance      |
| Student Model     | Dataclasses                    |

---

# How to Run

Make sure Python 3 is installed.

Check the Python version:

```bash
python --version
```

Run an individual program:

```bash
python program.py
```

For the Stack and Queue package, keep the files in the same project directory and run:

```bash
python main.py
```

---

# Conclusion

These six programs demonstrate important Python programming concepts and algorithmic techniques. They cover efficient algorithms such as Merge Sort and 0/1 Knapsack, reusable data structures using packages, memory-efficient generators, and object-oriented programming using abstraction, inheritance, type hints, and dataclasses.

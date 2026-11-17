

# 🧪 Test Cases - Python Online Examination System

This document contains the test cases performed to verify the functionality of the Python Online Examination System.

---

# Test Case 1: Pass with Minimum Passing Score

## Description
Verify that the system correctly calculates the score and declares **Pass** when the user achieves exactly 40%.

## Inputs

| Question | User Answer | Result |
|-----------|------------|---------|
| Q1 | b | Correct |
| Q2 | c | Correct |
| Q3 | a | Wrong |
| Q4 | a | Wrong |
| Q5 | a | Wrong |

## Expected Output

- Correct Answers = 2
- Wrong Answers = 3
- Skipped Questions = 0
- Score = 4/10
- Percentage = 40%
- Result = Pass

## Actual Output

✅ Test Passed

### Screenshot

![Test Case 1](sampleOutput (1))

---

# Test Case 2: High Score Pass

## Description

Verify that the system correctly calculates marks and percentage when most answers are correct.

## Inputs

| Question | User Answer | Result |
|-----------|------------|---------|
| Q1 | b | Correct |
| Q2 | c | Correct |
| Q3 | a | Wrong |
| Q4 | b | Correct |
| Q5 | b | Correct |

## Expected Output

- Correct Answers = 4
- Wrong Answers = 1
- Skipped Questions = 0
- Score = 8/10
- Percentage = 80%
- Result = Pass

## Actual Output

✅ Test Passed

### Screenshot

![Test Case 2](sampleOutput%20(1).png)

---

# Additional Test Cases

## Test Case 3: All Correct Answers

### Input

```text
b
c
b
b
b
```

### Expected Output

```text
Corrected: 5
Wrong: 0
Skipped: 0
Score: 10/10
Percentage: 100.00%
Result: Pass
```

✅ Expected Behavior Verified

---

## Test Case 4: All Wrong Answers

### Input

```text
a
a
a
a
a
```

### Expected Output

```text
Corrected: 0
Wrong: 5
Skipped: 0
Score: 0/10
Percentage: 0.00%
Result: Fail
```

✅ Expected Behavior Verified

---

## Test Case 5: All Questions Skipped

### Input

```text
s
s
s
s
s
```

### Expected Output

```text
Corrected: 0
Wrong: 0
Skipped: 5
Score: 0/10
Percentage: 0.00%
Result: Fail
```

✅ Expected Behavior Verified

---

## Test Case 6: Invalid Input Handling

### Input

```text
x
1
@
b
```

### Expected Output

The system should display:

```text
Invalid Options: Enter a ,b c, d or s to skip.
```

until a valid option is entered.

✅ Expected Behavior Verified

---

# Test Summary

| Test Case | Status |
|------------|---------|
| Pass at 40% | ✅ Passed |
| High Score Pass | ✅ Passed |
| All Correct | ✅ Passed |
| All Wrong | ✅ Passed |
| All Skipped | ✅ Passed |
| Invalid Input Handling | ✅ Passed |

---

## Conclusion

All major functionalities of the Online Examination System were tested successfully, including:

- Answer Validation
- Score Calculation
- Percentage Calculation
- Pass/Fail Logic
- Skip Functionality
- Invalid Input Handling

The application behaves as expected under all tested scenarios.
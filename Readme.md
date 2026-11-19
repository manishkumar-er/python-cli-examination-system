## About ME !

    * Name: Manish Kumar
    * ERP : 01355
    * Section: M
    * Class : SA16
#### Project-Tile: Online_Examination-System


# 📝Python Online Examination System
    
📌Project Overview

     PyExam Console is a console-based online examination system developed in Python. It allows users to attempt multiple-choice questions (MCQs), validates user input, evaluates responses, calculates scores automatically, and displays the final result along with performance statistics.


This project is designed to demonstrate fundamental Python programming concepts such as functions, lists, dictionaries, loops, conditional statements, user input handling, and result processing.



[🚀] Features:- 
   * Multiple Choice Question (MCQ) based examination
   * Five pre-defined quiz questions
   * Four answer options for each question (a/A,b/B,c/C,d/D)
   * Option to skip questions
   * Input validation for incorrect entries
   * Automatic score calculation
   * Percentage calculation
   * Pass/Fail result generation
   * Summary of correct, wrong, and skipped answers
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
[📂] Project Structure:- 
    The entire examination system is implemented inside a single function:

    def online_exam():
    This improves code organization, readability, and reusability.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
[🗃] Question Bank:----
    Questions are stored using a List of Dictionaries.
    Example:

    {
        "q": "Python is written in which language?",
        "options": "a) C++  b) C  c) Python  d) None",
        "ans": "b"
    }
    Dictionary Keys
    Key	Description
    q	Question text
    options	Available answer choices
    ans	Correct answer
    This structure makes it easy to add, modify, or remove questions.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

[🎯] Variables Used:-----
   * (Total Marks)
    total_marks = 10
    The exam consists of 5 questions, each carrying 2 marks.

    * (Correct Answers Counter)
    correct = 0
    Stores the number of correctly answered questions.

   * (Wrong Answers Counter)
    wrong = 0
    Stores the number of incorrectly answered questions.

   * (Skipped Questions Counter)
    skip = 0
    Stores the number of skipped questions.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

[📢] User Instructions:----
    Before the examination begins, the program displays instructions to help the user understand:

   * Total number of questions
   * Available answer options
   * How to skip a question
   * Input format requirements
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

[🔄] Examination Flow::-----
    The examination process uses a for loop to iterate through each question.

    for question in container:
    For every question, the following steps occur:

    Display the question.
    Display available options.
    Accept user input.
    Validate the input.
    Evaluate the response.
    Update result counters.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

[✅] Input Validation::-----
    A while loop ensures that only valid inputs are accepted.

    while(True):
    Accepted inputs:

    a
    b
    c
    d
    s
    Where:
        a, b, c, d → Answer choices
        s → Skip the question
        Invalid inputs are rejected and the user is prompted again.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
[🎯] Answer Evaluation Logic:-----
    Correct Answer
    if choose_opt == question["ans"]:
        correct += 1
    The correct answer counter is incremented.

    Skipped Question
    elif choose_opt == "s":
        skip += 1
    The skipped question counter is incremented.

    Wrong Answer
    else:
        wrong += 1
    The wrong answer counter is incremented.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
[📊] Score Calculation::-----
    Obtained Marks
            obtained_marks = 2 * correct
            Each correct answer awards 2 marks.

    Example:
            4 Correct Answers
            Score = 4 × 2 = 8
            Percentage Calculation
            percentage = (obtained_marks / total_marks) * 100
    Formula:
         Percentage = (Obtained Marks / Total Marks) × 100
    Example:
          8 / 10 × 100 = 80%
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

[🏆] Result Declaration
    The program evaluates the final percentage to determine the result.

    if percentage >= 40:
    Criteria
        Percentage ≥ 40%  → PASS
        Percentage < 40%  → FAIL
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

[📋] Final Report::----
    After completion of the examination, the system displays:

   -> Number of Correct Answers
   -> Number of Wrong Answers
   -> Number of Skipped Questions
   -> Total Score
   -> Percentage
   -> Pass/Fail Result

    Example:
        Correct: 4
        Wrong: 1
        Skipped: 0

        Score: 8/10
        Percentage: 80%

        Result: PASS
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
[🧠] Python Concepts Demonstrated::------
        {This project covers the following Python fundamentals}

     Functions:
        def online_exam():
        Lists
        container = []
        Dictionaries
        {
            "q": "",
            "options": "",
            "ans": ""
        }
    
    For Loops:
        for question in container

    While Loops:
        while(True)

    Conditional Statements:
                        if
                        elif
                        else

    User Input Handling:
                 input()

    Formatted Strings (f-Strings):
              f"Percentage: {percentage:.2f}%"

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
🔮 Future Enhancements
        Potential improvements include:

        (:)User Authentication System
        (:)Question Timer
        (:)Negative Marking
        (:)Random Question Generation
        (:)Category-wise Quizzes
        (:)Database Integration
        (:)Performance History
        (:)Leaderboard System
        (:)GUI using Tkinter
        (:)Web Application using Flask or Django
        (:)Exportable Result Reports

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
🎓 Learning Outcomes:::-----
    After studying this project, a beginner will understand:

    (*)Function creation and usage
    (*)List and Dictionary data structures
    (*)Loop implementation
    (*)Conditional decision-making
    (*)Input validation techniques
    (*)Score calculation logic
    (*)Percentage calculation
    (*)Basic project design and organization
    (*)Console-based application development
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

[✅] Conclusion::---
         Terminal Console is a beginner-friendly Python project that simulates an online examination environment. It effectively demonstrates core Python programming concepts while providing a practical example of user interaction, input validation, result processing, and performance evaluation.
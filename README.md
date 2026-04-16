# Task-1-MuhammadDawood
# 📝 Simple Task Manager (Python CLI)

This is a beginner-friendly Python program that lets users create, view, and modify a list of tasks directly from the command line.

---

## 🚀 Features

* Add multiple tasks dynamically
* View all tasks with index numbers
* Modify any existing task
* Simple and interactive user input system

---

## 📌 How It Works

1. The program asks you to enter tasks one by one
2. You can keep adding tasks by pressing `y`
3. Press `n` to stop adding tasks
4. All tasks are displayed with their index numbers
5. You get an option to modify any task
6. If you choose to modify:

   * Enter the task number (index)
   * Enter the new task
7. Updated task list is displayed

---

## 💻 Example Run

```
Enter the task: Study Python
Press y to enter tasks or n to stop: y
Enter the task: Build project
Press y to enter tasks or n to stop: n

0 Study Python
1 Build project

Press y to modify any task or n to keep the previous tasks: y
Enter the task number to modify: 0
Enter the new task: Practice Python

0 Practice Python
1 Build project
```

---

## ⚙️ Requirements

* Python 3.x

---

## ▶️ How to Run

1. Save the code in a file, for example:

   ```
   task_manager.py
   ```
2. Open terminal or command prompt
3. Run the script:

   ```
   python task_manager.py
   ```

---

## 📚 Concepts Used

* Lists
* Loops (`while`, `for`)
* Conditional statements (`if`)
* User input (`input()`)
* List indexing and modification

---

## 🧠 Notes

* Task numbers start from `0` (index-based)
* Make sure to enter a valid task number when modifying
* This is a basic version — can be extended with:

  * Delete task feature
  * Save tasks to file
  * GUI interface

---

## 📄 License

This project is open-source and free to use for learning purposes.

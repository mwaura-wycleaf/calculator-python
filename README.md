# 🧮 Simple Python Calculator

A command-line calculator built in Python that performs basic arithmetic operations, supports memory functions, and keeps track of calculation history.

---

## 🚀 Features

- ✅ Addition
- ✅ Subtraction
- ✅ Multiplication
- ✅ Division (with division-by-zero handling)
- ✅ Memory Functions:
  - **M+** → Store value
  - **MR** → Recall value
  - **MC** → Clear memory
- ✅ Stores last **5 calculations** in history
- ✅ Input validation (prevents crashes from invalid input)
- ✅ Option to reuse stored memory in calculations
- ✅ Clean menu-driven interface

---

## 📂 Project Structure

```
calculator.py
README.md
```

---

## 🛠️ How It Works

### 1️⃣ Arithmetic Operations

The calculator supports:

| Operation        | Symbol | Description |
|------------------|--------|------------|
| Addition         | `+`    | Adds two numbers |
| Subtraction      | `-`    | Subtracts second number from first |
| Multiplication   | `*`    | Multiplies two numbers |
| Division         | `/`    | Divides first number by second (prevents division by zero) |

---

### 2️⃣ Memory Functions

The calculator includes built-in memory functionality:

- **M+** → Stores a value in memory
- **MR** → Recalls stored value
- **MC** → Clears stored memory
- You can enter `'M'` during number input to use the stored value.

---

### 3️⃣ History Feature

- Stores up to **5 most recent calculations**
- Users can:
  - View history
  - Clear history manually

Example history entry:

```
5.0 + 3.0 = 8.0
```

---

## 📥 Installation & Usage

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/calculator-python.git
cd calculator-python
```

### Step 2: Run the calculator

```bash
python calculator.py
```

Make sure you have **Python 3.x** installed.

---

## 🖥️ Example Usage

```
=== Simple Calculator ===
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exit
6. Memory Functions (M+, MR, MC)
7. View History
```

User selects operation → Enters numbers → Gets result → Optionally saves to memory.

---

## 🧠 Input Validation

- Prevents invalid number input
- Handles division by zero safely
- Prevents using empty memory
- Ensures menu selections are valid

---

## 🔒 Error Handling Example

If user attempts:

```
10 / 0
```

Output:

```
Error: Division by zero is not allowed!
```

---

## 🧑‍💻 Technologies Used

- Python 3
- Functions
- Loops
- Conditionals
- Lists
- Input validation
- String formatting

---

## 🎯 Learning Concepts Demonstrated

This project demonstrates:

- Function modularization
- Menu-driven program design
- Error handling
- State management (memory & history)
- Input validation loops
- Clean CLI user interaction

---

## 📌 Future Improvements (Optional Ideas)

- Add scientific calculator functions (√, %, power, etc.)
- Add GUI using Tkinter or PyQt
- Store history in a file
- Add unit testing
- Convert into a web calculator (Flask/Django)

---

## 📄 License

This project is open-source and free to use for learning purposes.

---

## 👨‍💻 Author

**Wycliff Ng'ang'a Mwaura**

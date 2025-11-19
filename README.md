# 📂 Project Navigation (Table of Contents)

Click the links below to jump to a specific chapter:

* **[📘 Chapter 1: Python Basics, Math & Patterns](#-chapter-1-python-basics-math--patterns)**
* **[📘 Chapter 2: Classes, Strings & Logic](#-chapter-2-classes-strings--logic)** 
* **[📚 Chapter 3: Stack Applications & Simulations](#-chapter-3-stack-applications--simulations)**
* **[📚 Chapter 4: Queue Data Structures](#-chapter-4-queue-data-structures)**
* **[🔗 Chapter 5: Linked Data Structures](#-chapter-5-linked-data-structures)**
* **[🔄 Chapter 6: Recursion & Backtracking](#-chapter-6-recursion--backtracking)**
* **[🌳 Chapter 7: Binary Search Trees (BST)](#-chapter-7-binary-search-trees-bst)**
* **[🌳 Chapter 8: AVL Trees (Self-Balancing BST)](#-chapter-8-avl-trees-self-balancing-bst)**
* **[🔢 Chapter 9: Sorting Algorithms](#-chapter-9-sorting-algorithms)**
* **[🔎 Chapter 10: Search & Hashing](#-chapter-10-search--hashing)**
* **[🕸️ Chapter 11: Graph Algorithms](#%EF%B8%8F-chapter-11-graph-algorithms)**

---

# 📘 Chapter 1: Python Basics, Math & Patterns

This repository contains the first set of Python exercises, focusing on fundamental control structures (`if/else`, `loops`), mathematical logic (Pascal's Triangle, Physics word problems), and complex ASCII art generation.

## 📂 Table of Contents

| File | Challenge Name | Description |
| :--- | :--- | :--- |
| `Chapter1_1.py` | **Rabbit, Turtle & Fly** | Solves a physics word problem to calculate the total distance a fly travels. |
| `Chapter1_2.py` | **Multiplication or Sum** | Simple conditional logic based on the product of two numbers. |
| `Chapter1_3.py` | **Pascal's Triangle** | Generates the famous mathematical triangle structure for $n$ rows. |
| `Chapter1_4.py` | **Fun with Drawing** | Generates a complex geometric ASCII art pattern based on input size. |
| `Chapter1_5.py` | **Countdown Search** | Scans a list of numbers to find valid "Countdown" sequences (e.g., 3, 2, 1). |

---

## 📝 Exercise Details

### 1. Rabbit, Turtle & Fly (`Chapter1_1.py`)
**Goal:** Calculate the total distance a fly travels back and forth between a Rabbit and a Turtle until they meet.
* **Input:** `d` (distance between Rabbit/Turtle), `Vr` (Rabbit speed), `Vt` (Turtle speed), `Vf` (Fly speed).
* **Constraints:** `Vt > Vr` (Turtle is faster in this fable), No Loops allowed.
* **Logic:** Calculates time to impact ($t = d / (V_t - V_r)$) and multiplies by fly speed ($Distance = V_f \times t$).

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `100 10 20 50` | `500.00` | Time = 10s. Fly travels $50 \times 10 = 500$. |

---

### 2. Multiplication or Sum (`Chapter1_2.py`)
**Goal:** Decide whether to multiply or add two numbers.
* **Input:** Two integers.
* **Logic:**
    * If `Product <= 1000`: Print the **Product**.
    * If `Product > 1000`: Print the **Sum**.

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `20 30` | `600` | $20 \times 30 = 600 (\le 1000)$. |
| `50 40` | `90` | $50 \times 40 = 2000 (> 1000)$, so $50 + 40 = 90$. |

---

### 3. Pascal's Triangle (`Chapter1_3.py`)
**Goal:** Print Pascal's Triangle up to $n$ rows.
* **Input:** Integer `n`.
* **Logic:** Uses the combinatorics formula to calculate the value of the next number in the row based on the previous one: `C = C * (i - j) // j`.

| Input | Output (Example for n=4) |
| :--- | :--- |
| `4` | `1`<br>`1 1`<br>`1 2 1`<br>`1 3 3 1` |

---

### 4. Fun with Drawing (`Chapter1_4.py`)
**Goal:** Create a complex "Diamond-in-a-Square" style pattern using ASCII characters (`.`, `*`, `+`).
* **Input:** Integer `n` (Controls the size).
* **Logic:** Uses nested loops to handle three distinct sections:
    1.  Top Pyramid (expanding `+` zones).
    2.  Middle Divider.
    3.  Bottom Inverted Pyramid.
    * Calculates spacing dynamically using formulas like `2*(n-i-1) - 1`.

| Input | Output (Partial Visual for n=3) |
| :--- | :--- |
| `3` | `....*....`<br>`..+*.*+..`<br>`.+*...*+.`<br>`*.......*` (and so on...) |

---

### 5. Fun with Countdown (`Chapter1_5.py`)
**Goal:** Identify sequences of numbers that count down by 1 and end in 1 (e.g., `3 2 1`, `2 1`).
* **Input:** A list of integers (e.g., `4 8 3 2 1 2`).
* **Logic:**
    * Iterates through the list checking if `current == next + 1`.
    * If a sequence ends in `1`, it is recorded.
    * **Backtracking:** If a sequence breaks (e.g., `3 2 5`), the index rewinds to check if the `2` starts a new sequence.
* **Output:** `[Count of sequences, [List of sequences]]`.

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `4 8 3 2 1 2` | `[1, [[3, 2, 1]]]` | Found one sequence: 3->2->1. |
| `1 1 2 1` | `[3, [[1], [1], [2, 1]]]` | `1` is a valid countdown of length 1. |

---

## 🚀 How to Run

Ensure you have Python 3 installed. Open your terminal and run any file:

```bash
# Example
python Chapter1_5.py
```

# 📘 Chapter 2: Classes, Strings & Logic

This repository contains Python exercises focusing on bitwise operators, logical looping (weird subtraction), advanced list processing (finding triplets), and Class-based game logic.

## 📂 Table of Contents

| File | Challenge Name | Description |
| :--- | :--- | :--- |
| `Chapter2_1.py` | **Right Shift** | Performs a bitwise right-shift operation (`>>`) on a number. |
| `Chapter2_2.py` | **Weird Subtract** | A loop-based subtraction requiring logic for handling trailing zeros. |
| `Chapter2_3.py` | **TorKham (Word Game)** | A word chain game Class checking character matching rules (Last 2 vs First 2). |
| `Chapter2_4.py` | **3 Sum (Target 5)** | Finds all unique triplets in a list that sum up to exactly 5. |
| `Chapter2_5.py` | **TorKham HanSaa** | (Variant/Duplicate of 2.3) The complete implementation of the TorKham word game. |

---

## 📝 Exercise Details

### 1. Right Shift (`Chapter2_1.py`)
**Goal:** Calculate the result of shifting a number `n` to the right by `s` bits.
* **Input:** Two integers `n` (number) and `s` (shift count).
* **Logic:** Uses the `>>` operator. Mathematically, this is equivalent to integer division by $2^s$.

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `8 1` | `4` | Binary `1000` >> 1 becomes `0100` (4). |
| `3888 4` | `243` | $3888 / 2^4 = 3888 / 16 = 243$. |

---

### 2. Weird Subtract (`Chapter2_2.py`)
**Goal:** reduce a number `n` by performing an operation `s` times.
* **Input:** `n` (starting number) and `s` (iterations).
* **Rules:**
    1. If `n` ends in **0**, remove the last digit (e.g., `20` $\to$ `2`).
    2. Otherwise, subtract **1** (e.g., `21` $\to$ `20`).
* **Logic:** Checks `n % 10` or string logic to detect trailing zeros.

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `21 3` | `1` | `21` $\xrightarrow{-1}$ `20` $\xrightarrow{pop 0}$ `2` $\xrightarrow{-1}$ `1`. |
| `100 1` | `10` | `100` ends in 0 $\to$ `10`. |

---

### 3 & 5. TorKham Game (`Chapter2_3.py` / `Chapter2_5.py`)
**Goal:** Implement a "Word Chain" game using a Class structure.
* **Input:** A list of commands separated by commas (e.g., `P Apple, P Lemon, X`).
* **Commands:**
    * `P <word>`: Play a word.
    * `R`: Restart the game.
    * `X`: Exit.
* **Rules:**
    * The **last 2 letters** of the previous word must match the **first 2 letters** of the new word (Case insensitive).
    * Words cannot be repeated.

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `P Apple, P Lemon, X` | `'Apple' -> ['Apple']`<br>`'Lemon' -> ['Apple', 'Lemon']` | `le` (end of Apple) matches `Le` (start of Lemon). |
| `P Apple, P Onion, X` | `'Onion' -> game over` | `le` does not match `On`. |

---

### 4. 3 Sum Target 5 (`Chapter2_4.py`)
**Goal:** Find all groups of 3 numbers in a list that sum up to **5**.
* **Input:** A list of integers.
* **Constraints:** List length must be > 2.
* **Logic:** Uses nested loops (or optimized pointers) to check combinations `arr[i] + arr[j] + arr[k] == 5`. Returns unique sorted triplets.

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `-25 -10 -7 -3 2 4 8 10` | `[[-7, 2, 10], [-7, 4, 8]]` | $-7+2+10=5$ and $-7+4+8=5$. |
| `-3 2 4 6 8 10` | `[[-3, 2, 6]]` | $-3+2+6=5$. |

---

## 🚀 How to Run

Ensure you have Python 3 installed. Open your terminal and run any file:

```bash
# Example: Run the Weird Subtract exercise
python Chapter2_2.py
```

# 📚 Chapter 3: Stack Applications & Simulations

This repository contains Python exercises focused on the **Stack** data structure. The challenges range from simple arithmetic filtering to complex simulations like weightlifting plate management and game combat logic.

## 📂 Table of Contents

| File | Challenge Name | Description |
| :--- | :--- | :--- |
| `Chapter3_1.py` | **Always 5 or 10** | Filters a list into a stack based on specific arithmetic relationships (Sum/Diff = 5 or 10). |
| `Chapter3_2.py` | **Barbell Management** | Simulates adding/removing weight plates on a barbell to reach target weights. |
| `Chapter3_3.py` | **Stack Fighting** | A combat simulation where damage dealt to the front enemy overflows to the next one behind them. |
| `Chapter3_4.py` | **Next Greater Element** | Finds the first larger number to the right for every element in a list. |
| `Chapter3_5.py` | **Trapping Rain Water** | Calculates how much water can be trapped between walls of varying heights. |

---

## 📝 Exercise Details

### 1. Always 5 or 10 (`Chapter3_1.py`)
**Goal:** Build a stack from a list of numbers, accepting a new number only if it forms a "5 or 10 relationship" with the top of the stack.
* **Input:** A list of integers.
* **Condition:** A number `n` is added if:
    * `n + top == 5` OR `abs(n - top) == 5`
    * `n + top == 10` OR `abs(n - top) == 10`
* **Logic:** Iterates through the list, checking the condition against `stack[-1]`.

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `1 10 4 9 5` | `1 4 9` | Start `1`. `10` (no relation). `4` (1+4=5) -> Stack: `1, 4`. `9` (9-4=5) -> Stack: `1, 4, 9`. |

---

### 2. Barbell Management (`Chapter3_2.py`)
**Goal:** Calculate how to load a barbell (starting weight 20kg) to reach specific target weights using standard plates (1.25kg to 25kg).
* **Input:** A list of target weights.
* **Logic:**
    * Determines necessary plates for a target weight.
    * Compares current plates on the bar vs. needed plates.
    * Issues `PO` (Pop/Remove) and `PU` (Push/Add) commands to transition between weights efficiently.
    * **Constraint:** Plates must be loaded in descending order (heavy inside, light outside).

| Input | Output Snippet | Explanation |
| :--- | :--- | :--- |
| `40` | `PU:10`<br>`Barbell: [10, 10]` | Needs 20kg extra (10kg per side). |
| `45` | `PO:10`, `PU:1.25`, `PU:1.25`... | Adjusts from previous state to new target. |

---

### 3. Stack Fighting (`Chapter3_3.py`)
**Goal:** Simulate a hero attacking a line of enemies.
* **Input:** Initial enemy HPs / Actions (`spawn <hp>` or `dmg <val>`).
* **Structure:** Enemies are stored in a stack (last one spawned is the first one hit).
* **Logic:**
    * **Spawn:** Adds a new enemy to the stack.
    * **Dmg:** Deals damage to the top enemy. If `Damage > HP`, the enemy dies, and the *remaining* damage carries over to the next enemy.
    * **Win Condition:** Stack becomes empty.

| Input | Output Snippet | Explanation |
| :--- | :--- | :--- |
| `30/dmg 40` | `deal 40 damage, killed 1 enemy`<br>`>>>> Player Wins <<<<` | Enemy (30 HP) takes 40 dmg. Dies. |
| `50 10/dmg 20` | `deal 20 damage, killed 1 enemy`<br>`[40]` | Top enemy (10 HP) dies. Remaining 10 dmg hits the 50 HP enemy (leaving 40). |

---

### 4. Next Greater Element (`Chapter3_4.py`)
**Goal:** For each number in a list, find the nearest number to its **right** that is larger.
* **Input:** A list of integers.
* **Logic:** Uses a **Monotonic Stack**.
    * Stores indices of numbers that haven't found a "greater" match yet.
    * When a new number is larger than `stack.peek()`, it means we found the answer for the numbers in the stack. Pop them and record the result.



| Input | Output | Explanation |
| :--- | :--- | :--- |
| `1 2 3 4 5` | `[2, 3, 4, 5, -1]` | 1 sees 2. 2 sees 3. 5 sees nothing (-1). |
| `5 1 3 2 6` | `[6, 3, 6, 6, -1]` | 5 waits for 6. 1 sees 3. 3 sees 6. |

---

### 5. Trapping Rain Water (`Chapter3_5.py`)
**Goal:** Calculate the units of water trapped between bars of different heights.
* **Input:** A list of non-negative integers representing elevation map.
* **Logic:**
    * Water at index `i` = `min(max_left, max_right) - height[i]`.
    * Pre-calculates the maximum height to the left and right of every index.
    * Sums the water accumulated at each index.



| Input | Output | Explanation |
| :--- | :--- | :--- |
| `4 2 0 3 2 5` | `9` | Water fills the valleys between the high walls (4 and 5). |
| `3 0 0 2 0 4` | `10` | Deep valley between 3 and 4. |

---

## 🚀 How to Run

Ensure you have Python 3 installed. Open your terminal and run any file:

```bash
# Example: Run the Trapping Rain Water solution
python Chapter3_5.py
```

# 📚 Chapter 4: Queue Data Structures

This repository contains Python exercises focused on **Queue** implementations. The challenges simulate real-world scenarios like printer task management, group formation with constraints, and organizational line-ups.

## 📂 Table of Contents

| File | Challenge Name | Description |
| :--- | :--- | :--- |
| `Chapter4_1.py` | **Basic Queue** | Implements standard `Enqueue` (E) and `Dequeue` (D) operations with state logging. |
| `Chapter4_2.py` | **Make a Group** | Allocates students into groups while enforcing specific conflict rules (e.g., Green vs. Pink). |
| `Chapter4_3.py` | **Hot Potato** | Simulates the classic elimination game using a circular queue. |
| `Chapter4_4.py` | **Printer Simulator** | A complex time-based simulation of a printer handling tasks, paper refills, and queue limits. |
| `Chapter4_5.py` | **Organization Queue** | Implements a "Group Queue" where new arrivals join their department's existing line instead of the absolute back. |

---

## 📝 Exercise Details

### 1. Basic Queue (`Chapter4_1.py`)
**Goal:** Manage a standard queue based on input commands.
* **Commands:**
    * `E <value>`: Enqueue value. Prints the index where it was added.
    * `D`: Dequeue the front element. Prints the value removed and remaining size.
* **Output:** Final state of the queue or "Empty".

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `E 10, E 20, D` | `Add 10 index is 0`<br>`Add 20 index is 1`<br>`Pop 10 size in queue is 1` | 10 enters, 20 enters. 10 leaves. 20 remains. |

---

### 2. Make a Group (`Chapter4_2.py`)
**Goal:** Arrange a list of students into groups of a specific size, rejecting those who violate conflict rules.
* **Input:** `Size, List of Names` (e.g., `3, Green Pink Blue...`).
* **Rules:**
    * **Green** cannot be with **Pink** (unless **Blue** is present).
    * **Blue** cannot be with **Yellow** (unless **Red** is present).
    * If a student fits, add to current group (Queue). If full, print group and start new one.
    * If a student violates the rule, they go to the `Rejected` queue.

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `2, Green Pink` | `Group 1 : Green`<br>`Rejected : Pink` | Pink cannot be with Green (no Blue present). |
| `3, Green Blue Pink`| `Group 1 : Green, Blue, Pink` | Blue acts as a mediator, allowing Green & Pink. |

---

### 3. Hot Potato (`Chapter4_3.py`)
**Goal:** Determine the winner of the Hot Potato game.
* **Input:** `Names / Number` (e.g., `Tom,Jerry,Bill/2`).
* **Logic:**
    * Players stand in a circle (Queue).
    * The "Potato" is passed `N` times. The person holding it at the end of the pass is **Eliminated** (Dequeued).
    * Repeat until 1 person remains.

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `A,B,C/1` | `Winner: C` | A passes to B. B eliminated. A passes to C. A eliminated. C wins. |

---

### 4. Printer Simulator (`Chapter4_4.py`)
**Goal:** Simulate a printer's minute-by-minute operation.
* **Input:** A timeline of commands (e.g., `P:0 DocA, R:5 10`).
* **Commands:**
    * `P:Time Name`: Print request. (Queue limit: 3 jobs).
    * `R:Time N`: Refill `N` sheets of paper.
    * `S:Time`: Show status.
* **Constraints:** Printing takes time (5 chars/min). Uses 1 paper/job. If out of paper, it errors.

| Input | Output |
| :--- | :--- |
| `P:0 A, S:1` | `[Time 1] Status: Printing... "A" and Pending 0 file(s)` |

---

### 5. Organization Queue (`Chapter4_5.py`)
**Goal:** Implement a queue where members of the same "Organization" (ID prefix) cut in line to join their friends.
* **Input:** `en <ID>, de, ...`
* **Logic:**
    * **Enqueue:** Extract Org ID (first digit).
        * If that Org is already in the main queue, insert the new person **behind** the last person of the *same* Org.
        * If not, add to the **end** of the main queue.
    * **Dequeue:** Standard FIFO from the front of the combined line.



| Input | Output | Explanation |
| :--- | :--- | :--- |
| `en 101, en 201, en 102` | `101, 102, 201` | 102 cuts in line to join 101 because they are both Org '1'. |
| `en 201, en 101, en 102` | `201, 101, 102` | 201 was first. 101 starts new group. 102 joins 101. |

---

## 🚀 How to Run

Ensure you have Python 3 installed. Open your terminal and run any file:

```bash
# Example: Run the Organization Queue simulation
python Chapter4_5.py
```

# 🔗 Chapter 5: Linked Data Structures

This repository contains Python exercises focused on **Singly Linked Lists**. The challenges range from basic pointer manipulation (finding and moving nodes) to simulating complex systems like Git repositories and Ant colonies using node-based logic.

## 📂 Table of Contents

| File | Challenge Name | Description |
| :--- | :--- | :--- |
| `Chapter5_1.py` | **Locomotive (Reorder)** | Rotates a linked list so the "Locomotive" (Node '0') moves to the front while preserving order. |
| `Chapter5_2.py` | **Bubble Sort LL** | Implements the Bubble Sort algorithm directly on a Linked List structure. |
| `Chapter5_3.py` | **Git Merge History** | Simulates Git branches using Linked Lists to detect common ancestors and count merges. |
| `Chapter5_4.py` | **Ant Colony** | A complex state-machine simulation managing "Worker" and "Army" ant nodes to gather food and fight. |
| `Chapter5_5.py` | **Ant Army (Alt. Reverse)** | Reverses nodes in groups of $k$, but skips every alternate group (Reverse $k$, Skip $k$, Reverse $k$...). |

---

## 📝 Exercise Details

### 1. Locomotive (`Chapter5_1.py`)
**Goal:** Find the "Locomotive" (represented by `0`) and move it to the head of the train (list), keeping the relative order of the carriages behind it.
* **Input:** A space-separated list of wagon IDs (e.g., `2 3 1 0 4 5`).
* **Logic:**
    * Traverses the list to find `0`.
    * Splits the list into `Before_0` and `After_0` (starting with 0).
    * Re-links the end of `Before_0` to follow `After_0`.
* **Constraint:** Effectively rotates the list until `0` is the head.

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `2 3 1 0 4 5` | `0 <- 4 <- 5 <- 2 <- 3 <- 1` | `0` becomes head. `4-5` follow. `2-3-1` wrap around to the end. |

---

### 2. Bubble Sort Linked List (`Chapter5_2.py`)
**Goal:** Sort a Linked List using the Bubble Sort algorithm.
* **Input:** Comma-separated integers.
* **Logic:**
    * Uses nested loops to compare `current.data` with `current.next.data`.
    * If `current > next`, swaps the **data** (or pointers).
    * Prints every swap action for visualization.

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `3,0,1` | `0->1->3` | Swaps `3,0` -> `0,3,1`. Swaps `3,1` -> `0,1,3`. |

---

### 3. Git Merge History (`Chapter5_3.py`)
**Goal:** Determine if multiple Git branches belong to the same repository and count how many times they merged.
* **Structure:** Branches are Linked Lists sharing common nodes (commits).
* **Input:** String representing branches separated by `|` (e.g., `A->B->C | D->B->C`).
* **Logic:**
    * **Same Repo?** Checks if the tail node (last commit) is identical for all branches.
    * **Merge Count:** 

[Image of Git Branching]
 Finds nodes that appear in multiple branches (excluding the common root) to identify merge points.

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `5->3->1 | 8->7->3->1` | `Same Repo: True`<br>`1 Merge(s)` | Both end in `1`. They merge at node `3`. |

---

### 4. Ant Colony (`Chapter5_4.py`)
**Goal:** Manage a colony of Ants (Linked List nodes) to perform tasks based on their type.
* **Types:**
    * **W (Worker):** Carries 2 food, Fights 5 DMG.
    * **A (Army):** Carries 5 food, Fights 10 DMG.
* **Commands:**
    * `C <amount>`: Carry food (Prioritizes Workers).
    * `F <hp>`: Fight enemy (Prioritizes Army).
    * `W/A <num>`: Add new ants.
* **Failure:** If ants cannot complete a task (e.g., HP > Total Attack), the colony takes damage or is destroyed.

| Input | Output Snippet |
| :--- | :--- |
| `W 3, A 2, F 15` | `Attack mission: A1 A2 (Total 20 DMG)` | Army ants used first. Success. |
| `F 100` | `Ant nest has fallen!` | Not enough attack power. |

---

### 5. Ant Army - Alternate Reverse (`Chapter5_5.py`)
**Goal:** Reorder a list by reversing every other group of `k` nodes.
* **Input:** `List, k` (e.g., `1 2 3 4 5 6, 2`).
* **Pattern:**
    1.  **Reverse** first $k$ nodes.
    2.  **Skip** next $k$ nodes (keep original order).
    3.  **Reverse** next $k$ nodes.
    4.  Repeat...
* **Logic:** Uses a dummy node and pointer manipulation to flip segments without using auxiliary arrays.



| Input | Output | Explanation |
| :--- | :--- | :--- |
| `1 2 3 4 5 6 7 8, 2` | `2->1->3->4->6->5->7->8` | Rev(1,2)->`2,1`. Skip(3,4)->`3,4`. Rev(5,6)->`6,5`. Skip(7,8). |

---

## 🚀 How to Run

Ensure you have Python 3 installed. Open your terminal and run any file:

```bash
# Example: Run the Ant Army simulation
python Chapter5_5.py
```

# 🔄 Chapter 6: Recursion & Backtracking

This repository contains Python exercises designed to master **Recursive Programming**. The challenges progress from simple mathematical sequences to complex state-space searches (Flood Fill) and reverse-engineering optimization problems.

## 📂 Table of Contents

| File | Challenge Name | Description |
| :--- | :--- | :--- |
| `Chapter6_1.py` | **Fibonacci** | Calculates the $n$-th Fibonacci number using standard recursion. |
| `Chapter6_2.py` | **Lucky Number** | Recursively sums the digits of a number until a single-digit "Lucky Number" remains. |
| `Chapter6_3.py` | **Combinations** | Generates all possible subsets (Power Set) of a given list. |
| `Chapter6_4.py` | **Water Flow (Flood Fill)** | Simulates water spreading across a terrain map based on height differentials. |
| `Chapter6_5.py` | **Alchemy (Reverse logic)** | A complex optimization problem calculating the maximum raw material weight needed to craft an item using a specific fusion formula. |

---

## 📝 Exercise Details

### 1. Fibonacci (`Chapter6_1.py`)
**Goal:** Find the $n$-th number in the Fibonacci sequence ($1, 1, 2, 3, 5, \dots$).
* **Input:** Integer `n`.
* **Logic:**
    * Base Case: If $n \le 2$, return $1$.
    * Recursive Step: $F(n) = F(n-1) + F(n-2)$.

| Input | Output |
| :--- | :--- |
| `5` | `fibo(5) = 5` |
| `7` | `fibo(7) = 13` |

---

### 2. Lucky Number (`Chapter6_2.py`)
**Goal:** Find the "Lucky Number" by repeatedly summing digits.
* **Input:** A positive integer.
* **Logic:**
    * Sums digits: $666 \to 6+6+6 = 18$.
    * Checks result: If digits $> 1$, recurse on the new sum ($18 \to 1+8 = 9$).
    * Base Case: Single digit found.

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `666` | `Sum #1 : 18`<br>`Lucky Number: 9` | $6+6+6=18$. $1+8=9$. |
| `79` | `Sum #1 : 16`<br>`Lucky Number: 7` | $7+9=16$. $1+6=7$. |

---

### 3. Combinations (`Chapter6_3.py`)
**Goal:** Generate all possible subsets (combinations) of a list.
* **Input:** A list of integers (e.g., `1 2`).
* **Logic:** Uses the "Include/Exclude" backtracking pattern.
    1.  **Include** current element in `combo` and recurse.
    2.  **Exclude** current element (pop it) and recurse.
    3.  Base Case: List is empty $\to$ Add current `combo` to answers.

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `1 2` | `[[1, 2], [1], [2], []]` | All possible groupings. |
| `10 20` | `[[10, 20], [10], [20], []]` | Order may vary based on stack implementation. |

---

### 4. Water Flow (`Chapter6_4.py`)
**Goal:** Simulate a flood on a grid map. Water flows from a start point to neighbors with **equal or lower** height.
* **Input:** `Rows, Cols / MapData / StartRow, StartCol`.
* **Logic:**
    * **Flood Fill Algorithm:**
    * If neighbor (Up, Down, Left, Right) height $\le$ current height, water flows there.
    * Visited/Flooded nodes are set to `0`.
* **Visualization:**


| Input Snippet | Output Snippet | Explanation |
| :--- | :--- | :--- |
| `3,3/123,456,789/0,0` | `023`<br>`456`<br>`789` | Starts at (0,0)=1. Neighbors are 2 and 4 (both higher). Water stops immediately. |

---

### 5. Alchemy (`Chapter6_5.py`)
**Goal:** Calculate the maximum weight of "Purity 1" raw materials required to create a final item of Purity $N$ and Weight $W$.
* **The Rule:** To make an item of purity $k+1$, you mix two items of purity $k$ (weights $a$ and $b$). The result weight is $(a + b + C_k) // 2$.
* **Logic:**
    * This requires **Reverse Recursion**. We know the final weight $W$ and need to find the original inputs ($a, b$).
    * Since $W_{new} = (a + b + C_k) // 2$, we must test possible values of $a$ and $b$ that satisfy this integer division equation to maximize the sum of base materials.
    * Uses **Memoization** to store results of `(purity, weight)` to avoid recalculating overlapping subproblems.

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `2 5` | `20` | To get Purity 2 weight 5, we need optimal Purity 1 inputs summing to 20. |

---

## 🚀 How to Run

Ensure you have Python 3 installed. Open your terminal and run any file:

```bash
# Example: Run the Lucky Number exercise
python Chapter6_2.py
```

# 🌳 Chapter 7: Binary Search Trees (BST)

This repository contains Python exercises focused on the **Binary Search Tree** data structure. The challenges explore tree construction, custom traversal algorithms (BFS variants), mathematical operations on nodes, and structural modifications like mirroring.

## 📂 Table of Contents

| File | Challenge Name | Description |
| :--- | :--- | :--- |
| `Chapter7_1.py` | **Know Your Tree** | Implements a basic BST with insertion logic and a visual "rotated" print function. |
| `Chapter7_2.py` | **Weird BFS** | traverse a tree using a modified Breadth-First Search (Right-to-Left priority). |
| `Chapter7_3.py` | **Sum & Multiply** | Calculates the sum of all nodes and multiplies values greater than a specific threshold. |
| `Chapter7_4.py` | **Treasure Hunting** | A pathfinding simulation to find a "Treasure" node and then an "Escape" node without retracing steps. |
| `Chapter7_5.py` | **Mirror Tree** | Mirrors (swaps left/right children) the tree structure starting from a specific depth. |

---

## 📝 Exercise Details

### 1. Know Your Tree (`Chapter7_1.py`)
**Goal:** Create a Binary Search Tree class and display it.
* **Input:** A list of integers to insert.
* **Logic:**
    * **Insert:** Standard BST logic. Smaller values go Left, larger/equal values go Right.
    * **Print:** Uses recursive Depth-First Search (Right-Root-Left) to print the tree horizontally (rotated 90 degrees).



| Input | Output (Visual) |
| :--- | :--- |
| `10 5 20` | `     20`<br>`10`<br>`     5` |

---

### 2. Weird BFS (`Chapter7_2.py`)
**Goal:** Convert a tree into a list using a specific traversal order.
* **Input:** List of numbers to build the tree.
* **Logic:**
    * Implements a **Breadth-First Search (BFS)** using a Queue.
    * **Variation:** Unlike standard BFS (Left -> Right), this exercise likely requires a modified order (e.g., Right -> Left or specific depth priority) to match the "Weird" output requirement.
* **Output:** A flat list representing the traversed nodes.

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `1 2 3` | `[1, 3, 2]` | Visits Root, then Right child, then Left child. |

---

### 3. Sum of Tree (`Chapter7_3.py`)
**Goal:** Perform mathematical operations on the tree nodes.
* **Input:** `Tree Values / Multiplier` (e.g., `5 3 8 / 4`).
* **Features:**
    1.  **`find_sum()`**: Traverses the tree (DFS) to sum all node values.
    2.  **`multiply(k)`**: Traverses the tree; if `node.data > k`, updates `node.data = node.data * k`.

| Input | Output Snippet | Explanation |
| :--- | :--- | :--- |
| `5 2 8 / 3` | `Sum: 15`<br>`Sum: 31` | Initial sum $5+2+8=15$. Nodes $>3$ (5, 8) become $15, 24$. New sum $15+2+24$. |

---

### 4. Treasure Hunting (`Chapter7_4.py`)
**Goal:** Find a valid path from Root $\to$ Treasure $\to$ Escape.
* **Input:** `Tree Values / Treasure / Escape`.
* **Constraints:**
    * Directed path only (cannot go back up to parent).
    * Must visit Treasure first, then Escape.
* **Logic:**
    * Checks if `Treasure` exists in the tree.
    * Checks if `Escape` exists in the subtree of `Treasure`.
    * Records the path taken.

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `8 3 10 / 10 / 11` | `8 -> 10 -> 11` | Valid path found. |
| `8 3 10 / 3 / 10` | `Mission Failed` | Cannot go from 3 (Left) to 10 (Right) without going back up. |

---

### 5. Mirror Tree (`Chapter7_5.py`)
**Goal:** Reverse the structure (Left $\leftrightarrow$ Right) of the tree, but only for nodes deeper than a specific level.
* **Input:** `Level-Order List, Depth`.
* **Logic:**
    * Constructs tree from list.
    * **Mirror Logic:** For every node at `current_depth >= target_depth`, swap its `.left` and `.right` pointers.
    * This affects all sub-children of that node as well.

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `1 2 3, 0` | `1 3 2` | Root (Depth 0) swaps children 2 and 3. |

---

## 🚀 How to Run

Ensure you have Python 3 installed. Open your terminal and run any file:

```bash
# Example: Run the Treasure Hunting simulation
python Chapter7_4.py
```

# 🌳 Chapter 8: AVL Trees (Self-Balancing BST)

This repository contains Python exercises focused on **AVL Trees**. The challenges explore the mechanics of self-balancing trees, including node rotation, height calculation, structural comparison, and applying AVL trees to manage sorted data like movie ratings.

## 📂 Table of Contents

| File | Challenge Name | Description |
| :--- | :--- | :--- |
| `Chapter8_1.py` | **Standard AVL** | Implements a full AVL Tree with insertion and auto-rebalancing (Rotations). |
| `Chapter8_2.py` | **Same Tree?** | Builds two AVL trees from different input sequences and checks if they are structurally identical. |
| `Chapter8_3.py` | **Max Sum Path** | Finds the path from the root to a leaf that produces the maximum sum of node values. |
| `Chapter8_4.py` | **Burn the Tree (ASCII)** | A visual challenge to build a BST/AVL and display it using complex ASCII art (or check AVL properties). |
| `Chapter8_5.py` | **Rotten Potato (Movies)** | A movie ranking system using AVL Trees to handle insertions, deletions, and range queries efficiently. |

---

## 📝 Exercise Details

### 1. Standard AVL (`Chapter8_1.py`)
**Goal:** Construct an AVL Tree from a list of inputs and display the Post-order traversal.
* **Input:** A list of integers.
* **Logic:**
    * **Insertion:** Standard BST insert.
    * **Rebalance:** After every insert, checks the `Balance Value` (Height Right - Height Left).
    * **Rotations:** Performs Left, Right, Left-Right, or Right-Left rotations to ensure $|Balance| \le 1$.
    * **Output:** Prints the tree structure and the Post-order traversal.



| Input | Output | Explanation |
| :--- | :--- | :--- |
| `1 2 3` | `AVLTree post-order : 1 3 2` | Tree balances to `2` at root, `1` left, `3` right. Post-order: Left(1), Right(3), Root(2). |

---

### 2. Same Tree or Not? (`Chapter8_2.py`)
**Goal:** Determine if two sets of inputs result in identical AVL Trees.
* **Input:** `List1 / List2` (e.g., `1 2 3 / 3 2 1`).
* **Logic:**
    * Builds `Tree1` and `Tree2` independently using AVL logic.
    * **Comparison:** Traverses both trees simultaneously to check if every node's value and position match exactly.
* **Note:** Even if input order differs, AVL balancing might result in the same structure (or different, depending on the sequence).

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `1 2 3 / 3 2 1` | `Same Tree` | Both sequences balance to become `2` (root) with `1` and `3` as children. |
| `5 1 / 1 5` | `Same Tree` | Root 5, Left 1 vs Root 1, Right 5. Wait, AVL might balance differently? Actually, specific rotations make them identical or different. |

---

### 3. Max Sum Path (`Chapter8_3.py`)
**Goal:** Find the "Golden Apple" path (Root to Leaf) that yields the highest sum.
* **Input:** A list of numbers to build the AVL Tree.
* **Logic:**
    * recursive DFS to calculate the max sum path for Left vs Right subtrees.
    * Returns the path list and the total value.

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `10 5 20` | `10 + 20 = 30` | Path `10 -> 20` is greater than `10 -> 5`. |

---

### 4. Burn the Tree / ASCII View (`Chapter8_4.py`)
**Goal:** Visualize the Tree structure or calculate Balance Factors.
* **Input:** A list of integers.
* **Features:**
    * **`update_height`**: Recursively updates node heights.
    * **`balance_factor`**: Calculates `Height(Left) - Height(Right)`.
    * **Visualization:** Prints the tree in a sideways format for easy debugging.

| Input | Output (Visual) |
| :--- | :--- |
| `1 2 3` | `      3`<br>` 2`<br>`      1` |

---

### 5. Rotten Potato Movie Database (`Chapter8_5.py`)
**Goal:** A comprehensive system to manage movie ratings.
* **Input:** Commands to manipulate the database.
    * `I <Name> <Score>`: Insert a new movie.
    * `D <Name>`: Delete a movie.
    * `T <N>`: Show Top `N` highest-rated movies.
    * `R <Min> <Max>`: Show movies with ratings between `Min` and `Max`.
* **Logic:**
    * Uses `AVLTree` keyed by `rating`.
    * Handles duplicate ratings by chaining or specific insertion logic.
    * **Deletion:** Standard BST deletion + AVL Rebalancing.

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `I IronMan 9.0, T 1` | `IronMan(9.0)` | Inserts and retrieves top 1. |
| `R 8.0 9.5` | `Inception(9.1), IronMan(9.0)` | Range query. |

---

## 🚀 How to Run

Ensure you have Python 3 installed. Open your terminal and run any file:

```bash
# Example: Run the Movie Database
python Chapter8_5.py
```

# 🔢 Chapter 9: Sorting Algorithms

This repository contains Python exercises focused on **Sorting Algorithms**. The challenges explore how to implement standard algorithms like Bubble Sort and Insertion Sort, as well as how to write custom comparison logic for sorting objects based on multiple criteria (e.g., Frequency, Suit/Rank, or League Points).

## 📂 Table of Contents

| File | Challenge Name | Description |
| :--- | :--- | :--- |
| `Chapter9_1.py` | **Bubble Sort (Visual)** | Implements Bubble Sort and prints the state of the list at specific steps. |
| `Chapter9_2.py` | **Sort by Frequency** | Counts number occurrences and sorts them based on frequency (Most frequent first). |
| `Chapter9_3.py` | **Insertion Sort (Cards)** | Sorts a hand of playing cards based on Rank and Suit using Insertion Sort logic. |
| `Chapter9_4.py` | **Fun with Words** | Sorts a list of strings based on calculated "Weight" or "Vowel Priority". |
| `Chapter9_5.py` | **Premier League** | Sorts football teams based on Points first, then Goal Difference. |

---

## 📝 Exercise Details

### 1. Bubble Sort Visualizer (`Chapter9_1.py`)
**Goal:** Sort a list of integers using Bubble Sort and display the sorting process.
* **Input:** A list of integers.
* **Logic:**
    * Standard Bubble Sort: Compares `arr[j]` and `arr[j+1]`. Swaps if left > right.
    * **Visualization:** Tracks the "last moved" element and prints the list state when a specific condition (like `mid_sorted`) is met, or just the final step.
    * Optimized to stop early if the list is already sorted.



[Image of Bubble Sort Algorithm]


| Input | Output Snippet | Explanation |
| :--- | :--- | :--- |
| `4 3 2 1` | `1 step : [3, 2, 1, 4] move[4]`<br>`...` | Shows `4` bubbling to the end. |

---

### 2. Sort by Frequency (`Chapter9_2.py`)
**Goal:** Sort numbers based on how often they appear in the input list.
* **Input:** A list of integers (e.g., `1 1 2 2 2 3`).
* **Logic:**
    * Counts frequencies using a dictionary.
    * Sorts the unique numbers based on their count (Descending order).
    * Uses a simple sorting loop (Bubble sort logic on the dictionary items).

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `1 1 2 2 2 3` | `number 2, total: 3`<br>`number 1, total: 2`<br>`number 3, total: 1` | `2` appears 3 times (most), `1` appears 2 times, `3` appears once. |

---

### 3. Insertion Sort - Cards (`Chapter9_3.py`)
**Goal:** Sort playing cards according to Rank and Suit order.
* **Input:** List of cards (e.g., `2C KH 5D`) and sorting mode.
* **Order:**
    * **Suits:** Clubs (C) < Diamonds (D) < Hearts (H) < Spades (S).
    * **Ranks:** 2 < 3 ... < 9 < T (10) < J < Q < K < A.
* **Logic:**
    * Converts cards to comparable values (tuples of `(rank_val, suit_val)`).
    * Uses **Insertion Sort** to place cards in the correct position.
    * Handles duplicate detection and removal.



[Image of Insertion Sort Logic]


| Input | Output | Explanation |
| :--- | :--- | :--- |
| `4H 2C TC` | `2C 4H TC` | 2 Clubs (Lowest suit/rank combo) -> 4 Hearts -> 10 Clubs. |

---

### 4. Fun with Words (`Chapter9_4.py`)
**Goal:** Sort strings based on custom calculated metrics.
* **Input:** `Words / Mode` (e.g., `apple banana / Ascending`).
* **Metrics:**
    * **Weight:** Sum of character values (`a=1, b=2... z=26`).
    * **Vowel Priority:** Likely sorts based on the most valuable vowel or count of vowels (logic depends on specific mode implementation).
* **Logic:**
    * Calculates metrics for each word.
    * Sorts the list of words based on these calculated values using a standard sort algorithm.

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `abc z / Ascending` | `abc z` | `abc` weight $1+2+3=6$. `z` weight $26$. |

---

### 5. Premier League Score (`Chapter9_5.py`)
**Goal:** Generate a sorted league table from raw team stats.
* **Input:** List of team strings: `Name,Wins,Loss,Draws,Scored,Conceded`.
* **Calculations:**
    * **Points:** $(Wins \times 3) + (Draws \times 1)$.
    * **Goal Difference (GD):** $Scored - Conceded$.
* **Sorting Logic (Multi-Key):**
    1.  Higher **Points**.
    2.  If Points are equal, higher **Goal Difference**.
* **Algorithm:** Uses a nested loop sort (Bubble Sort variant) comparing dictionaries.

| Input Snippet | Output Snippet | Explanation |
| :--- | :--- | :--- |
| `ManU,2,0,0,5,0 / Liv,1,0,1,2,2` | `['ManU', {'points': 6}, {'gd': 5}]`<br>`['Liv', {'points': 4}, {'gd': 0}]` | ManU (6 pts) > Liverpool (4 pts). |

---

## 🚀 How to Run

Ensure you have Python 3 installed. Open your terminal and run any file:

```bash
# Example: Run the Card Sorting exercise
python Chapter9_3.py
```

# 🔎 Chapter 10: Search & Hashing

This repository contains Python exercises focused on **Search Algorithms** and **Hash Tables**. The challenges explore binary search applications (calculating percentiles), self-organizing lists (Move-to-Front), and robust Hashing implementations (Quadratic Probing & Rehashing).

## 📂 Table of Contents

| File | Challenge Name | Description |
| :--- | :--- | :--- |
| `Chapter10_1.py` | **Binary Search (Percentile)** | Uses Binary Search to find the index of a number in a sorted list and calculates its percentile. |
| `Chapter10_2.py` | **Move To Front** | Simulates a self-organizing search strategy where accessed items are moved to the front to reduce future search costs. |
| `Chapter10_3.py` | **Fun with Hashing** | Implements a Hash Table with **Quadratic Probing** to resolve collisions. |
| `Chapter10_4.py` | **Rehashing** | Expands the previous Hash Table to support auto-resizing (Rehashing) when a load factor threshold is exceeded. |
| `Chapter10_5.py` | **Box Packing (Min Time)** | Uses Binary Search on the "Answer" to find the minimum time required for $k$ workers to complete a set of jobs. |

---

## 📝 Exercise Details

### 1. Binary Search - Percentile (`Chapter10_1.py`)
**Goal:** Find the position of a number in a sorted list and calculate its percentile rank.
* **Input:** `Sorted List / Target Number`.
* **Logic:**
    * Uses **Binary Search** to find the index.
    * If the number doesn't exist, interpolates the index based on neighbors.
    * **Percentile Formula:** `(index + 1) * 100 / N`.
    * Handles edge cases (Min, Max, Not Found).



[Image of Binary Search Algorithm]


| Input | Output Snippet | Explanation |
| :--- | :--- | :--- |
| `1 2 3 4 5 / 3` | `index: 2.0`<br>`percentile: 60.0` | Found at index 2. (2+1)/5 * 100 = 60%. |
| `1 2 3 4 5 / 3.5`| `index: 2.5`<br>`percentile: 70.0` | Interpolated between 3 and 4. |

---

### 2. Move To Front Search (`Chapter10_2.py`)
**Goal:** Simulate a library system where frequently accessed books move to the front.
* **Input:** `Initial Shelf / Request Sequence`.
* **Rules:**
    1.  **Found:** Move book to index 0. Cost = `index + 1`.
    2.  **Not Found (First time):** Add to "Storage" (not shelf). Cost = `len(shelf) + 1`.
    3.  **Not Found (In Storage):** Add to index 0 of shelf. Cost = 1.
* **Logic:** Standard Linear Search + List manipulation.

| Input | Output Snippet | Explanation |
| :--- | :--- | :--- |
| `A B C / B A` | `Search B -> found at 2 move to front`<br>`Shelf: B A C` | B was at 2, moves to 1. Cost 2. |

---

### 3. Fun with Hashing (`Chapter10_3.py`)
**Goal:** Implement a Hash Table using ASCII summation and Quadratic Probing.
* **Input:** `Table Size, Max Collisions / Data1, Data2...`.
* **Logic:**
    * **Hash Function:** `Sum(ASCII) % Size`.
    * **Collision Resolution:** Uses **Quadratic Probing** (`(Hash + k^2) % Size`).
    * If collisions exceed `Max Collisions`, print "Max of collisionChain" and discard.
    * Stops if the table is full.



| Input | Output Snippet | Explanation |
| :--- | :--- | :--- |
| `3 2 / A B C` | `#1 (A, Value)`<br>`collision number 1 at ...` | A fills slot. B collides -> Probes next slot. |

---

### 4. Rehashing (`Chapter10_4.py`)
**Goal:** Upgrade the Hash Table to resize itself automatically.
* **Input:** `Size, MaxCol, Threshold / Data...`.
* **Logic:**
    * **Load Factor Check:** Before inserting, if `(Count+1)/Size * 100 > Threshold`, Trigger Rehash.
    * **Collision Check:** If insertion fails (Max Collisions reached), Trigger Rehash.
    * **Rehash Process:**
        1.  Find next prime number `>= Size * 2`.
        2.  Create new table.
        3.  Re-insert **old data** (from history).
        4.  Insert **new data**.

| Input Snippet | Output Snippet | Explanation |
| :--- | :--- | :--- |
| `5 1 70 / ...` | `****** Data over threshold - Rehash !!! ******` | Table gets too full, expands to size 11 (next prime > 10). |

---

### 5. Box Packing - Min Time (`Chapter10_5.py`)
**Goal:** Find the minimum time required for $k$ workers to complete jobs of varying weights.
* **Input:** `Jobs / Workers` (e.g., `1 2 3 4 5 / 2`).
* **Logic:**
    * This is a **Binary Search on Answer** problem.
    * **Range:** `Low = Max(Job)`, `High = Sum(Jobs)`.
    * **Check Function:** Can we fit all jobs into $k$ buckets such that no bucket exceeds `Time X`? (Greedy/Backtracking approach).
    * Adjusts `Low/High` to find the smallest valid `Time X`.

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `8 8 8 8 / 4` | `8` | 4 workers, each takes one 8-unit job. Max time = 8. |
| `1 2 3 4 5 / 2` | `8` | Worker1: 5+3=8. Worker2: 4+2+1=7. Max time is 8. |

---

## 🚀 How to Run

Ensure you have Python 3 installed. Open your terminal and run any file:

```bash
# Example: Run the Rehashing simulation
python Chapter10_4.py
```

# 🕸️ Chapter 11: Graph Algorithms

This repository contains Python exercises focused on **Graph Theory**. The challenges explore how to represent graphs programmatically using Adjacency Matrices and how to solve the "Shortest Path" problem using Dijkstra's Algorithm.

## 📂 Table of Contents

| File | Challenge Name | Description |
| :--- | :--- | :--- |
| `Chapter11_1.py` | **Adjacency Matrix** | Converts a list of edges (A B, B C) into a grid-based Matrix representation. |
| `Chapter11_5.py` | **Dijkstra's Shortest Path** | Finds the shortest distance and the specific path between two nodes in a weighted graph. |

---

## 📝 Exercise Details

### 1. Adjacency Matrix (`Chapter11_1.py`)
**Goal:** Represent a Directed Graph as a square matrix.
* **Input:** A list of edges (e.g., `A B, B C`).
* **Logic:**
    1.  **Identify Nodes:** Scans all edges to find unique nodes (A, B, C) and sorts them.
    2.  **Initialize Matrix:** Creates an $N \times N$ grid of zeros.
    3.  **Fill Edges:** If there is an edge from $Source \to Dest$, set `matrix[src_index][dst_index] = 1`.
* **Visualization:**
    * Rows represent Source nodes.
    * Columns represent Destination nodes.
    * `1` indicates a connection, `0` indicates no connection.



| Input | Output Snippet | Explanation |
| :--- | :--- | :--- |
| `A B, B C` | `    A  B  C`<br>`A : 0, 1, 0`<br>`B : 0, 0, 1` | A connects to B (Row A, Col B = 1). B connects to C. |

---

### 2. Dijkstra's Shortest Path (`Chapter11_5.py`)
**Goal:** Find the minimum weight path between a Start and Target node.
* **Input:** `Start Target` (e.g., `A F`).
* **Graph Data:** Hardcoded dictionary representing a weighted graph (e.g., `A -> B (1)`, `A -> C (2)`).
* **Logic:**
    * **Initialization:** Set all distances to $\infty$, except Start (0).
    * **Greedy Search:** Always selects the unvisited node with the smallest known distance.
    * **Relaxation:** Checks neighbors; if a shorter path is found through the current node, update the neighbor's distance and record the "Previous Node" to reconstruct the path later.
    * **Backtracking:** Uses the `previous_nodes` map to trace the path from Target back to Start.



| Input | Output | Explanation |
| :--- | :--- | :--- |
| `A D` | `Shortest distance is 10`<br>`Path is ['A', 'C', 'D']` | Direct A->B->D is 1+12=13. A->C->D is 2+9=11. Wait, path logic depends on specific weights in code. |

---

## 🚀 How to Run

Ensure you have Python 3 installed. Open your terminal and run any file:

```bash
# Example: Run the Shortest Path calculator
python Chapter11_5.py
```

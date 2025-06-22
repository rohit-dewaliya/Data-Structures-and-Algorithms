
# 📊 Complexity Profiler Decorator

A lightweight Python decorator for profiling **execution time** and **memory usage**, with an **approximate time complexity estimate** based on runtime.

This utility is useful for analyzing algorithm performance during development or debugging.

---

## 🚀 Features

- ⏱️ **Execution Time Measurement**
- 💾 **Peak Memory Usage Tracking**
- 🔍 **Function Call Argument Logging**
- 🧠 **Estimated Time Complexity Classification**
- ⚡ Easy-to-use decorator for quick performance insights

---

## 🧩 Installation

No external dependencies required (uses built-in Python modules: `time`, `tracemalloc`, and `functools`).

Just copy the `complexity_profiler` function into your project file or utility module.

---

## 🧪 Usage

```python
from time_decorator import complexity_profiler  # or from your_module import complexity_profiler

@complexity_profiler
def my_function(n):
    return sum(i for i in range(n))

my_function(10000)
````

---

## 📋 Output Example

```
🔹 Function: my_function
Arguments are: (10000,)
⏳ Time Taken: 0.001234 sec
💾 Peak Memory Used: 0.3125 KB
🟠 Likely O(N log N) or O(N²)
50005000
```

---

## 📈 Time Complexity Estimation Logic

The decorator **approximates** time complexity using elapsed execution time:

| Time Taken (sec) | Estimated Complexity   |
| ---------------- | ---------------------- |
| `< 1e-6`         | 🟢 O(1) or O(log N)    |
| `< 1e-3`         | 🟡 O(N)                |
| `< 1`            | 🟠 O(N log N) or O(N²) |
| `>= 1`           | 🔴 O(2ⁿ) or worse      |

> ⚠️ Note: These are **heuristic estimations**, not mathematically guaranteed complexity evaluations.

---

## 📁 File Structure (if applicable)

```
your_project/
├── time_decorator.py    # Contains complexity_profiler
├── your_script.py       # Where you import and use the decorator
```

---

## 🧠 Notes

* Use this tool for **quick diagnostics**, not formal benchmarking.
* For more accurate profiling, consider Python libraries like `line_profiler`, `memory_profiler`, or `cProfile`.


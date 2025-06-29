
---

## List vs. Tuple: Mutability & Modification Methods Chart (with Emojis for emphasis)

| Feature / Method      | **Lists (Mutable)** | **Tuples (Immutable)** |
| :-------------------- | :------------------------------------------------ | :---------------------------------------------------- |
| **Mutability** | ✅ **Mutable** (Can be changed after creation)       | ❌ **Immutable** (Cannot be changed after creation)      |
| **`append()` Method** | ✅ **Available.** Adds a single element to the end.  | ❌ **Not Available.** Raises an `AttributeError`.        |
| **`extend()` Method** | ✅ **Available.** Adds elements from an iterable to the end. | ❌ **Not Available.** Raises an `AttributeError`.        |
| **`add()` Method** | ℹ️ Not Available (for `set` objects).                | ℹ️ Not Available (for `set` objects).                    |
| **Direct Assignment** | ✅ **Available.** Change an element (`my_list[idx] = new_val`). | ❌ **Not Available.** Raises a `TypeError`.              |
| **`insert()` Method** | ✅ **Available.** Inserts an element at a specific index. | ❌ **Not Available.** Raises an `AttributeError`.        |
| **`remove()` Method** | ✅ **Available.** Removes the first occurrence of a value. | ❌ **Not Available.** Raises an `AttributeError`.        |
| **`pop()` Method** | ✅ **Available.** Removes and returns element by index. | ❌ **Not Available.** Raises an `AttributeError`.        |
| **`del` Keyword** | ✅ **Available.** Deletes element(s) by index or slice. | ❌ Not Available (for elements; raises `TypeError`).      |
| **`sort()` Method** | ✅ **Available.** Sorts the list in-place.           | ❌ Not Available (use `sorted()` for a new list/tuple).  |
| **`reverse()` Method**| ✅ **Available.** Reverses the list in-place.        | ❌ Not Available (use slicing `[::-1]` for a new tuple). |
| **Concatenation (`+`)**| ✅ Available (creates a *new* list).                | ✅ Available (creates a *new* tuple).                   |
| **Repetition (`*`)** | ✅ Available (creates a *new* list).                | ✅ Available (creates a *new* tuple).                   |

---

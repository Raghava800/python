
---

## 🔁 List vs. Tuple in Python — Mutability & Modification 🐍

Python offers both **lists** and **tuples** for storing collections. But they behave very differently!

| Feature / Method        | ![List](https://img.shields.io/badge/List-Mutable-green?style=flat-square) | ![Tuple](https://img.shields.io/badge/Tuple-Immutable-red?style=flat-square) |
| ----------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Mutability**          | ✅ Can be modified after creation                                           | ❌ Cannot be modified after creation                                          |
| **`append()`**          | ✅ Adds element to the end  <br> `my_list.append(4)`                        | ❌ `AttributeError`                                                           |
| **`extend()`**          | ✅ Adds multiple elements  <br> `my_list.extend([4,5])`                     | ❌ `AttributeError`                                                           |
| **`add()`**             | ❌ Not supported for lists <br> *(used in sets)*                            | ❌ Not supported                                                              |
| **Direct Assignment**   | ✅ `my_list[0] = 100`                                                       | ❌ `TypeError`                                                                |
| **`insert()`**          | ✅ Insert at position <br> `my_list.insert(1, 200)`                         | ❌ `AttributeError`                                                           |
| **`remove()`**          | ✅ Remove by value <br> `my_list.remove(3)`                                 | ❌ `AttributeError`                                                           |
| **`pop()`**             | ✅ Remove by index <br> `my_list.pop(0)`                                    | ❌ `AttributeError`                                                           |
| **`del` keyword**       | ✅ Delete element(s) <br> `del my_list[0]`                                  | ❌ `TypeError` on item deletion                                               |
| **`sort()`**            | ✅ In-place sort <br> `my_list.sort()`                                      | ❌ Use `sorted(my_tuple)` instead                                             |
| **`reverse()`**         | ✅ In-place reverse <br> `my_list.reverse()`                                | ❌ Use `my_tuple[::-1]`                                                       |
| **Concatenation (`+`)** | ✅ `new_list = [1,2] + [3,4]`                                               | ✅ `new_tuple = (1,2) + (3,4)`                                                |
| **Repetition (`*`)**    | ✅ `[1,2]*2 → [1,2,1,2]`                                                    | ✅ `(1,2)*2 → (1,2,1,2)`                                                      |

---

### 🧪 Code Snippet Examples

```python
# ✅ List: Mutable
my_list = [1, 2, 3]
my_list.append(4)
my_list[0] = 100
my_list.extend([5, 6])
print(my_list)  # [100, 2, 3, 4, 5, 6]

# ❌ Tuple: Immutable
my_tuple = (1, 2, 3)
try:
    my_tuple[0] = 100  # Raises TypeError
except TypeError as e:
    print(e)

# 🔁 Concatenation and Repetition
print([1, 2] + [3, 4])       # [1, 2, 3, 4]
print((1, 2) + (3, 4))       # (1, 2, 3, 4)
print([1, 2] * 2)            # [1, 2, 1, 2]
print((1, 2) * 2)            # (1, 2, 1, 2)
```

---

### 💡 Summary

* Use **lists** when you need to modify, sort, or append items frequently.
* Use **tuples** when immutability and performance are important (e.g., dictionary keys, function arguments).

---

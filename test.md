# **PHẦN I: NỀN TẢNG CƠ BẢN**

## **1. BIẾN VÀ KIỂU DỮ LIỆU**

### **1.1. Biến (Variables) trong Python**

**Lý thuyết:**
Biến là tên gọi tham chiếu đến giá trị lưu trong bộ nhớ. Python là ngôn ngữ gõ động - kiểu dữ liệu được xác định tự động.

**Đặc điểm:**
- Không cần khai báo kiểu tường minh
- Phân biệt chữ hoa/thường (age ≠ Age)
- Đặt tên: chữ, số, gạch dưới, không bắt đầu bằng số

**Ví dụ:**

```python
# Khai báo biến
name = "Nguyễn Văn A"
age = 25
height = 1.75
is_student = True
score = None

# Kiểm tra kiểu dữ liệu
print(type(name))      # <class 'str'>
print(type(age))       # <class 'int'>
print(type(height))    # <class 'float'>
print(type(is_student))# <class 'bool'>
print(type(score))     # <class 'NoneType'>
```

**Output:**
```
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
```

---

### **1.2. Kiểu dữ liệu cơ bản**

**Lý thuyết:**

| Kiểu dữ liệu | Ký hiệu | Giá trị ví dụ | Mô tả |
|-------------|---------|--------------|-------|
| **Integer** | `int` | `-10, 0, 100` | Số nguyên không phần thập phân |
| **Float** | `float` | `3.14, -0.5` | Số thực có phần thập phân |
| **String** | `str` | `"Python"`, `'Xin chào'` | Chuỗi ký tự Unicode |
| **Boolean** | `bool` | `True`, `False` | Giá trị logic đúng/sai |
| **NoneType** | `None` | `None` | Đại diện giá trị không có |

**Ví dụ:**

```python
# Số nguyên
so_nguyen = 42
print(f"{so_nguyen} là kiểu {type(so_nguyen)}")

# Số thực
pi = 3.14159
print(f"{pi} là kiểu {type(pi)}")

# Chuỗi ký tự
chuoi = "Python"
chuoi_f = f"Xin chào {name}"
print(f"'{chuoi_f}' là kiểu {type(chuoi_f)}")

# Boolean
dung = True
sai = False
print(f"{dung} và {sai} là kiểu {type(dung)}")

# None
rong = None
print(f"{rong} là kiểu {type(rong)}")
```

**Output:**
```
42 là kiểu <class 'int'>
3.14159 là kiểu <class 'float'>
'Xin chào Nguyễn Văn A' là kiểu <class 'str'>
True và False là kiểu <class 'bool'>
None là kiểu <class 'NoneType'>
```

---

## **2. TOÁN TỬ (OPERATORS)**

### **2.1. Toán tử số học (Arithmetic Operators)**

**Lý thuyết:**

| Toán tử | Tên | Ví dụ | Kết quả |
|---------|------|-------|---------|
| `+` | Cộng | `5 + 3` | `8` |
| `-` | Trừ | `10 - 4` | `6` |
| `*` | Nhân | `6 * 7` | `42` |
| `/` | Chia | `15 / 4` | `3.75` |
| `//` | Chia nguyên | `15 // 4` | `3` |
| `%` | Chia dư | `15 % 4` | `3` |
| `**` | Lũy thừa | `2 ** 3` | `8` |

**Ví dụ:**

```python
a, b = 10, 3

print(f"{a} + {b} = {a + b}")    # 13
print(f"{a} - {b} = {a - b}")    # 7
print(f"{a} * {b} = {a * b}")    # 30
print(f"{a} / {b} = {a / b:.2f}")# 3.33
print(f"{a} // {b} = {a // b}")  # 3
print(f"{a} % {b} = {a % b}")    # 1
print(f"{a} ** {b} = {a ** b}")  # 1000
```

---

### **2.2. Toán tử so sánh (Comparison Operators)**

**Lý thuyết:**
So sánh hai giá trị, trả về `True` hoặc `False`.

| Toán tử | Ý nghĩa | Ví dụ | Kết quả |
|---------|---------|-------|---------|
| `==` | Bằng | `5 == 5` | `True` |
| `!=` | Khác | `5 != 3` | `True` |
| `>` | Lớn hơn | `5 > 3` | `True` |
| `<` | Nhỏ hơn | `5 < 3` | `False` |
| `>=` | Lớn hơn hoặc bằng | `5 >= 5` | `True` |
| `<=` | Nhỏ hơn hoặc bằng | `5 <= 3` | `False` |

**Ví dụ:**

```python
x, y = 10, 20

print(f"{x} == {y}: {x == y}")  # False
print(f"{x} != {y}: {x != y}")  # True
print(f"{x} > {y}: {x > y}")    # False
print(f"{x} < {y}: {x < y}")    # True
print(f"{x} >= {y}: {x >= y}")  # False
print(f"{x} <= {y}: {x <= y}")  # True
```

---

### **2.3. Toán tử logic (Logical Operators)**

**Lý thuyết:**
Kết hợp nhiều điều kiện, trả về `True` hoặc `False`.

| Toán tử | Ý nghĩa | Ví dụ | Kết quả |
|---------|---------|-------|---------|
| `and` | Và (cả hai đúng) | `True and False` | `False` |
| `or` | Hoặc (một đúng) | `True or False` | `True` |
| `not` | Phủ định | `not True` | `False` |

**Bảng chân lý:**

| A | B | A and B | A or B | not A |
|---|---|---------|--------|-------|
| True | True | True | True | False |
| True | False | False | True | False |
| False | True | False | True | True |
| False | False | False | False | True |

**Ví dụ:**

```python
# Toán tử cơ bản
print(f"True and False: {True and False}")  # False
print(f"True or False: {True or False}")    # True
print(f"not True: {not True}")              # False

# Kết hợp nhiều điều kiện
age = 25
has_degree = True
experience = 2

eligible = (18 <= age <= 30) and has_degree and (experience > 0)
print(f"Đủ điều kiện ứng tuyển: {eligible}")  # True
```

---

## **3. KIỂU DỮ LIỆU TẬP HỢP**

### **3.1. List (Danh sách)**

**Lý thuyết:**
- **List**: Có thứ tự, thay đổi được (mutable), cho phép phần tử trùng
- Tạo bằng dấu `[]`, chỉ số bắt đầu từ 0

**Phương thức quan trọng:**

| Phương thức | Chức năng | Ví dụ |
|------------|-----------|-------|
| `append(x)` | Thêm vào cuối | `list.append(5)` |
| `insert(i, x)` | Chèn tại vị trí i | `list.insert(0, 10)` |
| `remove(x)` | Xóa phần tử x đầu tiên | `list.remove(5)` |
| `pop(i)` | Xóa và trả về phần tử tại i | `list.pop(0)` |
| `sort()` | Sắp xếp tăng dần | `list.sort()` |

**Ví dụ:**

```python
# Tạo và truy cập list
numbers = [1, 2, 3, 4, 5]
print(f"List: {numbers}")
print(f"Phần tử đầu: {numbers[0]}")    # 1
print(f"Phần tử cuối: {numbers[-1]}")  # 5

# Cắt list (slicing)
print(f"2 phần tử đầu: {numbers[:2]}")   # [1, 2]
print(f"Từ vị trí 2: {numbers[2:]}")    # [3, 4, 5]
print(f"Các phần tử chẵn: {numbers[::2]}") # [1, 3, 5]

# Thay đổi list
numbers.append(6)          # Thêm vào cuối
numbers.insert(0, 0)       # Chèn ở đầu
numbers[1] = 100           # Thay đổi giá trị
print(f"Sau khi thay đổi: {numbers}")

# List comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Bình phương 1-5: {squares}")  # [1, 4, 9, 16, 25]
```

**Output:**
```
List: [1, 2, 3, 4, 5]
Phần tử đầu: 1
Phần tử cuối: 5
2 phần tử đầu: [1, 2]
Từ vị trí 2: [3, 4, 5]
Các phần tử chẵn: [1, 3, 5]
Sau khi thay đổi: [0, 100, 2, 3, 4, 5, 6]
Bình phương 1-5: [1, 4, 9, 16, 25]
```

---

### **3.2. Tuple**

**Lý thuyết:**
- **Tuple**: Có thứ tự, không thay đổi được (immutable), cho phép phần tử trùng
- Tạo bằng dấu `()`, nhanh hơn List về hiệu suất
- Dùng cho dữ liệu cố định (tọa độ, cấu hình)

**So sánh List vs Tuple:**

| Đặc điểm | List | Tuple |
|----------|------|-------|
| Khai báo | `[]` | `()` |
| Thay đổi | Được (mutable) | Không (immutable) |
| Hiệu suất | Chậm hơn | Nhanh hơn |
| Bộ nhớ | Tốn hơn | Tiết kiệm hơn |
| Dùng khi | Dữ liệu thay đổi | Dữ liệu cố định |

**Ví dụ:**

```python
# Tạo tuple
point = (10, 20)
colors = ("red", "green", "blue")
mixed = (1, "hello", 3.14, True)

print(f"Tuple điểm: {point}")
print(f"Phần tử thứ 2: {colors[1]}")  # green

# Không thể thay đổi
# point[0] = 100  # Lỗi: 'tuple' object does not support item assignment

# Tuple unpacking
x, y = point
print(f"x = {x}, y = {y}")  # x = 10, y = 20

# Chuyển đổi qua lại với list
my_list = list(colors)
my_tuple = tuple(my_list)
print(f"List từ tuple: {my_list}")
print(f"Tuple từ list: {my_tuple}")
```

---

### **3.3. Dictionary (Từ điển)**

**Lý thuyết:**
- **Dictionary**: Lưu trữ dữ liệu dạng `key: value`
- Key phải là immutable (string, number, tuple), value có thể là bất kỳ kiểu nào
- Tạo bằng dấu `{}`, từ Python 3.7+ có thứ tự

**Phương thức quan trọng:**

| Phương thức | Chức năng | Ví dụ |
|------------|-----------|-------|
| `get(key, default)` | Lấy giá trị theo key | `dict.get('name')` |
| `keys()` | Lấy danh sách keys | `dict.keys()` |
| `values()` | Lấy danh sách values | `dict.values()` |
| `items()` | Lấy cặp (key, value) | `dict.items()` |
| `update(dict2)` | Cập nhật từ dict2 | `dict.update(other)` |

**Ví dụ:**

```python
# Tạo dictionary
student = {
    "name": "Trần Thị B",
    "age": 20,
    "grades": [8.5, 9.0, 7.5],
    "graduated": False
}

print(f"Dictionary: {student}")

# Truy cập giá trị
print(f"Tên: {student['name']}")          # Trần Thị B
print(f"Tuổi: {student.get('age')}")      # 20
print(f"Địa chỉ: {student.get('address', 'Chưa có')}")  # Chưa có

# Thêm/sửa phần tử
student["class"] = "CNTT01"  # Thêm key mới
student["age"] = 21          # Sửa giá trị
print(f"Sau khi cập nhật: {student}")

# Duyệt dictionary
print("\nDuyệt bằng items():")
for key, value in student.items():
    print(f"  {key}: {value}")

# Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print(f"\nDictionary comprehension: {squares}")
```

**Output:**
```
Dictionary: {'name': 'Trần Thị B', 'age': 20, 'grades': [8.5, 9.0, 7.5], 'graduated': False}
Tên: Trần Thị B
Tuổi: 20
Địa chỉ: Chưa có
Sau khi cập nhật: {'name': 'Trần Thị B', 'age': 21, 'grades': [8.5, 9.0, 7.5], 'graduated': False, 'class': 'CNTT01'}

Duyệt bằng items():
  name: Trần Thị B
  age: 21
  grades: [8.5, 9.0, 7.5]
  graduated: False
  class: CNTT01

Dictionary comprehension: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

### **3.4. Set (Tập hợp)**

**Lý thuyết:**
- **Set**: Tập hợp các phần tử duy nhất, không có thứ tự
- Không cho phép phần tử trùng, tạo bằng dấu `{}` (không có key:value)
- Hỗ trợ các phép toán tập hợp: hợp, giao, hiệu

**Phép toán tập hợp:**

| Phép toán | Toán tử | Phương thức | Kết quả |
|-----------|---------|-------------|---------|
| Hợp (Union) | `\|` | `set.union()` | Phần tử thuộc A hoặc B |
| Giao (Intersection) | `&` | `set.intersection()` | Phần tử thuộc cả A và B |
| Hiệu (Difference) | `-` | `set.difference()` | Phần tử thuộc A, không thuộc B |

**Ví dụ:**

```python
# Tạo set
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Phép toán tập hợp
print(f"Hợp (A | B): {set_a | set_b}")           # {1, 2, 3, 4, 5, 6, 7, 8}
print(f"Giao (A & B): {set_a & set_b}")          # {4, 5}
print(f"Hiệu (A - B): {set_a - set_b}")          # {1, 2, 3}
print(f"Hiệu (B - A): {set_b - set_a}")          # {6, 7, 8}

# Phương thức cơ bản
set_a.add(6)          # Thêm phần tử
set_a.remove(1)       # Xóa phần tử (lỗi nếu không tồn tại)
set_a.discard(10)     # Xóa phần tử (không lỗi nếu không tồn tại)
print(f"\nSet A sau thay đổi: {set_a}")

# Kiểm tra phần tử
print(f"Có 3 trong set_a: {3 in set_a}")    # True
print(f"Có 10 trong set_a: {10 in set_a}")  # False

# Set comprehension
even_numbers = {x for x in range(10) if x % 2 == 0}
print(f"\nSố chẵn 0-9: {even_numbers}")
```

**Output:**
```
Set A: {1, 2, 3, 4, 5}
Set B: {4, 5, 6, 7, 8}
Hợp (A | B): {1, 2, 3, 4, 5, 6, 7, 8}
Giao (A & B): {4, 5}
Hiệu (A - B): {1, 2, 3}
Hiệu (B - A): {6, 7, 8}

Set A sau thay đổi: {2, 3, 4, 5, 6}
Có 3 trong set_a: True
Có 10 trong set_a: False

Số chẵn 0-9: {0, 2, 4, 6, 8}
```

---

**Tóm tắt Phần I:**

| Kiểu dữ liệu | Cú pháp | Có thứ tự | Thay đổi được | Cho phép trùng | Key-Value |
|-------------|---------|-----------|---------------|----------------|-----------|
| **List** | `[]` | ✓ | ✓ | ✓ | ✗ |
| **Tuple** | `()` | ✓ | ✗ | ✓ | ✗ |
| **Dictionary** | `{}` | ✓ (3.7+) | ✓ | Key: ✗, Value: ✓ | ✓ |
| **Set** | `{}` | ✗ | ✓ | ✗ | ✗ |

# **PHẦN II: CẤU TRÚC ĐIỀU KHIỂN VÀ HÀM**

## **4. CẤU TRÚC ĐIỀU KHIỂN**

### **4.1. Câu lệnh điều kiện (if-elif-else)**

**Lý thuyết:**
Thực thi code khác nhau dựa trên điều kiện đúng/sai.

**Luồng thực thi:**
```
if (điều kiện 1):
    # khối code 1
elif (điều kiện 2):
    # khối code 2
else:
    # khối code 3
```

**Ví dụ:**

```python
# Phân loại điểm số
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B" 
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Điểm {score} -> Xếp loại {grade}")

# Điều kiện lồng nhau
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("Được phép lái xe")
    else:
        print("Cần có bằng lái")
else:
    print("Chưa đủ tuổi lái xe")
```

**Output:**
```
Điểm 85 -> Xếp loại B
Được phép lái xe
```

---

### **4.2. Vòng lặp (Loops)**

#### **4.2.1. Vòng lặp for**

**Lý thuyết:**
Lặp qua từng phần tử trong một chuỗi (list, tuple, string, range).

**Cú pháp:**
```python
for biến in chuỗi:
    # khối code
```

**Hàm range():**
- `range(stop)`: 0 → stop-1
- `range(start, stop)`: start → stop-1  
- `range(start, stop, step)`: start → stop-1, bước nhảy step

**Ví dụ:**

```python
# Lặp qua list
fruits = ["táo", "chuối", "cam"]
for fruit in fruits:
    print(f"Tôi thích {fruit}")

# Dùng range()
print("\nĐếm 1-5:")
for i in range(1, 6):
    print(i)

print("\nSố chẵn 0-10:")
for i in range(0, 11, 2):
    print(i, end=" ")

# Dùng enumerate() lấy cả index
print("\n\nDanh sách với số thứ tự:")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
```

**Output:**
```
Tôi thích táo
Tôi thích chuối
Tôi thích cam

Đếm 1-5:
1
2
3
4
5

Số chẵn 0-10:
0 2 4 6 8 10 

Danh sách với số thứ tự:
1. táo
2. chuối
3. cam
```

---

#### **4.2.2. Vòng lặp while**

**Lý thuyết:**
Lặp khi điều kiện còn đúng, cần cơ chế để điều kiện trở thành sai.

**Cú pháp:**
```python
while điều_kiện:
    # khối code
```

**Ví dụ:**

```python
# Đếm ngược
count = 5
while count > 0:
    print(count)
    count -= 1
print("Bắt đầu!")

# Vòng lặp với break
number = 1
while True:
    if number % 7 == 0 and number % 3 == 0:
        print(f"Số đầu tiên chia hết cho 3 và 7 là: {number}")
        break
    number += 1

# Vòng lặp với continue
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue  # Bỏ qua số chẵn
    print(i, end=" ")
```

**Output:**
```
5
4
3
2
1
Bắt đầu!
Số đầu tiên chia hết cho 3 và 7 là: 21
1 3 5 7 9
```

---

#### **4.2.3. break, continue và else trong vòng lặp**

**Lý thuyết:**

| Lệnh | Chức năng |
|------|-----------|
| `break` | Thoát hoàn toàn khỏi vòng lặp |
| `continue` | Bỏ qua phần còn lại, chuyển sang lần lặp tiếp |
| `else` (trong vòng lặp) | Thực thi khi vòng lặp kết thúc bình thường (không break) |

**Ví dụ:**

```python
# break - tìm số đầu tiên chia hết cho 13
for i in range(1, 101):
    if i % 13 == 0:
        print(f"Số đầu tiên chia hết cho 13: {i}")
        break

# continue - bỏ qua số chia hết cho 3
print("\nSố 1-10 (bỏ qua số chia hết cho 3):")
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i, end=" ")

# else trong vòng lặp
print("\n\nKiểm tra số nguyên tố:")
num = 7
for i in range(2, num):
    if num % i == 0:
        print(f"{num} không phải số nguyên tố")
        break
else:
    # Chỉ chạy nếu không break
    print(f"{num} là số nguyên tố")
```

**Output:**
```
Số đầu tiên chia hết cho 13: 13

Số 1-10 (bỏ qua số chia hết cho 3):
1 2 4 5 7 8 10 

Kiểm tra số nguyên tố:
7 là số nguyên tố
```

---

## **5. HÀM (FUNCTIONS)**

### **5.1. Khái niệm và cú pháp cơ bản**

**Lý thuyết:**
Hàm là khối code có tên, thực hiện một nhiệm vụ cụ thể, có thể tái sử dụng.

**Cú pháp:**
```python
def tên_hàm(thamsố1, thamsố2=giátrị_mặcđịnh):
    """Docstring - mô tả hàm"""
    # thân hàm
    return kết_quả
```

**Ví dụ:**

```python
# Hàm không tham số
def chao():
    print("Xin chào!")

# Hàm có tham số
def binh_phuong(x):
    """Trả về bình phương của x"""
    return x ** 2

# Hàm có tham số mặc định
def tinh_luong(gio, luong_gio=50000):
    """Tính lương dựa trên số giờ làm"""
    return gio * luong_gio

# Gọi hàm
chao()
print(f"Bình phương của 5: {binh_phuong(5)}")
print(f"Lương 8 giờ: {tinh_luong(8):,} VND")
print(f"Lương 8 giờ với lương 60k/giờ: {tinh_luong(8, 60000):,} VND")
```

**Output:**
```
Xin chào!
Bình phương của 5: 25
Lương 8 giờ: 400,000 VND
Lương 8 giờ với lương 60k/giờ: 480,000 VND
```

---

### **5.2. Các loại tham số**

**Lý thuyết:**

| Loại tham số | Cú pháp | Mô tả |
|-------------|---------|-------|
| **Bắt buộc** | `def f(a, b)` | Phải truyền đầy đủ |
| **Mặc định** | `def f(a, b=10)` | Có giá trị mặc định nếu không truyền |
| **Tùy ý (*args)** | `def f(*args)` | Nhận nhiều tham số dưới dạng tuple |
| **Từ khóa (**kwargs)** | `def f(**kwargs)` | Nhận nhiều keyword arguments dưới dạng dict |

**Ví dụ:**

```python
# *args - nhận nhiều tham số
def tong(*args):
    """Tính tổng nhiều số"""
    return sum(args)

print(f"Tổng 3 số: {tong(1, 2, 3)}")
print(f"Tổng 5 số: {tong(1, 2, 3, 4, 5)}")

# **kwargs - nhận keyword arguments
def tao_ho_so(**kwargs):
    """Tạo hồ sơ từ các thông tin"""
    return kwargs

ho_so = tao_ho_so(ten="An", tuoi=25, dia_chi="Hà Nội")
print(f"Hồ sơ: {ho_so}")

# Kết hợp các loại tham số
def ham_day_du(bat_buoc, *args, mac_dinh=10, **kwargs):
    print(f"Bắt buộc: {bat_buoc}")
    print(f"Args: {args}")
    print(f"Mặc định: {mac_dinh}")
    print(f"Kwargs: {kwargs}")

ham_day_du("bắt buộc", 1, 2, 3, ten="An", tuoi=25)
```

**Output:**
```
Tổng 3 số: 6
Tổng 5 số: 15
Hồ sơ: {'ten': 'An', 'tuoi': 25, 'dia_chi': 'Hà Nội'}
Bắt buộc: bắt buộc
Args: (1, 2, 3)
Mặc định: 10
Kwargs: {'ten': 'An', 'tuoi': 25}
```

---

### **5.3. Phạm vi biến (Variable Scope)**

**Lý thuyết:**

| Phạm vi | Mô tả | Ví dụ |
|---------|-------|-------|
| **Local** | Trong hàm | `def f(): x = 10` |
| **Enclosing** | Trong hàm ngoài (hàm lồng nhau) | `def outer(): x=1; def inner(): ...` |
| **Global** | Ngoài tất cả hàm | `x = 10` ở module level |
| **Built-in** | Có sẵn trong Python | `len(), print(), type()` |

**Quy tắc LEGB (tìm biến):**
Local → Enclosing → Global → Built-in

**Ví dụ:**

```python
# Global scope
global_var = "Toàn cục"

def ham_ngoai():
    # Enclosing scope
    enclosing_var = "Hàm ngoài"
    
    def ham_trong():
        # Local scope
        local_var = "Hàm trong"
        print(f"Trong hàm: {local_var}")
        print(f"Truy cập enclosing: {enclosing_var}")
        print(f"Truy cập global: {global_var}")
    
    ham_trong()

# Gọi hàm
ham_ngoai()
print(f"Ngoài hàm: {global_var}")

# Thay đổi global từ trong hàm
count = 0

def tang_dem():
    global count  # Khai báo sử dụng biến global
    count += 1

print(f"\nTrước: {count}")
tang_dem()
print(f"Sau: {count}")
```

**Output:**
```
Trong hàm: Hàm trong
Truy cập enclosing: Hàm ngoài
Truy cập global: Toàn cục
Ngoài hàm: Toàn cục

Trước: 0
Sau: 1
```

---

### **5.4. Lambda Functions (Hàm ẩn danh)**

**Lý thuyết:**
Hàm một dòng, không có tên, tạo bằng từ khóa `lambda`.

**Cú pháp:**
```python
lambda arguments: expression
```

**So sánh với hàm thường:**

| Lambda Function | Hàm Thường |
|----------------|------------|
| `lambda x: x*2` | `def f(x): return x*2` |
| Không có tên | Có tên |
| Chỉ 1 biểu thức | Nhiều câu lệnh |

**Ví dụ:**

```python
# Lambda cơ bản
binh_phuong = lambda x: x ** 2
print(f"Bình phương 5: {binh_phuong(5)}")

# Lambda nhiều tham số
cong = lambda a, b: a + b
print(f"Tổng 3 + 4: {cong(3, 4)}")

# Lambda với điều kiện
chan_le = lambda x: "chẵn" if x % 2 == 0 else "lẻ"
print(f"Số 10 là số {chan_le(10)}")

# Dùng với map() và filter()
numbers = [1, 2, 3, 4, 5]

# map() - áp dụng hàm lên từng phần tử
bp_list = list(map(lambda x: x**2, numbers))
print(f"Bình phương: {bp_list}")

# filter() - lọc phần tử thỏa điều kiện
so_chan = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Số chẵn: {so_chan}")

# Sắp xếp với lambda
students = [
    {"ten": "An", "diem": 8.5},
    {"ten": "Bình", "diem": 7.0},
    {"ten": "Chi", "diem": 9.0}
]

# Sắp xếp theo điểm
sx_diem = sorted(students, key=lambda x: x["diem"], reverse=True)
print("\nSắp xếp theo điểm (giảm dần):")
for sv in sx_diem:
    print(f"  {sv['ten']}: {sv['diem']}")
```

**Output:**
```
Bình phương 5: 25
Tổng 3 + 4: 7
Số 10 là số chẵn
Bình phương: [1, 4, 9, 16, 25]
Số chẵn: [2, 4]

Sắp xếp theo điểm (giảm dần):
  Chi: 9.0
  An: 8.5
  Bình: 7.0
```

---

### **5.5. Docstrings và Documentation**

**Lý thuyết:**
Docstring là chuỗi mô tả hàm, nằm ngay sau định nghĩa.

**Quy ước:**
1. Dùng triple quotes (`"""` hoặc `'''`)
2. Dòng đầu: mô tả ngắn
3. Dòng trống
4. Chi tiết: tham số, giá trị trả về, ví dụ

**Ví dụ:**

```python
def tinh_diem_trung_binh(diem_so):
    """
    Tính điểm trung bình từ danh sách điểm.
    
    Args:
        diem_so (list): Danh sách điểm (số thực)
        
    Returns:
        float: Điểm trung bình
        
    Raises:
        ValueError: Nếu danh sách rỗng hoặc có giá trị không phải số
        
    Example:
        >>> tinh_diem_trung_binh([8.5, 9.0, 7.5])
        8.333333333333334
    """
    if not diem_so:
        raise ValueError("Danh sách điểm không được rỗng")
    
    # Kiểm tra tất cả là số
    if not all(isinstance(d, (int, float)) for d in diem_so):
        raise ValueError("Tất cả điểm phải là số")
    
    return sum(diem_so) / len(diem_so)

# Sử dụng hàm
try:
    diem = [8.5, 9.0, 7.5]
    tb = tinh_diem_trung_binh(diem)
    print(f"Điểm trung bình: {tb:.2f}")
    
    # Xem docstring
    print(f"\nDocstring của hàm:")
    print(tinh_diem_trung_binh.__doc__)
    
except ValueError as e:
    print(f"Lỗi: {e}")
```

**Output:**
```
Điểm trung bình: 8.33

Docstring của hàm:
    Tính điểm trung bình từ danh sách điểm.
    
    Args:
        diem_so (list): Danh sách điểm (số thực)
        
    Returns:
        float: Điểm trung bình
        
    Raises:
        ValueError: Nếu danh sách rỗng hoặc có giá trị không phải số
        
    Example:
        >>> tinh_diem_trung_binh([8.5, 9.0, 7.5])
        8.333333333333334
```

---

**Tóm tắt Phần II:**

| Cấu trúc | Mục đích | Cú pháp |
|----------|----------|---------|
| **if-elif-else** | Phân nhánh điều kiện | `if cond: ... elif: ... else: ...` |
| **for** | Lặp qua chuỗi | `for x in sequence: ...` |
| **while** | Lặp khi đk đúng | `while cond: ...` |
| **break** | Thoát vòng lặp | `break` |
| **continue** | Bỏ qua lần lặp | `continue` |
| **Hàm** | Tái sử dụng code | `def f(): ...` |
| **Lambda** | Hàm ẩn danh | `lambda x: x*2` |

# **PHẦN III: LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG NÂNG CAO**

## **6. KẾ THỪA NÂNG CAO & ABSTRACT CLASSES**

### **6.1. Multiple Inheritance (Đa kế thừa)**

**Lý thuyết:**
Cho phép một class kế thừa từ nhiều class cha. Python giải quyết xung đột bằng **MRO (Method Resolution Order)**.

**Diamond Problem (Vấn đề hình thoi):**
```
    A
   / \
  B   C
   \ /
    D
```
Khi D gọi phương thức, Python dùng MRO để xác định thứ tự tìm kiếm.

**MRO (Method Resolution Order):**
- Thứ tự tìm kiếm phương thức khi có đa kế thừa
- Dùng thuật toán C3 Linearization
- Kiểm tra: `ClassName.__mro__` hoặc `ClassName.mro()`

**Ví dụ:**

```python
class A:
    def show(self):
        return "A"

class B(A):
    def show(self):
        return "B"

class C(A):
    def show(self):
        return "C"

class D(B, C):
    pass

# Kiểm tra MRO
print("MRO của D:", [cls.__name__ for cls in D.__mro__])

# Tạo đối tượng và gọi phương thức
d = D()
print(f"d.show() = {d.show()}")  # Gọi theo MRO: D → B → C → A → object
```

**Output:**
```
MRO của D: ['D', 'B', 'C', 'A', 'object']
d.show() = B
```

**Lưu ý quan trọng:**
- MRO xác định thứ tự tìm kiếm phương thức
- `super()` gọi phương thức theo MRO
- Tránh đa kế thừa phức tạp gây khó bảo trì

---

### **6.2. Abstract Base Classes (ABCs)**

**Lý thuyết:**
Lớp trừu tượng định nghĩa interface mà các lớp con phải triển khai. Không thể tạo instance trực tiếp.

**Tại sao cần ABCs:**
1. Đảm bảo lớp con triển khai đủ phương thức
2. Định nghĩa interface rõ ràng
3. Hỗ trợ kiểm tra kiểu và tài liệu

**So sánh:**
| ABC (Abstract Class) | Interface (trong ngôn ngữ khác) |
|---------------------|--------------------------------|
| Có thể có phương thức cụ thể | Chỉ có phương thức trừu tượng |
| Có thể có thuộc tính | Chỉ có phương thức |
| Dùng `@abstractmethod` | Tất cả phương thức đều abstract |

**Ví dụ:**

```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract Base Class cho các hình học"""
    
    @abstractmethod
    def area(self):
        """Tính diện tích - PHẢI triển khai ở subclass"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Tính chu vi - PHẢI triển khai ở subclass"""
        pass
    
    def describe(self):
        """Phương thức cụ thể - đã có implementation"""
        return f"Diện tích: {self.area():.2f}, Chu vi: {self.perimeter():.2f}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# Sử dụng
shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(f"{shape.__class__.__name__}: {shape.describe()}")

# Không thể tạo instance của abstract class
try:
    s = Shape()  # Lỗi!
except TypeError as e:
    print(f"\nLỗi khi tạo Shape: {e}")
```

**Output:**
```
Circle: Diện tích: 78.54, Chu vi: 31.42
Rectangle: Diện tích: 24.00, Chu vi: 20.00

Lỗi khi tạo Shape: Can't instantiate abstract class Shape with abstract methods area, perimeter
```

---

### **6.3. Mixin Classes**

**Lý thuyết:**
Mixin là class cung cấp phương thức để được kế thừa bởi các class khác, nhưng không được thiết kế để đứng độc lập.

**Đặc điểm Mixin:**
- Không nên có `__init__` (hoặc gọi `super().__init__()`)
- Cung cấp functionality cụ thể
- Tên thường kết thúc bằng "Mixin"
- Không instantiate trực tiếp

**Khi nào dùng Mixin:**
- Thêm tính năng cụ thể vào nhiều class khác nhau
- Tránh đa kế thừa phức tạp
- Code tái sử dụng cao

**Ví dụ:**

```python
class JSONMixin:
    """Mixin cung cấp chức năng JSON serialization"""
    
    def to_json(self):
        """Chuyển object sang JSON string"""
        import json
        data = {k: v for k, v in self.__dict__.items() 
                if not k.startswith('_')}
        data['__class__'] = self.__class__.__name__
        return json.dumps(data, indent=2)

class ReprMixin:
    """Mixin cung cấp __repr__ tự động"""
    
    def __repr__(self):
        class_name = self.__class__.__name__
        attrs = ', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())
        return f'{class_name}({attrs})'

# Sử dụng Mixins
class Person(JSONMixin, ReprMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Tạo và sử dụng
p = Person("An", 25)
print("Object representation:", p)
print("\nJSON format:", p.to_json())
```

**Output:**
```
Object representation: Person(name='An', age=25)

JSON format: {
  "name": "An",
  "age": 25,
  "__class__": "Person"
}
```

---

## **7. MAGIC METHODS NÂNG CAO**

### **7.1. Container Protocol**

**Lý thuyết:**
Cho phép đối tượng hoạt động như container (list, dict). Các magic methods quan trọng:

| Magic Method | Mô tả | Gọi khi |
|-------------|-------|---------|
| `__len__()` | Trả về số phần tử | `len(obj)` |
| `__getitem__(key)` | Truy cập phần tử | `obj[key]` |
| `__setitem__(key, value)` | Gán giá trị | `obj[key] = value` |
| `__delitem__(key)` | Xóa phần tử | `del obj[key]` |
| `__contains__(item)` | Kiểm tra chứa | `item in obj` |
| `__iter__()` | Trả về iterator | `for x in obj` |

**Ví dụ:**

```python
class SimpleList:
    """Class mô phỏng list đơn giản"""
    
    def __init__(self, *items):
        self._items = list(items)
    
    def __len__(self):
        return len(self._items)
    
    def __getitem__(self, index):
        return self._items[index]
    
    def __setitem__(self, index, value):
        self._items[index] = value
    
    def __delitem__(self, index):
        del self._items[index]
    
    def __contains__(self, item):
        return item in self._items
    
    def __iter__(self):
        return iter(self._items)
    
    def __repr__(self):
        return f"SimpleList{tuple(self._items)}"

# Sử dụng
lst = SimpleList(1, 2, 3, 4, 5)

print(f"List: {lst}")
print(f"Độ dài: {len(lst)}")
print(f"Phần tử thứ 2: {lst[1]}")
print(f"Có số 3: {3 in lst}")

# Thay đổi phần tử
lst[0] = 100
print(f"Sau khi thay đổi: {lst}")

# Duyệt qua phần tử
print("Các phần tử:", end=" ")
for item in lst:
    print(item, end=" ")
```

**Output:**
```
List: SimpleList(1, 2, 3, 4, 5)
Độ dài: 5
Phần tử thứ 2: 2
Có số 3: True
Sau khi thay đổi: SimpleList(100, 2, 3, 4, 5)
Các phần tử: 100 2 3 4 5
```

---

### **7.2. Callable Protocol và Functors**

**Lý thuyết:**
Đối tượng có thể gọi được như hàm thông qua `__call__()`. Gọi là **functors** hoặc **callable objects**.

**Khi nào dùng:**
1. Stateful functions (hàm có trạng thái)
2. Function decorators
3. Strategy pattern, Command pattern

**Ví dụ:**

```python
class Multiplier:
    """Functor nhân với hệ số cố định"""
    
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

class Polynomial:
    """Functor biểu diễn đa thức: ax² + bx + c"""
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def __call__(self, x):
        return self.a * x**2 + self.b * x + self.c

# Sử dụng functors
double = Multiplier(2)
triple = Multiplier(3)

print(f"Gấp đôi 5: {double(5)}")    # 10
print(f"Gấp ba 5: {triple(5)}")     # 15

# Đa thức: 2x² + 3x + 1
p = Polynomial(2, 3, 1)
print(f"p(0) = {p(0)}")    # 1
print(f"p(1) = {p(1)}")    # 6
print(f"p(2) = {p(2)}")    # 15

# Strategy pattern với functors
class DiscountStrategy:
    """Chiến lược giảm giá (Strategy Pattern)"""
    
    def __call__(self, amount):
        raise NotImplementedError

class TenPercentDiscount(DiscountStrategy):
    def __call__(self, amount):
        return amount * 0.9

class FixedDiscount(DiscountStrategy):
    def __init__(self, discount):
        self.discount = discount
    
    def __call__(self, amount):
        return max(0, amount - self.discount)

# Sử dụng
ten_percent = TenPercentDiscount()
fixed_1000 = FixedDiscount(1000)

print(f"\nGiảm 10% cho 5000: {ten_percent(5000):.0f}")
print(f"Giảm 1000 cho 5000: {fixed_1000(5000):.0f}")
```

**Output:**
```
Gấp đôi 5: 10
Gấp ba 5: 15
p(0) = 1
p(1) = 6
p(2) = 15

Giảm 10% cho 5000: 4500
Giảm 1000 cho 5000: 4000
```

---

### **7.3. Context Manager Protocol**

**Lý thuyết:**
Cho phép đối tượng được dùng với `with statement`, đảm bảo tài nguyên được giải phóng đúng cách.

**Phương thức cần triển khai:**
1. `__enter__()`: Được gọi khi vào block `with`
2. `__exit__(exc_type, exc_val, exc_tb)`: Được gọi khi ra khỏi block `with`

**Khi nào dùng:**
- Quản lý tài nguyên (file, network, database)
- Đo thời gian, logging
- Thiết lập và dọn dẹp môi trường

**Ví dụ:**

```python
class Timer:
    """Context Manager đo thời gian thực thi"""
    
    def __enter__(self):
        import time
        self.start = time.time()
        print("Bắt đầu đo thời gian...")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        elapsed = self.end - self.start
        print(f"Kết thúc. Thời gian: {elapsed:.2f} giây")
        return True  # Ngăn exception lan truyền

class FileManager:
    """Context Manager quản lý file"""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        print(f"Mở file: {self.filename}")
        self.file = open(self.filename, self.mode, encoding='utf-8')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Đóng file: {self.filename}")
        self.file.close()
        if exc_type:
            print(f"Có lỗi: {exc_val}")
        return True

# Sử dụng Timer
print("1. Đo thời gian:")
with Timer():
    total = 0
    for i in range(1000000):
        total += i

# Sử dụng FileManager
print("\n2. Quản lý file:")
with FileManager("test.txt", "w") as f:
    f.write("Hello, Context Manager!\n")
    f.write("File sẽ tự động đóng.\n")

print("\n3. Đọc file vừa ghi:")
with FileManager("test.txt", "r") as f:
    content = f.read()
    print(content)
```

**Output:**
```
1. Đo thời gian:
Bắt đầu đo thời gian...
Kết thúc. Thời gian: 0.06 giây

2. Quản lý file:
Mở file: test.txt
Đóng file: test.txt

3. Đọc file vừa ghi:
Mở file: test.txt
Hello, Context Manager!
File sẽ tự động đóng.
Đóng file: test.txt
```

---

**Tóm tắt Phần III:**

| Khái niệm | Mục đích | Key Methods/Features |
|-----------|----------|---------------------|
| **Multiple Inheritance** | Kế thừa nhiều class cha | MRO, `super()`, diamond problem |
| **Abstract Classes** | Định nghĩa interface | `@abstractmethod`, ABC |
| **Mixin** | Thêm tính năng cụ thể | Không __init__, tái sử dụng code |
| **Container Protocol** | Đối tượng như container | `__len__`, `__getitem__`, `__iter__` |
| **Callable Protocol** | Đối tượng gọi được | `__call__()`, functors |
| **Context Manager** | Quản lý tài nguyên với `with` | `__enter__()`, `__exit__()` |

# **PHẦN IV: EXCEPTION HANDLING & FILE OPERATIONS**

## **8. XỬ LÝ LỖI (EXCEPTION HANDLING)**

### **8.1. try-except cơ bản**

**Lý thuyết:**
Xử lý lỗi trong Python dùng `try-except`. Khi code trong `try` gây lỗi, chương trình chuyển sang `except` thay vì crash.

**Cấu trúc:**
```python
try:
    # Code có thể gây lỗi
    risky_operation()
except ExceptionType:
    # Xử lý khi lỗi xảy ra
    handle_error()
```

**Ví dụ:**

```python
# Xử lý lỗi chia cho 0
try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
    print(f"Kết quả: {result}")
except ZeroDivisionError:
    print("❌ Lỗi: Không thể chia cho 0!")

# Xử lý nhiều loại lỗi
try:
    number = int("abc")  # ValueError
    data = [1, 2, 3]
    print(data[10])      # IndexError
except ValueError:
    print("❌ Không thể chuyển thành số")
except IndexError:
    print("❌ Chỉ số vượt quá giới hạn")
except Exception as e:   # Bắt tất cả lỗi còn lại
    print(f"❌ Lỗi khác: {type(e).__name__}")
```

**Output:**
```
❌ Lỗi: Không thể chia cho 0!
❌ Không thể chuyển thành số
```

---

### **8.2. try-except-else-finally**

**Lý thuyết:**
- `else`: Chạy nếu không có lỗi
- `finally`: Luôn chạy (dọn dẹp tài nguyên)

**Ví dụ:**

```python
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("❌ Không thể chia cho 0")
        return None
    except TypeError:
        print("❌ Sai kiểu dữ liệu")
        return None
    else:
        print(f"✅ Phép chia thành công")
        return result
    finally:
        print("🔧 Luôn chạy - dọn dẹp")

# Test
print("Test 1 - Chia bình thường:")
print(f"Kết quả: {divide(10, 2)}")

print("\nTest 2 - Chia cho 0:")
print(f"Kết quả: {divide(10, 0)}")

print("\nTest 3 - Sai kiểu dữ liệu:")
print(f"Kết quả: {divide(10, '2')}")
```

**Output:**
```
Test 1 - Chia bình thường:
✅ Phép chia thành công
🔧 Luôn chạy - dọn dẹp
Kết quả: 5.0

Test 2 - Chia cho 0:
❌ Không thể chia cho 0
🔧 Luôn chạy - dọn dẹp
Kết quả: None

Test 3 - Sai kiểu dữ liệu:
❌ Sai kiểu dữ liệu
🔧 Luôn chạy - dọn dẹp
Kết quả: None
```

---

### **8.3. Tạo Custom Exception**

**Lý thuyết:**
Tạo exception riêng bằng cách kế thừa từ `Exception`.

**Ví dụ:**

```python
class InvalidAgeError(Exception):
    """Exception cho tuổi không hợp lệ"""
    def __init__(self, age, message="Tuổi không hợp lệ"):
        self.age = age
        self.message = message
        super().__init__(f"{message}: {age}")

def register_user(age):
    if age < 0:
        raise InvalidAgeError(age, "Tuổi không thể âm")
    elif age < 18:
        raise InvalidAgeError(age, "Chưa đủ 18 tuổi")
    elif age > 120:
        raise InvalidAgeError(age, "Tuổi quá cao")
    else:
        print(f"✅ Đăng ký thành công cho tuổi {age}")

# Test
ages = [15, 25, -5, 150, 30]

for age in ages:
    try:
        register_user(age)
    except InvalidAgeError as e:
        print(f"❌ {e}")
```

**Output:**
```
❌ Chưa đủ 18 tuổi: 15
✅ Đăng ký thành công cho tuổi 25
❌ Tuổi không thể âm: -5
❌ Tuổi quá cao: 150
✅ Đăng ký thành công cho tuổi 30
```

---

### **8.4. assert statement**

**Lý thuyết:**
Dùng `assert` để kiểm tra điều kiện trong development, tự động raise `AssertionError` nếu sai.

**Ví dụ:**

```python
def calculate_discount(price, discount):
    assert price > 0, "Giá phải > 0"
    assert 0 <= discount <= 1, "Discount phải từ 0 đến 1"
    
    return price * (1 - discount)

# Test
try:
    print(f"Giảm 20% cho 100: {calculate_discount(100, 0.2)}")
    # print(calculate_discount(-50, 0.2))  # AssertionError
    # print(calculate_discount(100, 1.5))  # AssertionError
except AssertionError as e:
    print(f"❌ Assertion failed: {e}")
```

**Output:**
```
Giảm 20% cho 100: 80.0
```

---

## **9. FILE HANDLING (XỬ LÝ FILE)**

### **9.1. Mở và đọc file**

**Lý thuyết:**
Các mode mở file:
- `'r'`: Read (mặc định)
- `'w'`: Write (ghi đè)
- `'a'`: Append (thêm vào cuối)
- `'b'`: Binary mode
- `'t'`: Text mode (mặc định)

**Ví dụ:**

```python
# Ghi file
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Dòng 1: Hello Python\n")
    f.write("Dòng 2: File Handling\n")
    f.write("Dòng 3: 1,2,3,4,5\n")

print("✅ Đã ghi file data.txt")

# Đọc toàn bộ file
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("\nĐọc toàn bộ:")
    print(content)

# Đọc từng dòng
with open("data.txt", "r", encoding="utf-8") as f:
    print("\nĐọc từng dòng:")
    for i, line in enumerate(f, 1):
        print(f"{i}: {line.strip()}")
```

**Output:**
```
✅ Đã ghi file data.txt

Đọc toàn bộ:
Dòng 1: Hello Python
Dòng 2: File Handling
Dòng 3: 1,2,3,4,5

Đọc từng dòng:
1: Dòng 1: Hello Python
2: Dòng 2: File Handling
3: Dòng 3: 1,2,3,4,5
```

---

### **9.2. Xử lý file nâng cao**

**Lý thuyết:**
- `readline()`: Đọc một dòng
- `readlines()`: Đọc tất cả dòng thành list
- `seek()`: Di chuyển con trỏ file
- `tell()`: Vị trí hiện tại

**Ví dụ:**

```python
with open("sample.txt", "w+", encoding="utf-8") as f:
    # Ghi nhiều dòng
    lines = ["Python\n", "Java\n", "JavaScript\n", "C++\n"]
    f.writelines(lines)
    
    # Di chuyển về đầu file
    f.seek(0)
    
    # Đọc và xử lý
    print("Vị trí ban đầu:", f.tell())
    
    first_line = f.readline()
    print(f"Dòng 1: {first_line.strip()}")
    
    f.seek(0)  # Về đầu file
    all_lines = f.readlines()
    print(f"\nTất cả dòng ({len(all_lines)}):")
    for line in all_lines:
        print(f"  - {line.strip()}")
```

**Output:**
```
Vị trí ban đầu: 0
Dòng 1: Python

Tất cả dòng (4):
  - Python
  - Java
  - JavaScript
  - C++
```

---

### **9.3. JSON Serialization**

**Lý thuyết:**
JSON là định dạng trao đổi dữ liệu phổ biến. Python có module `json`.

**Ví dụ:**

```python
import json

# Dữ liệu Python
data = {
    "name": "Nguyễn Văn A",
    "age": 25,
    "courses": ["Python", "Data Science"],
    "graduated": False
}

# Chuyển thành JSON string
json_str = json.dumps(data, indent=2, ensure_ascii=False)
print("JSON String:")
print(json_str)

# Lưu vào file
with open("user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print("\n✅ Đã lưu vào user.json")

# Đọc từ file
with open("user.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    print("\nĐọc từ file:")
    print(f"Tên: {loaded_data['name']}")
    print(f"Tuổi: {loaded_data['age']}")
```

**Output:**
```
JSON String:
{
  "name": "Nguyễn Văn A",
  "age": 25,
  "courses": [
    "Python",
    "Data Science"
  ],
  "graduated": false
}

✅ Đã lưu vào user.json

Đọc từ file:
Tên: Nguyễn Văn A
Tuổi: 25
```

---

### **9.4. CSV File Handling**

**Lý thuyết:**
CSV (Comma-Separated Values) là định dạng bảng đơn giản.

**Ví dụ:**

```python
import csv

# Ghi file CSV
data = [
    ["Name", "Age", "City"],
    ["An", 25, "Hà Nội"],
    ["Bình", 30, "TP.HCM"],
    ["Chi", 22, "Đà Nẵng"]
]

with open("users.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)
print("✅ Đã ghi users.csv")

# Đọc file CSV
with open("users.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    print("\nĐọc CSV:")
    for row in reader:
        print(f"  {row}")
```

**Output:**
```
✅ Đã ghi users.csv

Đọc CSV:
  ['Name', 'Age', 'City']
  ['An', '25', 'Hà Nội']
  ['Bình', '30', 'TP.HCM']
  ['Chi', '22', 'Đà Nẵng']
```

---

**Tóm tắt Phần IV:**

| Kỹ thuật | Mục đích | Key Syntax |
|----------|----------|------------|
| **try-except** | Xử lý lỗi | `try: ... except: ...` |
| **try-else-finally** | Xử lý hoàn chỉnh | `try: ... except: ... else: ... finally: ...` |
| **Custom Exception** | Exception riêng | `class MyError(Exception):` |
| **assert** | Kiểm tra điều kiện | `assert condition, message` |
| **File Read/Write** | Xử lý file | `open()`, `read()`, `write()` |
| **JSON** | Serialization | `json.dumps()`, `json.loads()` |
| **CSV** | Bảng dữ liệu | `csv.reader()`, `csv.writer()` |

**Best Practices:**
1. Luôn dùng `with open()` để tự động đóng file
2. Xác định cụ thể loại exception (`except ValueError:`)
3. Dùng `finally` cho cleanup (đóng file, kết nối DB)
4. Validate data trước khi xử lý
5. Dùng encoding `utf-8` cho tiếng Việt

# **PHẦN V: MODULES, PACKAGES & STANDARD LIBRARY**

## **10. MODULES VÀ PACKAGES**

### **10.1. Modules là gì?**

**Lý thuyết:**
Module là file Python chứa code có thể tái sử dụng (hàm, class, biến).

**Tại sao cần modules:**
1. Tổ chức code thành phần nhỏ
2. Tái sử dụng code
3. Tránh xung đột tên
4. Che giấu implementation details

**Ví dụ:**
```python
# File: calculator.py (module)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

PI = 3.14159

# File: main.py (sử dụng module)
import calculator

result = calculator.add(5, 3)
print(f"5 + 3 = {result}")
print(f"PI = {calculator.PI}")

# Import cụ thể
from calculator import subtract
print(f"10 - 4 = {subtract(10, 4)}")

# Import với alias
import calculator as calc
print(f"7 + 2 = {calc.add(7, 2)}")
```

**Output:**
```
5 + 3 = 8
PI = 3.14159
10 - 4 = 6
7 + 2 = 9
```

---

### **10.2. Packages là gì?**

**Lý thuyết:**
Package là collection của nhiều modules, có file `__init__.py`.

**Cấu trúc package:**
```
my_package/
├── __init__.py
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
```

**Ví dụ:**
```python
# Tạo package đơn giản
# my_math/__init__.py
print("📦 Package my_math được import")

# my_math/operations.py
def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# my_math/geometry.py
def circle_area(radius):
    return 3.14159 * radius ** 2

# Sử dụng package
from my_math.operations import multiply, divide
from my_math.geometry import circle_area

print(f"6 × 7 = {multiply(6, 7)}")
print(f"15 ÷ 3 = {divide(15, 3)}")
print(f"Diện tích hình tròn r=5: {circle_area(5):.2f}")
```

**Output:**
```
📦 Package my_math được import
6 × 7 = 42
15 ÷ 3 = 5.0
Diện tích hình tròn r=5: 78.54
```

---

### **10.3. Import System**

**Lý thuyết:**
Các cách import khác nhau:

| Cách import | Ví dụ | Đặc điểm |
|------------|-------|----------|
| **Absolute** | `import package.module` | Import từ gốc |
| **Relative** | `from . import module` | Import tương đối |
| **Wildcard** | `from module import *` | Import tất cả (không nên dùng) |

**Ví dụ:**
```python
# Relative imports (trong package)
# from .submodule import function
# from ..parent_module import Class

# Kiểm tra __name__
print(f"Tên module: {__name__}")

# Chạy code chỉ khi là main
if __name__ == "__main__":
    print("Chạy trực tiếp file này")
else:
    print("Được import từ module khác")

# Kiểm tra sys.path
import sys
print(f"\nPath để tìm modules: {sys.path[:3]}...")
```

**Output (khi chạy trực tiếp):**
```
Tên module: __main__
Chạy trực tiếp file này

Path để tìm modules: ['/current/dir', '/usr/lib/python3.x', '/usr/lib/python3.x/site-packages']...
```

---

## **11. STANDARD LIBRARY QUAN TRỌNG**

### **11.1. Collections Module**

**Lý thuyết:**
Module `collections` cung cấp các container data types nâng cao.

**Các loại quan trọng:**
| Type | Mục đích | Ví dụ |
|------|----------|-------|
| `Counter` | Đếm phần tử | `Counter(['a', 'b', 'a'])` |
| `defaultdict` | Dict với giá trị mặc định | `defaultdict(list)` |
| `OrderedDict` | Dict giữ thứ tự | `OrderedDict()` |
| `deque` | Double-ended queue | `deque([1, 2, 3])` |
| `namedtuple` | Tuple với tên field | `Point = namedtuple('Point', 'x y')` |

**Ví dụ:**
```python
from collections import Counter, defaultdict, deque, namedtuple

# Counter - đếm phần tử
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = Counter(words)
print(f"Counter: {word_count}")
print(f"apple xuất hiện: {word_count['apple']} lần")

# defaultdict - dict với giá trị mặc định
fruit_colors = defaultdict(lambda: "unknown")
fruit_colors["apple"] = "red"
fruit_colors["banana"] = "yellow"
print(f"\ndefaultdict: {dict(fruit_colors)}")
print(f"Màu của orange: {fruit_colors['orange']}")  # Không lỗi

# deque - queue hai đầu
queue = deque([1, 2, 3])
queue.append(4)     # Thêm vào cuối
queue.appendleft(0) # Thêm vào đầu
print(f"\ndeque: {queue}")
print(f"Pop từ đầu: {queue.popleft()}")

# namedtuple - tuple có tên
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(f"\nnamedtuple: {p}")
print(f"Tọa độ x: {p.x}, y: {p.y}")
```

**Output:**
```
Counter: Counter({'apple': 3, 'banana': 2, 'orange': 1})
apple xuất hiện: 3 lần

defaultdict: {'apple': 'red', 'banana': 'yellow', 'orange': 'unknown'}
Màu của orange: unknown

deque: deque([0, 1, 2, 3, 4])
Pop từ đầu: 0

namedtuple: Point(x=10, y=20)
Tọa độ x: 10, y: 20
```

---

### **11.2. Datetime Module**

**Lý thuyết:**
Module `datetime` xử lý ngày giờ.

**Các class chính:**
| Class | Mục đích | Ví dụ |
|-------|----------|-------|
| `datetime` | Ngày + giờ | `datetime(2024, 1, 15, 10, 30)` |
| `date` | Chỉ ngày | `date(2024, 1, 15)` |
| `time` | Chỉ giờ | `time(10, 30)` |
| `timedelta` | Khoảng thời gian | `timedelta(days=5)` |

**Ví dụ:**
```python
from datetime import datetime, date, time, timedelta

# Ngày giờ hiện tại
now = datetime.now()
print(f"Hiện tại: {now}")
print(f"Năm: {now.year}, Tháng: {now.month}, Ngày: {now.day}")
print(f"Giờ: {now.hour}:{now.minute}:{now.second}")

# Định dạng ngày giờ
formatted = now.strftime("%d/%m/%Y %H:%M:%S")
print(f"Định dạng VN: {formatted}")

# Phân tích chuỗi thành datetime
date_str = "15/01/2024 14:30"
parsed = datetime.strptime(date_str, "%d/%m/%Y %H:%M")
print(f"Phân tích từ chuỗi: {parsed}")

# Tính toán với timedelta
today = date.today()
next_week = today + timedelta(days=7)
print(f"\nHôm nay: {today}")
print(f"7 ngày sau: {next_week}")

# So sánh thời gian
new_year = date(2024, 1, 1)
days_since = (today - new_year).days
print(f"Số ngày từ Tết đến nay: {days_since}")
```

**Output (sẽ thay đổi theo thời gian thực):**
```
Hiện tại: 2024-01-15 10:30:45.123456
Năm: 2024, Tháng: 1, Ngày: 15
Giờ: 10:30:45
Định dạng VN: 15/01/2024 10:30:45
Phân tích từ chuỗi: 2024-01-15 14:30:00

Hôm nay: 2024-01-15
7 ngày sau: 2024-01-22
Số ngày từ Tết đến nay: 14
```

---

### **11.3. Random Module**

**Lý thuyết:**
Module `random` tạo số ngẫu nhiên.

**Ví dụ:**
```python
import random

# Số ngẫu nhiên cơ bản
print(f"Số ngẫu nhiên 0-1: {random.random():.3f}")
print(f"Số nguyên 1-10: {random.randint(1, 10)}")
print(f"Số thực 1-10: {random.uniform(1, 10):.2f}")

# Chọn ngẫu nhiên từ list
colors = ["red", "green", "blue", "yellow"]
print(f"Màu ngẫu nhiên: {random.choice(colors)}")
print(f"2 màu ngẫu nhiên: {random.sample(colors, 2)}")
print(f"Xáo trộn list: {random.shuffle(colors)}; Sau shuffle: {colors}")

# Seed để kết quả có thể lặp lại
random.seed(42)  # Cố định seed
first = [random.randint(1, 100) for _ in range(3)]
random.seed(42)  # Reset với cùng seed
second = [random.randint(1, 100) for _ in range(3)]
print(f"\nVới seed=42: {first}")
print(f"Reset seed=42: {second}")
print(f"Kết quả giống nhau: {first == second}")
```

**Output (mỗi lần chạy khác nhau):**
```
Số ngẫu nhiên 0-1: 0.456
Số nguyên 1-10: 7
Số thực 1-10: 5.23
Màu ngẫu nhiên: green
2 màu ngẫu nhiên: ['red', 'blue']
Xáo trộn list: None; Sau shuffle: ['blue', 'green', 'red', 'yellow']

Với seed=42: [82, 15, 4]
Reset seed=42: [82, 15, 4]
Kết quả giống nhau: True
```

---

### **11.4. Pathlib (Modern Path Handling)**

**Lý thuyết:**
`pathlib` là cách hiện đại để làm việc với file paths (Python 3.4+).

**So sánh:**
| `os.path` (cũ) | `pathlib` (mới) |
|----------------|-----------------|
| `os.path.join('dir', 'file')` | `Path('dir') / 'file'` |
| `os.path.exists(path)` | `Path(path).exists()` |
| Hàm riêng lẻ | OOP style |

**Ví dụ:**
```python
from pathlib import Path

# Tạo Path object
current = Path.cwd()
print(f"Thư mục hiện tại: {current}")

# Tạo path mới
new_file = current / "data" / "file.txt"
print(f"Đường dẫn file: {new_file}")
print(f"Tên file: {new_file.name}")
print(f"Thư mục cha: {new_file.parent}")
print(f"Phần mở rộng: {new_file.suffix}")

# Kiểm tra file/directory
home = Path.home()
print(f"\nHome directory: {home}")
print(f"Home tồn tại: {home.exists()}")
print(f"Home là thư mục: {home.is_dir()}")

# Tạo thư mục và file
data_dir = Path("my_data")
data_dir.mkdir(exist_ok=True)  # Tạo nếu chưa có

file_path = data_dir / "data.txt"
file_path.write_text("Hello, Pathlib!", encoding="utf-8")

# Đọc file
content = file_path.read_text(encoding="utf-8")
print(f"\nNội dung file: {content}")

# Xóa
file_path.unlink()  # Xóa file
data_dir.rmdir()    # Xóa thư mục (phải rỗng)
print("Đã xóa file và thư mục")
```

**Output:**
```
Thư mục hiện tại: /current/working/directory
Đường dẫn file: /current/working/directory/data/file.txt
Tên file: file.txt
Thư mục cha: /current/working/directory/data
Phần mở rộng: .txt

Home directory: /home/username
Home tồn tại: True
Home là thư mục: True

Nội dung file: Hello, Pathlib!
Đã xóa file và thư mục
```

---

## **12. VIRTUAL ENVIRONMENTS**

### **12.1. Tại sao cần Virtual Environment?**

**Lý thuyết:**
Virtual environment tạo môi trường Python cô lập cho từng project.

**Lợi ích:**
1. Cô lập dependencies giữa các project
2. Tránh xung đột phiên bản package
3. Dễ replicate môi trường
4. An toàn cho system Python

### **12.2. Tạo và sử dụng venv**

**Ví dụ:**
```bash
# Tạo virtual environment
python -m venv myenv

# Kích hoạt (Linux/Mac)
source myenv/bin/activate

# Kích hoạt (Windows)
myenv\Scripts\activate

# Cài package trong venv
pip install requests numpy

# Xem installed packages
pip list

# Lưu requirements
pip freeze > requirements.txt

# Cài từ requirements.txt
pip install -r requirements.txt

# Tắt virtual environment
deactivate
```

**File `requirements.txt` mẫu:**
```
requests==2.28.1
numpy==1.23.5
pandas==1.5.0
```

---

### **12.3. Pipenv và Poetry (Modern Tools)**

**Lý thuyết:**
Tools hiện đại quản lý dependencies tốt hơn pip thuần.

| Tool | Ưu điểm |
|------|---------|
| **pipenv** | Combines pip + venv, có Pipfile |
| **poetry** | Dependency resolution tốt, publishing packages |

**Ví dụ Pipenv:**
```bash
# Cài đặt
pip install pipenv

# Tạo environment và cài package
pipenv install requests numpy

# Chạy script trong environment
pipenv run python script.py

# Vào shell của environment
pipenv shell
```

---

**Tóm tắt Phần V:**

| Kỹ thuật | Mục đích | Key Features |
|----------|----------|--------------|
| **Modules** | Tái sử dụng code | `.py` file, `import` statement |
| **Packages** | Tổ chức modules | `__init__.py`, directory structure |
| **Collections** | Data structures nâng cao | `Counter`, `defaultdict`, `deque` |
| **Datetime** | Xử lý ngày giờ | `datetime`, `timedelta`, `strftime/strptime` |
| **Random** | Tạo số ngẫu nhiên | `random()`, `choice()`, `shuffle()`, `seed()` |
| **Pathlib** | Xử lý đường dẫn | OOP style, `/` operator |
| **Virtual Env** | Cô lập môi trường | `venv`, `pip freeze`, `requirements.txt` |

**Best Practices:**
1. Đặt tên module/package không trùng với stdlib
2. Dùng absolute imports trong production code
3. Tránh `from module import *` (trừ `__init__.py`)
4. Luôn dùng virtual environment cho project
5. Ghi dependencies vào `requirements.txt`

# **PHẦN VI: PRACTICAL PYTHON & BEST PRACTICES**

## **13. REGULAR EXPRESSIONS (REGEX)**

### **13.1. Khái niệm Regex**

**Lý thuyết:**
Regular Expression là chuỗi đặc biệt mô tả pattern tìm kiếm trong text.

**Ký tự đặc biệt cơ bản:**
| Pattern | Ý nghĩa | Ví dụ |
|---------|---------|-------|
| `.` | Bất kỳ ký tự | `a.c` → "abc", "a c" |
| `*` | 0 hoặc nhiều | `ab*` → "a", "ab", "abb" |
| `+` | 1 hoặc nhiều | `ab+` → "ab", "abb" |
| `?` | 0 hoặc 1 | `ab?` → "a", "ab" |
| `[]` | Ký tự trong tập | `[aeiou]` → nguyên âm |
| `^` | Bắt đầu | `^Hello` → "Hello..." |
| `$` | Kết thúc | `end$` → "...end" |
| `\d` | Số | `\d` → "0"-"9" |
| `\w` | Chữ cái/số | `\w` → "a-z", "A-Z", "0-9", "_" |

**Ví dụ:**
```python
import re

text = "Python 3.10 released in 2021"
pattern = r'\d+'  # Tìm số

# Tìm tất cả số
numbers = re.findall(pattern, text)
print(f"Số trong text: {numbers}")

# Tìm và thay thế
new_text = re.sub(r'\d+', 'X', text)
print(f"Sau khi thay số: {new_text}")

# Tách bằng nhiều delimiter
data = "apple, banana; cherry|date"
items = re.split(r'[;,|]', data)
print(f"Các item: {items}")
```

**Output:**
```
Số trong text: ['3', '10', '2021']
Sau khi thay số: Python X.X released in X
Các item: ['apple', ' banana', ' cherry', 'date']
```

---

### **13.2. Regex thực tế**

**Ví dụ:**
```python
import re

# Validate email
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

emails = ["test@example.com", "invalid.email", "user@domain.co.uk"]
for email in emails:
    valid = "✓" if is_valid_email(email) else "✗"
    print(f"{valid} {email}")

# Extract phone numbers
text = "Liên hệ: 0912-345-678 hoặc 0987-654-321"
pattern = r'\d{4}-\d{3}-\d{3}'
phones = re.findall(pattern, text)
print(f"\nSố điện thoại: {phones}")

# Named groups để dễ đọc
pattern = r'(?P<prefix>\d{4})-(?P<middle>\d{3})-(?P<end>\d{3})'
match = re.search(pattern, text)
if match:
    print(f"Mã đầu: {match.group('prefix')}")
    print(f"Toàn bộ: {match.group()}")
```

**Output:**
```
✓ test@example.com
✗ invalid.email
✓ user@domain.co.uk

Số điện thoại: ['0912-345-678', '0987-654-321']
Mã đầu: 0912
Toàn bộ: 0912-345-678
```

---

## **14. LOGGING**

### **14.1. Logging cơ bản**

**Lý thuyết:**
Logging ghi lại hoạt động của chương trình, hữu ích cho debug và monitoring.

**Levels của log:**
| Level | Giá trị | Khi nào dùng |
|-------|--------|--------------|
| DEBUG | 10 | Thông tin chi tiết debug |
| INFO | 20 | Thông tin bình thường |
| WARNING | 30 | Cảnh báo vấn đề tiềm ẩn |
| ERROR | 40 | Lỗi chức năng nào đó |
| CRITICAL | 50 | Lỗi nghiêm trọng, crash |

**Ví dụ:**
```python
import logging

# Cấu hình cơ bản
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

# Ghi log các mức
logging.debug("Thông tin debug chi tiết")
logging.info("Ứng dụng bắt đầu chạy")
logging.warning("Cảnh báo: ổ đĩa sắp đầy")
logging.error("Lỗi mở file")
logging.critical("Hệ thống gặp sự cố nghiêm trọng")

# Log với context
user = "Nguyễn Văn A"
logging.info(f"Người dùng {user} đã đăng nhập")
```

**Output (console và file app.log):**
```
2024-01-15 10:30:45,123 - INFO - Ứng dụng bắt đầu chạy
2024-01-15 10:30:45,124 - WARNING - Cảnh báo: ổ đĩa sắp đầy
2024-01-15 10:30:45,125 - ERROR - Lỗi mở file
2024-01-15 10:30:45,126 - CRITICAL - Hệ thống gặp sự cố nghiêm trọng
2024-01-15 10:30:45,127 - INFO - Người dùng Nguyễn Văn A đã đăng nhập
```

---

### **14.2. Logging nâng cao**

**Ví dụ:**
```python
import logging

# Tạo logger riêng cho module
logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)

# Handler cho console (chỉ hiển thị INFO+)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Handler cho file (chỉ lưu ERROR+)
file_handler = logging.FileHandler("errors.log")
file_handler.setLevel(logging.ERROR)

# Định dạng khác nhau
console_format = logging.Formatter('%(levelname)s: %(message)s')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# Gắn handlers vào logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Sử dụng
logger.debug("Debug chi tiết")
logger.info("Thao tác thành công")
logger.error("Có lỗi xảy ra - ghi cả file và console")
```

**Output (console):**
```
INFO: Thao tác thành công
ERROR: Có lỗi xảy ra - ghi cả file và console
```

---

## **15. COMMAND LINE ARGUMENTS**

### **15.1. argparse Module**

**Lý thuyết:**
Xử lý tham số dòng lệnh chuyên nghiệp với `argparse`.

**Ví dụ:**
```python
import argparse

# Tạo parser
parser = argparse.ArgumentParser(
    description="Công cụ xử lý văn bản",
    prog="text_tool"
)

# Thêm các argument
parser.add_argument(
    "file",
    help="File đầu vào cần xử lý"
)

parser.add_argument(
    "-o", "--output",
    help="File đầu ra (mặc định: output.txt)",
    default="output.txt"
)

parser.add_argument(
    "-v", "--verbose",
    action="store_true",  # Không cần giá trị, có/không
    help="Hiển thị chi tiết xử lý"
)

parser.add_argument(
    "--count",
    type=int,
    default=1,
    help="Số lần lặp lại (mặc định: 1)"
)

# Giả lập parse arguments
args = parser.parse_args(["input.txt", "-v", "--count", "3"])

# Sử dụng các argument
print(f"Xử lý file: {args.file}")
print(f"Đầu ra: {args.output}")
print(f"Số lần lặp: {args.count}")
print(f"Verbose: {'Có' if args.verbose else 'Không'}")

# Chạy thực tế: python script.py input.txt -v --count 3
```

**Output:**
```
Xử lý file: input.txt
Đầu ra: output.txt
Số lần lặp: 3
Verbose: Có
```

---

### **15.2. Đọc Input từ User**

**Ví dụ:**
```python
# Đọc input đơn giản
name = input("Nhập tên của bạn: ")
print(f"Xin chào, {name}!")

# Chuyển đổi kiểu
age = int(input("Nhập tuổi: "))
print(f"Sau 5 năm bạn sẽ {age + 5} tuổi")

# Menu đơn giản
while True:
    print("\n--- MENU ---")
    print("1. Xem thông tin")
    print("2. Thay đổi cài đặt")
    print("3. Thoát")
    
    choice = input("Chọn: ")
    
    if choice == "3":
        print("Tạm biệt!")
        break
    elif choice == "1":
        print("Thông tin hệ thống...")
    elif choice == "2":
        print("Cài đặt hệ thống...")
    else:
        print("Lựa chọn không hợp lệ!")
```

---

## **16. TYPE HINTS & DOCUMENTATION**

### **16.1. Type Hints**

**Lý thuyết:**
Gợi ý kiểu dữ liệu giúp code rõ ràng, IDE hỗ trợ tốt hơn.

**Ví dụ:**
```python
from typing import List, Dict, Optional, Union, Tuple

# Hàm với type hints
def greet(name: str, age: int = 20) -> str:
    """Chào hỏi với tên và tuổi"""
    return f"Xin chào {name}, {age} tuổi"

# List và Dict với type hints
def process_items(items: List[str]) -> Dict[str, int]:
    """Xử lý list thành dict đếm độ dài"""
    return {item: len(item) for item in items}

# Optional (có thể None)
def find_user(user_id: int) -> Optional[str]:
    users = {1: "An", 2: "Bình"}
    return users.get(user_id)  # Trả về str hoặc None

# Union (nhiều kiểu có thể)
def calculate(value: Union[int, float]) -> Union[int, float]:
    return value * 2

# Sử dụng
print(greet("Nguyễn Văn A", 25))
print(process_items(["táo", "chuối"]))
print(f"User 1: {find_user(1)}")
print(f"Gấp đôi 5: {calculate(5)}")
```

**Output:**
```
Xin chào Nguyễn Văn A, 25 tuổi
{'táo': 6, 'chuối': 6}
User 1: An
Gấp đôi 5: 10
```

---

### **16.2. Documentation chuẩn**

**Lý thuyết:**
Docstring theo chuẩn giúp generate documentation tự động.

**Ví dụ:**
```python
def calculate_bmi(weight: float, height: float) -> float:
    """
    Tính chỉ số BMI (Body Mass Index).
    
    Công thức: BMI = weight / (height ** 2)
    
    Parameters
    ----------
    weight : float
        Cân nặng tính bằng kg
    height : float
        Chiều cao tính bằng mét
        
    Returns
    -------
    float
        Giá trị BMI
        
    Raises
    ------
    ValueError
        Nếu cân nặng hoặc chiều cao ≤ 0
        
    Examples
    --------
    >>> calculate_bmi(70, 1.75)
    22.86
    """
    if weight <= 0 or height <= 0:
        raise ValueError("Cân nặng và chiều cao phải > 0")
    
    return weight / (height ** 2)

# Sử dụng và xem documentation
print(f"BMI: {calculate_bmi(70, 1.75):.2f}")
print("\nDocumentation:")
print(calculate_bmi.__doc__)
```

**Output:**
```
BMI: 22.86

Documentation:
    Tính chỉ số BMI (Body Mass Index).
    
    Công thức: BMI = weight / (height ** 2)
    
    Parameters
    ----------
    weight : float
        Cân nặng tính bằng kg
    height : float
        Chiều cao tính bằng mét
        
    Returns
    -------
    float
        Giá trị BMI
        
    Raises
    ------
    ValueError
        Nếu cân nặng hoặc chiều cao ≤ 0
        
    Examples
    --------
    >>> calculate_bmi(70, 1.75)
    22.86
```

---

## **17. BEST PRACTICES TỔNG HỢP**

### **17.1. Code Style (PEP 8)**

**Quy tắc chính PEP 8:**
1. **Thụt lề**: 4 spaces (không dùng tab)
2. **Độ dài dòng**: ≤ 79 ký tự (code), ≤ 72 (comments)
3. **Đặt tên**:
   - Biến: `snake_case` (`user_name`)
   - Hàm: `snake_case` (`calculate_total`)
   - Class: `PascalCase` (`UserAccount`)
   - Constant: `UPPER_CASE` (`MAX_USERS`)
4. **Import order**: stdlib → third-party → local

**Ví dụ:**
```python
# GOOD STYLE
import os
import sys
from typing import List, Dict

import requests
import numpy as np

from my_module import MyClass

MAX_RETRIES = 3

def calculate_average(numbers: List[float]) -> float:
    """Tính trung bình của list số"""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

class DataProcessor:
    def __init__(self, data: List[int]):
        self.data = data
    
    def process(self) -> List[int]:
        return [x * 2 for x in self.data]

# BAD STYLE (tránh)
import os, sys  # Nhiều import một dòng
def CalculateTotal():  # Tên hàm nên snake_case
    pass
class data_processor:  # Tên class nên PascalCase
    pass
```

---

### **17.2. Error Handling Best Practices**

**Nguyên tắc:**
1. Specific exceptions trước
2. Không dùng bare `except:`
3. Dùng `finally` cho cleanup
4. Log đầy đủ thông tin

**Ví dụ:**
```python
import logging

logger = logging.getLogger(__name__)

def read_config_file(filename: str) -> dict:
    """
    Đọc file cấu hình.
    
    Trả về dict hoặc raise exception nếu lỗi.
    """
    config = {}
    file = None
    
    try:
        file = open(filename, 'r', encoding='utf-8')
        content = file.read()
        
        # Giả lập parse JSON
        import json
        config = json.loads(content)
        
        logger.info(f"Đọc thành công file: {filename}")
        
    except FileNotFoundError:
        logger.error(f"File không tồn tại: {filename}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"File JSON không hợp lệ: {e}")
        raise ValueError("Cấu hình không hợp lệ")
    except Exception as e:
        logger.exception(f"Lỗi không xác định: {e}")
        raise
    finally:
        if file:
            file.close()
            logger.debug("Đã đóng file")
    
    return config

# Test
try:
    config = read_config_file("config.json")
    print(f"Cấu hình: {config}")
except (FileNotFoundError, ValueError) as e:
    print(f"Lỗi: {e}")
```

---

### **17.3. Performance Tips**

**Mẹo tối ưu:**
1. List comprehension thay cho for loop
2. Dùng built-in functions (`sum()`, `map()`, `filter()`)
3. `join()` thay vì `+` cho nhiều strings
4. Tránh global variables

**Ví dụ so sánh:**
```python
import time

# CHẬM: Dùng + cho nhiều strings
start = time.time()
result = ""
for i in range(10000):
    result += str(i)
slow_time = time.time() - start

# NHANH: Dùng join()
start = time.time()
result = "".join(str(i) for i in range(10000))
fast_time = time.time() - start

print(f"Nối chuỗi với +: {slow_time:.4f}s")
print(f"Nối chuỗi với join: {fast_time:.4f}s")
print(f"join() nhanh hơn {slow_time/fast_time:.0f} lần")
```

**Output:**
```
Nối chuỗi với +: 0.0035s
Nối chuỗi với join: 0.0012s
join() nhanh hơn 3 lần
```

---

**Tóm tắt Phần VI:**

| Kỹ thuật | Mục đích | Key Features |
|----------|----------|--------------|
| **Regular Expressions** | Tìm kiếm/thay thế văn bản | `re.findall()`, `re.sub()`, patterns |
| **Logging** | Ghi log chương trình | Levels, handlers, formatters |
| **Command Line Args** | Xử lý tham số CLI | `argparse`, `input()` |
| **Type Hints** | Rõ ràng kiểu dữ liệu | `List`, `Dict`, `Optional`, `Union` |
| **Documentation** | Tài liệu hóa code | Docstrings, examples |
| **Best Practices** | Code chất lượng | PEP 8, error handling, performance |

**Quy tắc vàng:**
1. **DRY**: Don't Repeat Yourself
2. **KISS**: Keep It Simple, Stupid
3. **YAGNI**: You Ain't Gonna Need It
4. **Readability counts**: Code dễ đọc quan trọng hơn thông minh

# **PHẦN VII: KỸ THUẬT NÂNG CAO**

## **18. DECORATORS (HÀM TRANG TRÍ)**

### **18.1. Khái niệm Decorator**

**Lý thuyết:**
Decorator là hàm nhận một hàm làm tham số, trả về một hàm mới, cho phép thay đổi hành vi mà không sửa code gốc.

**Cơ chế hoạt động:**
```
@decorator
def function(): ... 

Tương đương: function = decorator(function)
```

**Ứng dụng:**
- Logging, timing
- Authentication, validation
- Caching, memoization
- Transaction management

**Ví dụ cơ bản:**

```python
def simple_decorator(func):
    """Decorator đơn giản: thêm dòng trước và sau"""
    def wrapper():
        print("═" * 30)
        print("Bắt đầu thực thi...")
        func()
        print("Hoàn thành!")
        print("═" * 30)
    return wrapper

@simple_decorator
def say_hello():
    print("Xin chào Python!")

say_hello()
```

**Output:**
```
══════════════════════════════
Bắt đầu thực thi...
Xin chào Python!
Hoàn thành!
══════════════════════════════
```

---

### **18.2. Decorator với tham số**

**Lý thuyết:**
Decorator có thể nhận tham số, trở thành **decorator factory** (hàm tạo decorator).

**Cấu trúc:**
```python
def decorator_factory(param):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Sử dụng param
            return func(*args, **kwargs)
        return wrapper
    return decorator

@decorator_factory(param_value)
def function(): ...
```

**Ví dụ:**

```python
def repeat(n_times):
    """Decorator gọi hàm n lần"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for i in range(n_times):
                print(f"Lần {i+1}: ", end="")
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Xin chào {name}!")
    return f"Đã chào {name}"

result = greet("An")
print(f"Kết quả: {result}")
```

**Output:**
```
Lần 1: Xin chào An!
Lần 2: Xin chào An!
Lần 3: Xin chào An!
Kết quả: ['Đã chào An', 'Đã chào An', 'Đã chào An']
```

---

### **18.3. Decorator cho hàm có tham số**

**Lý thuyết:**
Decorator wrapper cần xử lý cả `*args` và `**kwargs` để truyền tham số cho hàm gốc.

**Ví dụ:**

```python
import time

def measure_time(func):
    """Decorator đo thời gian thực thi"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️ {func.__name__} thực thi: {end-start:.4f}s")
        return result
    return wrapper

def validate_non_negative(func):
    """Decorator kiểm tra tham số không âm"""
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError("Tham số không được âm")
        return func(*args, **kwargs)
    return wrapper

@measure_time
@validate_non_negative
def factorial(n):
    """Tính giai thừa"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Test
print(f"5! = {factorial(5)}")
print(f"10! = {factorial(10)}")
```

**Output:**
```
⏱️ factorial thực thi: 0.0000s
5! = 120
⏱️ factorial thực thi: 0.0000s
10! = 3628800
```

---

### **18.4. Class Decorator**

**Lý thuyết:**
Decorator có thể áp dụng cho class, thay đổi hoặc bổ sung thuộc tính/phương thức.

**Ví dụ:**

```python
def add_methods(cls):
    """Decorator thêm phương thức vào class"""
    def greet(self):
        return f"Hello from {self.__class__.__name__}"
    
    cls.greet = greet
    cls.version = "1.0"
    return cls

@add_methods
class Person:
    def __init__(self, name):
        self.name = name

# Sử dụng
p = Person("An")
print(p.greet())      # Phương thức được thêm
print(Person.version) # Thuộc tính được thêm
```

**Output:**
```
Hello from Person
1.0
```

---

## **19. GENERATORS & ITERATORS**

### **19.1. Iterators**

**Lý thuyết:**
Iterator là đối tượng cho phép duyệt qua collection một phần tử tại một thời điểm.

**Protocol Iterator:**
1. `__iter__()`: Trả về chính iterator
2. `__next__()`: Trả về phần tử tiếp theo, ném `StopIteration` khi hết

**So sánh Iterable vs Iterator:**

| Iterable | Iterator |
|----------|----------|
| Có thể duyệt (for loop) | Thực hiện việc duyệt |
| Có `__iter__()` | Có `__iter__()` và `__next__()` |
| List, Tuple, String | Đối tượng từ `iter()` |

**Ví dụ:**

```python
class Countdown:
    """Iterator đếm ngược"""
    
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        num = self.current
        self.current -= 1
        return num

# Sử dụng
print("Đếm ngược từ 5:")
for num in Countdown(5):
    print(num, end=" ")

# Sử dụng next() trực tiếp
print("\n\nDùng next() trực tiếp:")
counter = Countdown(3)
try:
    while True:
        print(next(counter), end=" ")
except StopIteration:
    print("\nĐã hết!")
```

**Output:**
```
Đếm ngược từ 5:
5 4 3 2 1 

Dùng next() trực tiếp:
3 2 1 
Đã hết!
```

---

### **19.2. Generators**

**Lý thuyết:**
Generator là cách đơn giản tạo iterator, dùng từ khóa `yield` thay vì `return`.

**Đặc điểm:**
- Tự động có `__iter__()` và `__next__()`
- Giữ trạng thái giữa các lần gọi
- Hiệu quả bộ nhớ (lazy evaluation)

**So sánh Function vs Generator:**

| Function | Generator |
|----------|-----------|
| `return` trả giá trị, kết thúc | `yield` trả giá trị, tạm dừng |
| Chạy từ đầu mỗi lần gọi | Tiếp tục từ `yield` cuối |
| Trả về giá trị | Trả về generator object |

**Ví dụ:**

```python
def countdown_gen(n):
    """Generator đếm ngược"""
    while n > 0:
        yield n
        n -= 1

def fibonacci_gen(limit):
    """Generator dãy Fibonacci"""
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

# Sử dụng generator
print("Đếm ngược từ 3:")
for num in countdown_gen(3):
    print(num, end=" ")

print("\n\n10 số Fibonacci đầu:")
for num in fibonacci_gen(10):
    print(num, end=" ")

# Generator expression (giống list comprehension)
print("\n\nGenerator expression:")
squares = (x**2 for x in range(5))
print(f"Kiểu: {type(squares)}")
print(f"Giá trị: {list(squares)}")
```

**Output:**
```
Đếm ngược từ 3:
3 2 1 

10 số Fibonacci đầu:
0 1 1 2 3 5 8 13 21 34 

Generator expression:
Kiểu: <class 'generator'>
Giá trị: [0, 1, 4, 9, 16]
```

---

### **19.3. Generator với send() và yield from**

**Lý thuyết:**
Generators hỗ trợ tương tác hai chiều:
- `send(value)`: Gửi giá trị vào generator
- `yield from`: Ủy quyền cho generator khác

**Ví dụ:**

```python
def accumulator():
    """Generator có thể nhận giá trị qua send()"""
    total = 0
    while True:
        value = yield total  # Nhận giá trị, trả về total
        if value is None:
            break
        total += value

# Sử dụng với send()
print("Accumulator với send():")
gen = accumulator()
next(gen)  # Khởi tạo generator

print(f"Total: {gen.send(10)}")   # Gửi 10
print(f"Total: {gen.send(20)}")   # Gửi 20
print(f"Total: {gen.send(5)}")    # Gửi 5
gen.close()

# yield from
def chain_generators(*generators):
    """Chain nhiều generators lại"""
    for gen in generators:
        yield from gen

print("\nChain generators:")
gen1 = (x for x in range(3))
gen2 = (x**2 for x in range(3))
for value in chain_generators(gen1, gen2):
    print(value, end=" ")
```

**Output:**
```
Accumulator với send():
Total: 10
Total: 30
Total: 35

Chain generators:
0 1 2 0 1 4
```

---

## **20. CONTEXT MANAGERS**

### **20.1. Context Manager với @contextmanager**

**Lý thuyết:**
Module `contextlib` cung cấp `@contextmanager` để tạo context manager dễ dàng hơn bằng generator.

**Cấu trúc:**
```python
from contextlib import contextmanager

@contextmanager
def context_manager():
    # Setup code
    yield resource
    # Cleanup code
```

**Ví dụ:**

```python
from contextlib import contextmanager
import time

@contextmanager
def timer(name):
    """Context Manager đo thời gian"""
    start = time.time()
    print(f"⏱️ {name} bắt đầu...")
    yield
    print(f"✅ {name} hoàn thành: {time.time() - start:.2f}s")

@contextmanager 
def change_dir(path):
    """Tạm thời thay đổi thư mục làm việc"""
    import os
    old_dir = os.getcwd()
    print(f"📁 Chuyển đến: {path}")
    os.chdir(path)
    yield
    os.chdir(old_dir)
    print(f"📁 Quay về: {old_dir}")

# Sử dụng
print("1. Đo thời gian:")
with timer("tính tổng 1 triệu số"):
    total = sum(range(1000000))
    print(f"Tổng: {total:,}")

print("\n2. Multiple context managers:")
with timer("tổng hợp công việc"):
    # Nested context managers
    with open("test.txt", "w") as f:
        f.write("Hello World\n")
    
    with open("test.txt", "r") as f:
        print(f"Nội dung: {f.read()}")
```

**Output:**
```
1. Đo thời gian:
⏱️ tính tổng 1 triệu số bắt đầu...
Tổng: 499,999,500,000
✅ tính tổng 1 triệu số hoàn thành: 0.04s

2. Multiple context managers:
⏱️ tổng hợp công việc bắt đầu...
Nội dung: Hello World
✅ tổng hợp công việc hoàn thành: 0.00s
```

---

### **20.2. Context Manager thực tế**

**Ví dụ:**

```python
from contextlib import contextmanager

@contextmanager
def suppress_errors(*exceptions):
    """Context Manager bỏ qua lỗi cụ thể"""
    try:
        yield
    except exceptions as e:
        print(f"⚠️ Bỏ qua lỗi: {type(e).__name__}: {e}")

@contextmanager
def open_file(filename, mode='r'):
    """Context Manager mở file với xử lý lỗi"""
    file = None
    try:
        file = open(filename, mode, encoding='utf-8')
        yield file
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        raise
    finally:
        if file:
            file.close()
            print(f"✅ Đã đóng file: {filename}")

# Sử dụng
print("1. Bỏ qua lỗi ZeroDivisionError:")
with suppress_errors(ZeroDivisionError):
    result = 10 / 0  # Lỗi nhưng không crash
    print("Không chạy tới đây")

print("\n2. Quản lý file:")
try:
    with open_file("data.txt", "w") as f:
        f.write("Test data\n")
        # raise ValueError("Lỗi test")  # Thử uncomment
except:
    print("Có lỗi xảy ra")
```

**Output:**
```
1. Bỏ qua lỗi ZeroDivisionError:
⚠️ Bỏ qua lỗi: ZeroDivisionError: division by zero

2. Quản lý file:
✅ Đã đóng file: data.txt
```

---

**Tóm tắt Phần VII:**

| Kỹ thuật | Mục đích | Key Features |
|----------|----------|--------------|
| **Decorators** | Thay đổi hành vi hàm | `@decorator`, wrapper function |
| **Iterators** | Duyệt collection | `__iter__()`, `__next__()`, `StopIteration` |
| **Generators** | Tạo iterator đơn giản | `yield`, generator expression |
| **Context Managers** | Quản lý tài nguyên | `with`, `__enter__()`, `__exit__()`, `@contextmanager` |

**So sánh quan trọng:**
- **List comprehension** vs **Generator expression**: List tạo toàn bộ list, generator tạo từng phần tử khi cần
- **Function** vs **Generator**: Function chạy từ đầu, generator tiếp tục từ yield cuối
- **try-finally** vs **Context Manager**: Context manager rõ ràng và gọn hơn cho resource management

# **PHẦN VIII: META-PROGRAMMING & CONCURRENCY**

## **21. METACLASSES & DESCRIPTORS**

### **21.1. Khái niệm Metaclass**

**Lý thuyết:**
Metaclass là "class của class". Trong Python, mọi thứ đều là object, kể cả class. Metaclass kiểm soát cách class được tạo ra.

**Hierarchy trong Python:**
```
object (lớp cơ sở)
    ↓
type (metaclass mặc định)
    ↓
class (do metaclass tạo ra)
    ↓
instance (đối tượng)
```

**Tại sao cần Metaclass:**
1. Kiểm soát quá trình tạo class
2. Tự động thêm/modify methods/attributes
3. Validation class definition
4. ORM, API tự động

**So sánh:**
| | Instance (đối tượng) | Class | Metaclass |
|---|-------------------|-------|-----------|
| **Tạo ra** | Class | Metaclass | `type` hoặc metaclass khác |
| **Kiểm tra** | `isinstance()` | `issubclass()` | `isinstance(cls, type)` |
| **Mặc định** | - | `type` | `type` |

**Ví dụ:**

```python
# Kiểm tra metaclass mặc định
class SimpleClass:
    pass

obj = SimpleClass()

print(f"Kiểu của obj: {type(obj)}")          # <class '__main__.SimpleClass'>
print(f"Kiểu của SimpleClass: {type(SimpleClass)}")  # <class 'type'>
print(f"Kiểu của type: {type(type)}")        # <class 'type'>

# Tạo class bằng type (metaclass mặc định)
# type(name, bases, attrs)
Person = type('Person', (), {'name': 'Unknown', 'greet': lambda self: f"Hello, {self.name}"})

p = Person()
p.name = "An"
print(f"\nClass tạo bằng type: {p.greet()}")
```

**Output:**
```
Kiểu của obj: <class '__main__.SimpleClass'>
Kiểu của SimpleClass: <class 'type'>
Kiểu của type: <class 'type'>

Class tạo bằng type: Hello, An
```

---

### **21.2. Tạo Metaclass đơn giản**

**Lý thuyết:**
Metaclass kế thừa từ `type`, có thể override `__new__` hoặc `__init__`.

**Ví dụ:**

```python
class MyMeta(type):
    """Metaclass đơn giản: tự động thêm prefix cho tên class"""
    
    def __new__(cls, name, bases, attrs):
        # Thay đổi tên class
        new_name = f"Prefixed_{name}"
        
        # Thêm attribute mới
        attrs['created_by'] = "MyMeta"
        
        # Tạo class
        return super().__new__(cls, new_name, bases, attrs)

# Sử dụng metaclass
class MyClass(metaclass=MyMeta):
    pass

print(f"Tên class: {MyClass.__name__}")
print(f"Tạo bởi: {MyClass.created_by}")
print(f"Kiểu của MyClass: {type(MyClass)}")
```

**Output:**
```
Tên class: Prefixed_MyClass
Tạo bởi: MyMeta
Kiểu của MyClass: <class '__main__.MyMeta'>
```

---

### **21.3. Singleton Pattern với Metaclass**

**Lý thuyết:**
Singleton đảm bảo chỉ có một instance duy nhất của class.

**Ví dụ:**

```python
class SingletonMeta(type):
    """Metaclass tạo Singleton pattern"""
    
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print(f"🆕 Tạo instance mới của {cls.__name__}")
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        else:
            print(f"♻️ Sử dụng instance có sẵn của {cls.__name__}")
        
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connected = False
    
    def connect(self):
        if not self.connected:
            print(f"🔗 Kết nối đến: {self.connection_string}")
            self.connected = True

# Test Singleton
print("Singleton Pattern:")
db1 = Database("postgres://localhost/db1")
db1.connect()

db2 = Database("postgres://localhost/db2")  # Vẫn dùng instance đầu
print(f"db1 is db2: {db1 is db2}")
```

**Output:**
```
Singleton Pattern:
🆕 Tạo instance mới của Database
🔗 Kết nối đến: postgres://localhost/db1
♻️ Sử dụng instance có sẵn của Database
db1 is db2: True
```

---

### **21.4. Descriptors (Bộ mô tả)**

**Lý thuyết:**
Descriptor là object với `__get__()`, `__set__()`, hoặc `__delete__()` kiểm soát việc truy cập attributes.

**Loại Descriptor:**
| Loại | Có phương thức | Ví dụ |
|------|---------------|-------|
| Non-data descriptor | `__get__()` | Method, `@property` (chỉ getter) |
| Data descriptor | `__get__()` và `__set__()`/`__delete__()` | `@property` với setter |

**Protocol Descriptor:**
- `__get__(self, instance, owner)`: Truy cập attribute
- `__set__(self, instance, value)`: Gán giá trị
- `__delete__(self, instance)`: Xóa attribute

**Ví dụ:**

```python
class PositiveNumber:
    """Descriptor kiểm tra số dương"""
    
    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, 0)
    
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{self.name} phải là số dương")
        instance.__dict__[self.name] = value

class Person:
    age = PositiveNumber("age")  # Descriptor
    height = PositiveNumber("height")
    
    def __init__(self, age, height):
        self.age = age
        self.height = height

# Sử dụng
try:
    p = Person(25, 170)
    print(f"Tuổi: {p.age}, Chiều cao: {p.height}")
    
    p.age = 30  # Hợp lệ
    print(f"Sau thay đổi - Tuổi: {p.age}")
    
    # p.age = -5  # ValueError: age phải là số dương
    # p.height = -10  # ValueError: height phải là số dương
    
except ValueError as e:
    print(f"Lỗi: {e}")
```

**Output:**
```
Tuổi: 25, Chiều cao: 170
Sau thay đổi - Tuổi: 30
```

---

### **21.5. Property Descriptor**

**Lý thuyết:**
`@property` là built-in descriptor decorator, tạo attribute với getter/setter.

**Ví dụ:**

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter - lấy giá trị Celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter - đặt giá trị Celsius với validation"""
        if value < -273.15:
            raise ValueError("Nhiệt độ không thể dưới -273.15°C")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Property chỉ đọc (không có setter)"""
        return (self._celsius * 9/5) + 32

# Sử dụng
temp = Temperature(25)
print(f"{temp.celsius}°C = {temp.fahrenheit:.1f}°F")

temp.celsius = 30  # Dùng setter
print(f"Sau thay đổi: {temp.celsius}°C = {temp.fahrenheit:.1f}°F")

# temp.fahrenheit = 100  # Lỗi: property chỉ đọc
# temp.celsius = -300    # Lỗi: validation
```

**Output:**
```
25°C = 77.0°F
Sau thay đổi: 30°C = 86.0°F
```

---

## **22. CONCURRENCY & PARALLELISM**

### **22.1. Khái niệm cơ bản**

**Lý thuyết:**
- **Concurrency (Đồng thời)**: Nhiều tác vụ được thực hiện xen kẽ
- **Parallelism (Song song)**: Nhiều tác vụ được thực hiện cùng lúc

**GIL (Global Interpreter Lock):**
- Python (CPython) có GIL ngăn nhiều thread chạy Python code cùng lúc
- Threading chỉ hiệu quả cho I/O-bound tasks
- Multiprocessing vượt qua GIL bằng cách dùng nhiều process

**So sánh:**
| | Threading | Multiprocessing | Asyncio |
|---|-----------|----------------|---------|
| **Loại task** | I/O-bound | CPU-bound | I/O-bound |
| **GIL** | Bị ảnh hưởng | Không ảnh hưởng | Không áp dụng |
| **Bộ nhớ** | Chia sẻ | Riêng biệt | Chia sẻ |
| **Độ phức tạp** | Trung bình | Cao | Cao |

---

### **22.2. Threading (I/O-bound tasks)**

**Lý thuyết:**
Dùng `threading` module cho I/O operations (network, file, database).

**Ví dụ:**

```python
import threading
import time

def download_file(filename, seconds):
    """Hàm giả lập download file"""
    print(f"📥 Bắt đầu download {filename}...")
    time.sleep(seconds)  # Giả lập I/O
    print(f"✅ Hoàn thành {filename}")

# Tạo và chạy threads
print("Download nhiều file song song:")
threads = []

files = [("file1.txt", 2), ("file2.txt", 1), ("file3.txt", 3)]

for filename, sec in files:
    thread = threading.Thread(target=download_file, args=(filename, sec))
    threads.append(thread)
    thread.start()

# Chờ tất cả threads hoàn thành
for thread in threads:
    thread.join()

print("🎯 Tất cả download hoàn thành!")
```

**Output:**
```
Download nhiều file song song:
📥 Bắt đầu download file1.txt...
📥 Bắt đầu download file2.txt...
📥 Bắt đầu download file3.txt...
✅ Hoàn thành file2.txt
✅ Hoàn thành file1.txt
✅ Hoàn thành file3.txt
🎯 Tất cả download hoàn thành!
```

---

### **22.3. Multiprocessing (CPU-bound tasks)**

**Lý thuyết:**
Dùng `multiprocessing` module cho CPU-intensive tasks.

**Ví dụ:**

```python
import multiprocessing
import time
import math

def calculate_squares(numbers, result, index):
    """Tính bình phương của các số (CPU-bound)"""
    start = time.time()
    squares = [n**2 for n in numbers]
    result[index] = squares
    print(f"🔢 Process {index}: Tính {len(numbers)} số trong {time.time()-start:.2f}s")

if __name__ == "__main__":
    print("Multiprocessing cho CPU-bound tasks:")
    
    # Chia dữ liệu
    numbers = list(range(1, 1000001))
    chunk_size = len(numbers) // 4
    
    # Chia thành 4 phần
    chunks = [numbers[i:i+chunk_size] for i in range(0, len(numbers), chunk_size)]
    
    # Shared memory
    manager = multiprocessing.Manager()
    result = manager.dict()
    
    # Tạo processes
    processes = []
    start_time = time.time()
    
    for i, chunk in enumerate(chunks):
        p = multiprocessing.Process(target=calculate_squares, args=(chunk, result, i))
        processes.append(p)
        p.start()
    
    # Chờ processes hoàn thành
    for p in processes:
        p.join()
    
    total_time = time.time() - start_time
    print(f"\n⏱️ Tổng thời gian: {total_time:.2f}s")
    print(f"🎯 Đã tính bình phương của {len(numbers):,} số")
```

**Output:**
```
Multiprocessing cho CPU-bound tasks:
🔢 Process 0: Tính 250000 số trong 0.05s
🔢 Process 1: Tính 250000 số trong 0.05s
🔢 Process 2: Tính 250000 số trong 0.05s
🔢 Process 3: Tính 250000 số trong 0.05s

⏱️ Tổng thời gian: 0.10s
🎯 Đã tính bình phương của 1,000,000 số
```

---

### **22.4. Asyncio (Asynchronous Programming)**

**Lý thuyết:**
Dùng `asyncio` cho I/O-bound tasks, sử dụng `async/await`.

**Khái niệm:**
- **Coroutine**: Hàm bất đồng bộ (`async def`)
- **Event Loop**: Quản lý các coroutines
- **Task**: Coroutine được chạy trong event loop
- **await**: Chờ coroutine khác hoàn thành

**Ví dụ:**

```python
import asyncio
import time

async def fetch_data(task_id, seconds):
    """Coroutine giả lập fetch data"""
    print(f"🚀 Task {task_id} bắt đầu")
    await asyncio.sleep(seconds)  # Non-blocking sleep
    print(f"✅ Task {task_id} hoàn thành sau {seconds}s")
    return f"Data_{task_id}"

async def main():
    """Main coroutine"""
    print("Bắt đầu async tasks...")
    
    # Tạo tasks
    tasks = [
        fetch_data(1, 2),
        fetch_data(2, 1),
        fetch_data(3, 3)
    ]
    
    # Chạy đồng thời và chờ kết quả
    start = time.time()
    results = await asyncio.gather(*tasks)
    elapsed = time.time() - start
    
    print(f"\n🎯 Tất cả tasks hoàn thành trong {elapsed:.2f}s")
    print(f"Kết quả: {results}")

# Chạy event loop
asyncio.run(main())
```

**Output:**
```
Bắt đầu async tasks...
🚀 Task 1 bắt đầu
🚀 Task 2 bắt đầu
🚀 Task 3 bắt đầu
✅ Task 2 hoàn thành sau 1s
✅ Task 1 hoàn thành sau 2s
✅ Task 3 hoàn thành sau 3s

🎯 Tất cả tasks hoàn thành trong 3.00s
Kết quả: ['Data_1', 'Data_2', 'Data_3']
```

---

### **22.5. Kết hợp các kỹ thuật**

**Ví dụ:**

```python
import concurrent.futures
import asyncio
import time

def cpu_intensive(n):
    """CPU-bound task"""
    return sum(i*i for i in range(n))

async def async_io_task(task_id):
    """Async I/O-bound task"""
    await asyncio.sleep(1)
    return f"Async_{task_id}"

def run_mixed():
    """Kết hợp threading và multiprocessing"""
    with concurrent.futures.ThreadPoolExecutor() as thread_executor:
        # I/O tasks với threading
        io_futures = [thread_executor.submit(time.sleep, 1) for _ in range(3)]
        print("🚀 Chạy 3 I/O tasks với threading...")
    
    with concurrent.futures.ProcessPoolExecutor() as process_executor:
        # CPU tasks với multiprocessing
        cpu_futures = [process_executor.submit(cpu_intensive, 1000000) for _ in range(3)]
        print("🔢 Chạy 3 CPU tasks với multiprocessing...")
        
        results = [f.result() for f in cpu_futures]
        print(f"Kết quả CPU tasks: {results}")

async def run_async_tasks():
    """Chạy async tasks"""
    tasks = [async_io_task(i) for i in range(3)]
    results = await asyncio.gather(*tasks)
    print(f"Kết quả async tasks: {results}")

# Chạy tất cả
print("Kết hợp các kỹ thuật:")
run_mixed()

print("\nChạy async tasks:")
asyncio.run(run_async_tasks())
```

**Output:**
```
Kết hợp các kỹ thuật:
🚀 Chạy 3 I/O tasks với threading...
🔢 Chạy 3 CPU tasks với multiprocessing...
Kết quả CPU tasks: [333332833333500000, 333332833333500000, 333332833333500000]

Chạy async tasks:
Kết quả async tasks: ['Async_0', 'Async_1', 'Async_2']
```

---

**Tóm tắt Phần VIII:**

| Kỹ thuật | Mục đích | Key Features |
|----------|----------|--------------|
| **Metaclasses** | Kiểm soát tạo class | Kế thừa `type`, `__new__`, `__init__` |
| **Descriptors** | Kiểm soát attribute access | `__get__`, `__set__`, `__delete__`, `@property` |
| **Threading** | I/O-bound tasks | `threading.Thread`, GIL limitations |
| **Multiprocessing** | CPU-bound tasks | `multiprocessing.Process`, vượt GIL |
| **Asyncio** | Async I/O-bound tasks | `async/await`, `asyncio.run()`, event loop |

**Quy tắc chọn kỹ thuật:**
1. **I/O-bound, đơn giản** → Threading
2. **CPU-bound** → Multiprocessing
3. **I/O-bound, nhiều connections** → Asyncio
4. **Kết hợp I/O và CPU** → ThreadPool + ProcessPool

# **PHẦN IX: MEMORY MANAGEMENT & OPTIMIZATION**

## **23. QUẢN LÝ BỘ NHỚ TRONG PYTHON**

### **23.1. Cơ chế Reference Counting**

**Lý thuyết:**
Python dùng **reference counting** làm cơ chế chính: mỗi object có biến đếm tham chiếu (refcount). Khi refcount = 0, object được giải phóng.

**Cơ chế:**
1. Object tạo: refcount = 1
2. Thêm reference: refcount += 1
3. Xóa reference: refcount -= 1
4. refcount = 0 → object bị xóa

**Ví dụ:**

```python
import sys

a = [1, 2, 3]  # refcount = 1
print(f"Refcount của a: {sys.getrefcount(a) - 1}")

b = a  # refcount = 2
print(f"Sau b = a: {sys.getrefcount(a) - 1}")

c = [a]  # refcount = 3 (trong list)
print(f"Sau c = [a]: {sys.getrefcount(a) - 1}")

del b    # refcount = 2
del c[0] # refcount = 1 (list còn chứa a)
del a    # refcount = 0 → object được giải phóng
```

**Output:**
```
Refcount của a: 1
Sau b = a: 2
Sau c = [a]: 3
```

---

### **23.2. Circular References và Garbage Collection**

**Lý thuyết:**
**Circular reference** xảy ra khi các object tham chiếu vòng (A → B → A). Reference counting không giải quyết được, cần **Garbage Collector (GC)**.

**Garbage Collector:**
- **Generation 0**: Object mới
- **Generation 1**: Object sống sót sau GC
- **Generation 2**: Object sống sót lâu

**Ví dụ:**

```python
import gc

class Node:
    def __init__(self, name):
        self.name = name
        self.next = None
    
    def __del__(self):
        print(f"🗑️ Node {self.name} được giải phóng")

# Tạo circular reference
node1 = Node("A")
node2 = Node("B")
node1.next = node2
node2.next = node1  # Circular: A ↔ B

print("Circular reference đã tạo")
print(f"Node1 refcount: {sys.getrefcount(node1) - 1}")
print(f"Node2 refcount: {sys.getrefcount(node2) - 1}")

# Xóa reference bên ngoài
del node1
del node2

# Kích hoạt GC
print(f"\nGC thu thập: {gc.collect()} object(s)")
```

**Output:**
```
Circular reference đã tạo
Node1 refcount: 2
Node2 refcount: 2

GC thu thập: 2 object(s)
🗑️ Node B được giải phóng
🗑️ Node A được giải phóng
```

---

## **24. TỐI ƯU BỘ NHỚ**

### **24.1. Sử dụng __slots__**

**Lý thuyết:**
`__slots__` giảm memory usage bằng cách cố định thuộc tính, thay vì dùng `__dict__` động.

**So sánh:**

| Feature | Với `__dict__` | Với `__slots__` |
|---------|---------------|----------------|
| Memory usage | Cao | Thấp hơn 40-50% |
| Access speed | Bình thường | Nhanh hơn |
| Add attributes | Được | Không được |
| `__dict__` | Có | Không |

**Ví dụ:**

```python
class StudentNormal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class StudentSlots:
    __slots__ = ['name', 'age']
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Tạo objects
s1 = StudentNormal("An", 20)
s2 = StudentSlots("Bình", 21)

print(f"StudentNormal có __dict__: {hasattr(s1, '__dict__')}")
print(f"StudentSlots có __dict__: {hasattr(s2, '__dict__')}")

# So sánh memory
import sys
size_normal = sys.getsizeof(s1) + sys.getsizeof(s1.__dict__)
size_slots = sys.getsizeof(s2)

print(f"\nMemory usage:")
print(f"  StudentNormal: {size_normal} bytes")
print(f"  StudentSlots: {size_slots} bytes")
print(f"  Tiết kiệm: {((size_normal - size_slots) / size_normal * 100):.1f}%")

# Không thể thêm thuộc tính động với __slots__
s1.email = "an@email.com"  # OK
# s2.email = "binh@email.com"  # Lỗi: AttributeError
```

**Output:**
```
StudentNormal có __dict__: True
StudentSlots có __dict__: False

Memory usage:
  StudentNormal: 120 bytes
  StudentSlots: 56 bytes
  Tiết kiệm: 53.3%
```

---

### **24.2. Tối ưu Memory Usage**

**Lý thuyết:**
| Kỹ thuật | Mục đích | Ví dụ |
|----------|----------|-------|
| Generator | Tiết kiệm bộ nhớ lớn | `(x for x in range(N))` |
| `array` module | Mảng số hiệu quả | `array('i', [1, 2, 3])` |
| Memory views | Chia sẻ memory | `memoryview(bytearray)` |
| String interning | Trùng string object | `sys.intern()` |

**Ví dụ:**

```python
import sys
import array

# 1. Generator vs List
list_nums = [x for x in range(1000000)]  # Tạo list
gen_nums = (x for x in range(1000000))   # Tạo generator

print(f"List memory: {sys.getsizeof(list_nums):,} bytes")
print(f"Generator memory: {sys.getsizeof(gen_nums):,} bytes")

# 2. Array vs List
import array
list_ints = list(range(1000))
array_ints = array.array('i', range(1000))

print(f"\nList of ints: {sys.getsizeof(list_ints):,} bytes")
print(f"Array of ints: {sys.getsizeof(array_ints):,} bytes")

# 3. String interning
a = "hello"
b = "hello"
c = "hell" + "o"
print(f"\na is b: {a is b}")  # True - cùng object
print(f"a is c: {a is c}")    # True - Python tự optimize

# 4. Memory view
data = bytearray(b'abcdefgh')
mv = memoryview(data)
print(f"\nMemory view slice không copy: {mv[2:5].tobytes()}")
```

**Output:**
```
List memory: 8,448 bytes
Generator memory: 112 bytes

List of ints: 8,056 bytes
Array of ints: 4,060 bytes

a is b: True
a is c: True

Memory view slice không copy: b'cde'
```

---

## **25. PERFORMANCE OPTIMIZATION**

### **25.1. Profiling cơ bản**

**Lý thuyết:**
Profiling giúp tìm bottlenecks trong code.

**Công cụ:**
1. **`timeit`**: Đo thời gian thực thi
2. **`cProfile`**: Phân tích chi tiết
3. **`memory_profiler`**: Phân tích memory

**Ví dụ:**

```python
import timeit

def sum_list_loop(n):
    """Tính tổng bằng vòng lặp"""
    total = 0
    for i in range(n):
        total += i
    return total

def sum_builtin(n):
    """Tính tổng bằng built-in"""
    return sum(range(n))

def sum_formula(n):
    """Tính tổng bằng công thức"""
    return n * (n - 1) // 2

# Benchmark với timeit
n = 1000000
print(f"n = {n:,}")
print(f"Vòng lặp: {timeit.timeit(lambda: sum_list_loop(n), number=10):.4f}s")
print(f"Built-in sum: {timeit.timeit(lambda: sum_builtin(n), number=10):.4f}s")
print(f"Công thức: {timeit.timeit(lambda: sum_formula(n), number=10):.4f}s")
```

**Output:**
```
n = 1,000,000
Vòng lặp: 0.6855s
Built-in sum: 0.1014s
Công thức: 0.0000s
```

---

### **25.2. Tối ưu thuật toán**

**Lý thuyết:**
Chọn đúng thuật toán quan trọng hơn tối ưu chi tiết.

**Ví dụ:**

```python
import time

# O(n²) - Chậm
def find_duplicates_slow(lst):
    duplicates = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j] and lst[i] not in duplicates:
                duplicates.append(lst[i])
    return duplicates

# O(n) - Nhanh
def find_duplicates_fast(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

# Test
data = list(range(1000)) + [1, 2, 3, 1, 2, 3]

start = time.time()
result_slow = find_duplicates_slow(data)
time_slow = time.time() - start

start = time.time()
result_fast = find_duplicates_fast(data)
time_fast = time.time() - start

print(f"Duplicates: {result_fast}")
print(f"Thời gian O(n²): {time_slow:.4f}s")
print(f"Thời gian O(n): {time_fast:.6f}s")
print(f"Nhanh hơn: {time_slow/time_fast:.0f}x")
```

**Output:**
```
Duplicates: [1, 2, 3]
Thời gian O(n²): 0.1765s
Thời gian O(n): 0.0001s
Nhanh hơn: 1765x
```

---

### **25.3. Caching với lru_cache**

**Lý thuyết:**
`@lru_cache` cache kết quả hàm, hiệu quả cho hàm đệ quy hoặc tính toán nặng.

**Ví dụ:**

```python
from functools import lru_cache
import time

# Không cache
def fib_no_cache(n):
    if n <= 1:
        return n
    return fib_no_cache(n-1) + fib_no_cache(n-2)

# Có cache
@lru_cache(maxsize=None)
def fib_cached(n):
    if n <= 1:
        return n
    return fib_cached(n-1) + fib_cached(n-2)

print("Fibonacci không cache:")
start = time.time()
result1 = fib_no_cache(30)
time1 = time.time() - start
print(f"fib(30) = {result1}, thời gian: {time1:.2f}s")

print("\nFibonacci có cache:")
start = time.time()
result2 = fib_cached(30)
time2 = time.time() - start
print(f"fib(30) = {result2}, thời gian: {time2:.4f}s")
print(f"Nhanh hơn: {time1/time2:.0f}x")
```

**Output:**
```
Fibonacci không cache:
fib(30) = 832040, thời gian: 0.36s

Fibonacci có cache:
fib(30) = 832040, thời gian: 0.0001s
Nhanh hơn: 3600x
```

---

**Tóm tắt Phần IX:**

| Kỹ thuật | Mục đích | Key Points |
|----------|----------|------------|
| **Reference Counting** | Quản lý bộ nhớ | refcount = 0 → giải phóng |
| **Garbage Collection** | Xử lý circular ref | 3 generations, `gc.collect()` |
| **__slots__** | Giảm memory usage | Không `__dict__`, fixed attributes |
| **Generators** | Memory hiệu quả | `yield`, lazy evaluation |
| **Profiling** | Tìm bottlenecks | `timeit`, `cProfile` |
| **Algorithm** | Tối ưu performance | Chọn O(n) thay vì O(n²) |
| **Caching** | Tránh tính lại | `@lru_cache`, memoization |
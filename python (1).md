# LỜI NÓI ĐẦU

## 1. Giới thiệu về Python

Python là một ngôn ngữ lập trình bậc cao, thông dịch, hướng đối tượng và có ngữ nghĩa động. Ngôn ngữ này được thiết kế với triết lý ưu tiên khả năng đọc mã nguồn, cú pháp rõ ràng và dễ học. Python hỗ trợ nhiều mô hình lập trình, bao gồm lập trình cấu trúc, hướng đối tượng và lập trình hàm.

Python có nhiều phiên bản, trong đó hai nhánh chính là Python 2 và Python 3. Phiên bản Python 2 đã ngừng hỗ trợ từ ngày 1 tháng 1 năm 2020. Phiên bản Python 3 (bắt đầu từ 3.0) có nhiều thay đổi không tương thích ngược so với Python 2, tập trung vào việc loại bỏ các thiết kế không nhất quán và cải thiện ngôn ngữ. Người dùng mới nên bắt đầu với Python 3.

## 2. Mục tiêu tài liệu

Tài liệu này được biên soạn với mục tiêu cung cấp kiến thức toàn diện và chuyên sâu về ngôn ngữ lập trình Python, từ cú pháp cơ bản đến các kỹ thuật nâng cao và thư viện chuẩn. Tài liệu hướng đến đối tượng là người mới bắt đầu, lập trình viên có kinh nghiệm muốn nâng cao kiến thức, và các chuyên gia cần tra cứu chi tiết.

## 3. Cài đặt môi trường Python

Để sử dụng Python, trước hết cần cài đặt trình thông dịch (interpreter). Có nhiều cách để cài đặt Python:

1.  **Tải từ trang chủ python.org:** Truy cập [https://www.python.org/downloads/](https://www.python.org/downloads/) và tải bộ cài đặt phù hợp với hệ điều hành (Windows, macOS, Linux). Trong quá trình cài đặt, nhớ chọn tùy chọn "Add Python to PATH" (trên Windows) để có thể chạy lệnh `python` từ Command Prompt hoặc Terminal.
2.  **Sử dụng trình quản lý gói (Linux/macOS):** Trên các hệ điều hành dựa trên Unix, có thể sử dụng trình quản lý gói như `apt` (Ubuntu/Debian), `yum` (CentOS/RHEL), hoặc `brew` (macOS).
3.  **Sử dụng trình quản lý môi trường:** Các công cụ như `pyenv` (Linux/macOS) hoặc `pyenv-win` (Windows) cho phép cài đặt và quản lý nhiều phiên bản Python cùng lúc.

## 4. Giải thích các phần khi cài Python (IDE, PyCharm, v.v.)

Sau khi cài đặt trình thông dịch Python, bạn có thể viết mã bằng bất kỳ trình soạn thảo văn bản nào. Tuy nhiên, sử dụng Môi trường phát triển tích hợp (IDE) hoặc trình soạn thảo mã nguồn chuyên dụng sẽ nâng cao năng suất đáng kể nhờ các tính năng như gợi ý mã, gỡ lỗi, quản lý dự án.

-   **IDLE:** Là IDE mặc định đi kèm với bộ cài đặt Python. Phù hợp cho người mới bắt đầu với các tính năng cơ bản.
-   **PyCharm:** Một IDE mạnh mẽ, chuyên biệt cho Python do JetBrains phát triển. Có phiên bản Community (miễn phí) và Professional (trả phí). Cung cấp đầy đủ công cụ cho phát triển chuyên nghiệp.
-   **Visual Studio Code (VS Code):** Một trình soạn thảo mã nguồn nhẹ, mạnh mẽ và mở rộng được của Microsoft. Khi cài đặt extension "Python", nó trở thành một môi trường phát triển Python rất hiệu quả.
-   **Jupyter Notebook/JupyterLab:** Môi trường tương tác dựa trên web, lý tưởng cho khoa học dữ liệu, học máy và thử nghiệm mã từng phần.

## 5. Ứng dụng code tốt nhất (VS Code) và tùy thuộc vào hệ điều hành

Visual Studio Code (VS Code) được nhiều cộng đồng lập trình viên đánh giá cao nhờ sự kết hợp giữa hiệu suất, khả năng tùy biến và hệ sinh thái extension phong phú. Nó chạy được trên cả Windows, macOS và Linux.

-   **Trên Windows:** Cài đặt từ trang chủ Microsoft. Extension Python hỗ trợ đầy đủ, bao gồm thông dịch, gỡ lỗi, linting và quản lý môi trường ảo.
-   **Trên macOS:** Cài đặt tương tự, hoặc thông qua `brew`. VS Code tích hợp tốt với Terminal.
-   **Trên Linux:** Cài đặt qua trình quản lý gói (như `snap` hoặc tải file `.deb`/`.rpm`). Hoạt động ổn định với các công cụ dòng lệnh của Linux.

**Giảng thêm về các hệ điều hành:**
Mã Python về cơ bản là đa nền tảng (cross-platform), nghĩa là cùng một đoạn mã có thể chạy trên các hệ điều hành khác nhau mà không cần sửa đổi, nhờ vào trình thông dịch Python. Tuy nhiên, có một số điểm khác biệt cần lưu ý:
-   **Đường dẫn tệp:** Windows sử dụng dấu gạch chéo ngược (`\`), trong khi Unix (macOS, Linux) sử dụng dấu gạch chéo (`/`). Nên sử dụng mô-đun `os.path` hoặc `pathlib` để xử lý đường dẫn một cách an toàn.
-   **Biến môi trường:** Cách thiết lập và truy cập biến môi trường có sự khác biệt giữa các hệ thống.
-   **Quyền thực thi:** Trên hệ thống Unix, bạn cần cấp quyền thực thi (`chmod +x`) cho script Python nếu muốn chạy trực tiếp.
-   **Ký tự xuống dòng:** Windows sử dụng `\r\n` (CRLF), Unix sử dụng `\n` (LF). Mô-đun `open()` trong Python thường xử lý tự động sự khác biệt này.

---

# PHẦN I: NỀN TẢNG CƠ BẢN

## 1. CÚ PHÁP CƠ BẢN VÀ CẤU TRÚC CHƯƠNG TRÌNH

### 1.1. Python Comments

Chú thích (comments) là những đoạn văn bản trong mã nguồn được trình thông dịch Python bỏ qua, không thực thi. Chúng dùng để giải thích logic, ghi chú hoặc vô hiệu hóa mã tạm thời.

#### 1.1.1. Comment dòng đơn

Bắt đầu bằng dấu `#`. Tất cả ký tự từ `#` đến cuối dòng đều là chú thích.

```python
# Đây là một chú thích dòng đơn
x = 5  # Gán giá trị 5 cho biến x, đây cũng là chú thích
```

#### 1.1.2. Comment nhiều dòng

Python không có cú pháp riêng cho chú thích nhiều dòng. Thay vào đó, người ta thường sử dụng nhiều dòng chú thích đơn, hoặc sử dụng chuỗi ký tự (string) nhiều dòng (dùng ba dấu nháy đơn `'''` hoặc ba dấu nháy kép `"""`) mà không gán cho biến nào. Cách này thường được dùng cho docstring.

```python
# Đây là dòng chú thích thứ nhất
# Đây là dòng chú thích thứ hai
# Đây là dòng chú thích thứ ba

"""
Đoạn văn bản này nằm trong chuỗi ba nháy kép.
Trình thông dịch sẽ đọc nó như một chuỗi,
nhưng vì không được gán hay sử dụng,
nó không tạo ra hiệu ứng gì và có thể coi là chú thích.
Tuy nhiên, nó vẫn được phân tích cú pháp và chiếm bộ nhớ.
"""
```

#### 1.1.3. Docstrings

Docstring (viết tắt của documentation string) là một chuỗi ký tự đặc biệt xuất hiện ngay sau định nghĩa của một mô-đun, hàm, lớp hoặc phương thức. Nó được bao bởi ba dấu nháy kép (`"""`). Docstring được sử dụng để lưu trữ tài liệu mô tả chính thức cho đối tượng đó và có thể được truy xuất thông qua thuộc tính `__doc__`.

```python
def tinh_tong(a, b):
    """
    Hàm này trả về tổng của hai số.

    Tham số:
    a (int hoặc float): Số hạng thứ nhất.
    b (int hoặc float): Số hạng thứ hai.

    Trả về:
    int hoặc float: Tổng của a và b.
    """
    return a + b

# Truy xuất docstring
print(tinh_tong.__doc__)
```

**OUTPUT:**
```
    Hàm này trả về tổng của hai số.

    Tham số:
    a (int hoặc float): Số hạng thứ nhất.
    b (int hoặc float): Số hạng thứ hai.

    Trả về:
    int hoặc float: Tổng của a và b.
```

### 1.2. Indentation và Code Blocks

Khác với nhiều ngôn ngữ sử dụng dấu ngoặc nhọn `{}` để xác định khối mã (code block), Python sử dụng **thụt đầu dòng (indentation)**. Số lượng khoảng trắng thụt đầu dòng phải nhất quán trong toàn bộ khối mã. Theo quy ước PEP 8, nên sử dụng **4 khoảng trắng** cho mỗi cấp độ thụt đầu dòng. Không trộn lẫn tab và khoảng trắng.

```python
if 5 > 2:
    print("Năm lớn hơn hai!")  # Dòng này thuộc khối lệnh của if
    print("Đây vẫn là trong khối if.") # Cùng cấp thụt đầu dòng
print("Dòng này nằm ngoài khối if.") # Không thụt đầu dòng, không thuộc khối if
```

**OUTPUT:**
```
Năm lớn hơn hai!
Đây vẫn là trong khối if.
Dòng này nằm ngoài khối if.
```

### 1.3. Câu lệnh và Biểu thức

-   **Biểu thức (Expression):** Là một tổ hợp của các giá trị, biến, toán tử và lời gọi hàm. Biểu thức được **đánh giá (evaluate)** để tạo ra một **giá trị**. Ví dụ: `2 + 3`, `x * y`, `len("hello")`.
-   **Câu lệnh (Statement):** Là một đơn vị mã thực hiện một hành động, chẳng hạn như gán giá trị, điều khiển luồng, hoặc định nghĩa. Câu lệnh thường chứa biểu thức. Ví dụ: `x = 5` (câu lệnh gán), `if x > 0:` (câu lệnh điều kiện), `def hello():` (câu lệnh định nghĩa hàm).

Một chương trình Python về cơ bản là một chuỗi các câu lệnh được thực thi tuần tự.

### 1.4. Structure of a Python Program

Một chương trình Python thường có cấu trúc như sau, mặc dù không phải tất cả đều bắt buộc:

1.  **Dòng shebang (chỉ trên Unix/Linux):** `#!/usr/bin/env python3` - Chỉ định trình thông dịch để chạy script trực tiếp.
2.  **Encoding declaration (Python 2, hoặc cần thiết):** `# -*- coding: utf-8 -*-` - Khai báo mã hóa ký tự của tệp.
3.  **Module docstring:** Mô tả ngắn gọn về mô-đun.
4.  **Các lệnh `import`:** Nhập các mô-đun cần thiết.
5.  **Hằng số (constants):** Định nghĩa các biến không thay đổi.
6.  **Định nghĩa hàm và lớp (function/class definitions):** Phần thân chính của chương trình.
7.  **Mã thực thi chính:** Thường được đặt trong một điều kiện `if __name__ == "__main__":`. Điều này đảm bảo đoạn mã chỉ chạy khi tệp được thực thi trực tiếp, không phải khi được nhập như một mô-đun.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
mymodule.py
Đây là docstring của mô-đun, mô tả chức năng chính.
"""

import sys
import os

MAX_VALUE = 100  # Hằng số

def main():
    """Hàm chính của chương trình."""
    print("Chương trình đang chạy...")
    # ... logic chính ở đây ...

if __name__ == "__main__":
    main()  # Chỉ gọi hàm main() khi chạy script này
```

## 2. BIẾN VÀ KIỂU DỮ LIỆU CƠ BẢN

### 2.1. Variables trong Python

Biến là một vùng nhớ được đặt tên, dùng để lưu trữ dữ liệu. Trong Python, biến được tạo ra tại thời điểm bạn gán giá trị cho nó lần đầu tiên.

#### 2.1.1. Khai báo biến

Không cần từ khóa khai báo (như `int`, `var`). Chỉ cần dùng toán tử gán `=`.

```python
ten_bien = "Gia tri"
so_nguyen = 10
so_thuc = 3.14
```

#### 2.1.2. Quy tắc đặt tên biến

-   Tên biến phải bắt đầu bằng chữ cái (a-z, A-Z) hoặc dấu gạch dưới (`_`).
-   Phần còn lại có thể chứa chữ cái, chữ số (0-9) và dấu gạch dưới.
-   Tên biến **phân biệt chữ hoa chữ thường** (`age`, `Age`, và `AGE` là ba biến khác nhau).
-   Không được trùng với các từ khóa của Python (như `if`, `for`, `while`, `class`, v.v.).
-   Theo quy ước PEP 8, nên sử dụng **snake_case** (chữ thường, các từ phân cách bằng dấu gạch dưới) cho tên biến và hàm.

**Ví dụ hợp lệ:** `_private_var`, `ten_sinh_vien`, `bien_so_1`
**Ví dụ không hợp lệ:** `2bien` (bắt đầu bằng số), `ten-bien` (có dấu gạch ngang), `class` (trùng từ khóa)

#### 2.1.3. Gán nhiều biến

Python cho phép gán giá trị cho nhiều biến trong một dòng.

-   **Gán cùng một giá trị:** `x = y = z = 0`
-   **Gán nhiều giá trị:** `a, b, c = 1, 2, "hello"`

```python
# Gán cùng một giá trị
x = y = z = 10
print(f"x={x}, y={y}, z={z}")

# Gán nhiều giá trị
ten, tuoi, cao = "An", 25, 1.75
print(f"Tên: {ten}, Tuổi: {tuoi}, Chiều cao: {cao}")
```

**OUTPUT:**
```
x=10, y=10, z=10
Tên: An, Tuổi: 25, Chiều cao: 1.75
```

#### 2.1.4. Dynamic Typing (gõ động)

Python là ngôn ngữ gõ động (dynamically typed). Kiểu dữ liệu của biến được xác định tự động tại thời điểm chạy (runtime) dựa trên giá trị được gán cho nó. Một biến có thể được gán lại với giá trị thuộc kiểu dữ liệu khác.

```python
bien_linh_hoat = 4      # Hiện tại là kiểu int
print(type(bien_linh_hoat))

bien_linh_hoat = "bốn" # Giờ là kiểu str
print(type(bien_linh_hoat))

bien_linh_hoat = 4.0    # Giờ là kiểu float
print(type(bien_linh_hoat))
```

**OUTPUT:**
```
<class 'int'>
<class 'str'>
<class 'float'>
```

#### 2.1.5. Unpacking (gán giá trị từ collection cho nhiều biến)

Kỹ thuật "unpacking" cho phép bạn trích xuất các phần tử từ một tập hợp (như danh sách, tuple) và gán chúng vào các biến riêng lẻ.

```python
# Unpacking một list
danh_sach = [1, 2, 3]
a, b, c = danh_sach
print(f"a={a}, b={b}, c={c}")

# Unpacking một tuple
thong_tin = ("Bob", 30, "Hà Nội")
ten, tuoi, thanh_pho = thong_tin
print(f"{ten} sống ở {thanh_pho}")
```

**OUTPUT:**
```
a=1, b=2, c=3
Bob sống ở Hà Nội
```

### 2.2. Kiểu dữ liệu cơ bản

Python có nhiều kiểu dữ liệu dựng sẵn (built-in), được phân loại chính như sau:

| Loại | Tên kiểu | Mô tả | Ví dụ |
| :--- | :--- | :--- | :--- |
| **Số** | `int` | Số nguyên, không giới hạn độ dài. | `5`, `-10`, `1000000` |
| | `float` | Số thực dấu phẩy động (chính xác kép). | `3.14`, `-0.001`, `2.0e8` |
| | `complex` | Số phức, có phần thực và phần ảo. | `1+2j`, `3j` |
| **Boolean** | `bool` | Chỉ có hai giá trị: `True` hoặc `False`. | `True`, `False` |
| **Không** | `NoneType` | Đại diện cho sự không có giá trị, một đối tượng `None` duy nhất. | `None` |
| **Chuỗi** | `str` | Dãy các ký tự Unicode. | `"hello"`, `'Python'` |

#### 2.2.1. Numeric Types (`int`, `float`, `complex`)

-   `int`: Có thể là số âm hoặc dương, không có giới hạn. Toán tử chia (`/`) luôn trả về `float`. Toán tử chia lấy phần nguyên (`//`) và chia lấy phần dư (`%`) trả về `int`.
-   `float`: Được biểu diễn dưới dạng số thực dấu phẩy động. Có thể sử dụng ký hiệu khoa học (`e` hoặc `E`). Cẩn thận với sai số làm tròn khi so sánh.
-   `complex`: Được viết dưới dạng `a + bj`, trong đó `a` là phần thực, `b` là phần ảo. Có thể sử dụng `j` hoặc `J`. Phần thực và phần ảo là các số `float`.

#### 2.2.2. Boolean Type (`bool`) (gồm Truthy và Falsy values)

Kiểu `bool` là một trường hợp đặc biệt của `int`, trong đó `True` tương đương với `1` và `False` tương đương với `0`.

**Truthy và Falsy:**
Trong ngữ cảnh yêu cầu giá trị boolean (như điều kiện `if`, `while`), Python sẽ tự động chuyển đổi bất kỳ giá trị nào thành `True` hoặc `False`.
-   **Falsy values:** Các giá trị được coi là `False`. Bao gồm:
    -   `None`
    -   `False`
    -   Số `0` (cả `0` và `0.0`)
    -   Các chuỗi/rỗng: `""`, `''`
    -   Các tập hợp rỗng: `[]`, `()`, `{}`, `set()`
-   **Truthy values:** Tất cả các giá trị khác đều được coi là `True`.

```python
# Truthy và Falsy
if 0:
    print("Số 0 là Truthy")  # Không chạy
else:
    print("Số 0 là Falsy")   # Chạy dòng này

if "hello":
    print("Chuỗi không rỗng là Truthy")  # Chạy dòng này

if []:
    print("List rỗng là Truthy")  # Không chạy
else:
    print("List rỗng là Falsy")   # Chạy dòng này
```

**OUTPUT:**
```
Số 0 là Falsy
Chuỗi không rỗng là Truthy
List rỗng là Falsy
```

#### 2.2.3. None Type

`None` là một hằng số đặc biệt, đại diện cho sự vắng mặt của một giá trị. Nó là đối tượng duy nhất của kiểu `NoneType`. Thường được dùng để khởi tạo biến hoặc để chỉ ra rằng một hàm không trả về giá trị hữu ích nào.

```python
gia_tri_mac_dinh = None

def ham_khong_tra_ve_gi():
    print("Xin chào")
    # Không có lệnh return, hoặc có `return None`

ket_qua = ham_khong_tra_ve_gi()
print(ket_qua)  # Sẽ in ra None
```

**OUTPUT:**
```
Xin chào
None
```

### 2.3. Type Conversion (Casting)

Chuyển đổi kiểu dữ liệu là quá trình chuyển đổi giá trị từ kiểu này sang kiểu khác. Có hai loại: ngầm định (implicit) và tường minh (explicit).

#### 2.3.1. Implicit Conversion

Trình thông dịch Python tự động thực hiện khi cần thiết, thường là trong các phép toán hỗn hợp kiểu số.

```python
# int + float -> float
so_nguyen = 5
so_thuc = 2.5
ket_qua = so_nguyen + so_thuc  # Python tự chuyển `so_nguyen` thành 5.0
print(ket_qua, type(ket_qua))

# bool được dùng như int trong phép toán số học
print(True + 1)  # True là 1 -> 1+1=2
print(False * 10) # False là 0 -> 0*10=0
```

**OUTPUT:**
```
7.5 <class 'float'>
2
0
```

#### 2.3.2. Explicit Conversion (dùng `int()`, `float()`, `str()`, v.v.)

Sử dụng các hàm dựng sẵn để chuyển đổi một cách rõ ràng.

| Hàm | Mô tả | Ví dụ | Kết quả | Lưu ý |
| :--- | :--- | :--- | :--- | :--- |
| `int(x)` | Chuyển `x` thành số nguyên. | `int(3.9)` | `3` (cắt phần thập phân) |
| | | `int("42")` | `42` | Chuỗi phải biểu diễn số nguyên hợp lệ. |
| | | `int(True)` | `1` | |
| `float(x)` | Chuyển `x` thành số thực. | `float(7)` | `7.0` | |
| | | `float("3.14")` | `3.14` | Chuỗi phải biểu diễn số hợp lệ. |
| `str(x)` | Chuyển `x` thành chuỗi ký tự. | `str(100)` | `'100'` | |
| | | `str([1,2])` | `'[1, 2]'` | |
| `bool(x)` | Chuyển `x` thành boolean. | `bool(0)` | `False` | Theo quy tắc Truthy/Falsy. |
| | | `bool("Hi")` | `True` | |

```python
# Chuyển đổi tường minh
print(int(3.9))   # Kết quả: 3 (làm tròn xuống/cắt bỏ)
print(float(7))   # Kết quả: 7.0
print(str(123))   # Kết quả: '123'
print(bool(""))   # Kết quả: False

# Lỗi khi chuyển đổi không hợp lệ
# print(int("hello")) # ValueError: invalid literal for int()
# print(float("abc")) # ValueError: could not convert string to float:
```

**OUTPUT:**
```
3
7.0
123
False
```

### 2.4. Type Checking (`type()`, `isinstance()`)

-   `type(obj)`: Trả về đối tượng kiểu (type object) chính xác của `obj`.
-   `isinstance(obj, classinfo)`: Kiểm tra xem đối tượng `obj` có phải là một thể hiện của `classinfo` (hoặc một lớp con của nó) hay không. Hữu ích hơn khi kiểm tra tính kế thừa.

```python
so = 10
chuoi = "text"
danh_sach = [1, 2]

print(type(so))             # <class 'int'>
print(type(chuoi))          # <class 'str'>
print(type(danh_sach))      # <class 'list'>

print(isinstance(so, int))  # True
print(isinstance(so, float)) # False
print(isinstance(3.14, (int, float))) # True (kiểm tra trong một tuple các kiểu)
```

**OUTPUT:**
```
<class 'int'>
<class 'str'>
<class 'list'>
True
False
True
```

### 2.5. So sánh các kiểu dữ liệu cơ bản

| Kiểu dữ liệu | Ký hiệu | Đặc điểm chính | Khả năng thay đổi | Ví dụ |
| :--- | :--- | :--- | :--- | :--- |
| **Số nguyên** | `int` | Không giới hạn, không có phần thập phân. | Bất biến (immutable) | `x = 10` |
| **Số thực** | `float` | Có phần thập phân, có thể sai số. | Bất biến | `y = 3.14159` |
| **Số phức** | `complex` | Gồm phần thực và phần ảo. | Bất biến | `z = 2+3j` |
| **Boolean** | `bool` | Chỉ `True` hoặc `False`. | Bất biến | `flag = True` |
| **Chuỗi** | `str` | Dãy ký tự Unicode. | Bất biến | `s = "Hello"` |
| **NoneType** | `NoneType` | Đại diện cho không có giá trị. | Bất biến | `var = None` |

*Bất biến (Immutable)*: Giá trị của đối tượng không thể thay đổi sau khi được tạo. Khi bạn "thay đổi" nó, thực chất bạn đang tạo một đối tượng mới.
*Khả biến (Mutable)*: Giá trị có thể thay đổi tại chỗ.

## 3. TOÁN TỬ (OPERATORS)

Toán tử là các ký hiệu đặc biệt thực hiện các phép toán trên các toán hạng (biến và giá trị).

### 3.1. Arithmetic Operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`)

| Toán tử | Tên | Ví dụ | Kết quả | Ghi chú |
| :--- | :--- | :--- | :--- | :--- |
| `+` | Cộng | `5 + 3` | `8` | Với chuỗi, là nối chuỗi. |
| `-` | Trừ | `5 - 3` | `2` | |
| `*` | Nhân | `5 * 3` | `15` | Với chuỗi/list, là lặp lại. |
| `/` | Chia | `5 / 2` | `2.5` | Luôn trả về `float`. |
| `//` | Chia lấy phần nguyên | `5 // 2` | `2` | Làm tròn xuống (floor division). |
| `%` | Chia lấy phần dư | `5 % 2` | `1` | |
| `**` | Lũy thừa | `5 ** 2` | `25` | `5 ** 3` = 125 |

```python
a, b = 10, 3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")
```

**OUTPUT:**
```
10 + 3 = 13
10 - 3 = 7
10 * 3 = 30
10 / 3 = 3.3333333333333335
10 // 3 = 3
10 % 3 = 1
10 ** 3 = 1000
```

**Phân tích các trường hợp xảy ra:**
-   **Chia cho 0:** `5 / 0`, `5 // 0`, `5 % 0` đều gây ra lỗi `ZeroDivisionError`.
-   **Nhân số nguyên với số thực:** Kết quả luôn là `float`. Ví dụ: `3 * 2.5 = 7.5`.
-   **Cộng chuỗi với số:** `"Hello" + 5` gây ra lỗi `TypeError: can only concatenate str (not "int") to str`. Phải chuyển số thành chuỗi trước: `"Hello" + str(5)`.

### 3.2. Comparison Operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)

Dùng để so sánh hai giá trị, trả về `True` hoặc `False`.

| Toán tử | Tên | Ví dụ | Kết quả |
| :--- | :--- | :--- | :--- |
| `==` | Bằng | `5 == 5` | `True` |
| `!=` | Khác | `5 != 3` | `True` |
| `>` | Lớn hơn | `5 > 3` | `True` |
| `<` | Nhỏ hơn | `5 < 3` | `False` |
| `>=` | Lớn hơn hoặc bằng | `5 >= 5` | `True` |
| `<=` | Nhỏ hơn hoặc bằng | `5 <= 3` | `False` |

Các toán tử so sánh có thể được xâu chuỗi (chaining): `a < b <= c` tương đương với `a < b and b <= c`.

```python
x, y = 7, 10
print(f"{x} == {y}: {x == y}")
print(f"{x} != {y}: {x != y}")
print(f"{x} > {y}: {x > y}")
print(f"{x} < {y}: {x < y}")
print(f"{x} >= {y}: {x >= y}")
print(f"{x} <= {y}: {x <= y}")

# Xâu chuỗi so sánh
print(f"5 < 6 <= 10: {5 < 6 <= 10}")
```

**OUTPUT:**
```
7 == 10: False
7 != 10: True
7 > 10: False
7 < 10: True
7 >= 10: False
7 <= 10: True
5 < 6 <= 10: True
```

### 3.3. Logical Operators (`and`, `or`, `not`)

Dùng để kết hợp các điều kiện boolean.

| Toán tử | Mô tả | Ví dụ | Kết quả |
| :--- | :--- | :--- | :--- |
| `and` | Trả về `True` nếu **cả hai** điều kiện đều đúng. | `(5 > 3) and (10 > 5)` | `True` |
| `or` | Trả về `True` nếu **ít nhất một** điều kiện đúng. | `(5 > 3) or (5 > 10)` | `True` |
| `not` | Đảo ngược kết quả: `True` thành `False` và ngược lại. | `not(5 > 3)` | `False` |

Python sử dụng **đánh giá ngắn mạch (short-circuit evaluation)**:
-   Với `and`: Nếu điều kiện đầu tiên là `False`, kết quả chắc chắn là `False`, điều kiện thứ hai không được đánh giá.
-   Với `or`: Nếu điều kiện đầu tiên là `True`, kết quả chắc chắn là `True`, điều kiện thứ hai không được đánh giá.

```python
a, b = True, False
print(f"a and b: {a and b}")
print(f"a or b: {a or b}")
print(f"not a: {not a}")

# Short-circuit
def ham_loi():
    print("Hàm này được gọi")
    return True

print("Short-circuit với 'and':")
False and ham_loi()  # ham_loi() KHÔNG được gọi vì vế đầu đã False
print("Short-circuit với 'or':")
True or ham_loi()    # ham_loi() KHÔNG được gọi vì vế đầu đã True
```

**OUTPUT:**
```
a and b: False
a or b: True
not a: False
Short-circuit với 'and':
Short-circuit với 'or':
```

### 3.4. Assignment Operators (`=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`)

Toán tử gán dùng để gán giá trị cho biến. Các toán tử gán kết hợp (`+=`, `-=`, v.v.) thực hiện một phép toán trước rồi mới gán kết quả.

| Toán tử | Ví dụ | Tương đương với |
| :--- | :--- | :--- |
| `=` | `x = 5` | `x = 5` |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |
| `//=` | `x //= 3` | `x = x // 3` |
| `%=` | `x %= 3` | `x = x % 3` |
| `**=` | `x **= 3` | `x = x ** 3` |

```python
x = 10
print(f"Giá trị ban đầu: {x}")

x += 5  # x = 10 + 5 = 15
print(f"Sau x += 5: {x}")

x *= 2  # x = 15 * 2 = 30
print(f"Sau x *= 2: {x}")

x //= 4 # x = 30 // 4 = 7
print(f"Sau x //= 4: {x}")

x **= 2 # x = 7 ** 2 = 49
print(f"Sau x **= 2: {x}")
```

**OUTPUT:**
```
Giá trị ban đầu: 10
Sau x += 5: 15
Sau x *= 2: 30
Sau x //= 4: 7
Sau x **= 2: 49
```

### 3.5. Bitwise Operators (`&`, `|`, `^`, `~`, `<<`, `>>`)

Toán tử bitwise thao tác trực tiếp trên các bit của số nguyên.

| Toán tử | Tên | Mô tả | Ví dụ (`a=5=0b0101`, `b=3=0b0011`) |
| :--- | :--- | :--- | :--- |
| `&` | AND | Mỗi bit kết quả là 1 nếu cả hai bit tương ứng là 1. | `a & b = 1 (0b0001)` |
| `|` | OR | Mỗi bit kết quả là 1 nếu ít nhất một bit tương ứng là 1. | `a | b = 7 (0b0111)` |
| `^` | XOR | Mỗi bit kết quả là 1 nếu hai bit tương ứng khác nhau. | `a ^ b = 6 (0b0110)` |
| `~` | NOT | Đảo ngược tất cả các bit. (`~x = -x - 1`) | `~a = -6` |
| `<<` | Left shift | Dịch các bit sang trái, thêm 0 vào bên phải. `x << n = x * (2**n)` | `a << 1 = 10 (0b1010)` |
| `>>` | Right shift | Dịch các bit sang phải. `x >> n = x // (2**n)` | `a >> 1 = 2 (0b0010)` |

```python
a, b = 5, 3  # 5 = 0101, 3 = 0011
print(f"a = {a} (0b{a:04b}), b = {b} (0b{b:04b})")
print(f"a & b  = {a & b} (0b{(a & b):04b})  # AND")
print(f"a | b  = {a | b} (0b{(a | b):04b})  # OR")
print(f"a ^ b  = {a ^ b} (0b{(a ^ b):04b})  # XOR")
print(f"~a     = {~a}                      # NOT (bù 2)")
print(f"a << 1 = {a << 1} (0b{(a << 1):04b}) # Dịch trái")
print(f"a >> 1 = {a >> 1} (0b{(a >> 1):04b}) # Dịch phải")
```

**OUTPUT:**
```
a = 5 (0b0101), b = 3 (0b0011)
a & b  = 1 (0b0001)  # AND
a | b  = 7 (0b0111)  # OR
a ^ b  = 6 (0b0110)  # XOR
~a     = -6                      # NOT (bù 2)
a << 1 = 10 (0b1010) # Dịch trái
a >> 1 = 2 (0b0010) # Dịch phải
```

### 3.6. Identity Operators (`is`, `is not`)

Kiểm tra xem hai biến có tham chiếu đến **cùng một đối tượng** trong bộ nhớ hay không, chứ không phải so sánh giá trị.

#### 3.6.1. So sánh `==` (so sánh giá trị) vs `is` (so sánh đối tượng)

-   `==` (Equality): So sánh **giá trị** của các đối tượng. Hai đối tượng khác nhau có thể có giá trị bằng nhau.
-   `is` (Identity): So sánh **địa chỉ bộ nhớ** (id) của các đối tượng. Trả về `True` chỉ khi cả hai biến tham chiếu đến chính xác cùng một đối tượng.

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1  # list3 tham chiếu đến cùng đối tượng với list1

print("So sánh giá trị (==):")
print(f"list1 == list2: {list1 == list2}")  # True, vì giá trị giống nhau
print(f"list1 == list3: {list1 == list3}")  # True

print("\nSo sánh đối tượng (is):")
print(f"list1 is list2: {list1 is list2}")  # False, vì là hai đối tượng khác nhau
print(f"list1 is list3: {list1 is list3}")  # True, cùng một đối tượng

print(f"\nid(list1): {id(list1)}")
print(f"id(list2): {id(list2)}")
print(f"id(list3): {id(list3)}")
```

**OUTPUT:**
```
So sánh giá trị (==):
list1 == list2: True
list1 == list3: True

So sánh đối tượng (is):
list1 is list2: False
list1 is list3: True

id(list1): 140199485692544 (số này sẽ thay đổi mỗi lần chạy)
id(list2): 140199485693504
id(list3): 140199485692544
```

#### 3.6.2. Giải thích cơ chế CPython caching cho số nguyên nhỏ

Trình thông dịch CPython (phiên bản Python phổ biến nhất) tối ưu hóa bằng cách **cache (lưu trữ trước)** một dải số nguyên nhỏ (thường là từ -5 đến 256). Điều này có nghĩa là mỗi số nguyên trong dải đó chỉ tồn tại **một đối tượng duy nhất** trong bộ nhớ. Mọi biến gán cùng một số trong dải này đều sẽ tham chiếu đến cùng một đối tượng được cache.

**Đây là một hành vi tối ưu hóa của trình thông dịch CPython và không được đảm bảo trong mọi tình huống hoặc mọi triển khai Python khác (như PyPy, Jython).**

```python
a = 100
b = 100
print(f"a is b (với 100): {a is b}")  # True, vì 100 nằm trong dải cache

c = 300
d = 300
print(f"c is d (với 300): {c is d}")  # Có thể True hoặc False tùy môi trường/trình thông dịch.
# Trong chế độ tương tác (REPL), thường là False.
# Trong script, với CPython, có thể là True do tối ưu hóa peephole.
# KHÔNG nên dựa vào hành vi này.

# Luôn dùng `==` để so sánh giá trị số.
print(f"c == d (với 300): {c == d}")  # Luôn True
```

**OUTPUT (có thể thay đổi):**
```
a is b (với 100): True
c is d (với 300): True  # Hoặc False
c == d (với 300): True
```

### 3.7. Membership Operators (`in`, `not in`)

Kiểm tra xem một giá trị có tồn tại trong một chuỗi, danh sách, tuple, từ điển (khóa) hoặc tập hợp hay không.

-   `in`: Trả về `True` nếu tìm thấy giá trị trong tập hợp.
-   `not in`: Trả về `True` nếu không tìm thấy giá trị trong tập hợp.

```python
chuoi = "Hello World"
danh_sach = [1, 2, 3, 4, 5]
tu_dien = {"tên": "An", "tuổi": 25}

print(f"'H' in chuoi: {'H' in chuoi}")
print(f"'x' not in chuoi: {'x' not in chuoi}")
print(f"3 in danh_sach: {3 in danh_sach}")
print(f"6 not in danh_sach: {6 not in danh_sach}")
print(f"'tên' in tu_dien: {'tên' in tu_dien}")  # Kiểm tra khóa
print(f"'An' in tu_dien: {'An' in tu_dien}")    # 'An' là giá trị, không phải khóa -> False
```

**OUTPUT:**
```
'H' in chuoi: True
'x' not in chuoi: True
3 in danh_sach: True
6 not in danh_sach: True
'tên' in tu_dien: True
'An' in tu_dien: False
```

### 3.8. Walrus Operator (`:=`) (Python 3.8+)

Toán tử "walrus" (hải mã) cho phép **vừa gán giá trị cho biến vừa trả về giá trị đó** trong một biểu thức. Điều này giúp viết mã ngắn gọn hơn, đặc biệt trong các vòng lặp và điều kiện.

```python
# Không dùng walrus
nhap = input("Nhập một số: ")
while nhap != "quit":
    print(f"Bạn đã nhập: {nhap}")
    nhap = input("Nhập một số: ")

# Dùng walrus operator
while (nhap := input("Nhập một số (hoặc 'quit' để dừng): ")) != "quit":
    print(f"Bạn đã nhập: {nhap}")
```

**OUTPUT (ví dụ chạy):**
```
Nhập một số (hoặc 'quit' để dừng): 10
Bạn đã nhập: 10
Nhập một số (hoặc 'quit' để dừng): 20
Bạn đã nhập: 20
Nhập một số (hoặc 'quit' để dừng): quit
```

```python
# Ví dụ khác: Tính toán và kiểm tra trong if
if (n := len([1,2,3,4])) > 3:
    print(f"Danh sách có {n} phần tử, nhiều hơn 3.")
```

**OUTPUT:**
```
Danh sách có 4 phần tử, nhiều hơn 3.
```

### 3.9. Operator Precedence (Thứ tự ưu tiên)

Khi một biểu thức có nhiều toán tử, thứ tự thực hiện được quyết định bởi độ ưu tiên của toán tử. Toán tử có độ ưu tiên cao hơn sẽ được thực hiện trước.

**Thứ tự ưu tiên từ cao xuống thấp (một phần):**

1.  `()` (Dấu ngoặc đơn - Parentheses)
2.  `**` (Lũy thừa - Exponentiation)
3.  `+x`, `-x`, `~x` (Toán tử một ngôi - Unary plus, minus, bitwise NOT)
4.  `*`, `/`, `//`, `%` (Nhân, chia, lấy phần nguyên, lấy phần dư)
5.  `+`, `-` (Cộng, trừ)
6.  `<<`, `>>` (Dịch bit)
7.  `&` (Bitwise AND)
8.  `^` (Bitwise XOR)
9.  `|` (Bitwise OR)
10. `==`, `!=`, `>`, `>=`, `<`, `<=`, `is`, `is not`, `in`, `not in` (So sánh, identity, membership)
11. `not` (Logical NOT)
12. `and` (Logical AND)
13. `or` (Logical OR)
14. `:=` (Walrus - Assignment expression)

```python
# Ví dụ về thứ tự ưu tiên
ket_qua = 3 + 4 * 2 ** 2 / 2 - 1
# Thực hiện: 2 ** 2 = 4
#           4 * 4 = 16
#           16 / 2 = 8.0
#           3 + 8.0 = 11.0
#           11.0 - 1 = 10.0
print(f"3 + 4 * 2 ** 2 / 2 - 1 = {ket_qua}")

# Sử dụng ngoặc đơn để thay đổi thứ tự ưu tiên
ket_qua_khac = (3 + 4) * (2 ** (2 / 2)) - 1
# Thực hiện: 3+4=7, 2/2=1.0, 2**1.0=2.0
#           7 * 2.0 = 14.0
#           14.0 - 1 = 13.0
print(f"(3 + 4) * (2 ** (2 / 2)) - 1 = {ket_qua_khac}")
```

**OUTPUT:**
```
3 + 4 * 2 ** 2 / 2 - 1 = 10.0
(3 + 4) * (2 ** (2 / 2)) - 1 = 13.0
```

## 4. KIỂU DỮ LIỆU TẬP HỢP (COLLECTIONS)

Các kiểu dữ liệu dùng để lưu trữ nhiều giá trị trong một biến duy nhất.

### 4.0. So sánh các Collection Types (Bảng tổng hợp)

| Kiểu | Tên | Khả năng thay đổi | Cho phép trùng lặp | Có thứ tự | Cú pháp khởi tạo | Truy cập phần tử |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **List** | Danh sách | Có (Mutable) | Có | Có (theo chỉ số) | `[1, 2, 3]` hoặc `list()` | Bằng chỉ số: `my_list[0]` |
| **Tuple** | Bộ giá trị | Không (Immutable) | Có | Có (theo chỉ số) | `(1, 2, 3)` hoặc `tuple()` | Bằng chỉ số: `my_tuple[0]` |
| **Set** | Tập hợp | Có (Mutable) | Không | Không | `{1, 2, 3}` hoặc `set()` | Không truy cập bằng chỉ số, chỉ duyệt. |
| **Frozenset** | Tập hợp đóng băng | Không (Immutable) | Không | Không | `frozenset([1,2,3])` | Không truy cập bằng chỉ số. |
| **Dict** | Từ điển | Có (Mutable) | Khóa là duy nhất, giá trị có thể trùng. | Có thứ tự từ Python 3.7 (bảo toàn thứ tự chèn). | `{'a':1, 'b':2}` hoặc `dict()` | Bằng khóa: `my_dict['a']` |
| **String** | Chuỗi | Không (Immutable) | Có (ký tự) | Có (theo chỉ số) | `"hello"` hoặc `str()` | Bằng chỉ số: `my_str[0]` |
| **Range** | Dải số | Không (Immutable) | Không (tạo ra dải số) | Có (theo mẫu) | `range(start, stop, step)` | Bằng chỉ số: `my_range[0]` |

### 4.1. Strings (`str`)

Chuỗi là dãy các ký tự Unicode được đặt trong dấu nháy đơn (`'`), nháy kép (`"`) hoặc nháy ba (``'``'' hoặc `"""`).

#### 4.1.1. String Creation và Manipulation

```python
s1 = 'Đây là chuỗi nháy đơn.'
s2 = "Đây là chuỗi nháy kép."
s3 = """Đây là chuỗi
nhiều dòng
sử dụng nháy ba."""
s4 = str(123)  # Chuyển số thành chuỗi: "123"

print(s1)
print(s2)
print(s3)
print(s4)
```

**OUTPUT:**
```
Đây là chuỗi nháy đơn.
Đây là chuỗi nháy kép.
Đây là chuỗi
nhiều dòng
sử dụng nháy ba.
123
```

**Tính bất biến của chuỗi:** Bạn không thể thay đổi một ký tự trong chuỗi. Phải tạo một chuỗi mới.

```python
chuoi = "hello"
# chuoi[0] = 'H'  # Lỗi: 'str' object does not support item assignment
chuoi_moi = 'H' + chuoi[1:]  # Tạo chuỗi mới
print(chuoi_moi)
```

**OUTPUT:**
```
Hello
```

#### 4.1.2. String Slicing và Indexing

Các ký tự trong chuỗi có thể được truy cập bằng chỉ số (index). Chỉ số bắt đầu từ 0 (từ trái sang phải) hoặc từ -1 (từ phải sang trái).

| `H` | `e` | `l` | `l` | `o` | ` ` | `W` | `o` | `r` | `l` | `d` |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  |
| -11 | -10 | -9  | -8  | -7  | -6  | -5  | -4  | -3  | -2  | -1  |

**Cắt lát (Slicing):** `chuoi[start:stop:step]`
-   `start`: Vị trí bắt đầu (bao gồm). Mặc định là 0.
-   `stop`: Vị trí kết thúc (không bao gồm). Mặc định là độ dài chuỗi.
-   `step`: Bước nhảy. Mặc định là 1. Nếu âm, cắt từ phải sang trái.

```python
s = "Hello World"
print(f"Chuỗi gốc: '{s}'")
print(f"s[0]: '{s[0]}'")          # Ký tự đầu tiên
print(f"s[-1]: '{s[-1]}'")        # Ký tự cuối cùng
print(f"s[0:5]: '{s[0:5]}'")      # Từ 0 đến 4 (không bao gồm 5)
print(f"s[:5]: '{s[:5]}'")        # Tương tự trên
print(f"s[6:]: '{s[6:]}'")        # Từ 6 đến hết
print(f"s[::2]: '{s[::2]}'")      # Mọi ký tự thứ 2
print(f"s[::-1]: '{s[::-1]}'")    # Đảo ngược chuỗi
```

**OUTPUT:**
```
Chuỗi gốc: 'Hello World'
s[0]: 'H'
s[-1]: 'd'
s[0:5]: 'Hello'
s[:5]: 'Hello'
s[6:]: 'World'
s[::2]: 'HloWrd'
s[::-1]: 'dlroW olleH'
```

#### 4.1.3. String Methods (đầy đủ 47+ methods)

Python cung cấp rất nhiều phương thức tích hợp để thao tác với chuỗi. Dưới đây là các nhóm chính.

##### 4.1.3.1. Case Manipulation

```python
s = "hello World"
print(f"Chuỗi gốc: '{s}'")
print(f"upper(): '{s.upper()}'")       # Chữ hoa
print(f"lower(): '{s.lower()}'")       # Chữ thường
print(f"capitalize(): '{s.capitalize()}'") # Viết hoa chữ đầu câu
print(f"title(): '{s.title()}'")       # Viết hoa chữ đầu mỗi từ
print(f"swapcase(): '{s.swapcase()}'") # Đảo hoa/thường
```

**OUTPUT:**
```
Chuỗi gốc: 'hello World'
upper(): 'HELLO WORLD'
lower(): 'hello world'
capitalize(): 'Hello world'
title(): 'Hello World'
swapcase(): 'HELLO wORLD'
```

##### 4.1.3.2. Formatting (`casefold`, `zfill`, `expandtabs`)

```python
# casefold(): Tương tự lower() nhưng mạnh hơn, dùng cho so sánh không phân biệt hoa thường
print("Straße".casefold())  # 'strasse'

# zfill(width): Điền số 0 vào đầu cho đủ độ rộng
print("42".zfill(5))        # '00042'
print("-3.14".zfill(8))     # '-003.14'

# expandtabs(tabsize): Thay thế tab bằng khoảng trắng
print("a\tb".expandtabs(4)) # 'a   b'
```

**OUTPUT:**
```
strasse
00042
-003.14
a   b
```

##### 4.1.3.3. Validation & Testing (`isidentifier`, `isprintable`, `isascii` (Python 3.7+))

```python
# isidentifier(): Kiểm tra xem chuỗi có phải là định danh hợp lệ (tên biến) không
print("var_name".isidentifier())  # True
print("2var".isidentifier())      # False

# isprintable(): Kiểm tra xem tất cả ký tự có thể in được không
print("Hello\n".isprintable())    # False (vì có \n)
print("Hello".isprintable())      # True

# isascii(): Kiểm tra xem tất cả ký tự có nằm trong bảng ASCII không
print("Hello".isascii())          # True
print("Xin chào".isascii())       # False (có dấu)
```

**OUTPUT:**
```
True
False
False
True
True
False
```

##### 4.1.3.4. Encoding & Bytes (`encode`, `translate`, `maketrans`)

```python
# encode(): Mã hóa chuỗi thành bytes
chuoi_unicode = "café"
bytes_utf8 = chuoi_unicode.encode('utf-8')
print(f"'{chuoi_unicode}' encode UTF-8: {bytes_utf8}")

# translate() và maketrans(): Dịch/Thay thế ký tự
# Tạo bảng dịch: thay 'a'->'@', 'e'->'3'
bang_dich = str.maketrans('ae', '@3')
s = "apple and egg"
print(s.translate(bang_dich))  # '@ppl3 @nd 3gg'
```

**OUTPUT:**
```
'café' encode UTF-8: b'caf\xc3\xa9'
@ppl3 @nd 3gg
```

##### 4.1.3.5. Partitioning (`partition`, `rpartition`)

```python
# partition(sep): Tách chuỗi thành 3 phần: (trước sep, sep, sau sep)
# Chỉ tách lần đầu tiên tìm thấy.
s = "python.is.fun"
print(s.partition('.'))  # ('python', '.', 'is.fun')

# rpartition(sep): Tách từ bên phải.
print(s.rpartition('.')) # ('python.is', '.', 'fun')

# Nếu không tìm thấy sep, trả về (chuỗi_gốc, '', '')
print(s.partition(','))  # ('python.is.fun', '', '')
```

**OUTPUT:**
```
('python', '.', 'is.fun')
('python.is', '.', 'fun')
('python.is.fun', '', '')
```

##### 4.1.3.6. Justification (`center`, `ljust`, `rjust`)

```python
s = "Hi"
print(f"'{s.center(10)}'")   # Căn giữa trong độ rộng 10
print(f"'{s.ljust(10)}'")    # Căn trái
print(f"'{s.rjust(10)}'")    # Căn phải
print(f"'{s.center(10, '*')}'") # Dùng '*' thay vì khoảng trắng
```

**OUTPUT:**
```
'    Hi    '
'Hi        '
'        Hi'
'****Hi****'
```

##### 4.1.3.7. Strip Variations (`removeprefix`, `removesuffix` (Python 3.9+))

```python
s = "HelloWorld"
print(s.removeprefix("Hello"))  # 'World'
print(s.removesuffix("World"))  # 'Hello'

# strip(), lstrip(), rstrip(): Loại bỏ ký tự whitespace (hoặc ký tự chỉ định) ở đầu/cuối
s2 = "  hello  \n"
print(f"'{s2.strip()}'")   # 'hello'
print(f"'{s2.lstrip()}'")  # 'hello  \n'
print(f"'{s2.rstrip()}'")  # '  hello'
s3 = "xxxhelloxxx"
print(s3.strip('x'))       # 'hello'
```

**OUTPUT:**
```
World
Hello
'hello'
'hello  \n'
'  hello'
hello
```

#### 4.1.4. String Formatting

Định dạng chuỗi giúp nhúng giá trị của biến vào trong chuỗi một cách dễ đọc.

##### 4.1.4.1. %-formatting (Cũ)

```python
ten = "An"
tuoi = 25
print("Tên: %s, Tuổi: %d" % (ten, tuoi))
print("Giá trị: %.2f" % 3.14159)  # Làm tròn 2 chữ số thập phân
```

**OUTPUT:**
```
Tên: An, Tuổi: 25
Giá trị: 3.14
```

##### 4.1.4.2. `str.format()`

```python
ten = "Bình"
tuoi = 30
print("Tên: {}, Tuổi: {}".format(ten, tuoi))
print("Tên: {1}, Tuổi: {0}".format(tuoi, ten)) # Chỉ số vị trí
print("Tên: {name}, Tuổi: {age}".format(name=ten, age=tuoi)) # Từ khóa
```

**OUTPUT:**
```
Tên: Bình, Tuổi: 30
Tên: Bình, Tuổi: 30
Tên: Bình, Tuổi: 30
```

##### 4.1.4.3. f-strings (Python 3.6+) (bao gồm debug formatting `x=`)

f-string là cách hiện đại và được khuyến nghị.

```python
ten = "Châu"
tuoi = 22
print(f"Tên: {ten}, Tuổi: {tuoi}")

# Có thể chứa biểu thức
print(f"Tuổi năm sau: {tuoi + 1}")

# Định dạng số
pi = 3.14159265
print(f"Pi: {pi:.2f}")          # Làm tròn 2 chữ số
print(f"Số lớn: {1000000:,}")   # Ngăn cách hàng nghìn

# Debug formatting (Python 3.8+): In cả tên biến và giá trị
diem = 9.5
print(f"{diem=}")  # Sẽ in ra 'diem=9.5'
```

**OUTPUT:**
```
Tên: Châu, Tuổi: 22
Tuổi năm sau: 23
Pi: 3.14
Số lớn: 1,000,000
diem=9.5
```

##### 4.1.4.4. Template Strings

An toàn hơn cho đầu vào từ người dùng, ít tính năng hơn.

```python
from string import Template
t = Template('Tên: $name, Tuổi: $age')
print(t.substitute(name="Dũng", age=28))
```

**OUTPUT:**
```
Tên: Dũng, Tuổi: 28
```

##### 4.1.4.5. Format Specification Mini-Language chi tiết

Cú pháp: `{value:format_spec}`

| Loại | Ví dụ | Kết quả | Mô tả |
| :--- | :--- | :--- | :--- |
| **Căn lề** | `f'{"hi":<10}'` | `'hi        '` | Căn trái |
| | `f'{"hi":>10}'` | `'        hi'` | Căn phải |
| | `f'{"hi":^10}'` | `'    hi    '` | Căn giữa |
| **Số** | `f'{1000000:,}'` | `'1,000,000'` | Dấu phân cách hàng nghìn |
| | `f'{3.14159:.2f}'` | `'3.14'` | 2 chữ số thập phân |
| | `f'{0.25:.1%}'` | `'25.0%'` | Định dạng phần trăm |
| | `f'{255:o}'` | `'377'` | Hệ bát phân |
| | `f'{255:x}'` | `'ff'` | Hệ thập lục phân (chữ thường) |
| | `f'{255:X}'` | `'FF'` | Hệ thập lục phân (chữ hoa) |
| | `f'{42:b}'` | `'101010'` | Hệ nhị phân |

```python
# Ví dụ tổng hợp
number = 12345.6789
print(f"Căn phải, 15 ký tự: {number:>15.2f}")
print(f"Căn trái, dấu phân cách: {number:<15,.2f}")
print(f"Phần trăm: {0.12345:.2%}")
```

**OUTPUT:**
```
Căn phải, 15 ký tự:       12345.68
Căn trái, dấu phân cách: 12,345.68
Phần trăm: 12.35%
```

#### 4.1.5. Escape Sequences

Dãy escape bắt đầu bằng dấu `\` để biểu diễn các ký tự đặc biệt trong chuỗi.

| Escape Sequence | Ý nghĩa | Ví dụ | Kết quả |
| :--- | :--- | :--- | :--- |
| `\'` | Dấu nháy đơn | `'It\'s me'` | `It's me` |
| `\"` | Dấu nháy kép | `"He said \"Hi\""` | `He said "Hi"` |
| `\\` | Dấu gạch chéo ngược | `"C:\\Users"` | `C:\Users` |
| `\n` | Xuống dòng mới | `"Line1\nLine2"` | `Line1` rồi xuống dòng `Line2` |
| `\t` | Tab ngang | `"a\tb"` | `a    b` |
| `\r` | Carriage Return | `"Hello\rWorld"` | `World` (con trỏ về đầu dòng) |
| `\b` | Backspace | `"Hel\blo"` | `Helo` |
| `\f` | Form Feed | `"Page1\fPage2"` | (Ít dùng) |
| `\ooo` | Ký tự với giá trị octal | `"\110\145\154\154\157"` | `Hello` |
| `\xhh` | Ký tự với giá trị hex | `"\x48\x65\x6c\x6c\x6f"` | `Hello` |

Chuỗi thô (raw string) bỏ qua hầu hết các escape sequence: `r"chuỗi\n"` sẽ giữ nguyên `\n`.

```python
print("Đây là dòng 1.\nĐây là dòng 2.")
print("Đường dẫn: C:\\Users\\Admin")
print(r"Đường dẫn thô: C:\Users\Admin") # Raw string
print("Dấu nháy: \"Xin chào\"")
```

**OUTPUT:**
```
Đây là dòng 1.
Đây là dòng 2.
Đường dẫn: C:\Users\Admin
Đường dẫn thô: C:\Users\Admin
Dấu nháy: "Xin chào"
```

#### 4.1.6. String Constants (`string` module: `ascii_letters`, `digits`, `punctuation`, v.v.)

Mô-đun `string` cung cấp các hằng số chuỗi hữu ích.

```python
import string

print(f"Chữ cái ASCII: {string.ascii_letters}")
print(f"Chữ thường: {string.ascii_lowercase}")
print(f"Chữ hoa: {string.ascii_uppercase}")
print(f"Chữ số: {string.digits}")
print(f"Chữ số hex: {string.hexdigits}")
print(f"Chữ số octal: {string.octdigits}")
print(f"Dấu câu: {string.punctuation}")
print(f"Ký tự khoảng trắng: {repr(string.whitespace)}") # repr để hiển thị \t, \n
print(f"Có thể in được: {string.printable}")
```

**OUTPUT:**
```
Chữ cái ASCII: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
Chữ thường: abcdefghijklmnopqrstuvwxyz
Chữ hoa: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Chữ số: 0123456789
Chữ số hex: 0123456789abcdefABCDEF
Chữ số octal: 01234567
Dấu câu: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
Ký tự khoảng trắng: ' \t\n\r\x0b\x0c'
Có thể in được: 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ \t\n\r\x0b\x0c
```

### 4.2. Lists (`list`)

List là một tập hợp có thứ tự, có thể thay đổi (mutable) và cho phép các phần tử trùng lặp.

#### 4.2.1. List Creation và Access

```python
# Tạo list bằng dấu ngoặc vuông
list1 = [1, 2, 3, 4, 5]
list2 = ["apple", "banana", "cherry"]
list3 = [True, False, False]
list4 = [1, "hello", 3.14, True]  # Có thể chứa nhiều kiểu dữ liệu
list5 = []  # List rỗng
list6 = list() # Sử dụng constructor
list7 = list("abc") # Từ một iterable: ['a', 'b', 'c']

print(list1)
print(list4)
print(list7)
```

**OUTPUT:**
```
[1, 2, 3, 4, 5]
[1, 'hello', 3.14, True]
['a', 'b', 'c']
```

Truy cập phần tử bằng chỉ số (tương tự chuỗi).

```python
my_list = ["a", "b", "c", "d", "e"]
print(my_list[0])   # 'a'
print(my_list[-1])  # 'e'
print(my_list[1:4]) # ['b', 'c', 'd']
```

**OUTPUT:**
```
a
e
['b', 'c', 'd']
```

#### 4.2.2. List Slicing

Cắt lát hoạt động tương tự như với chuỗi, tạo ra một list mới.

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:6])    # [2, 3, 4, 5]
print(numbers[:5])     # [0, 1, 2, 3, 4]
print(numbers[5:])     # [5, 6, 7, 8, 9]
print(numbers[::2])    # [0, 2, 4, 6, 8] (cách 2)
print(numbers[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (đảo ngược)
```

**OUTPUT:**
```
[2, 3, 4, 5]
[0, 1, 2, 3, 4]
[5, 6, 7, 8, 9]
[0, 2, 4, 6, 8]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

#### 4.2.3. List Methods (đầy đủ 11 methods + Magic methods)

Danh sách các phương thức thông dụng của list.

| Phương thức | Mô tả | Ví dụ (trước -> sau) |
| :--- | :--- | :--- |
| `append(x)` | Thêm phần tử `x` vào cuối list. | `[1,2].append(3)` -> `[1,2,3]` |
| `extend(iterable)` | Nối thêm các phần tử từ iterable vào cuối list. | `[1,2].extend([3,4])` -> `[1,2,3,4]` |
| `insert(i, x)` | Chèn phần tử `x` vào vị trí `i`. | `[1,3].insert(1,2)` -> `[1,2,3]` |
| `remove(x)` | Xóa phần tử **đầu tiên** có giá trị `x`. Lỗi nếu không tìm thấy. | `[1,2,3,2].remove(2)` -> `[1,3,2]` |
| `pop([i])` | Xóa và trả về phần tử tại vị trí `i`. Nếu không chỉ định, xóa phần tử cuối. | `[1,2,3].pop()` -> `3`, list còn `[1,2]` |
| `clear()` | Xóa tất cả phần tử. | `[1,2,3].clear()` -> `[]` |
| `index(x[, start[, end]])` | Trả về chỉ số của phần tử **đầu tiên** có giá trị `x`. | `[10,20,30,20].index(20)` -> `1` |
| `count(x)` | Đếm số lần xuất hiện của giá trị `x`. | `[1,2,1,3,1].count(1)` -> `3` |
| `sort(key=None, reverse=False)` | Sắp xếp list **tại chỗ** (in-place). | `[3,1,2].sort()` -> `[1,2,3]` |
| `reverse()` | Đảo ngược thứ tự các phần tử **tại chỗ**. | `[1,2,3].reverse()` -> `[3,2,1]` |
| `copy()` | Trả về một bản sao nông (shallow copy) của list. | `a=[1,2]; b=a.copy(); b[0]=9` -> `a` vẫn `[1,2]` |

```python
# Ví dụ minh họa một số phương thức
fruits = ["apple", "banana", "cherry", "banana"]

fruits.append("orange")
print(f"Sau append('orange'): {fruits}")

fruits.insert(1, "grape")
print(f"Sau insert(1, 'grape'): {fruits}")

fruits.remove("banana")  # Xóa lần xuất hiện đầu tiên
print(f"Sau remove('banana'): {fruits}")

popped = fruits.pop(2)   # Xóa phần tử tại index 2 ('cherry')
print(f"Phần tử bị pop: {popped}")
print(f"List sau pop(2): {fruits}")

print(f"Index của 'grape': {fruits.index('grape')}")
print(f"Số lần 'banana' xuất hiện: {fruits.count('banana')}")

numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(f"List số sau sort: {numbers}")
numbers.reverse()
print(f"List số sau reverse: {numbers}")
```

**OUTPUT:**
```
Sau append('orange'): ['apple', 'banana', 'cherry', 'banana', 'orange']
Sau insert(1, 'grape'): ['apple', 'grape', 'banana', 'cherry', 'banana', 'orange']
Sau remove('banana'): ['apple', 'grape', 'cherry', 'banana', 'orange']
Phần tử bị pop: cherry
List sau pop(2): ['apple', 'grape', 'banana', 'orange']
Index của 'grape': 1
Số lần 'banana' xuất hiện: 1
List số sau sort: [1, 1, 2, 3, 4, 5, 9]
List số sau reverse: [9, 5, 4, 3, 2, 1, 1]
```

**Magic Methods (Dunder Methods):** Các phương thức đặc biệt bắt đầu và kết thúc bằng `__`. Chúng được gọi ngầm định bởi Python. Ví dụ:
- `__add__`: Được gọi bởi toán tử `+` (`list1 + list2`).
- `__iadd__`: Được gọi bởi toán tử `+=` (`list1 += list2`).
- `__mul__`, `__imul__`: Được gọi bởi `*` và `*=` (`list1 * 3`).
- `__contains__`: Được gọi bởi toán tử `in`.
- `__len__`: Được gọi bởi hàm `len()`.
- `__getitem__`, `__setitem__`, `__delitem__`: Được gọi khi truy cập, gán, xóa phần tử bằng chỉ số (`list[i]`, `list[i]=x`, `del list[i]`).
- `__iter__`: Được gọi bởi vòng lặp `for` để lấy iterator.
- `__reversed__`: Được gọi bởi hàm `reversed()`.

#### 4.2.4. List Comprehensions (bao gồm nested và transposed list)

List comprehension cung cấp cú pháp ngắn gọn để tạo list dựa trên các iterable khác.

**Cú pháp cơ bản:** `[expression for item in iterable]`
**Cú pháp có điều kiện:** `[expression for item in iterable if condition]`

```python
# Tạo list bình phương các số từ 0 đến 9
squares = [x**2 for x in range(10)]
print(f"Bình phương: {squares}")

# Chỉ lấy bình phương của số chẵn
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Bình phương số chẵn: {even_squares}")

# Tạo list các chuỗi viết hoa
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"Chữ hoa: {upper_words}")
```

**OUTPUT:**
```
Bình phương: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
Bình phương số chẵn: [0, 4, 16, 36, 64]
Chữ hoa: ['HELLO', 'WORLD', 'PYTHON']
```

**Nested List Comprehension:** Tạo list đa chiều.

```python
# Tạo ma trận 3x3
matrix = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]
print(f"Ma trận 3x3: {matrix}")
# Tương đương với:
# matrix = []
# for i in range(3):
#     row = []
#     for j in range(3):
#         row.append(i * 3 + j + 1)
#     matrix.append(row)

# Làm phẳng (flatten) một ma trận 2D
flat = [num for row in matrix for num in row]
print(f"Ma trận phẳng: {flat}")
```

**OUTPUT:**
```
Ma trận 3x3: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Ma trận phẳng: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Transposed List (Chuyển vị):** Đổi hàng thành cột.

```python
# Giả sử có ma trận 2x3
matrix = [[1, 2, 3], [4, 5, 6]]
# Dùng zip(*matrix) để chuyển vị
transposed = [list(row) for row in zip(*matrix)]
print(f"Ma trận gốc: {matrix}")
print(f"Ma trận chuyển vị: {transposed}")
```

**OUTPUT:**
```
Ma trận gốc: [[1, 2, 3], [4, 5, 6]]
Ma trận chuyển vị: [[1, 4], [2, 5], [3, 6]]
```

#### 4.2.5. Nested Lists

List có thể chứa các list khác, tạo thành cấu trúc đa chiều.

```python
# List 2D (như ma trận)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Phần tử hàng 1 cột 2: {matrix[0][1]}")  # Truy cập phần tử

# Duyệt qua nested list
for row in matrix:
    for item in row:
        print(item, end=' ')
    print()  # Xuống dòng sau mỗi hàng
```

**OUTPUT:**
```
Phần tử hàng 1 cột 2: 2
1 2 3
4 5 6
7 8 9
```

#### 4.2.6. List như Stack/Queue (sử dụng `append()`/`pop()` và đề cập `collections.deque`)

-   **Stack (Ngăn xếp - LIFO):** Sử dụng `append()` để đẩy (push) và `pop()` để lấy ra (pop).
    ```python
    stack = []
    stack.append(1)  # Push 1
    stack.append(2)  # Push 2
    stack.append(3)  # Push 3
    print(stack)
    print(stack.pop())  # Pop -> 3
    print(stack.pop())  # Pop -> 2
    print(stack)
    ```
    **OUTPUT:**
    ```
    [1, 2, 3]
    3
    2
    [1]
    ```

-   **Queue (Hàng đợi - FIFO):** List không hiệu quả cho queue vì `pop(0)` có độ phức tạp O(n). Nên sử dụng `collections.deque`.
    ```python
    from collections import deque
    queue = deque()
    queue.append(1)  # Enqueue 1
    queue.append(2)  # Enqueue 2
    queue.append(3)  # Enqueue 3
    print(queue)
    print(queue.popleft())  # Dequeue -> 1
    print(queue.popleft())  # Dequeue -> 2
    print(queue)
    ```
    **OUTPUT:**
    ```
    deque([1, 2, 3])
    1
    2
    deque([3])
    ```

### 4.3. Tuples (`tuple`)

Tuple là một tập hợp có thứ tự, **không thể thay đổi (immutable)** và cho phép các phần tử trùng lặp. Thường được dùng cho các nhóm dữ liệu liên quan, không thay đổi.

#### 4.3.1. Tuple Creation và Immutability

```python
# Tạo tuple bằng dấu ngoặc tròn
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ("apple", "banana", "cherry")
tuple3 = (True, False, False)
tuple4 = (1, "hello", 3.14, True)  # Nhiều kiểu
tuple5 = ()  # Tuple rỗng
tuple6 = tuple() # Constructor
tuple7 = tuple([1,2,3]) # Từ list: (1, 2, 3)

# Tuple một phần tử: cần dấu phẩy
not_a_tuple = (5)    # Đây là int 5
a_tuple = (5,)       # Đây là tuple (5,)
print(type(not_a_tuple), type(a_tuple))

print(tuple1)
print(tuple4)
```

**OUTPUT:**
```
<class 'int'> <class 'tuple'>
(1, 2, 3, 4, 5)
(1, 'hello', 3.14, True)
```

**Tính bất biến:** Không thể thay đổi, thêm, xóa phần tử sau khi tạo (trừ khi phần tử đó là mutable như list).

```python
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # Lỗi: 'tuple' object does not support item assignment
# Tuy nhiên, nếu tuple chứa list, list bên trong vẫn có thể thay đổi.
mixed_tuple = (1, [2, 3], 4)
mixed_tuple[1].append(5)  # Được phép vì phần tử index 1 là list
print(mixed_tuple)  # (1, [2, 3, 5], 4)
```

**OUTPUT:**
```
(1, [2, 3, 5], 4)
```

#### 4.3.2. Tuple Methods (`count`, `index`)

Chỉ có hai phương thức do tính bất biến.

```python
my_tuple = (1, 2, 3, 2, 4, 2, 5)
print(f"Số lần 2 xuất hiện: {my_tuple.count(2)}")
print(f"Chỉ số đầu tiên của 2: {my_tuple.index(2)}")
print(f"Chỉ số của 2 bắt đầu từ vị trí 2: {my_tuple.index(2, 2)}")
```

**OUTPUT:**
```
Số lần 2 xuất hiện: 3
Chỉ số đầu tiên của 2: 1
Chỉ số của 2 bắt đầu từ vị trí 2: 3
```

#### 4.3.3. Tuple Unpacking (bao gồm Extended unpacking và Nested unpacking)

Gán các phần tử của tuple cho các biến riêng biệt.

```python
# Unpacking cơ bản
point = (10, 20)
x, y = point
print(f"x={x}, y={y}")

# Extended unpacking (Python 3): Dùng * để gom nhiều phần tử
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"first={first}, middle={middle}, last={last}")

# Nested unpacking
data = ("Alice", 30, ("Math", "Physics"))
name, age, (subject1, subject2) = data
print(f"{name} học {subject1} và {subject2}")
```

**OUTPUT:**
```
x=10, y=20
first=1, middle=[2, 3, 4], last=5
Alice học Math và Physics
```

#### 4.3.4. Named Tuples (từ `collections`)

`namedtuple` tạo ra một lớp tuple với các trường được đặt tên, giúp code dễ đọc hơn.

```python
from collections import namedtuple

# Định nghĩa một namedtuple 'Point' với các trường x, y
Point = namedtuple('Point', ['x', 'y'])

# Tạo thể hiện
p = Point(10, 20)
print(p)        # Point(x=10, y=20)
print(p.x, p.y) # Truy cập bằng tên trường
print(p[0], p[1]) # Vẫn truy cập được bằng chỉ số

# Unpacking vẫn hoạt động
x, y = p
print(x, y)
```

**OUTPUT:**
```
Point(x=10, y=20)
10 20
10 20
10 20
```

#### 4.3.5. So sánh List vs Tuple

| Đặc điểm | List | Tuple |
| :--- | :--- | :--- |
| **Khả năng thay đổi** | **Mutable** - Có thể thay đổi nội dung. | **Immutable** - Không thể thay đổi sau khi tạo. |
| **Hiệu suất** | Chậm hơn một chút do chi phí thay đổi kích thước. | **Nhanh hơn** do cố định kích thước và đơn giản. |
| **Bộ nhớ** | Tốn nhiều bộ nhớ hơn do cơ chế dự phòng. | Tiết kiệm bộ nhớ hơn. |
| **Phương thức** | Nhiều phương thức để sửa đổi. | Chỉ có `count()` và `index()`. |
| **Trường hợp sử dụng** | Dùng cho tập hợp dữ liệu **có thể thay đổi**. | Dùng cho tập hợp dữ liệu **cố định**, **khóa từ điển**, **trả về nhiều giá trị từ hàm**. |
| **Cú pháp** | Dùng `[]`. | Dùng `()`. |

### 4.4. Dictionaries (`dict`)

Từ điển là một tập hợp không có thứ tự (trước Python 3.7) hoặc có thứ tự (từ Python 3.7, bảo toàn thứ tự chèn), có thể thay đổi, và lưu trữ các cặp **khóa-giá trị (key-value)**. Khóa phải là kiểu dữ liệu bất biến (như `str`, `int`, `float`, `tuple`), và phải là duy nhất trong một từ điển.

#### 4.4.1. Dictionary Creation

```python
# Tạo bằng dấu ngoặc nhọn {}
dict1 = {"name": "Alice", "age": 25, "city": "Hà Nội"}
dict2 = {}  # Từ điển rỗng
dict3 = dict() # Constructor
dict4 = dict(name="Bob", age=30) # Dùng từ khóa (khóa phải là chuỗi hợp lệ)
dict5 = dict([("a", 1), ("b", 2)]) # Từ list của tuple

print(dict1)
print(dict4)
```

**OUTPUT:**
```
{'name': 'Alice', 'age': 25, 'city': 'Hà Nội'}
{'name': 'Bob', 'age': 30}
```

#### 4.4.2. Dictionary Access và Modification

```python
my_dict = {"brand": "Toyota", "model": "Camry", "year": 2020}

# Truy cập giá trị bằng khóa
print(my_dict["brand"])  # Toyota
# print(my_dict["color"]) # Lỗi KeyError nếu khóa không tồn tại

# Sử dụng get() để tránh lỗi
print(my_dict.get("model"))    # Camry
print(my_dict.get("color"))    # None (không lỗi)
print(my_dict.get("color", "Không tìm thấy")) # Giá trị mặc định

# Thêm hoặc sửa phần tử
my_dict["year"] = 2022  # Sửa giá trị
my_dict["color"] = "red" # Thêm cặp mới
print(my_dict)

# Xóa phần tử
del my_dict["model"]
print("Sau khi xóa 'model':", my_dict)

# Kiểm tra khóa tồn tại
if "brand" in my_dict:
    print("Khóa 'brand' tồn tại")
```

**OUTPUT:**
```
Toyota
Camry
None
Không tìm thấy
{'brand': 'Toyota', 'model': 'Camry', 'year': 2022, 'color': 'red'}
Sau khi xóa 'model': {'brand': 'Toyota', 'year': 2022, 'color': 'red'}
Khóa 'brand' tồn tại
```

#### 4.4.3. Dictionary Methods (đầy đủ 11+ methods: `fromkeys`, `setdefault`, `popitem`)

| Phương thức | Mô tả |
| :--- | :--- |
| `clear()` | Xóa tất cả phần tử. |
| `copy()` | Trả về một bản sao nông. |
| `fromkeys(seq[, value])` | Tạo dict mới với khóa từ seq, giá trị mặc định là value. |
| `get(key[, default])` | Trả về giá trị của key, nếu không có trả về default. |
| `items()` | Trả về view của các cặp (key, value). |
| `keys()` | Trả về view của các khóa. |
| `values()` | Trả về view của các giá trị. |
| `pop(key[, default])` | Xóa khóa key và trả về giá trị. Nếu key không có, trả về default (nếu chỉ định) hoặc lỗi. |
| `popitem()` | Xóa và trả về cặp (key, value) **cuối cùng** được chèn (theo thứ tự LIFO). |
| `setdefault(key[, default])` | Nếu key có, trả về giá trị. Nếu không, chèn key với giá trị default và trả về default. |
| `update([other])` | Cập nhật dict với các cặp key/value từ other (có thể là dict hoặc iterable của cặp). |

```python
# Ví dụ một số phương thức
d = {"a": 1, "b": 2, "c": 3}

print("Keys:", list(d.keys()))
print("Values:", list(d.values()))
print("Items:", list(d.items()))

# setdefault: Nếu khóa chưa có, thêm vào với giá trị mặc định
value = d.setdefault("d", 4)
print(f"Sau setdefault('d', 4): {d}, giá trị trả về: {value}")
value2 = d.setdefault("a", 99) # 'a' đã có, không thay đổi
print(f"setdefault('a', 99) trả về: {value2}, dict: {d}")

# popitem: Xóa và trả về cặp cuối cùng
last_item = d.popitem()
print(f"popitem() trả về: {last_item}")
print(f"Dict sau popitem: {d}")

# fromkeys: Tạo dict mới
keys = ['x', 'y', 'z']
new_dict = dict.fromkeys(keys, 0)
print(f"fromkeys với giá trị mặc định 0: {new_dict}")
```

**OUTPUT:**
```
Keys: ['a', 'b', 'c']
Values: [1, 2, 3]
Items: [('a', 1), ('b', 2), ('c', 3)]
Sau setdefault('d', 4): {'a': 1, 'b': 2, 'c': 3, 'd': 4}, giá trị trả về: 4
setdefault('a', 99) trả về: 1, dict: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
popitem() trả về: ('d', 4)
Dict sau popitem: {'a': 1, 'b': 2, 'c': 3}
fromkeys với giá trị mặc định 0: {'x': 0, 'y': 0, 'z': 0}
```

#### 4.4.4. Dictionary Comprehensions (với conditions và inverted dict)

Tương tự list comprehension, nhưng tạo dictionary.

```python
# Tạo dict bình phương các số từ 0 đến 4
squares = {x: x**2 for x in range(5)}
print(f"Bình phương: {squares}")

# Chỉ lấy số chẵn
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Bình phương số chẵn: {even_squares}")

# Đảo ngược dict (khóa thành giá trị, giá trị thành khóa)
# Lưu ý: Chỉ hoạt động nếu tất cả giá trị đều có thể làm khóa (bất biến và duy nhất).
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(f"Dict gốc: {original}")
print(f"Dict đảo ngược: {inverted}")
```

**OUTPUT:**
```
Bình phương: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
Bình phương số chẵn: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
Dict gốc: {'a': 1, 'b': 2, 'c': 3}
Dict đảo ngược: {1: 'a', 2: 'b', 3: 'c'}
```

#### 4.4.5. Dictionary Views (`keys()`, `values()`, `items()`) (chi tiết về View objects)

Các phương thức `keys()`, `values()`, `items()` trả về các **view objects**. Chúng là cửa sổ động (dynamic) vào nội dung của từ điển: mọi thay đổi đối với từ điển sẽ phản ánh ngay lập tức lên view.

-   `dict_keys`: View của các khóa.
-   `dict_values`: View của các giá trị.
-   `dict_items`: View của các cặp (khóa, giá trị).

```python
d = {"a": 1, "b": 2, "c": 3}
keys_view = d.keys()
values_view = d.values()
items_view = d.items()

print(f"Keys view: {keys_view}")
print(f"Values view: {values_view}")
print(f"Items view: {items_view}")

# Thay đổi dict
d["d"] = 4
print(f"Sau khi thêm 'd':")
print(f"Keys view: {keys_view}")  # Tự động cập nhật
print(f"Values view: {values_view}")
print(f"Items view: {items_view}")

# View có thể chuyển đổi thành list, tuple, set
print(list(keys_view))
# Nhưng view KHÔNG hỗ trợ index trực tiếp: keys_view[0] sẽ lỗi.
```

**OUTPUT:**
```
Keys view: dict_keys(['a', 'b', 'c'])
Values view: dict_values([1, 2, 3])
Items view: dict_items([('a', 1), ('b', 2), ('c', 3)])
Sau khi thêm 'd':
Keys view: dict_keys(['a', 'b', 'c', 'd'])
Values view: dict_values([1, 2, 3, 4])
Items view: dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
['a', 'b', 'c', 'd']
```

#### 4.4.6. Dictionary Merging (`|`, `|=`) (Python 3.9+)

Python 3.9 giới thiệu toán tử `|` để hợp nhất (merge) hai từ điển. Toán tử `|=` thực hiện hợp nhất tại chỗ (in-place update).

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}  # Khóa 'b' trùng

# Hợp nhất, giá trị từ d2 ưu tiên khi trùng khóa
merged = d1 | d2
print(f"d1 | d2 = {merged}")  # {'a': 1, 'b': 3, 'c': 4}

# Hợp nhất tại chỗ
d1 |= d2  # Tương đương d1.update(d2)
print(f"Sau d1 |= d2, d1 = {d1}")
```

**OUTPUT:**
```
d1 | d2 = {'a': 1, 'b': 3, 'c': 4}
Sau d1 |= d2, d1 = {'a': 1, 'b': 3, 'c': 4}
```

### 4.5. Sets (`set`, `frozenset`)

Set là một tập hợp **không có thứ tự**, **có thể thay đổi (mutable)**, và **không chứa phần tử trùng lặp**. Các phần tử phải là bất biến (hashable). Thường dùng để kiểm tra thành viên, loại bỏ trùng lặp và thực hiện các phép toán tập hợp.

`frozenset` là phiên bản bất biến của set.

#### 4.5.1. Set Creation và Properties

```python
# Tạo set bằng dấu ngoặc nhọn {} (nhưng không phải cặp khóa-giá trị)
set1 = {1, 2, 3, 4, 5}
set2 = {"apple", "banana", "cherry"}
set3 = {True, False}
set4 = set()  # Set rỗng (dùng set(), vì {} tạo dict rỗng)
set5 = set([1, 2, 2, 3, 3])  # Từ list, tự loại bỏ trùng: {1, 2, 3}
set6 = {1, "hello", 3.14}    # Có thể chứa nhiều kiểu (miễn hashable)

print(set1)
print(set5)

# Phần tử trùng lặp bị loại bỏ
my_set = {1, 2, 2, 3, 3, 3}
print(my_set)  # {1, 2, 3}

# Set không hỗ trợ indexing (vì không có thứ tự)
# print(set1[0]) # Lỗi: 'set' object is not subscriptable
```

**OUTPUT:**
```
{1, 2, 3, 4, 5}
{1, 2, 3}
{1, 2, 3}
```

#### 4.5.2. Set Operations (`union`, `intersection`, `difference`, `symmetric_difference`) (với operators và methods)

| Phép toán | Toán tử | Phương thức | Mô tả | Ví dụ (A={1,2,3}, B={3,4,5}) |
| :--- | :--- | :--- | :--- | :--- |
| **Hợp (Union)** | `|` | `union(*others)` | Tập hợp tất cả phần tử thuộc A hoặc B. | `A | B` -> `{1,2,3,4,5}` |
| **Giao (Intersection)** | `&` | `intersection(*others)` | Tập hợp các phần tử thuộc cả A và B. | `A & B` -> `{3}` |
| **Hiệu (Difference)** | `-` | `difference(*others)` | Tập hợp các phần tử thuộc A nhưng không thuộc B. | `A - B` -> `{1,2}` |
| **Hiệu đối xứng (Symmetric Difference)** | `^` | `symmetric_difference(other)` | Tập hợp các phần tử thuộc A hoặc B nhưng không thuộc cả hai. | `A ^ B` -> `{1,2,4,5}` |

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(f"A = {A}")
print(f"B = {B}")
print(f"Hợp (A | B): {A | B}")
print(f"Giao (A & B): {A & B}")
print(f"Hiệu (A - B): {A - B}")
print(f"Hiệu đối xứng (A ^ B): {A ^ B}")

# Sử dụng phương thức
print(f"A.union(B): {A.union(B)}")
print(f"A.intersection(B): {A.intersection(B)}")
```

**OUTPUT:**
```
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
Hợp (A | B): {1, 2, 3, 4, 5, 6}
Giao (A & B): {3, 4}
Hiệu (A - B): {1, 2}
Hiệu đối xứng (A ^ B): {1, 2, 5, 6}
A.union(B): {1, 2, 3, 4, 5, 6}
A.intersection(B): {3, 4}
```

#### 4.5.3. Set Methods (đầy đủ: `update`, `intersection_update`, `isdisjoint`, `issubset`, `issuperset`, v.v.)

Ngoài các phương thức tương ứng với toán tử (trả về set mới), set còn có các phương thức cập nhật tại chỗ (in-place) và kiểm tra.

| Phương thức | Mô tả | Ví dụ (A={1,2}, B={2,3}) |
| :--- | :--- | :--- |
| **Cập nhật tại chỗ** | | |
| `update(*others)` | Cập nhật set, thêm phần tử từ others. | `A.update(B)` -> `A={1,2,3}` |
| `intersection_update(*others)` | Cập nhật set, chỉ giữ phần tử có trong tất cả others. | `A.intersection_update(B)` -> `A={2}` |
| `difference_update(*others)` | Cập nhật set, loại bỏ phần tử có trong others. | `A.difference_update(B)` -> `A={1}` |
| `symmetric_difference_update(other)` | Cập nhật set, chỉ giữ phần tử có trong đúng một trong hai set. | `A.symmetric_difference_update(B)` -> `A={1,3}` |
| **Thêm/Xóa** | | |
| `add(elem)` | Thêm phần tử `elem` vào set. | `A.add(4)` -> `A={1,2,4}` |
| `remove(elem)` | Xóa phần tử `elem`. Lỗi `KeyError` nếu không có. | `A.remove(2)` -> `A={1}` |
| `discard(elem)` | Xóa phần tử `elem`. Không lỗi nếu không có. | `A.discard(5)` (không lỗi) |
| `pop()` | Xóa và trả về một phần tử **bất kỳ**. Lỗi nếu set rỗng. | `A.pop()` trả về 1 hoặc 2. |
| `clear()` | Xóa tất cả phần tử. | `A.clear()` -> `set()` |
| **Kiểm tra** | | |
| `isdisjoint(other)` | Trả về `True` nếu set không có phần tử chung với `other`. | `A.isdisjoint({3,4})` -> `True` |
| `issubset(other)` | Trả về `True` nếu set là tập con của `other`. (`<=`) | `A.issubset({1,2,3})` -> `True` |
| `issuperset(other)` | Trả về `True` nếu set chứa `other`. (`>=`) | `{1,2,3}.issuperset(A)` -> `True` |

```python
S = {1, 2, 3}
T = {3, 4, 5}

S.update(T)  # Thêm các phần tử của T vào S
print(f"S sau update(T): {S}")

S.difference_update({1, 4}) # Loại bỏ 1 và 4 khỏi S
print(f"S sau difference_update({{1,4}}): {S}")

S.add(10)
print(f"S sau add(10): {S}")

S.discard(2)  # Xóa 2, không lỗi nếu không có
S.remove(3)   # Xóa 3, lỗi nếu không có
print(f"S sau discard và remove: {S}")

popped = S.pop()  # Xóa phần tử bất kỳ
print(f"Phần tử bị pop: {popped}, S còn lại: {S}")

print(f"S có giao với {{5}} không? {not S.isdisjoint({5})}")
print(f"S là tập con của {{5,10,20}}? {S.issubset({5,10,20})}")
```

**OUTPUT (có thể thay đổi do `pop()`):**
```
S sau update(T): {1, 2, 3, 4, 5}
S sau difference_update({1,4}): {2, 3, 5}
S sau add(10): {2, 3, 5, 10}
S sau discard và remove: {2, 5, 10}
Phần tử bị pop: 2, S còn lại: {10, 5}
S có giao với {5} không? True
S là tập con của {5,10,20}? True
```

#### 4.5.4. Set Comprehensions

```python
# Tạo set chứa bình phương các số từ 0 đến 9
squares_set = {x**2 for x in range(10)}
print(f"Bình phương (set): {squares_set}") # Tự loại bỏ trùng nếu có

# Tạo set từ chuỗi, chỉ lấy ký tự không phải nguyên âm
vowels = {'a', 'e', 'i', 'o', 'u'}
consonants = {ch for ch in 'abracadabra' if ch not in vowels}
print(f"Phụ âm trong 'abracadabra': {consonants}")
```

**OUTPUT:**
```
Bình phương (set): {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
Phụ âm trong 'abracadabra': {'r', 'b', 'c', 'd'}
```

#### 4.5.5. Frozenset (immutable set, dùng làm key trong dict)

`frozenset` là phiên bản bất biến của set. Nó có thể được sử dụng làm khóa (key) trong từ điển hoặc phần tử của một set khác, trong khi set thông thường thì không (vì set là mutable và không hashable).

```python
# Tạo frozenset
fs = frozenset([1, 2, 3, 3])
print(fs)  # frozenset({1, 2, 3})

# Các phép toán (trả về frozenset mới)
fs2 = frozenset([3, 4, 5])
print(fs.union(fs2))  # frozenset({1, 2, 3, 4, 5})

# Dùng làm khóa trong dict
d = {fs: "value1", frozenset([4,5]): "value2"}
print(d)
# Không thể thêm phần tử vào frozenset: fs.add(4) sẽ lỗi.
```

**OUTPUT:**
```
frozenset({1, 2, 3})
frozenset({1, 2, 3, 4, 5})
{frozenset({1, 2, 3}): 'value1', frozenset({4, 5}): 'value2'}
```

### 4.6. Bytes và Bytearray

Đối tượng `bytes` và `bytearray` được sử dụng để xử lý dữ liệu nhị phân (binary data). `bytes` là bất biến, `bytearray` là khả biến.

#### 4.6.1. Bytes Objects

```python
# Tạo bytes từ chuỗi với encoding
b = b"hello"  # Chỉ chấp nhận ký tự ASCII
print(b)  # b'hello'
print(type(b))  # <class 'bytes'>

b2 = bytes("Xin chào", encoding='utf-8')
print(b2)

# Tạo bytes từ list số nguyên (0-255)
b3 = bytes([65, 66, 67])  # ABC
print(b3)

# Truy cập phần tử trả về số nguyên
print(b[0])  # 104 (mã ASCII của 'h')
```

**OUTPUT:**
```
b'hello'
<class 'bytes'>
b'Xin ch\xc3\xa0o'
b'ABC'
104
```

#### 4.6.2. Bytearray Objects (mutable bytes)

```python
# Tạo bytearray
ba = bytearray(b"hello")
print(ba)  # bytearray(b'hello')

# Có thể thay đổi
ba[0] = 72  # 72 là 'H'
print(ba)   # bytearray(b'Hello')

# Thêm phần tử
ba.append(33)  # 33 là '!'
print(ba)      # bytearray(b'Hello!')
```

**OUTPUT:**
```
bytearray(b'hello')
bytearray(b'Hello')
bytearray(b'Hello!')
```

#### 4.6.3. Methods và Operations (tương tự string: `decode`, `hex`, `fromhex`, v.v.)

```python
# decode(): Chuyển bytes thành chuỗi
b = b'hello'
s = b.decode('utf-8')  # Giả sử encoding là utf-8
print(s)

# hex(): Trả về chuỗi hex biểu diễn bytes
print(b.hex())  # '68656c6c6f'

# fromhex(): Tạo bytes từ chuỗi hex
new_b = bytes.fromhex('68656c6c6f')
print(new_b)  # b'hello'

# Các phương thức khác tương tự str (find, replace, split, ...) nhưng trả về bytes
print(b.replace(b'l', b'L'))  # b'heLLo'
```

**OUTPUT:**
```
hello
68656c6c6f
b'hello'
b'heLLo'
```

### 4.7. Range Objects

`range` là một đối tượng bất biến đại diện cho một dãy số. Nó tiết kiệm bộ nhớ vì chỉ lưu trữ `start`, `stop`, và `step`, không tạo ra toàn bộ danh sách số ngay lập tức.

#### 4.7.1. `range()` Function

Cú pháp: `range(stop)` hoặc `range(start, stop[, step])`
-   `start`: Giá trị bắt đầu (mặc định 0).
-   `stop`: Giá trị kết thúc (**không bao gồm**).
-   `step`: Bước nhảy (mặc định 1). Có thể âm.

```python
# Tạo range object
r1 = range(5)        # 0,1,2,3,4
r2 = range(1, 6)     # 1,2,3,4,5
r3 = range(0, 10, 2) # 0,2,4,6,8
r4 = range(10, 0, -2) # 10,8,6,4,2

print(list(r1))
print(list(r2))
print(list(r3))
print(list(r4))
```

**OUTPUT:**
```
[0, 1, 2, 3, 4]
[1, 2, 3, 4, 5]
[0, 2, 4, 6, 8]
[10, 8, 6, 4, 2]
```

#### 4.7.2. Range Attributes (`start`, `stop`, `step`) và Methods (`count`, `index`, `__contains__`)

```python
r = range(2, 10, 3)
print(f"start: {r.start}")  # 2
print(f"stop: {r.stop}")    # 10
print(f"step: {r.step}")    # 3
print(f"List: {list(r)}")   # [2, 5, 8]

# count(value): Đếm số lần value xuất hiện (luôn là 0 hoặc 1 vì range là dãy duy nhất)
print(f"count(5): {r.count(5)}")  # 1
print(f"count(6): {r.count(6)}")  # 0

# index(value): Trả về chỉ số của value. Lỗi nếu không có.
print(f"index(5): {r.index(5)}")  # 1
# print(r.index(6)) # ValueError: 6 is not in range

# Toán tử `in` sử dụng __contains__ một cách hiệu quả
print(f"5 in r: {5 in r}")  # True
print(f"6 in r: {6 in r}")  # False
```

**OUTPUT:**
```
start: 2
stop: 10
step: 3
List: [2, 5, 8]
count(5): 1
count(6): 0
index(5): 1
5 in r: True
6 in r: False
```

#### 4.7.3. Range Slicing

Range hỗ trợ cắt lát, tạo ra một range object mới.

```python
r = range(20)
print(f"range gốc: {list(r)}")

r_slice = r[5:15:2]  # Từ 5 đến 14, bước 2
print(f"range sau slice [5:15:2]: {list(r_slice)}")  # [5, 7, 9, 11, 13]
```

**OUTPUT:**
```
range gốc: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
range sau slice [5:15:2]: [5, 7, 9, 11, 13]
```

### 4.8. Memoryview Objects

`memoryview` cho phép truy cập dữ liệu nhị phân bên trong một đối tượng (như `bytes`, `bytearray`, `array`) mà không cần sao chép. Hữu ích khi xử lý lượng dữ liệu lớn.

```python
# Tạo memoryview từ bytearray
data = bytearray(b'abcdef')
mv = memoryview(data)

print(mv)  # <memory at ...>
print(mv[0])  # 97 (mã 'a')
print(mv.tolist())  # [97, 98, 99, 100, 101, 102]

# Cắt lát memoryview tạo ra memoryview mới, không sao chép dữ liệu
mv_slice = mv[1:4]
print(mv_slice.tobytes())  # b'bcd'

# Thay đổi dữ liệu gốc sẽ phản ánh lên memoryview
data[2] = 122  # 'z'
print(mv_slice.tobytes())  # b'bzd' (đã thay đổi)
```

**OUTPUT:**
```
<memory at 0x7f8e8c0b4a00>
97
[97, 98, 99, 100, 101, 102]
b'bcd'
b'bzd'
```

## 5. BUILT-IN FUNCTIONS (71+ FUNCTIONS)

Các hàm dựng sẵn (built-in functions) là các hàm luôn có sẵn trong mọi môi trường Python mà không cần import bất kỳ module nào. Chúng cung cấp các chức năng cơ bản và thường dùng nhất.

### 5.0. Các hàm chưa được đề cập đầy đủ trong khung

Trong khung nội dung đã liệt kê rất nhiều hàm. Chúng ta sẽ đi qua từng nhóm một cách có hệ thống.

### 5.1. Type Conversion Functions

Các hàm chuyển đổi kiểu dữ liệu từ dạng này sang dạng khác.

#### 5.1.1. `int()`, `float()`, `str()`, `bool()`

Đã được đề cập chi tiết trong phần **2.3. Type Conversion (Casting)**.

#### 5.1.2. `list()`, `tuple()`, `dict()`, `set()`, `frozenset()`

Các hàm tạo collection từ các iterable khác.

```python
# Tạo list từ tuple
list_from_tuple = list((1, 2, 3))
print(f"list((1,2,3)): {list_from_tuple}")

# Tạo tuple từ list
tuple_from_list = tuple([1, 2, 3])
print(f"tuple([1,2,3]): {tuple_from_list}")

# Tạo dict từ list các tuple
dict_from_list = dict([('a', 1), ('b', 2)])
print(f"dict([('a',1),('b',2)]): {dict_from_list}")

# Tạo set từ list
set_from_list = set([1, 2, 2, 3])
print(f"set([1,2,2,3]): {set_from_list}")

# Tạo frozenset từ list
frozenset_from_list = frozenset([1, 2, 2, 3])
print(f"frozenset([1,2,2,3]): {frozenset_from_list}")
```

**OUTPUT:**
```
list((1,2,3)): [1, 2, 3]
tuple([1,2,3]): (1, 2, 3)
dict([('a',1),('b',2)]): {'a': 1, 'b': 2}
set([1,2,2,3]): {1, 2, 3}
frozenset([1,2,2,3]): frozenset({1, 2, 3})
```

#### 5.1.3. `bytes()`, `bytearray()`, `memoryview()`, `object()`, `slice()`

```python
# bytes() và bytearray()
b = bytes([65, 66, 67])  # Tạo bytes từ list số
print(f"bytes([65,66,67]): {b}")  # b'ABC'

ba = bytearray(b'hello')
print(f"bytearray(b'hello'): {ba}")

# memoryview()
mv = memoryview(b'abc')
print(f"memoryview(b'abc')[0]: {mv[0]}")  # 97

# object(): Tạo một đối tượng object mới, cơ sở của tất cả các lớp
obj = object()
print(f"type(object()): {type(obj)}")

# slice(): Tạo một đối tượng slice để sử dụng trong cắt lát
s = slice(2, 5, 2)  # Tương đương [2:5:2]
lst = [0, 1, 2, 3, 4, 5, 6]
print(f"lst[slice(2,5,2)]: {lst[s]}")  # [2, 4]
```

**OUTPUT:**
```
bytes([65,66,67]): b'ABC'
bytearray(b'hello'): bytearray(b'hello')
memoryview(b'abc')[0]: 97
type(object()): <class 'object'>
lst[slice(2,5,2)]: [2, 4]
```

#### 5.1.4. `bin()`, `oct()`, `hex()`, `chr()`, `ord()`, `ascii()`

Các hàm làm việc với biểu diễn số và ký tự.

```python
# bin(), oct(), hex(): Chuyển đổi số nguyên sang chuỗi nhị phân, bát phân, thập lục phân
num = 255
print(f"bin(255): {bin(num)}")  # '0b11111111'
print(f"oct(255): {oct(num)}")  # '0o377'
print(f"hex(255): {hex(num)}")  # '0xff'

# chr(): Trả về ký tự Unicode từ mã code point
print(f"chr(65): {chr(65)}")    # 'A'
print(f"chr(9731): {chr(9731)}") # '☃'

# ord(): Trả về mã code point của ký tự (ngược lại với chr)
print(f"ord('A'): {ord('A')}")  # 65
print(f"ord('☃'): {ord('☃')}")  # 9731

# ascii(): Trả về chuỗi biểu diễn ASCII an toàn, thay thế ký tự không phải ASCII bằng escape sequence
print(f"ascii('café'): {ascii('café')}")  # "'caf\\xe9'"
print(f"ascii('Python'): {ascii('Python')}")  # "'Python'"
```

**OUTPUT:**
```
bin(255): 0b11111111
oct(255): 0o377
hex(255): 0xff
chr(65): A
chr(9731): ☃
ord('A'): 65
ord('☃'): 9731
ascii('café'): 'caf\xe9'
ascii('Python'): 'Python'
```

### 5.2. Mathematical Functions

#### 5.2.1. `abs()`, `divmod()`, `pow()` (với 3 arguments)

```python
# abs(): Trị tuyệt đối
print(f"abs(-10): {abs(-10)}")      # 10
print(f"abs(3.14): {abs(3.14)}")    # 3.14
print(f"abs(3+4j): {abs(3+4j)}")    # 5.0 (căn bậc hai của (3²+4²))

# divmod(): Trả về cặp (thương, số dư) của phép chia
print(f"divmod(10, 3): {divmod(10, 3)}")  # (3, 1) vì 10 = 3*3 + 1
print(f"divmod(10.5, 2): {divmod(10.5, 2)}")  # (5.0, 0.5)

# pow(): Lũy thừa
print(f"pow(2, 3): {pow(2, 3)}")      # 8 (2³)
print(f"pow(2, 3, 3): {pow(2, 3, 3)}") # 2 (2³ mod 3 = 8 mod 3 = 2)
```

**OUTPUT:**
```
abs(-10): 10
abs(3.14): 3.14
abs(3+4j): 5.0
divmod(10, 3): (3, 1)
divmod(10.5, 2): (5.0, 0.5)
pow(2, 3): 8
pow(2, 3, 3): 2
```

#### 5.2.2. `round()` (với `ndigits` parameter), `sum()`, `max()`, `min()`

```python
# round(): Làm tròn số
print(f"round(3.14159): {round(3.14159)}")        # 3
print(f"round(3.14159, 2): {round(3.14159, 2)}")  # 3.14
print(f"round(2.675, 2): {round(2.675, 2)}")      # 2.67 (chú ý: do vấn đề dấu phẩy động)
print(f"round(1234, -2): {round(1234, -2)}")      # 1200 (làm tròn đến hàng trăm)

# sum(): Tính tổng các phần tử trong iterable
print(f"sum([1,2,3,4]): {sum([1,2,3,4])}")               # 10
print(f"sum([1,2,3,4], start=10): {sum([1,2,3,4], 10)}") # 20 (10 + tổng list)

# max() và min(): Tìm giá trị lớn nhất/nhỏ nhất
print(f"max(1, 2, 3): {max(1, 2, 3)}")            # 3
print(f"max([1, 2, 3]): {max([1, 2, 3])}")        # 3
print(f"min([1, 2, 3]): {min([1, 2, 3])}")        # 1

# Có thể dùng key function
words = ['apple', 'banana', 'cherry', 'date']
print(f"max(words, key=len): {max(words, key=len)}")  # 'banana' (dài nhất)
print(f"min(words, key=len): {min(words, key=len)}")  # 'date' (ngắn nhất)
```

**OUTPUT:**
```
round(3.14159): 3
round(3.14159, 2): 3.14
round(2.675, 2): 2.67
round(1234, -2): 1200
sum([1,2,3,4]): 10
sum([1,2,3,4], start=10): 20
max(1, 2, 3): 3
max([1, 2, 3]): 3
min([1, 2, 3]): 1
max(words, key=len): banana
min(words, key=len): date
```

#### 5.2.3. `complex()`, `hash()`

```python
# complex(): Tạo số phức
print(f"complex(3, 4): {complex(3, 4)}")      # (3+4j)
print(f"complex('3+4j'): {complex('3+4j')}")  # (3+4j)
print(f"complex(7): {complex(7)}")            # (7+0j)

# hash(): Trả về giá trị hash của đối tượng (số nguyên). Đối tượng phải hashable.
print(f"hash('hello'): {hash('hello')}")      # Một số nguyên (có thể khác nhau giữa các lần chạy)
print(f"hash(42): {hash(42)}")                # 42 (với số nguyên, hash thường bằng chính nó)
# hash((1,2,3)) cũng được vì tuple bất biến
# hash([1,2,3]) sẽ lỗi vì list không hashable
```

**OUTPUT (hash có thể thay đổi):**
```
complex(3, 4): (3+4j)
complex('3+4j'): (3+4j)
complex(7): (7+0j)
hash('hello'): 4474357901803235129
hash(42): 42
```

#### 5.2.4. `format()` (formatting built-in)

`format()` áp dụng định dạng cho một giá trị, tương tự như phương thức `str.format()`.

```python
# format(value, format_spec)
print(f"format(3.14159, '.2f'): {format(3.14159, '.2f')}")  # '3.14'
print(f"format(42, '05d'): {format(42, '05d')}")            # '00042'
print(f"format(255, 'x'): {format(255, 'x')}")              # 'ff' (hex thường)
print(f"format(255, 'X'): {format(255, 'X')}")              # 'FF' (hex hoa)
print(f"format(1000000, ','): {format(1000000, ',')}")      # '1,000,000'

# Có thể dùng với các đối tượng tùy chỉnh nếu chúng có __format__()
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __format__(self, format_spec):
        if format_spec == 'pretty':
            return f"Point(x={self.x}, y={self.y})"
        return f"({self.x}, {self.y})"

p = Point(3, 4)
print(f"format(p, 'pretty'): {format(p, 'pretty')}")  # 'Point(x=3, y=4)'
print(f"format(p): {format(p)}")                      # '(3, 4)'
```

**OUTPUT:**
```
format(3.14159, '.2f'): 3.14
format(42, '05d'): 00042
format(255, 'x'): ff
format(255, 'X'): FF
format(1000000, ','): 1,000,000
format(p, 'pretty'): Point(x=3, y=4)
format(p): (3, 4)
```

### 5.3. Sequence Functions

Các hàm làm việc với các đối tượng có thể lặp (iterable) hoặc chuỗi (sequence).

#### 5.3.1. `len()`, `sorted()` (với `key` và `reverse` parameters chi tiết), `reversed()` (cho sequences và `__reversed__` protocol)

```python
# len(): Trả về độ dài (số phần tử) của đối tượng
print(f"len('hello'): {len('hello')}")          # 5
print(f"len([1,2,3]): {len([1,2,3])}")         # 3
print(f"len({'a':1, 'b':2}): {len({'a':1, 'b':2})}")  # 2 (số cặp khóa-giá trị)

# sorted(): Trả về một list mới đã sắp xếp từ iterable
numbers = [3, 1, 4, 1, 5, 9, 2]
print(f"sorted(numbers): {sorted(numbers)}")   # [1, 1, 2, 3, 4, 5, 9]
print(f"sorted(numbers, reverse=True): {sorted(numbers, reverse=True)}")  # [9, 5, 4, 3, 2, 1, 1]

# Dùng key function để sắp xếp theo tiêu chí khác
words = ['apple', 'banana', 'Cherry', 'date']
print(f"sorted(words): {sorted(words)}")  # ['Cherry', 'apple', 'banana', 'date'] (theo mã ASCII/Unicode)
print(f"sorted(words, key=str.lower): {sorted(words, key=str.lower)}")  # ['apple', 'banana', 'Cherry', 'date'] (không phân biệt hoa thường)

# Sắp xếp list các tuple theo phần tử thứ 2
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
print(f"sorted(pairs, key=lambda x: x[1]): {sorted(pairs, key=lambda x: x[1])}")  # [(1, 'one'), (3, 'three'), (2, 'two')]

# reversed(): Trả về một iterator đảo ngược (không phải list)
seq = [1, 2, 3, 4]
rev = reversed(seq)
print(f"list(reversed([1,2,3,4])): {list(rev)}")  # [4, 3, 2, 1]
# reversed() cũng làm việc với các đối tượng có __reversed__() method hoặc __getitem__() và __len__()
print(f"list(reversed('hello')): {list(reversed('hello'))}")  # ['o', 'l', 'l', 'e', 'h']
```

**OUTPUT:**
```
len('hello'): 5
len([1,2,3]): 3
len({'a':1, 'b':2}): 2
sorted(numbers): [1, 1, 2, 3, 4, 5, 9]
sorted(numbers, reverse=True): [9, 5, 4, 3, 2, 1, 1]
sorted(words): ['Cherry', 'apple', 'banana', 'date']
sorted(words, key=str.lower): ['apple', 'banana', 'Cherry', 'date']
sorted(pairs, key=lambda x: x[1]): [(1, 'one'), (3, 'three'), (2, 'two')]
list(reversed([1,2,3,4])): [4, 3, 2, 1]
list(reversed('hello')): ['o', 'l', 'l', 'e', 'h']
```

#### 5.3.2. `enumerate()` (với `start` parameter), `zip()` (với strict mode Python 3.10+)

```python
# enumerate(): Gắn chỉ số vào các phần tử của iterable
fruits = ['apple', 'banana', 'cherry']
print(f"list(enumerate(fruits)): {list(enumerate(fruits))}")  # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
print(f"list(enumerate(fruits, start=1)): {list(enumerate(fruits, start=1))}")  # [(1, 'apple'), (2, 'banana'), (3, 'cherry')]

# zip(): Kết hợp các iterable thành các tuple
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
print(f"list(zip(names, ages)): {list(zip(names, ages))}")  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Nếu độ dài khác nhau, zip dừng ở iterable ngắn nhất
list1 = [1, 2, 3]
list2 = ['a', 'b']
print(f"list(zip(list1, list2)): {list(zip(list1, list2))}")  # [(1, 'a'), (2, 'b')]

# Python 3.10+: strict=True để đảm bảo các iterable có cùng độ dài
# Nếu không, sẽ raise ValueError
list3 = [1, 2]
list4 = ['a', 'b', 'c']
try:
    print(f"list(zip(list3, list4, strict=True)): {list(zip(list3, list4, strict=True))}")
except ValueError as e:
    print(f"Lỗi với strict=True: {e}")
```

**OUTPUT:**
```
list(enumerate(fruits)): [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
list(enumerate(fruits, start=1)): [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
list(zip(names, ages)): [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
list(zip(list1, list2)): [(1, 'a'), (2, 'b')]
Lỗi với strict=True: zip() argument 2 is longer than argument 1
```

#### 5.3.3. `all()`, `any()`

- `all(iterable)`: Trả về `True` nếu **tất cả** các phần tử của iterable là truthy (hoặc iterable rỗng).
- `any(iterable)`: Trả về `True` nếu **bất kỳ** phần tử nào của iterable là truthy.

```python
# all()
print(f"all([True, True, True]): {all([True, True, True])}")        # True
print(f"all([True, False, True]): {all([True, False, True])}")      # False
print(f"all([]): {all([])}")                                        # True (vì không có phần tử nào sai)

# any()
print(f"any([False, False, True]): {any([False, False, True])}")    # True
print(f"any([False, False, False]): {any([False, False, False])}")  # False
print(f"any([]): {any([])}")                                        # False (vì không có phần tử nào đúng)

# Ứng dụng thực tế: kiểm tra điều kiện trên list
numbers = [2, 4, 6, 8, 10]
print(f"Tất cả số chẵn? {all(n % 2 == 0 for n in numbers)}")  # True
print(f"Có số lẻ nào không? {any(n % 2 != 0 for n in numbers)}")  # False
```

**OUTPUT:**
```
all([True, True, True]): True
all([True, False, True]): False
all([]): True
any([False, False, True]): True
any([False, False, False]): False
any([]): False
Tất cả số chẵn? True
Có số lẻ nào không? False
```

#### 5.3.4. `filter()`, `map()`

- `filter(function, iterable)`: Lọc các phần tử của iterable mà function trả về `True`.
- `map(function, iterable, ...)`: Áp dụng function lên từng phần tử của iterable.

```python
# filter(): Lọc số chẵn
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Số chẵn: {even_numbers}")  # [2, 4, 6, 8, 10]

# filter() với None: loại bỏ các phần tử falsy (False, 0, '', None, ...)
mixed = [0, 1, False, 2, '', 3, None, 4]
truthy = list(filter(None, mixed))
print(f"Phần tử truthy: {truthy}")  # [1, 2, 3, 4]

# map(): Tính bình phương
squares = list(map(lambda x: x**2, range(5)))
print(f"Bình phương 0-4: {squares}")  # [0, 1, 4, 9, 16]

# map() với nhiều iterable: cộng từng phần tử tương ứng
list1 = [1, 2, 3]
list2 = [10, 20, 30]
sums = list(map(lambda x, y: x + y, list1, list2))
print(f"Tổng từng cặp: {sums}")  # [11, 22, 33]

# So sánh với list comprehension (thường được ưa chuộng hơn)
squares_lc = [x**2 for x in range(5)]
print(f"Bình phương (list comprehension): {squares_lc}")
```

**OUTPUT:**
```
Số chẵn: [2, 4, 6, 8, 10]
Phần tử truthy: [1, 2, 3, 4]
Bình phương 0-4: [0, 1, 4, 9, 16]
Tổng từng cặp: [11, 22, 33]
Bình phương (list comprehension): [0, 1, 4, 9, 16]
```

### 5.4. Object và Class Introspection Functions

Các hàm dùng để kiểm tra và lấy thông tin về đối tượng, lớp.

#### 5.4.1. `type()`, `isinstance()`, `issubclass()` (chi tiết)

```python
# type(): Trả về kiểu/class của đối tượng
print(f"type(42): {type(42)}")                # <class 'int'>
print(f"type('hello'): {type('hello')}")      # <class 'str'>
print(f"type([1,2]): {type([1,2])}")          # <class 'list'>

# isinstance(): Kiểm tra đối tượng có phải là thể hiện của class/kiểu hay không
num = 42
print(f"isinstance(num, int): {isinstance(num, int)}")          # True
print(f"isinstance(num, (int, float)): {isinstance(num, (int, float))}")  # True (kiểm tra trong tuple)
print(f"isinstance([1,2], list): {isinstance([1,2], list)}")    # True
print(f"isinstance([1,2], (list, tuple)): {isinstance([1,2], (list, tuple))}")  # True

# issubclass(): Kiểm tra class này có phải là lớp con của class kia hay không
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

print(f"issubclass(Dog, Animal): {issubclass(Dog, Animal)}")  # True
print(f"issubclass(Cat, Animal): {issubclass(Cat, Animal)}")  # True
print(f"issubclass(Dog, Cat): {issubclass(Dog, Cat)}")        # False
print(f"issubclass(Animal, object): {issubclass(Animal, object)}")  # True (mọi class đều kế thừa object)
```

**OUTPUT:**
```
type(42): <class 'int'>
type('hello'): <class 'str'>
type([1,2]): <class 'list'>
isinstance(num, int): True
isinstance(num, (int, float)): True
isinstance([1,2], list): True
isinstance([1,2], (list, tuple)): True
issubclass(Dog, Animal): True
issubclass(Cat, Animal): True
issubclass(Dog, Cat): False
issubclass(Animal, object): True
```

#### 5.4.2. `id()`, `hash()`, `callable()`

```python
# id(): Trả về "định danh" duy nhất của đối tượng (thường là địa chỉ bộ nhớ)
x = [1, 2, 3]
y = [1, 2, 3]
print(f"id(x): {id(x)}")
print(f"id(y): {id(y)}")
print(f"x is y: {x is y}")  # False vì id khác nhau

# hash(): Đã đề cập ở trên, trả về giá trị hash
print(f"hash(42): {hash(42)}")
print(f"hash('hello'): {hash('hello')}")

# callable(): Kiểm tra xem đối tượng có thể gọi được không (như hàm, phương thức, lớp)
print(f"callable(len): {callable(len)}")          # True (hàm)
print(f"callable(list): {callable(list)}")        # True (lớp có thể gọi để tạo instance)
print(f"callable('hello'): {callable('hello')}")  # False (chuỗi không gọi được)

class MyClass:
    def __call__(self):
        return "Được gọi"

obj = MyClass()
print(f"callable(obj): {callable(obj)}")  # True vì class có __call__ method
print(f"obj(): {obj()}")
```

**OUTPUT (id sẽ thay đổi):**
```
id(x): 140279741718272
id(y): 140279741719232
x is y: False
hash(42): 42
hash('hello'): 4474357901803235129
callable(len): True
callable(list): True
callable('hello'): False
callable(obj): True
obj(): Được gọi
```

#### 5.4.3. `repr()`, `str()`, `format()`, `ascii()` (so sánh `repr()` vs `str()` chi tiết)

- `repr()`: Trả về chuỗi biểu diễn "chính thức" (official) của đối tượng, thường có thể dùng `eval()` để tạo lại đối tượng.
- `str()`: Trả về chuỗi biểu diễn "đẹp" (informal), dễ đọc cho con người.
- `ascii()`: Giống `repr()` nhưng escape các ký tự không phải ASCII.

```python
s = "Hello\nWorld"
print(f"str(s): {str(s)}")        # Hiển thị thân thiện: Hello (xuống dòng) World
print(f"repr(s): {repr(s)}")      # 'Hello\nWorld' (có escape sequence)
print(f"ascii(s): {ascii(s)}")    # 'Hello\nWorld' (vì toàn bộ ASCII)

s2 = "café"
print(f"str(s2): {str(s2)}")      # café
print(f"repr(s2): {repr(s2)}")    # 'café' (có thể hiển thị ký tự đặc biệt tùy terminal)
print(f"ascii(s2): {ascii(s2)}")  # 'caf\xe9' (escape ký tự 'é')

import datetime
now = datetime.datetime.now()
print(f"str(now): {str(now)}")    # '2023-10-01 12:34:56.789012' (dễ đọc)
print(f"repr(now): {repr(now)}")  # 'datetime.datetime(2023, 10, 1, 12, 34, 56, 789012)' (chính xác)

# format(): Đã đề cập ở trên
print(f"format(3.14159, '.3f'): {format(3.14159, '.3f')}")
```

**OUTPUT (có thể thay đổi):**
```
str(s): Hello
World
repr(s): 'Hello\nWorld'
ascii(s): 'Hello\nWorld'
str(s2): café
repr(s2): 'café'
ascii(s2): 'caf\xe9'
str(now): 2023-10-01 12:34:56.789012
repr(now): datetime.datetime(2023, 10, 1, 12, 34, 56, 789012)
format(3.14159, '.3f'): 3.142
```

### 5.5. Input/Output Functions

#### 5.5.1. `print()` (chi tiết: `sep`, `end`, `file`, `flush`), `input()` (với prompt)

```python
# print(): In ra console
print("Hello", "World")                     # Hello World (mặc định sep=' ')
print("Hello", "World", sep=", ")           # Hello, World
print("Hello", end=" ")                     # Không xuống dòng, kết thúc bằng khoảng trắng
print("World")                              # Hello World (cùng dòng)

# Ghi vào file thay vì stdout
with open('output.txt', 'w') as f:
    print("Hello File", file=f)              # Ghi vào file output.txt
# Kiểm tra file output.txt sẽ có dòng "Hello File"

# flush=True: Buộc xả (flush) buffer ra output ngay lập tức
import time
print("Loading", end="", flush=True)
for _ in range(3):
    time.sleep(0.5)
    print(".", end="", flush=True)           # Hiển thị từng dấu . ngay lập tức
print(" Done!")

# input(): Nhận đầu vào từ người dùng
name = input("Nhập tên của bạn: ")          # Hiển thị prompt và chờ nhập
print(f"Xin chào, {name}!")
```

**OUTPUT (khi chạy):**
```
Hello World
Hello, World
Hello World
Loading... Done!
Nhập tên của bạn: [Chờ nhập]
```

#### 5.5.2. `open()` (các modes đầy đủ: `r`, `w`, `a`, `x`, `b`, `t`, `+`, `U`)

Hàm `open()` mở một file và trả về một file object. Các mode phổ biến:

| Mode | Mô tả |
| :--- | :--- |
| `'r'` | Mở để đọc (mặc định). |
| `'w'` | Mở để ghi, tạo file mới nếu chưa có, ghi đè nếu có. |
| `'a'` | Mở để ghi thêm vào cuối file, tạo file mới nếu chưa có. |
| `'x'` | Mở để ghi, nhưng thất bại (lỗi) nếu file đã tồn tại. |
| `'b'` | Binary mode: đọc/ghi dữ liệu nhị phân (bytes). |
| `'t'` | Text mode (mặc định). |
| `'+'` | Mở để cập nhật (đọc và ghi). |
| `'U'` | Universal newlines mode (cũ, không dùng trong Python 3). |

```python
# Tạo một file mẫu để thao tác
with open('example.txt', 'w') as f:
    f.write("Dòng 1\nDòng 2\nDòng 3\n")

# Mở để đọc (text mode, mặc định)
with open('example.txt', 'r') as f:  # 'rt' tương đương 'r'
    content = f.read()
    print(f"Đọc toàn bộ:\n{content}")

# Mở để đọc từng dòng
with open('example.txt', 'r') as f:
    lines = f.readlines()
    print(f"Đọc thành list: {lines}")

# Mở để ghi (ghi đè)
with open('example.txt', 'w') as f:
    f.write("Nội dung mới\n")

# Mở để ghi thêm (append)
with open('example.txt', 'a') as f:
    f.write("Dòng được thêm vào\n")

# Kiểm tra nội dung file sau khi thao tác
with open('example.txt', 'r') as f:
    print(f"Nội dung cuối cùng:\n{f.read()}")

# Mở file nhị phân (binary)
data = b'\x00\x01\x02\x03'
with open('binary.bin', 'wb') as f:
    f.write(data)

with open('binary.bin', 'rb') as f:
    binary_content = f.read()
    print(f"Nội dung binary: {binary_content}")

# Mở để đọc và ghi (mode '+')
with open('example.txt', 'r+') as f:
    # Con trỏ file ở đầu
    f.write("FIRST LINE\n")  # Ghi đè lên phần đầu
    # Di chuyển con trỏ về cuối để ghi tiếp
    f.seek(0, 2)  # 2 = SEEK_END
    f.write("END LINE\n")

# Dọn dẹp file tạo ra
import os
os.remove('example.txt')
os.remove('binary.bin')
```

**OUTPUT:**
```
Đọc toàn bộ:
Dòng 1
Dòng 2
Dòng 3

Đọc thành list: ['Dòng 1\n', 'Dòng 2\n', 'Dòng 3\n']
Nội dung cuối cùng:
Nội dung mới
Dòng được thêm vào

Nội dung binary: b'\x00\x01\x02\x03'
```

### 5.6. Namespace Functions

Các hàm làm việc với namespace (không gian tên) và scope (phạm vi).

#### 5.6.1. `globals()`, `locals()`, `vars()`

```python
# globals(): Trả về dict của global namespace hiện tại
global_var = "I'm global"
print(f"globals() có chứa 'global_var': {'global_var' in globals()}")

# locals(): Trả về dict của local namespace hiện tại
def my_func():
    local_var = "I'm local"
    print(f"locals() trong hàm: {locals()}")

my_func()

# vars(): Trả về __dict__ attribute của đối tượng, hoặc locals() nếu không có đối tượng
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = MyClass(10, 20)
print(f"vars(obj): {vars(obj)}")  # {'x': 10, 'y': 20}

# vars() không đối số tương đương locals()
print(f"vars() == locals(): {vars() == locals()}")
```

**OUTPUT:**
```
globals() có chứa 'global_var': True
locals() trong hàm: {'local_var': "I'm local"}
vars(obj): {'x': 10, 'y': 20}
vars() == locals(): True
```

#### 5.6.2. `dir()` (với parameter, tùy chỉnh kết quả)

`dir()` trả về danh sách các tên trong namespace hiện tại, hoặc các thuộc tính của đối tượng.

```python
# dir() không đối số: trả về tên trong current scope
print(f"dir() có chứa 'print': {'print' in dir()}")  # True

# dir() với đối tượng: trả về các thuộc tính của đối tượng
s = "hello"
print(f"Một số thuộc tính của chuỗi: {[attr for attr in dir(s) if not attr.startswith('_')][:5]}")

# dir() với module
import math
print(f"Một số thuộc tính của module math: {[attr for attr in dir(math) if not attr.startswith('_')][:5]}")

# Lưu ý: dir() không liệt kê tất cả, đặc biệt các thuộc tính được tạo động
class DynamicAttrs:
    pass

obj = DynamicAttrs()
obj.new_attr = "dynamic"
print(f"'new_attr' trong dir(obj): {'new_attr' in dir(obj)}")  # True
```

**OUTPUT:**
```
dir() có chứa 'print': True
Một số thuộc tính của chuỗi: ['capitalize', 'casefold', 'center', 'count', 'encode']
Một số thuộc tính của module math: ['acos', 'acosh', 'asin', 'asinh', 'atan']
'new_attr' trong dir(obj): True
```

### 5.7. Execution Functions

Các hàm thực thi mã động (dynamic code execution).

#### 5.7.1. `eval()`, `exec()`, `compile()`

- `eval(expression, globals=None, locals=None)`: Đánh giá (evaluate) một **biểu thức** Python và trả về giá trị.
- `exec(object, globals=None, locals=None)`: Thực thi một **khối mã** Python (như chuỗi, code object). Không trả về giá trị (trả về `None`).
- `compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)`: Biên dịch mã nguồn thành code object để có thể thực thi bởi `eval()` hoặc `exec()`.

```python
# eval(): Tính toán biểu thức
result = eval("3 + 4 * 2")
print(f"eval('3 + 4 * 2'): {result}")  # 11

# Có thể dùng với từ điển để cung cấp namespace
namespace = {'x': 10, 'y': 20}
result = eval("x + y", namespace)
print(f"eval('x + y', namespace): {result}")  # 30

# eval() chỉ chấp nhận biểu thức, không chấp nhận câu lệnh
# eval("print('hello')")  # Lỗi nếu print không có trong namespace

# exec(): Thực thi khối mã (có thể là nhiều dòng)
code_block = """
for i in range(3):
    print(f"Lần lặp {i}")
"""
exec(code_block)

# exec() có thể thay đổi namespace
my_globals = {}
exec("z = 100", my_globals)
print(f"my_globals sau exec: {my_globals}")  # {'z': 100}

# compile(): Biên dịch mã nguồn
code_str = "print('Hello from compiled code')"
compiled = compile(code_str, '<string>', 'exec')
exec(compiled)

# Chế độ 'eval' cho biểu thức
expr = "2 ** 8"
compiled_expr = compile(expr, '<string>', 'eval')
result = eval(compiled_expr)
print(f"Kết quả từ compiled eval: {result}")
```

**OUTPUT:**
```
eval('3 + 4 * 2'): 11
eval('x + y', namespace): 30
Lần lặp 0
Lần lặp 1
Lần lặp 2
my_globals sau exec: {'z': 100}
Hello from compiled code
Kết quả từ compiled eval: 256
```

**CẢNH BÁO:** `eval()` và `exec()` có thể nguy hiểm nếu sử dụng với đầu vào từ người dùng không được kiểm soát, vì chúng có thể thực thi mã tùy ý. Luôn hạn chế namespace khi sử dụng.

### 5.8. Iteration Functions
## 5.8.1. `iter()` (bao gồm `iter(callable, sentinel)`), `next()`

- `iter(iterable)`: Trả về một iterator object từ iterable.
- `iter(callable, sentinel)`: Tạo iterator gọi callable cho đến khi nó trả về sentinel.
- `next(iterator[, default])`: Lấy phần tử tiếp theo từ iterator. Nếu hết và có default, trả về default; không thì raise `StopIteration`.

```python
# iter() với iterable thông thường
lst = [1, 2, 3]
it = iter(lst)
print(f"next(it): {next(it)}")  # 1
print(f"next(it): {next(it)}")  # 2
print(f"next(it): {next(it)}")  # 3
# print(next(it))  # Lỗi StopIteration

# next() với giá trị mặc định
it = iter([1])
print(f"next(it, 'hết'): {next(it, 'hết')}")  # 1
print(f"next(it, 'hết'): {next(it, 'hết')}")  # 'hết'

# iter() với callable và sentinel
import random
def random_byte():
    return random.randint(0, 255)

# Tạo iterator sinh byte ngẫu nhiên cho đến khi gặp byte 0 (rất hiếm)
random_iter = iter(random_byte, 0)
# Lấy 5 byte đầu tiên (có thể dừng sớm nếu gặp 0)
for i, byte in enumerate(random_iter):
    if i >= 5:
        break
    print(f"Byte {i}: {byte}")
```

**OUTPUT (ngẫu nhiên):**
```
next(it): 1
next(it): 2
next(it): 3
next(it, 'hết'): 1
next(it, 'hết'): hết
Byte 0: 142
Byte 1: 87
Byte 2: 231
Byte 3: 199
Byte 4: 33
```

### 5.9. Other Built-in Functions

#### 5.9.1. `breakpoint()` (Python 3.7+)

Gọi trình gỡ lỗi (debugger) mặc định. Trong môi trường thông thường, nó gọi `pdb.set_trace()`.

```python
def faulty_function(x):
    result = x * 2
    # breakpoint()  # Bỏ comment để dừng tại đây khi chạy
    return result + 1

print(faulty_function(5))
```

**OUTPUT (nếu không dùng breakpoint):**
```
11
```

#### 5.9.2. `import()`

Hàm này được sử dụng nội bộ bởi câu lệnh `import`. Có thể dùng để import module động.

```python
# Import module bằng tên dạng chuỗi
math_module = __import__('math')
print(f"math.sqrt(16): {math_module.sqrt(16)}")  # 4.0

# Trong thực tế, nên dùng importlib.import_module()
import importlib
math_module2 = importlib.import_module('math')
print(f"math.pi: {math_module2.pi}")
```

**OUTPUT:**
```
math.sqrt(16): 4.0
math.pi: 3.141592653589793
```

---

# PHẦN II: CẤU TRÚC ĐIỀU KHIỂN VÀ HÀM

## 1. CẤU TRÚC ĐIỀU KHIỂN

Cấu trúc điều khiển cho phép điều hướng luồng thực thi chương trình dựa trên các điều kiện và vòng lặp.

### 1.1. Câu lệnh điều kiện

Câu lệnh điều kiện cho phép thực thi các khối mã khác nhau dựa trên việc kiểm tra một hoặc nhiều điều kiện.

#### 1.1.1. Câu lệnh `if`

Câu lệnh `if` kiểm tra một điều kiện, nếu điều kiện đúng (True) thì khối mã bên trong sẽ được thực thi.

**Cú pháp:**
```python
if điều_kiện:
    # Khối mã thực thi nếu điều_kiện là True
```

**Ví dụ:**
```python
# Kiểm tra số dương
x = 10
if x > 0:
    print("x là số dương")
```
**Output:**
```
x là số dương
```

#### 1.1.2. Câu lệnh `if-else`

Câu lệnh `if-else` cung cấp hai nhánh: một thực thi khi điều kiện đúng, một thực thi khi điều kiện sai.

**Cú pháp:**
```python
if điều_kiện:
    # Khối mã thực thi nếu điều_kiện là True
else:
    # Khối mã thực thi nếu điều_kiện là False
```

**Ví dụ:**
```python
# Kiểm tra số chẵn lẻ
x = 7
if x % 2 == 0:
    print("x là số chẵn")
else:
    print("x là số lẻ")
```
**Output:**
```
x là số lẻ
```

#### 1.1.3. Câu lệnh `if-elif-else`

Câu lệnh `if-elif-else` cho phép kiểm tra nhiều điều kiện tuần tự. Chỉ có khối mã đầu tiên có điều kiện đúng sẽ được thực thi.

**Cú pháp:**
```python
if điều_kiện_1:
    # Thực thi nếu điều_kiện_1 True
elif điều_kiện_2:
    # Thực thi nếu điều_kiện_2 True
elif điều_kiện_3:
    # Thực thi nếu điều_kiện_3 True
else:
    # Thực thi nếu tất cả điều kiện trên False
```

**Ví dụ:**
```python
# Xếp loại điểm số
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Điểm {score} xếp loại: {grade}")
```
**Output:**
```
Điểm 85 xếp loại: B
```

#### 1.1.4. Câu lệnh điều kiện lồng nhau

Câu lệnh điều kiện có thể được lồng trong nhau để tạo logic phức tạp hơn.

**Ví dụ:**
```python
# Kiểm tra số nguyên dương và chẵn/lẻ
x = 12
if x > 0:
    if x % 2 == 0:
        print("Số nguyên dương chẵn")
    else:
        print("Số nguyên dương lẻ")
else:
    print("Số không dương")
```
**Output:**
```
Số nguyên dương chẵn
```

#### 1.1.5. Toán tử điều kiện ba ngôi

Python cung cấp cú pháp rút gọn cho câu lệnh `if-else` dạng một dòng.

**Cú pháp:**
```python
giá_trị_1 if điều_kiện else giá_trị_2
```

**Ví dụ:**
```python
# Gán giá trị dựa trên điều kiện
x = 10
result = "dương" if x > 0 else "không dương"
print(f"Số {x} là số {result}")
```
**Output:**
```
Số 10 là số dương
```

### 1.2. Vòng lặp

Vòng lặp cho phép thực thi lặp lại một khối mã nhiều lần.

#### 1.2.1. Vòng lặp `for`

Vòng lặp `for` dùng để lặp qua các phần tử của một đối tượng có thể lặp (iterable) như danh sách, chuỗi, tuple, từ điển, tập hợp, hoặc sử dụng hàm `range()`.

**Cú pháp:**
```python
for biến in iterable:
    # Khối mã thực thi cho mỗi phần tử
```

**1.2.1.1. Lặp qua chuỗi (string)**

**Ví dụ:**
```python
# Duyệt qua từng ký tự trong chuỗi
text = "Python"
for char in text:
    print(char)
```
**Output:**
```
P
y
t
h
o
n
```

**1.2.1.2. Lặp qua danh sách (list)**

**Ví dụ:**
```python
# Tính tổng các số trong danh sách
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f"Tổng: {total}")
```
**Output:**
```
Tổng: 15
```

**1.2.1.3. Lặp qua từ điển (dictionary)**

Khi lặp qua từ điển, mặc định sẽ lặp qua các khóa (keys).

**Ví dụ:**
```python
# Lặp qua các khóa và giá trị của từ điển
student = {"name": "Alice", "age": 20, "grade": "A"}
for key in student:
    print(f"{key}: {student[key]}")
```
**Output:**
```
name: Alice
age: 20
grade: A
```

Có thể sử dụng phương thức `items()` để lặp qua cả khóa và giá trị cùng lúc:

```python
for key, value in student.items():
    print(f"{key}: {value}")
```

**1.2.1.4. Hàm `range()`**

Hàm `range()` tạo ra một chuỗi số nguyên, thường dùng với vòng lặp `for`.

**Cú pháp:**
- `range(stop)`: Tạo số từ 0 đến stop-1
- `range(start, stop)`: Tạo số từ start đến stop-1
- `range(start, stop, step)`: Tạo số từ start đến stop-1, bước nhảy step

**Ví dụ:**
```python
# In các số từ 0 đến 4
for i in range(5):
    print(i)
```
**Output:**
```
0
1
2
3
4
```

**Ví dụ với bước nhảy:**
```python
# In các số chẵn từ 0 đến 10
for i in range(0, 11, 2):
    print(i)
```
**Output:**
```
0
2
4
6
8
10
```

**1.2.1.5. Hàm `enumerate()`**

Hàm `enumerate()` thêm một bộ đếm vào đối tượng có thể lặp, trả về các cặp (index, value).

**Ví dụ:**
```python
# Đánh số thứ tự cho các phần tử
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```
**Output:**
```
0: apple
1: banana
2: cherry
```

Có thể chỉ định điểm bắt đầu đếm với tham số `start`:

```python
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
```

**1.2.1.6. Hàm `zip()`**

Hàm `zip()` kết hợp nhiều đối tượng có thể lặp thành các tuple.

**Ví dụ:**
```python
# Kết hợp hai danh sách
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```
**Output:**
```
Alice: 85
Bob: 92
Charlie: 78
```

Từ Python 3.10+, `zip()` hỗ trợ tham số `strict` để đảm bảo các iterables có độ dài bằng nhau:

```python
list1 = [1, 2, 3]
list2 = ['a', 'b']
# Sẽ gây lỗi vì độ dài khác nhau
for a, b in zip(list1, list2, strict=True):
    print(a, b)
```

#### 1.2.2. Vòng lặp `while`

Vòng lặp `while` thực thi một khối mã lặp đi lặp lại chừng nào điều kiện còn đúng.

**Cú pháp:**
```python
while điều_kiện:
    # Khối mã thực thi
```

**Ví dụ:**
```python
# Đếm ngược từ 5 đến 1
count = 5
while count > 0:
    print(count)
    count -= 1
print("Bắt đầu!")
```
**Output:**
```
5
4
3
2
1
Bắt đầu!
```

**Ví dụ với điều kiện phức tạp:**
```python
# Tính giai thừa
n = 5
factorial = 1
while n > 0:
    factorial *= n
    n -= 1
print(f"5! = {factorial}")
```
**Output:**
```
5! = 120
```

#### 1.2.3. Câu lệnh điều khiển vòng lặp

**1.2.3.1. Câu lệnh `break`**

Câu lệnh `break` dùng để thoát khỏi vòng lặp ngay lập tức.

**Ví dụ:**
```python
# Tìm số đầu tiên chia hết cho 7
for i in range(1, 20):
    if i % 7 == 0:
        print(f"Số đầu tiên chia hết cho 7 là: {i}")
        break
```
**Output:**
```
Số đầu tiên chia hết cho 7 là: 7
```

**1.2.3.2. Câu lệnh `continue`**

Câu lệnh `continue` bỏ qua phần còn lại của vòng lặp hiện tại và chuyển sang lần lặp tiếp theo.

**Ví dụ:**
```python
# In các số lẻ từ 1 đến 10
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
```
**Output:**
```
1
3
5
7
9
```

**1.2.3.3. Câu lệnh `pass`**

Câu lệnh `pass` là một câu lệnh rỗng, không làm gì cả. Thường dùng làm trình giữ chỗ.

**Ví dụ trong vòng lặp:**
```python
for i in range(5):
    # Chưa xác định xử lý gì
    pass

# Sử dụng trong hàm
def function_chua_hoan_thien():
    pass

# Sử dụng trong lớp
class LopChuaHoanThien:
    pass
```

#### 1.2.4. Mệnh đề `else` với vòng lặp

Mệnh đề `else` trong vòng lặp được thực thi khi vòng lặp kết thúc bình thường (không bị `break`).

**Ví dụ với vòng lặp `for`:**
```python
# Kiểm tra số nguyên tố
num = 13
for i in range(2, num):
    if num % i == 0:
        print(f"{num} không phải số nguyên tố")
        break
else:
    print(f"{num} là số nguyên tố")
```
**Output:**
```
13 là số nguyên tố
```

**Ví dụ với vòng lặp `while`:**
```python
# Đếm đến 3
count = 1
while count <= 3:
    print(count)
    count += 1
else:
    print("Đếm xong!")
```
**Output:**
```
1
2
3
Đếm xong!
```

#### 1.2.5. Vòng lặp lồng nhau

Vòng lặp có thể được lồng trong vòng lặp khác.

**Ví dụ:**
```python
# Tạo bảng cửu chương từ 1 đến 3
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("-" * 10)
```
**Output:**
```
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
----------
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
----------
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
----------
```

### 1.3. Khớp mẫu (Pattern Matching) (Python 3.10+)

Khớp mẫu là tính năng mới từ Python 3.10+, cho phép so khớp giá trị với các mẫu (pattern) và thực thi mã tương ứng.

#### 1.3.1. Câu lệnh `match`

Câu lệnh `match` tương tự như câu lệnh `switch` trong các ngôn ngữ khác, nhưng mạnh mẽ hơn.

**Cú pháp cơ bản:**
```python
match giá_trị:
    case mẫu_1:
        # Xử lý khi khớp mẫu_1
    case mẫu_2:
        # Xử lý khi khớp mẫu_2
    case _:
        # Xử lý mặc định (wildcard)
```

**Ví dụ:**
```python
# Đánh giá mã HTTP
http_code = 404
match http_code:
    case 200:
        print("Thành công")
    case 404:
        print("Không tìm thấy")
    case 500:
        print("Lỗi server")
    case _:
        print("Mã không xác định")
```
**Output:**
```
Không tìm thấy
```

#### 1.3.2. Các loại mẫu (Patterns)

**1.3.2.1. Mẫu chữ (Literal Patterns)**

So khớp với các giá trị cụ thể như số, chuỗi, None, True, False.

**Ví dụ:**
```python
# Kiểm tra giá trị boolean
value = True
match value:
    case True:
        print("Giá trị đúng")
    case False:
        print("Giá trị sai")
```
**Output:**
```
Giá trị đúng
```

**1.3.2.2. Mẫu chuỗi (Sequence Patterns)**

So khớp với các chuỗi (sequences) như list, tuple.

**Ví dụ:**
```python
# Kiểm tra cấu trúc của list
point = [0, 5]
match point:
    case [0, 0]:
        print("Gốc tọa độ")
    case [0, y]:
        print(f"Trên trục y tại y = {y}")
    case [x, 0]:
        print(f"Trên trục x tại x = {x}")
    case [x, y]:
        print(f"Tọa độ ({x}, {y})")
```
**Output:**
```
Trên trục y tại y = 5
```

**1.3.2.3. Mẫu ánh xạ (Mapping Patterns)**

So khớp với từ điển (dictionary).

**Ví dụ:**
```python
# Kiểm tra cấu trúc từ điển
data = {"type": "user", "name": "Alice", "age": 30}
match data:
    case {"type": "user", "name": name}:
        print(f"Người dùng: {name}")
    case {"type": "admin", "name": name}:
        print(f"Quản trị viên: {name}")
```
**Output:**
```
Người dùng: Alice
```

**1.3.2.4. Mẫu lớp (Class Patterns)**

So khớp với các đối tượng của lớp cụ thể.

**Ví dụ:**
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(1, 2)
match point:
    case Point(x=0, y=0):
        print("Gốc tọa độ")
    case Point(x=x, y=y):
        print(f"Điểm tại ({x}, {y})")
```
**Output:**
```
Điểm tại (1, 2)
```

**1.3.2.5. Mẫu ký tự đại diện (Wildcard Pattern)**

Ký tự `_` khớp với bất kỳ giá trị nào, nhưng không gán giá trị cho biến.

**Ví dụ:**
```python
value = 42
match value:
    case 0:
        print("Số không")
    case _:
        print("Khác không")
```
**Output:**
```
Khác không
```

**1.3.2.6. Mẫu OR Pattern**

Sử dụng `|` để khớp với một trong nhiều mẫu.

**Ví dụ:**
```python
value = 3
match value:
    case 1 | 3 | 5 | 7 | 9:
        print("Số lẻ một chữ số")
    case 2 | 4 | 6 | 8:
        print("Số chẵn một chữ số")
    case _:
        print("Số khác")
```
**Output:**
```
Số lẻ một chữ số
```

#### 1.3.3. Điều kiện bảo vệ (Guard Conditions)

Có thể thêm điều kiện bổ sung với từ khóa `if` trong mệnh đề `case`.

**Ví dụ:**
```python
# Kiểm tra điểm hợp lệ
score = 85
match score:
    case s if s >= 90:
        grade = "A"
    case s if s >= 80:
        grade = "B"
    case s if s >= 70:
        grade = "C"
    case s if s >= 60:
        grade = "D"
    case _:
        grade = "F"
print(f"Điểm {score}: {grade}")
```
**Output:**
```
Điểm 85: B
```

#### 1.3.4. Mẫu chuỗi chi tiết (Sequence Patterns)

Mẫu chuỗi có thể chứa các phần tử cụ thể và ký tự đại diện.

**Ví dụ với list:**
```python
# Phân tích list
items = [1, 2, 3, 4, 5]
match items:
    case [first, *middle, last]:
        print(f"Đầu: {first}, Giữa: {middle}, Cuối: {last}")
    case []:
        print("List rỗng")
```
**Output:**
```
Đầu: 1, Giữa: [2, 3, 4], Cuối: 5
```

**Ví dụ với tuple:**
```python
# Phân tích RGB tuple
color = (255, 0, 0)
match color:
    case (r, g, b) if r == g == b:
        print(f"Màu xám: ({r}, {g}, {b})")
    case (255, 0, 0):
        print("Màu đỏ")
    case (0, 255, 0):
        print("Màu xanh lá")
    case (0, 0, 255):
        print("Màu xanh dương")
    case (r, g, b):
        print(f"Màu RGB: ({r}, {g}, {b})")
```
**Output:**
```
Màu đỏ
```

#### 1.3.5. Mẫu ánh xạ chi tiết (Mapping Patterns)

**Ví dụ:**
```python
# Phân tích cấu trúc dữ liệu phức tạp
data = {
    "type": "employee",
    "details": {"name": "Bob", "position": "developer"},
    "status": "active"
}

match data:
    case {"type": "employee", "details": {"name": name, "position": pos}}:
        print(f"Nhân viên: {name}, Vị trí: {pos}")
    case {"type": "customer", "name": name}:
        print(f"Khách hàng: {name}")
```
**Output:**
```
Nhân viên: Bob, Vị trí: developer
```

#### 1.3.6. Thuộc tính `__match_args__`

Các lớp có thể định nghĩa thuộc tính `__match_args__` để chỉ định thứ tự các thuộc tính khi khớp mẫu.

**Ví dụ:**
```python
class Point:
    __match_args__ = ("x", "y")
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(3, 4)
match point:
    case Point(0, 0):
        print("Gốc tọa độ")
    case Point(x, y):
        print(f"Điểm ({x}, {y})")
```
**Output:**
```
Điểm (3, 4)
```

## 2. HÀM

Hàm là một khối mã được đặt tên, có thể tái sử dụng, thực hiện một nhiệm vụ cụ thể.

### 2.1. Cơ bản về hàm

#### 2.1.1. Định nghĩa hàm

Hàm được định nghĩa bằng từ khóa `def`, theo sau là tên hàm và dấu ngoặc đơn chứa tham số.

**Cú pháp:**
```python
def tên_hàm(tham_số1, tham_số2, ...):
    """Chuỗi tài liệu (docstring) - không bắt buộc"""
    # Thân hàm
    return giá_trị_trả_về
```

**Ví dụ:**
```python
# Định nghĩa hàm tính bình phương
def square(x):
    """Trả về bình phương của x"""
    return x ** 2
```

#### 2.1.2. Gọi hàm

Sau khi định nghĩa, hàm có thể được gọi bằng tên của nó và truyền đối số.

**Ví dụ:**
```python
# Gọi hàm square
result = square(5)
print(f"5 bình phương là: {result}")
```
**Output:**
```
5 bình phương là: 25
```

#### 2.1.3. Câu lệnh `return`

Câu lệnh `return` kết thúc hàm và trả về giá trị. Hàm không có `return` sẽ trả về `None`.

**Ví dụ:**
```python
# Hàm có return
def add(a, b):
    return a + b

# Hàm không có return
def greet(name):
    print(f"Xin chào {name}")

result1 = add(3, 4)
print(f"Tổng: {result1}")

result2 = greet("Alice")
print(f"Giá trị trả về: {result2}")
```
**Output:**
```
Tổng: 7
Xin chào Alice
Giá trị trả về: None
```

#### 2.1.4. Giá trị trả về `None`

`None` là một giá trị đặc biệt trong Python, đại diện cho không có gì (nothing). Nó là giá trị mặc định mà hàm trả về khi không có câu lệnh `return`.

**Ví dụ:**
```python
# Hàm không trả về giá trị cụ thể
def do_nothing():
    pass

result = do_nothing()
print(f"Kết quả: {result}")
print(f"result is None: {result is None}")
```
**Output:**
```
Kết quả: None
result is None: True
```

### 2.2. Tham số hàm

#### 2.2.1. Tham số vị trí (Positional Arguments)

Tham số vị trí được truyền theo thứ tự khai báo.

**Ví dụ:**
```python
def describe_person(name, age, city):
    print(f"{name} {age} tuổi, sống ở {city}")

# Truyền theo vị trí
describe_person("Alice", 25, "Hà Nội")
```
**Output:**
```
Alice 25 tuổi, sống ở Hà Nội
```

#### 2.2.2. Tham số từ khóa (Keyword Arguments)

Tham số từ khóa được truyền với tên tham số, không phụ thuộc vào vị trí.

**Ví dụ:**
```python
# Truyền theo từ khóa
describe_person(city="TP.HCM", age=30, name="Bob")
```
**Output:**
```
Bob 30 tuổi, sống ở TP.HCM
```

#### 2.2.3. Tham số mặc định (Default Parameters)

Tham số có thể có giá trị mặc định, được sử dụng khi không truyền đối số.

**Ví dụ:**
```python
def greet(name, greeting="Xin chào"):
    print(f"{greeting} {name}!")

# Sử dụng giá trị mặc định
greet("Alice")

# Truyền giá trị khác
greet("Bob", "Chào bạn")
```
**Output:**
```
Xin chào Alice!
Chào bạn Bob!
```

**Lưu ý:** Tham số mặc định chỉ được khởi tạo một lần khi hàm được định nghĩa.

**Ví dụ về vấn đề với tham số mặc định có thể thay đổi:**
```python
def add_item(item, items=[]):
    items.append(item)
    return items

# Vấn đề: items mặc định dùng chung
list1 = add_item("apple")
list2 = add_item("banana")
print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"list1 is list2: {list1 is list2}")
```
**Output:**
```
list1: ['apple', 'banana']
list2: ['apple', 'banana']
list1 is list2: True
```

**Giải pháp:** Sử dụng `None` làm giá trị mặc định:
```python
def add_item_fixed(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

list1 = add_item_fixed("apple")
list2 = add_item_fixed("banana")
print(f"list1: {list1}")
print(f"list2: {list2}")
```
**Output:**
```
list1: ['apple']
list2: ['banana']
```

#### 2.2.4. Tham số độ dài thay đổi (Variable-length Arguments)

##### 2.2.4.1. `*args` (Non-keyword Variable Arguments)

`*args` cho phép hàm nhận số lượng tham số vị trí tùy ý, được đóng gói thành tuple.

**Ví dụ:**
```python
def sum_all(*args):
    print(f"args kiểu: {type(args)}")
    print(f"args: {args}")
    return sum(args)

result = sum_all(1, 2, 3, 4, 5)
print(f"Tổng: {result}")
```
**Output:**
```
args kiểu: <class 'tuple'>
args: (1, 2, 3, 4, 5)
Tổng: 15
```

##### 2.2.4.2. `**kwargs` (Keyword Variable Arguments)

`**kwargs` cho phép hàm nhận số lượng tham số từ khóa tùy ý, được đóng gói thành dictionary.

**Ví dụ:**
```python
def print_info(**kwargs):
    print(f"kwargs kiểu: {type(kwargs)}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="Hà Nội")
```
**Output:**
```
kwargs kiểu: <class 'dict'>
name: Alice
age: 25
city: Hà Nội
```

##### 2.2.4.3. Kết hợp các loại tham số

Thứ tự tham số trong khai báo hàm: positional → *args → keyword-only → **kwargs

**Ví dụ:**
```python
def complex_func(a, b, *args, option=True, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"option: {option}")
    print(f"kwargs: {kwargs}")

complex_func(1, 2, 3, 4, 5, option=False, x=10, y=20)
```
**Output:**
```
a: 1, b: 2
args: (3, 4, 5)
option: False
kwargs: {'x': 10, 'y': 20}
```

##### 2.2.4.4. So sánh `*args` và `**kwargs`

**Bảng so sánh:**

| Đặc điểm | `*args` | `**kwargs` |
|----------|---------|------------|
| **Loại tham số** | Vị trí (positional) | Từ khóa (keyword) |
| **Kiểu dữ liệu** | Tuple | Dictionary |
| **Ký hiệu** | Dấu hoa thị (`*`) | Hai dấu hoa thị (`**`) |
| **Tên thông thường** | `args` | `kwargs` |
| **Ví dụ khai báo** | `def func(*args):` | `def func(**kwargs):` |
| **Ví dụ gọi** | `func(1, 2, 3)` | `func(a=1, b=2)` |
| **Thu thập** | Tham số vị trí thừa | Tham số từ khóa thừa |

##### 2.2.4.5. Giải nén (Unpacking) khi gọi hàm

Có thể giải nén tuple/list với `*` và dictionary với `**` khi gọi hàm.

**Ví dụ:**
```python
def print_three(a, b, c):
    print(f"a={a}, b={b}, c={c}")

# Giải nén tuple
args_tuple = (1, 2, 3)
print_three(*args_tuple)

# Giải nén list
args_list = [4, 5, 6]
print_three(*args_list)

# Giải nén dictionary
kwargs_dict = {'a': 7, 'b': 8, 'c': 9}
print_three(**kwargs_dict)
```
**Output:**
```
a=1, b=2, c=3
a=4, b=5, c=6
a=7, b=8, c=9
```

#### 2.2.5. Tham số chỉ vị trí (Positional-only Parameters) (Python 3.8+)

Sử dụng `/` để chỉ định các tham số trước nó chỉ có thể truyền theo vị trí.

**Ví dụ:**
```python
def positional_only(a, b, /, c, d):
    print(f"a={a}, b={b}, c={c}, d={d}")

# Đúng: a, b truyền theo vị trí
positional_only(1, 2, 3, 4)
positional_only(1, 2, c=3, d=4)

# Sai: a, b không thể truyền theo từ khóa
# positional_only(a=1, b=2, c=3, d=4)  # Lỗi!
```
**Output:**
```
a=1, b=2, c=3, d=4
a=1, b=2, c=3, d=4
```

#### 2.2.6. Tham số chỉ từ khóa (Keyword-only Parameters)

Sử dụng `*` để chỉ định các tham số sau nó chỉ có thể truyền theo từ khóa.

**Ví dụ:**
```python
def keyword_only(a, b, *, c, d):
    print(f"a={a}, b={b}, c={c}, d={d}")

# Đúng: c, d truyền theo từ khóa
keyword_only(1, 2, c=3, d=4)

# Sai: c, d không thể truyền theo vị trí
# keyword_only(1, 2, 3, 4)  # Lỗi!
```
**Output:**
```
a=1, b=2, c=3, d=4
```

### 2.3. Chú thích kiểu (Function Annotations)

Chú thích kiểu cung cấp thông tin về kiểu dữ liệu của tham số và giá trị trả về.

#### 2.3.1. Type Hints (PEP 484)

**Ví dụ:**
```python
def add(a: int, b: int) -> int:
    return a + b

result = add(5, 3)
print(f"Kết quả: {result}")
print(f"Chú thích: {add.__annotations__}")
```
**Output:**
```
Kết quả: 8
Chú thích: {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
```

#### 2.3.2. Biến chú thích (Variable Annotations) (PEP 526)

**Ví dụ:**
```python
# Chú thích biến
name: str = "Alice"
age: int = 25
scores: list[int] = [85, 92, 78]

print(f"Tên: {name}, Tuổi: {age}, Điểm: {scores}")
```
**Output:**
```
Tên: Alice, Tuổi: 25, Điểm: [85, 92, 78]
```

### 2.4. Phạm vi và không gian tên

#### 2.4.1. Quy tắc LEGB

Python tìm kiếm biến theo thứ tự:
- **L (Local)**: Trong phạm vi hàm hiện tại
- **E (Enclosing)**: Trong phạm vi hàm bao ngoài (closure)
- **G (Global)**: Trong phạm vi module
- **B (Built-in)**: Trong phạm vi built-in của Python

**Ví dụ:**
```python
# Biến built-in
print = "đây không phải hàm print"  # Ghi đè biến built-in

x = "global"  # Global

def outer():
    x = "enclosing"  # Enclosing
    
    def inner():
        x = "local"  # Local
        print(f"Local x: {x}")
    
    inner()
    print(f"Enclosing x: {x}")

outer()
print(f"Global x: {x}")

# Khôi phục hàm print
del print
print("Hàm print đã khôi phục")
```
**Output:**
```
Local x: local
Enclosing x: enclosing
Global x: global
Hàm print đã khôi phục
```

#### 2.4.2. Câu lệnh `global`

Câu lệnh `global` cho phép truy cập và sửa đổi biến toàn cục từ trong hàm.

**Ví dụ:**
```python
counter = 0

def increment():
    global counter
    counter += 1
    print(f"Counter bên trong: {counter}")

print(f"Counter ban đầu: {counter}")
increment()
increment()
print(f"Counter cuối cùng: {counter}")
```
**Output:**
```
Counter ban đầu: 0
Counter bên trong: 1
Counter bên trong: 2
Counter cuối cùng: 2
```

#### 2.4.3. Câu lệnh `nonlocal`

Câu lệnh `nonlocal` cho phép truy cập và sửa đổi biến của hàm bao ngoài (không phải global).

**Ví dụ:**
```python
def outer():
    x = 10
    
    def inner():
        nonlocal x
        x = 20
        print(f"inner: x = {x}")
    
    print(f"outer trước: x = {x}")
    inner()
    print(f"outer sau: x = {x}")

outer()
```
**Output:**
```
outer trước: x = 10
inner: x = 20
outer sau: x = 20
```

#### 2.4.4. Closure

Closure là hàm bên trong ghi nhớ biến từ phạm vi bao ngoài ngay cả khi hàm ngoài đã kết thúc.

**Ví dụ:**
```python
def make_multiplier(factor):
    """Tạo hàm nhân với hệ số factor"""
    def multiplier(x):
        return x * factor
    return multiplier

# Tạo các closure
double = make_multiplier(2)
triple = make_multiplier(3)

print(f"double(5) = {double(5)}")
print(f"triple(5) = {triple(5)}")

# Kiểm tra closure
print(f"double.__closure__: {double.__closure__}")
print(f"double.__closure__[0].cell_contents: {double.__closure__[0].cell_contents}")
```
**Output:**
```
double(5) = 10
triple(5) = 15
double.__closure__: (<cell at 0x...: int object at 0x...>,)
double.__closure__[0].cell_contents: 2
```

### 2.5. Hàm Lambda

Hàm lambda là hàm ẩn danh (anonymous) được định nghĩa bằng từ khóa `lambda`.

**Cú pháp:**
```python
lambda arguments: expression
```

**Ví dụ cơ bản:**
```python
# Hàm lambda tính bình phương
square = lambda x: x ** 2
print(f"Bình phương của 5: {square(5)}")

# Hàm lambda nhiều tham số
add = lambda a, b: a + b
print(f"Tổng 3 và 4: {add(3, 4)}")
```
**Output:**
```
Bình phương của 5: 25
Tổng 3 và 4: 7
```

#### 2.5.1. Sử dụng với `map()`

Hàm `map()` áp dụng hàm cho tất cả phần tử của iterable.

**Ví dụ:**
```python
# Sử dụng lambda với map
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(f"Danh sách bình phương: {squares}")
```
**Output:**
```
Danh sách bình phương: [1, 4, 9, 16, 25]
```

#### 2.5.2. Sử dụng với `filter()`

Hàm `filter()` lọc các phần tử thỏa mãn điều kiện.

**Ví dụ:**
```python
# Lọc số chẵn
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Số chẵn: {even_numbers}")
```
**Output:**
```
Số chẵn: [2, 4, 6, 8, 10]
```

#### 2.5.3. Sử dụng với `reduce()` (từ module functools)

Hàm `reduce()` tích lũy giá trị bằng cách áp dụng hàm lên các phần tử.

**Ví dụ:**
```python
from functools import reduce

# Tính tích các số
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f"Tích các số: {product}")

# Tìm số lớn nhất
max_number = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Số lớn nhất: {max_number}")
```
**Output:**
```
Tích các số: 120
Số lớn nhất: 5
```

### 2.6. Decorators

Decorator là hàm nhận một hàm khác làm đối số và mở rộng hoặc thay đổi hành vi của nó.

#### 2.6.1. Function Decorators

**Ví dụ cơ bản:**
```python
def my_decorator(func):
    def wrapper():
        print("Trước khi hàm chạy")
        func()
        print("Sau khi hàm chạy")
    return wrapper

@my_decorator
def say_hello():
    print("Xin chào!")

say_hello()
```
**Output:**
```
Trước khi hàm chạy
Xin chào!
Sau khi hàm chạy
```

**Decorator cho hàm có tham số:**
```python
def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print(f"Gọi hàm {func.__name__} với args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Hàm trả về: {result}")
        return result
    return wrapper

@decorator_with_args
def add(a, b):
    return a + b

result = add(3, 4)
print(f"Kết quả cuối: {result}")
```
**Output:**
```
Gọi hàm add với args=(3, 4), kwargs={}
Hàm trả về: 7
Kết quả cuối: 7
```

#### 2.6.2. Decorator với `functools.wraps`

Sử dụng `functools.wraps` để bảo toàn thông tin của hàm gốc.

**Ví dụ:**
```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Gọi {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    """Hàm ví dụ"""
    print("Hàm đang chạy")

example()
print(f"Tên hàm: {example.__name__}")
print(f"Docstring: {example.__doc__}")
```
**Output:**
```
Gọi example
Hàm đang chạy
Tên hàm: example
Docstring: Hàm ví dụ
```

#### 2.6.3. Decorator với tham số (Decorator Factory)

**Ví dụ:**
```python
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Xin chào {name}!")

greet("Alice")
```
**Output:**
```
Xin chào Alice!
Xin chào Alice!
Xin chào Alice!
```

#### 2.6.4. Nhiều decorator

Decorator được áp dụng theo thứ tự từ dưới lên.

**Ví dụ:**
```python
def decorator1(func):
    def wrapper():
        print("Decorator 1 trước")
        func()
        print("Decorator 1 sau")
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2 trước")
        func()
        print("Decorator 2 sau")
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Xin chào!")

say_hello()
```
**Output:**
```
Decorator 1 trước
Decorator 2 trước
Xin chào!
Decorator 2 sau
Decorator 1 sau
```

### 2.7. Generators và Iterators

#### 2.7.1. Iterator Protocol

Iterator là đối tượng có thể lặp, phải có phương thức `__iter__()` và `__next__()`.

**Ví dụ tạo iterator tùy chỉnh:**
```python
class CountDown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

# Sử dụng iterator
countdown = CountDown(3)
for number in countdown:
    print(number)
```
**Output:**
```
3
2
1
```

#### 2.7.2. Generator Functions

Generator là hàm sử dụng `yield` để trả về giá trị mà không kết thúc hàm.

**Ví dụ:**
```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Sử dụng generator
for number in countdown(3):
    print(number)

# Hoặc tạo generator object
gen = countdown(3)
print(next(gen))
print(next(gen))
print(next(gen))
```
**Output:**
```
3
2
1
3
2
1
```

#### 2.7.3. Generator Expressions

Tương tự list comprehension nhưng tạo generator thay vì list.

**Ví dụ:**
```python
# List comprehension
squares_list = [x**2 for x in range(5)]
print(f"List: {squares_list}, Kiểu: {type(squares_list)}")

# Generator expression
squares_gen = (x**2 for x in range(5))
print(f"Generator: {squares_gen}, Kiểu: {type(squares_gen)}")
print(f"Danh sách từ generator: {list(squares_gen)}")
```
**Output:**
```
List: [0, 1, 4, 9, 16], Kiểu: <class 'list'>
Generator: <generator object <genexpr> at 0x...>, Kiểu: <class 'generator'>
Danh sách từ generator: [0, 1, 4, 9, 16]
```

#### 2.7.4. Câu lệnh `yield from`

`yield from` ủy quyền cho generator khác.

**Ví dụ:**
```python
def chain(*iterables):
    for it in iterables:
        yield from it

result = list(chain([1, 2, 3], 'abc', (4, 5, 6)))
print(f"Kết quả: {result}")
```
**Output:**
```
Kết quả: [1, 2, 3, 'a', 'b', 'c', 4, 5, 6]
```

#### 2.7.5. Phương thức của Generator

Generator có các phương thức `send()`, `throw()`, `close()`.

**Ví dụ với `send()`:**
```python
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

acc = accumulator()
next(acc)  # Khởi tạo generator
print(f"Tổng: {acc.send(10)}")
print(f"Tổng: {acc.send(20)}")
print(f"Tổng: {acc.send(30)}")
acc.close()
```
**Output:**
```
Tổng: 10
Tổng: 30
Tổng: 60
```

### 2.8. Đệ quy

Đệ quy là kỹ thuật hàm gọi chính nó.

#### 2.8.1. Hàm đệ quy

**Ví dụ tính giai thừa:**
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"5! = {factorial(5)}")
print(f"10! = {factorial(10)}")
```
**Output:**
```
5! = 120
10! = 3628800
```

#### 2.8.2. Giới hạn đệ quy

Python có giới hạn độ sâu đệ quy mặc định là 1000.

**Ví dụ:**
```python
import sys

def recursive_func(depth):
    if depth <= 0:
        return 0
    return 1 + recursive_func(depth - 1)

# Kiểm tra giới hạn
print(f"Giới hạn đệ quy: {sys.getrecursionlimit()}")

# Thay đổi giới hạn
sys.setrecursionlimit(2000)
print(f"Giới hạn mới: {sys.getrecursionlimit()}")
```
**Output:**
```
Giới hạn đệ quy: 1000
Giới hạn mới: 2000
```

#### 2.8.3. Đệ quy đuôi (Tail Recursion)

Đệ quy đuôi là khi lời gọi đệ quy là thao tác cuối cùng của hàm.

**Ví dụ:**
```python
def factorial_tail(n, accumulator=1):
    if n <= 1:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)

print(f"5! = {factorial_tail(5)}")
```
**Output:**
```
5! = 120
```

### 2.9. Docstrings và Tài liệu

#### 2.9.1. Quy ước Docstring (PEP 257)

**Ví dụ:**
```python
def calculate_average(numbers):
    """
    Tính trung bình cộng của một danh sách số.
    
    Tham số:
    numbers (list): Danh sách các số
    
    Trả về:
    float: Giá trị trung bình
    
    Ném ra:
    ValueError: Nếu danh sách rỗng
    """
    if not numbers:
        raise ValueError("Danh sách không được rỗng")
    return sum(numbers) / len(numbers)
```

#### 2.9.2. Truy cập Docstring

**Ví dụ:**
```python
# Truy cập docstring
print(calculate_average.__doc__)

# Sử dụng help()
help(calculate_average)
```
**Output:**
```
    Tính trung bình cộng của một danh sách số.
    
    Tham số:
    numbers (list): Danh sách các số
    
    Trả về:
    float: Giá trị trung bình
    
    Ném ra:
    ValueError: Nếu danh sách rỗng
```

## 3. XỬ LÝ LỖI

### 3.1. Cơ bản về ngoại lệ

#### 3.1.1. Khối `try-except`

**Ví dụ:**
```python
try:
    result = 10 / 0
    print(f"Kết quả: {result}")
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")
```
**Output:**
```
Lỗi: Không thể chia cho 0!
```

#### 3.1.2. Nhiều mệnh đề `except`

**Ví dụ:**
```python
try:
    num = int("abc")
    result = 10 / num
except ValueError:
    print("Lỗi: Không thể chuyển đổi chuỗi thành số")
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0")
```
**Output:**
```
Lỗi: Không thể chuyển đổi chuỗi thành số
```

#### 3.1.3. Mệnh đề `except` chung

**Ví dụ:**
```python
try:
    file = open("khong_ton_tai.txt", "r")
except Exception as e:
    print(f"Đã xảy ra lỗi: {type(e).__name__}: {e}")
```
**Output:**
```
Đã xảy ra lỗi: FileNotFoundError: [Errno 2] No such file or directory: 'khong_ton_tai.txt'
```

### 3.2. Xử lý ngoại lệ nâng cao

#### 3.2.1. `try-except-else-finally`

**Ví dụ:**
```python
try:
    num = int("42")
    result = 100 / num
except (ValueError, ZeroDivisionError) as e:
    print(f"Lỗi: {type(e).__name__}")
else:
    print(f"Kết quả: {result}")
finally:
    print("Khối finally luôn được thực thi")
```
**Output:**
```
Kết quả: 2.380952380952381
Khối finally luôn được thực thi
```

#### 3.2.2. Khối `try` lồng nhau

**Ví dụ:**
```python
try:
    try:
        num = int("abc")
    except ValueError:
        print("Lỗi chuyển đổi trong khối bên trong")
        raise  # Ném lại ngoại lệ
except ValueError:
    print("Lỗi chuyển đổi trong khối bên ngoài")
```
**Output:**
```
Lỗi chuyển đổi trong khối bên trong
Lỗi chuyển đổi trong khối bên ngoài
```

### 3.3. Đối tượng ngoại lệ

#### 3.3.1. Cấu trúc phân cấp ngoại lệ

```
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 ├── GeneratorExit
 └── Exception
      ├── StopIteration
      ├── StopAsyncIteration
      ├── ArithmeticError
      │    ├── FloatingPointError
      │    ├── OverflowError
      │    └── ZeroDivisionError
      ├── AssertionError
      ├── AttributeError
      ├── BufferError
      ├── EOFError
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── MemoryError
      ├── NameError
      │    └── UnboundLocalError
      ├── OSError
      │    ├── BlockingIOError
      │    ├── ChildProcessError
      │    ├── ConnectionError
      │    │    ├── BrokenPipeError
      │    │    ├── ConnectionAbortedError
      │    │    ├── ConnectionRefusedError
      │    │    └── ConnectionResetError
      │    ├── FileExistsError
      │    ├── FileNotFoundError
      │    ├── InterruptedError
      │    ├── IsADirectoryError
      │    ├── NotADirectoryError
      │    ├── PermissionError
      │    ├── ProcessLookupError
      │    └── TimeoutError
      ├── ReferenceError
      ├── RuntimeError
      │    ├── NotImplementedError
      │    └── RecursionError
      ├── SyntaxError
      │    └── IndentationError
      │         └── TabError
      ├── SystemError
      ├── TypeError
      ├── ValueError
      │    └── UnicodeError
      │         ├── UnicodeDecodeError
      │         ├── UnicodeEncodeError
      │         └── UnicodeTranslateError
      └── Warning
           ├── DeprecationWarning
           ├── PendingDeprecationWarning
           ├── RuntimeWarning
           ├── SyntaxWarning
           ├── UserWarning
           ├── FutureWarning
           ├── ImportWarning
           ├── UnicodeWarning
           ├── BytesWarning
           └── ResourceWarning
```

#### 3.3.2. Thuộc tính của ngoại lệ

**Ví dụ:**
```python
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Loại ngoại lệ: {type(e).__name__}")
    print(f"Thông điệp: {e.args[0] if e.args else 'Không có thông điệp'}")
    print(f"args: {e.args}")
```
**Output:**
```
Loại ngoại lệ: ZeroDivisionError
Thông điệp: division by zero
args: ('division by zero',)
```

### 3.4. Ném ngoại lệ

#### 3.4.1. Câu lệnh `raise`

**Ví dụ:**
```python
def check_age(age):
    if age < 0:
        raise ValueError("Tuổi không thể âm")
    if age > 150:
        raise ValueError("Tuổi không thể lớn hơn 150")
    return f"Tuổi hợp lệ: {age}"

try:
    print(check_age(25))
    print(check_age(-5))
except ValueError as e:
    print(f"Lỗi: {e}")
```
**Output:**
```
Tuổi hợp lệ: 25
Lỗi: Tuổi không thể âm
```

#### 3.4.2. Chuỗi ngoại lệ (`raise ... from ...`)

**Ví dụ:**
```python
def process_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except OSError as e:
        raise RuntimeError(f"Không thể xử lý file {filename}") from e

try:
    process_file("khong_ton_tai.txt")
except RuntimeError as e:
    print(f"Lỗi: {e}")
    print(f"Nguyên nhân: {e.__cause__}")
```
**Output:**
```
Lỗi: Không thể xử lý file khong_ton_tai.txt
Nguyên nhân: [Errno 2] No such file or directory: 'khong_ton_tai.txt'
```

#### 3.4.3. Ném lại ngoại lệ

**Ví dụ:**
```python
def process_value(value):
    try:
        return int(value)
    except ValueError:
        print("Không thể chuyển đổi giá trị")
        raise  # Ném lại ngoại lệ gốc

try:
    process_value("abc")
except ValueError as e:
    print(f"Bắt được lỗi: {e}")
```
**Output:**
```
Không thể chuyển đổi giá trị
Bắt được lỗi: invalid literal for int() with base 10: 'abc'
```

### 3.5. Ngoại lệ tùy chỉnh

**Ví dụ:**
```python
class InvalidAgeError(Exception):
    """Ngoại lệ cho tuổi không hợp lệ"""
    def __init__(self, age, message="Tuổi không hợp lệ"):
        self.age = age
        self.message = message
        super().__init__(f"{message}: {age}")

def validate_age(age):
    if not (0 <= age <= 120):
        raise InvalidAgeError(age, "Tuổi phải trong khoảng 0-120")
    return age

try:
    validate_age(150)
except InvalidAgeError as e:
    print(f"Lỗi: {e}")
    print(f"Tuổi gây lỗi: {e.age}")
```
**Output:**
```
Lỗi: Tuổi phải trong khoảng 0-120: 150
Tuổi gây lỗi: 150
```

### 3.6. Nhóm ngoại lệ (Exception Groups) (Python 3.11+)

#### 3.6.1. Lớp `ExceptionGroup`

**Ví dụ:**
```python
# Python 3.11+
def validate_user(user_data):
    errors = []
    
    if not user_data.get('name'):
        errors.append(ValueError("Tên không được để trống"))
    
    if not user_data.get('email'):
        errors.append(ValueError("Email không được để trống"))
    
    if len(errors) > 1:
        raise ExceptionGroup("Nhiều lỗi xác thực", errors)
    elif errors:
        raise errors[0]

user_data = {'name': '', 'email': ''}
try:
    validate_user(user_data)
except* ValueError as e:
    print(f"Bắt được {len(e.exceptions)} lỗi ValueError")
    for error in e.exceptions:
        print(f"  - {error}")
```
**Output:**
```
Bắt được 2 lỗi ValueError
  - Tên không được để trống
  - Email không được để trống
```

#### 3.6.2. Cú pháp `except*`

**Ví dụ:**
```python
# Python 3.11+
def process_data(data):
    errors = []
    
    try:
        int(data['value'])
    except ValueError as e:
        errors.append(e)
    
    try:
        open(data['file'])
    except FileNotFoundError as e:
        errors.append(e)
    
    if errors:
        raise ExceptionGroup("Xử lý dữ liệu thất bại", errors)

data = {'value': 'abc', 'file': 'nonexistent.txt'}
try:
    process_data(data)
except* ValueError as e:
    print(f"Lỗi giá trị: {e.exceptions[0]}")
except* FileNotFoundError as e:
    print(f"Lỗi file: {e.exceptions[0]}")
```
**Output:**
```
Lỗi giá trị: invalid literal for int() with base 10: 'abc'
Lỗi file: [Errno 2] No such file or directory: 'nonexistent.txt'
```

### 3.7. Khẳng định (Assertions)

#### 3.7.1. Câu lệnh `assert`

**Ví dụ:**
```python
def calculate_discount(price, discount):
    assert price > 0, "Giá phải lớn hơn 0"
    assert 0 <= discount <= 1, "Chiết khấu phải trong khoảng 0-1"
    return price * (1 - discount)

# Đúng
print(f"Giá sau chiết khấu: {calculate_discount(100, 0.2)}")

# Sai
try:
    calculate_discount(-50, 0.2)
except AssertionError as e:
    print(f"Lỗi: {e}")
```
**Output:**
```
Giá sau chiết khấu: 80.0
Lỗi: Giá phải lớn hơn 0
```

### 3.8. Quản lý ngữ cảnh với ngoại lệ

#### 3.8.1. Câu lệnh `with`

**Ví dụ:**
```python
# Tự động đóng file
with open("test.txt", "w") as f:
    f.write("Hello, World!")

# File tự động đóng sau khối with
print(f"File đã đóng: {f.closed}")
```
**Output:**
```
File đã đóng: True
```

#### 3.8.2. Module `contextlib`

**Ví dụ với `suppress`:**
```python
from contextlib import suppress

# Bỏ qua lỗi cụ thể
with suppress(FileNotFoundError):
    with open("khong_ton_tai.txt") as f:
        print(f.read())
print("Tiếp tục chương trình...")
```
**Output:**
```
Tiếp tục chương trình...
```

**Ví dụ với `ExitStack`:**
```python
from contextlib import ExitStack

# Quản lý nhiều ngữ cảnh
with ExitStack() as stack:
    file1 = stack.enter_context(open("file1.txt", "w"))
    file2 = stack.enter_context(open("file2.txt", "w"))
    
    file1.write("Nội dung file 1")
    file2.write("Nội dung file 2")
    
print("Cả hai file đã đóng")
```

---

# PHẦN III: LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG

## 1. CLASSES VÀ OBJECTS

Lập trình hướng đối tượng (OOP) là mô hình lập trình sử dụng "đối tượng" để thiết kế ứng dụng. Mỗi đối tượng chứa dữ liệu (thuộc tính) và phương thức (hành vi).

### 1.1. Định nghĩa lớp

Lớp (class) là khuôn mẫu để tạo các đối tượng. Định nghĩa lớp sử dụng từ khóa `class`.

**Cú pháp:**
```python
class TênLớp:
    """Tài liệu về lớp (không bắt buộc)"""
    # Thuộc tính và phương thức
```

**Ví dụ đơn giản:**
```python
class Dog:
    """Lớp đại diện cho một con chó"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} đang sủa: Gâu gâu!"

# Tạo đối tượng từ lớp
dog1 = Dog("Buddy", 3)
print(dog1.bark())
```
**Output:**
```
Buddy đang sủa: Gâu gâu!
```

### 1.2. Tạo đối tượng (Khởi tạo)

Đối tượng (object) là thể hiện cụ thể của một lớp, được tạo bằng cách gọi tên lớp như một hàm.

**Ví dụ:**
```python
# Tạo nhiều đối tượng từ cùng lớp
dog2 = Dog("Max", 5)
dog3 = Dog("Lucy", 2)

print(f"{dog2.name} được {dog2.age} tuổi")
print(f"{dog3.name} được {dog3.age} tuổi")
```
**Output:**
```
Max được 5 tuổi
Lucy được 2 tuổi
```

### 1.3. Thuộc tính đối tượng

#### 1.3.1. Phương thức `__init__()`

Phương thức `__init__()` là phương thức khởi tạo, được gọi tự động khi tạo đối tượng mới. Tham số `self` tham chiếu đến đối tượng hiện tại.

**Ví dụ:**
```python
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []  # Thuộc tính mặc định
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

# Tạo và sử dụng đối tượng
student1 = Student("Alice", "S001")
student1.add_grade(8.5)
student1.add_grade(9.0)
print(f"{student1.name} có điểm trung bình: {student1.average_grade():.2f}")
```
**Output:**
```
Alice có điểm trung bình: 8.75
```

#### 1.3.2. Truy cập thuộc tính

Thuộc tính có thể được truy cập bằng ký hiệu dấu chấm (`.`).

**Ví dụ:**
```python
# Truy cập thuộc tính
print(f"Tên sinh viên: {student1.name}")
print(f"Mã sinh viên: {student1.student_id}")

# Truy cập thuộc tính động
attribute_name = "name"
print(f"Truy cập động: {getattr(student1, attribute_name)}")
```
**Output:**
```
Tên sinh viên: Alice
Mã sinh viên: S001
Truy cập động: Alice
```

#### 1.3.3. Sửa đổi thuộc tính

**Ví dụ:**
```python
# Sửa đổi thuộc tính trực tiếp
student1.name = "Alice Smith"
print(f"Tên mới: {student1.name}")

# Sửa đổi bằng setattr
setattr(student1, "student_id", "S001A")
print(f"Mã mới: {student1.student_id}")
```
**Output:**
```
Tên mới: Alice Smith
Mã mới: S001A
```

#### 1.3.4. Xóa thuộc tính (`del`)

**Ví dụ:**
```python
# Thêm thuộc tính mới
student1.email = "alice@example.com"
print(f"Email: {student1.email}")

# Xóa thuộc tính
del student1.email
# print(student1.email)  # Lỗi: AttributeError
```
**Output:**
```
Email: alice@example.com
```

### 1.4. Phương thức đối tượng

#### 1.4.1. Định nghĩa phương thức

Phương thức là hàm được định nghĩa bên trong lớp. Tham số đầu tiên luôn là `self`.

**Ví dụ:**
```python
class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, value):
        """Cộng thêm giá trị"""
        self.result += value
        return self
    
    def subtract(self, value):
        """Trừ giá trị"""
        self.result -= value
        return self
    
    def get_result(self):
        """Lấy kết quả hiện tại"""
        return self.result

# Sử dụng phương thức
calc = Calculator()
calc.add(10).subtract(3).add(5)
print(f"Kết quả: {calc.get_result()}")
```
**Output:**
```
Kết quả: 12
```

#### 1.4.2. Tham số `self`

`self` là tham chiếu đến đối tượng hiện tại, cho phép truy cập thuộc tính và phương thức của đối tượng.

**Ví dụ:**
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_to_origin(self):
        """Tính khoảng cách đến gốc tọa độ"""
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def move(self, dx, dy):
        """Di chuyển điểm"""
        self.x += dx
        self.y += dy
        return self

point = Point(3, 4)
print(f"Khoảng cách đến gốc: {point.distance_to_origin():.2f}")
point.move(1, -1)
print(f"Vị trí mới: ({point.x}, {point.y})")
```
**Output:**
```
Khoảng cách đến gốc: 5.00
Vị trí mới: (4, 3)
```

#### 1.4.3. Gọi phương thức

**Ví dụ:**
```python
# Gọi phương thức với cú pháp đối tượng.phương_thức()
point2 = Point(0, 0)
point2.move(5, 2)
distance = point2.distance_to_origin()

# Gọi phương thức với cú pháp lớp
# (phải truyền đối tượng làm tham số self)
distance2 = Point.distance_to_origin(point2)
print(f"Cả hai cách cho cùng kết quả: {distance} == {distance2}")
```
**Output:**
```
Cả hai cách cho cùng kết quả: 5.385164807134504 == 5.385164807134504
```

### 1.5. Phương thức đặc biệt (Magic/Dunder Methods)

#### 1.5.1. `__str__()` và `__repr__()`

- `__str__()`: Trả về chuỗi dễ đọc, dành cho người dùng
- `__repr__()`: Trả về chuỗi chính xác, dành cho nhà phát triển

**Bảng so sánh:**

| Đặc điểm | `__str__()` | `__repr__()` |
|----------|-------------|--------------|
| **Mục đích** | Đọc được (human-readable) | Chính xác (unambiguous) |
| **Được gọi khi** | `str(obj)`, `print(obj)` | `repr(obj)`, console interactive |
| **Mặc định** | Gọi `__repr__()` nếu không định nghĩa | Trả về `<__main__.ClassName object at 0x...>` |
| **Ví dụ** | `"Student: Alice"` | `"Student('Alice', 'S001')"` |

**Ví dụ:**
```python
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return f"'{self.title}' bởi {self.author}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

book = Book("Python Basics", "John Doe", 2023)
print(f"str: {str(book)}")
print(f"repr: {repr(book)}")
print(f"print: {book}")  # Gọi __str__
```
**Output:**
```
str: 'Python Basics' bởi John Doe
repr: Book('Python Basics', 'John Doe', 2023)
print: 'Python Basics' bởi John Doe
```

#### 1.5.2. Container Protocol

Các phương thức cho phép đối tượng hoạt động như container (list, dict, set).

**Ví dụ:**
```python
class Playlist:
    def __init__(self):
        self.songs = []
    
    def __len__(self):
        """Trả về số lượng bài hát"""
        return len(self.songs)
    
    def __getitem__(self, index):
        """Lấy bài hát theo chỉ số"""
        return self.songs[index]
    
    def __setitem__(self, index, value):
        """Gán bài hát tại chỉ số"""
        self.songs[index] = value
    
    def __delitem__(self, index):
        """Xóa bài hát tại chỉ số"""
        del self.songs[index]
    
    def add_song(self, song):
        self.songs.append(song)

playlist = Playlist()
playlist.add_song("Song 1")
playlist.add_song("Song 2")
playlist.add_song("Song 3")

print(f"Số bài hát: {len(playlist)}")
print(f"Bài hát đầu tiên: {playlist[0]}")
playlist[1] = "New Song"
print(f"Bài hát thứ 2: {playlist[1]}")
del playlist[2]
print(f"Số bài hát sau khi xóa: {len(playlist)}")
```
**Output:**
```
Số bài hát: 3
Bài hát đầu tiên: Song 1
Bài hát thứ 2: New Song
Số bài hát sau khi xóa: 2
```

#### 1.5.3. `__call__()` (Callable Objects)

Phương thức `__call__()` cho phép đối tượng được gọi như một hàm.

**Ví dụ:**
```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        """Gọi đối tượng như hàm"""
        return x * self.factor

# Tạo đối tượng có thể gọi được
double = Multiplier(2)
triple = Multiplier(3)

print(f"double(5) = {double(5)}")
print(f"triple(5) = {triple(5)}")
print(f"Đối tượng có thể gọi? {callable(double)}")
```
**Output:**
```
double(5) = 10
triple(5) = 15
Đối tượng có thể gọi? True
```

#### 1.5.4. `__del__()` (Destructor)

Phương thức `__del__()` được gọi khi đối tượng sắp bị hủy.

**Ví dụ:**
```python
class Resource:
    def __init__(self, name):
        self.name = name
        print(f"Tạo Resource: {self.name}")
    
    def __del__(self):
        print(f"Hủy Resource: {self.name}")

# Tạo và hủy đối tượng
res1 = Resource("A")
res2 = Resource("B")

print("Xóa res1...")
del res1
print("Kết thúc chương trình...")
# res2 sẽ tự động bị hủy khi chương trình kết thúc
```
**Output:**
```
Tạo Resource: A
Tạo Resource: B
Xóa res1...
Hủy Resource: A
Kết thúc chương trình...
Hủy Resource: B
```

## 2. CLASS ATTRIBUTES VÀ METHODS

### 2.1. Thuộc tính lớp

Thuộc tính lớp được chia sẻ bởi tất cả các đối tượng của lớp đó.

#### 2.1.1. Định nghĩa thuộc tính lớp

**Ví dụ:**
```python
class Employee:
    # Thuộc tính lớp
    company = "Tech Corp"
    employee_count = 0
    
    def __init__(self, name, salary):
        # Thuộc tính đối tượng
        self.name = name
        self.salary = salary
        # Truy cập và thay đổi thuộc tính lớp
        Employee.employee_count += 1
    
    def display_info(self):
        print(f"{self.name} làm việc tại {self.company}, lương: ${self.salary}")

# Tạo các đối tượng
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

emp1.display_info()
emp2.display_info()
print(f"Tổng số nhân viên: {Employee.employee_count}")
```
**Output:**
```
Alice làm việc tại Tech Corp, lương: $50000
Bob làm việc tại Tech Corp, lương: $60000
Tổng số nhân viên: 2
```

#### 2.1.2. Truy cập thuộc tính lớp

**Ví dụ:**
```python
# Truy cập từ lớp
print(f"Công ty: {Employee.company}")
print(f"Số nhân viên: {Employee.employee_count}")

# Truy cập từ đối tượng
print(f"emp1.company: {emp1.company}")

# Thay đổi thuộc tính lớp
Employee.company = "New Tech Corp"
print(f"Sau khi đổi: {emp1.company}, {emp2.company}")

# Thay đổi qua đối tượng (tạo thuộc tính đối tượng mới)
emp1.company = "Personal Company"
print(f"emp1.company: {emp1.company}")
print(f"emp2.company: {emp2.company}")
print(f"Employee.company: {Employee.company}")
```
**Output:**
```
Công ty: Tech Corp
Số nhân viên: 2
emp1.company: Tech Corp
Sau khi đổi: New Tech Corp, New Tech Corp
emp1.company: Personal Company
emp2.company: New Tech Corp
Employee.company: New Tech Corp
```

### 2.2. Phương thức lớp

Phương thức lớp nhận tham số `cls` thay vì `self` và có thể truy cập, sửa đổi thuộc tính lớp.

#### 2.2.1. Decorator `@classmethod`

**Ví dụ:**
```python
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    def display(self):
        return f"{self.day}/{self.month}/{self.year}"
    
    @classmethod
    def from_string(cls, date_string):
        """Tạo đối tượng Date từ chuỗi 'dd/mm/yyyy'"""
        day, month, year = map(int, date_string.split('/'))
        return cls(day, month, year)
    
    @classmethod
    def get_current_year(cls):
        """Trả về năm hiện tại (giả định)"""
        return 2024

# Sử dụng phương thức lớp
date1 = Date(25, 12, 2023)
date2 = Date.from_string("15/05/2024")

print(f"date1: {date1.display()}")
print(f"date2: {date2.display()}")
print(f"Năm hiện tại: {Date.get_current_year()}")
```
**Output:**
```
date1: 25/12/2023
date2: 15/05/2024
Năm hiện tại: 2024
```

#### 2.2.2. Tham số `cls`

`cls` tham chiếu đến lớp, tương tự như `self` tham chiếu đến đối tượng.

**Ví dụ:**
```python
class Product:
    discount_rate = 0.1  # 10% giảm giá
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @classmethod
    def set_discount_rate(cls, rate):
        """Thay đổi tỷ lệ giảm giá cho tất cả sản phẩm"""
        cls.discount_rate = rate
    
    @classmethod
    def create_with_discount(cls, name, price):
        """Tạo sản phẩm với giá đã giảm"""
        discounted_price = price * (1 - cls.discount_rate)
        return cls(name, discounted_price)
    
    def display(self):
        return f"{self.name}: ${self.price:.2f}"

# Sử dụng
product1 = Product("Laptop", 1000)
Product.set_discount_rate(0.2)  # 20% giảm giá
product2 = Product.create_with_discount("Tablet", 500)

print(f"product1: {product1.display()}")
print(f"product2: {product2.display()}")
print(f"Tỷ lệ giảm giá: {Product.discount_rate * 100}%")
```
**Output:**
```
product1: Laptop: $1000.00
product2: Tablet: $400.00
Tỷ lệ giảm giá: 20.0%
```

### 2.3. Phương thức tĩnh

Phương thức tĩnh không nhận `self` hay `cls`, hoạt động như hàm thông thường nhưng thuộc về không gian tên của lớp.

#### 2.3.1. Decorator `@staticmethod`

**Ví dụ:**
```python
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def is_even(number):
        return number % 2 == 0

# Sử dụng phương thức tĩnh
result1 = MathOperations.add(5, 3)
result2 = MathOperations.multiply(4, 6)
is_even = MathOperations.is_even(7)

print(f"5 + 3 = {result1}")
print(f"4 × 6 = {result2}")
print(f"7 chẵn? {is_even}")

# Cũng có thể gọi từ đối tượng
math = MathOperations()
print(f"Gọi từ đối tượng: {math.add(10, 20)}")
```
**Output:**
```
5 + 3 = 8
4 × 6 = 24
7 chẵn? False
Gọi từ đối tượng: 30
```

#### 2.3.2. Tình huống sử dụng

**Ví dụ thực tế:**
```python
class StringUtils:
    @staticmethod
    def is_palindrome(text):
        """Kiểm tra chuỗi đối xứng"""
        text = text.lower().replace(" ", "")
        return text == text[::-1]
    
    @staticmethod
    def count_vowels(text):
        """Đếm số nguyên âm"""
        vowels = "aeiouAEIOU"
        return sum(1 for char in text if char in vowels)
    
    @staticmethod
    def format_currency(amount):
        """Định dạng tiền tệ"""
        return f"${amount:,.2f}"

# Sử dụng
text1 = "A man a plan a canal Panama"
text2 = "Hello World"

print(f"'{text1}' đối xứng? {StringUtils.is_palindrome(text1)}")
print(f"'{text2}' đối xứng? {StringUtils.is_palindrome(text2)}")
print(f"Số nguyên âm trong '{text2}': {StringUtils.count_vowels(text2)}")
print(f"Định dạng tiền: {StringUtils.format_currency(1234567.89)}")
```
**Output:**
```
'A man a plan a canal Panama' đối xứng? True
'Hello World' đối xứng? False
Số nguyên âm trong 'Hello World': 3
Định dạng tiền: $1,234,567.89
```

#### 2.3.3. So sánh `@staticmethod` vs `@classmethod`

**Bảng so sánh:**

| Tiêu chí | `@staticmethod` | `@classmethod` |
|----------|----------------|----------------|
| **Tham số đầu tiên** | Không có tham số đặc biệt | `cls` (tham chiếu đến lớp) |
| **Truy cập thuộc tính lớp** | Không thể (trừ khi truy cập trực tiếp) | Có thể qua `cls` |
| **Truy cập thuộc tính đối tượng** | Không thể | Không thể (không có `self`) |
| **Tạo đối tượng mới** | Không thể (không biết lớp nào) | Có thể qua `cls()` |
| **Kế thừa** | Không bị ghi đè (không liên quan đến lớp) | Bị ghi đè (phụ thuộc vào lớp) |
| **Mục đích** | Tiện ích không phụ thuộc vào trạng thái | Hoạt động liên quan đến lớp |

**Ví dụ minh họa sự khác biệt:**
```python
class Parent:
    class_value = "Parent"
    
    @classmethod
    def class_method(cls):
        return f"Class method called from {cls.class_value}"
    
    @staticmethod
    def static_method():
        return "Static method called"

class Child(Parent):
    class_value = "Child"

# Gọi từ lớp cha
print(f"Parent.class_method(): {Parent.class_method()}")
print(f"Parent.static_method(): {Parent.static_method()}")

# Gọi từ lớp con
print(f"Child.class_method(): {Child.class_method()}")  # Sử dụng class_value của Child
print(f"Child.static_method(): {Child.static_method()}")  # Giống Parent
```
**Output:**
```
Parent.class_method(): Class method called from Parent
Parent.static_method(): Static method called
Child.class_method(): Class method called from Child
Child.static_method(): Static method called
```

## 3. TÍNH KẾ THỪA

Kế thừa cho phép một lớp (lớp con) kế thừa thuộc tính và phương thức từ lớp khác (lớp cha).

### 3.1. Kế thừa đơn

#### 3.1.1. Lớp cơ sở và lớp dẫn xuất

**Ví dụ:**
```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Một số âm thanh"
    
    def info(self):
        return f"{self.name} là một {self.species}"

class Dog(Animal):
    def __init__(self, name, breed):
        # Gọi phương thức __init__ của lớp cha
        super().__init__(name, "chó")
        self.breed = breed
    
    def make_sound(self):
        return "Gâu gâu!"
    
    def info(self):
        # Gọi phương thức của lớp cha và mở rộng
        return f"{super().info()}, giống {self.breed}"

# Sử dụng
animal = Animal("Thú", "động vật")
dog = Dog("Buddy", "Golden Retriever")

print(f"animal.info(): {animal.info()}")
print(f"animal.make_sound(): {animal.make_sound()}")
print(f"dog.info(): {dog.info()}")
print(f"dog.make_sound(): {dog.make_sound()}")
```
**Output:**
```
animal.info(): Thú là một động vật
animal.make_sound(): Một số âm thanh
dog.info(): Buddy là một chó, giống Golden Retriever
dog.make_sound(): Gâu gâu!
```

#### 3.1.2. Ghi đè phương thức

**Ví dụ:**
```python
class Shape:
    def __init__(self, color):
        self.color = color
    
    def area(self):
        return 0
    
    def perimeter(self):
        return 0
    
    def describe(self):
        return f"Hình màu {self.color}"

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):  # Ghi đè phương thức area
        return self.width * self.height
    
    def perimeter(self):  # Ghi đè phương thức perimeter
        return 2 * (self.width + self.height)
    
    def describe(self):  # Ghi đè và mở rộng
        base_description = super().describe()
        return f"{base_description}, hình chữ nhật {self.width}x{self.height}"

# Sử dụng
shape = Shape("đỏ")
rect = Rectangle("xanh", 5, 3)

print(f"shape.area(): {shape.area()}")
print(f"shape.describe(): {shape.describe()}")
print(f"rect.area(): {rect.area()}")
print(f"rect.perimeter(): {rect.perimeter()}")
print(f"rect.describe(): {rect.describe()}")
```
**Output:**
```
shape.area(): 0
shape.describe(): Hình màu đỏ
rect.area(): 15
rect.perimeter(): 16
rect.describe(): Hình màu xanh, hình chữ nhật 5x3
```

#### 3.1.3. Hàm `super()`

`super()` trả về đối tượng proxy cho lớp cha, cho phép truy cập các phương thức của lớp cha.

**Ví dụ:**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        return f"{self.name}, {self.age} tuổi"

class Employee(Person):
    def __init__(self, name, age, employee_id):
        # Cách 1: Gọi trực tiếp lớp cha
        # Person.__init__(self, name, age)
        
        # Cách 2: Sử dụng super() (khuyến khích)
        super().__init__(name, age)
        
        self.employee_id = employee_id
    
    def display(self):
        # Gọi phương thức display của lớp cha
        person_info = super().display()
        return f"{person_info}, ID: {self.employee_id}"

emp = Employee("Alice", 30, "E123")
print(emp.display())
```
**Output:**
```
Alice, 30 tuổi, ID: E123
```

### 3.2. Đa kế thừa

Python hỗ trợ đa kế thừa - một lớp có thể kế thừa từ nhiều lớp cha.

#### 3.2.1. Vấn đề hình thoi (Diamond Problem)

**Ví dụ:**
```python
class A:
    def method(self):
        return "A.method()"

class B(A):
    def method(self):
        return "B.method()"

class C(A):
    def method(self):
        return "C.method()"

class D(B, C):
    pass

d = D()
print(f"d.method(): {d.method()}")
print(f"Thứ tự độ phân giải phương thức (MRO): {[cls.__name__ for cls in D.__mro__]}")
```
**Output:**
```
d.method(): B.method()
Thứ tự độ phân giải phương thức (MRO): ['D', 'B', 'C', 'A', 'object']
```

#### 3.2.2. Thứ tự độ phân giải phương thức (MRO)

MRO xác định thứ tự tìm kiếm phương thức trong hệ thống phân cấp kế thừa. Python sử dụng thuật toán C3 Linearization.

**Ví dụ:**
```python
class X:
    def method(self):
        return "X.method()"

class Y:
    def method(self):
        return "Y.method()"

class Z(X, Y):
    pass

class W(Y, X):
    pass

z = Z()
w = W()

print(f"z.method(): {z.method()}")
print(f"Z MRO: {[cls.__name__ for cls in Z.__mro__]}")
print(f"w.method(): {w.method()}")
print(f"W MRO: {[cls.__name__ for cls in W.__mro__]}")

# Lỗi nếu thứ tự không nhất quán
class Inconsistent(Z, W):
    pass  # Lỗi: Cannot create a consistent method resolution order
```
**Output:**
```
z.method(): X.method()
Z MRO: ['Z', 'X', 'Y', 'object']
w.method(): Y.method()
W MRO: ['W', 'Y', 'X', 'object']
```

#### 3.2.3. `super()` với đa kế thừa

**Ví dụ:**
```python
class Base:
    def __init__(self):
        print("Base.__init__()")
        self.base_value = "base"

class Mixin1:
    def __init__(self):
        print("Mixin1.__init__()")
        self.mixin1_value = "mixin1"

class Mixin2:
    def __init__(self):
        print("Mixin2.__init__()")
        self.mixin2_value = "mixin2"

class Derived(Mixin1, Base, Mixin2):
    def __init__(self):
        print("Derived.__init__()")
        # Gọi __init__ của tất cả lớp cha theo MRO
        super().__init__()  # Gọi Mixin1.__init__
        super(Mixin1, self).__init__()  # Gọi Base.__init__
        super(Base, self).__init__()  # Gọi Mixin2.__init__
        self.derived_value = "derived"

d = Derived()
print(f"base_value: {d.base_value}")
print(f"mixin1_value: {d.mixin1_value}")
print(f"mixin2_value: {d.mixin2_value}")
print(f"derived_value: {d.derived_value}")
```
**Output:**
```
Derived.__init__()
Mixin1.__init__()
Base.__init__()
Mixin2.__init__()
base_value: base
mixin1_value: mixin1
mixin2_value: mixin2
derived_value: derived
```

### 3.3. Lớp cơ sở trừu tượng (ABCs)

ABCs định nghĩa giao diện mà các lớp con phải triển khai.

#### 3.3.1. Module `abc`

**Ví dụ:**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Tính diện tích"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Tính chu vi"""
        pass
    
    def describe(self):
        return "Đây là một hình"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Không thể tạo đối tượng từ lớp trừu tượng
# shape = Shape()  # Lỗi: TypeError

# Phải triển khai tất cả phương thức trừu tượng
circle = Circle(5)
print(f"Diện tích hình tròn: {circle.area():.2f}")
print(f"Chu vi hình tròn: {circle.perimeter():.2f}")
print(f"circle.describe(): {circle.describe()}")
```
**Output:**
```
Diện tích hình tròn: 78.54
Chu vi hình tròn: 31.42
circle.describe(): Đây là một hình
```

#### 3.3.2. Metaclass `ABCMeta`

**Ví dụ:**
```python
from abc import ABCMeta, abstractmethod

class Vehicle(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
    @property
    @abstractmethod
    def max_speed(self):
        pass

class Car(Vehicle):
    def __init__(self):
        self._max_speed = 200
    
    def start(self):
        return "Xe ô tô khởi động"
    
    def stop(self):
        return "Xe ô tô dừng lại"
    
    @property
    def max_speed(self):
        return self._max_speed

car = Car()
print(f"car.start(): {car.start()}")
print(f"car.max_speed: {car.max_speed} km/h")
```
**Output:**
```
car.start(): Xe ô tô khởi động
car.max_speed: 200 km/h
```

#### 3.3.3. So sánh ABC vs Interface

**Bảng so sánh:**

| Tiêu chí | Lớp trừu tượng (ABC) | Interface |
|----------|---------------------|-----------|
| **Định nghĩa** | Có thể chứa phương thức trừu tượng và cụ thể | Chỉ chứa phương thức trừu tượng |
| **Trạng thái** | Có thể có thuộc tính | Không có thuộc tính (thường) |
| **Mục đích** | Cung cấp triển khai một phần và yêu cầu triển khai phần còn lại | Chỉ định rõ hành vi mà lớp phải có |
| **Kế thừa đa** | Hỗ trợ kế thừa đa | Hỗ trợ implement đa interface |
| **Python** | Module `abc` | Không có interface riêng, dùng ABC thay thế |

### 3.4. Lớp Mixin

Mixin là lớp cung cấp chức năng cụ thể để các lớp khác kế thừa, nhưng không nhằm tạo đối tượng trực tiếp.

**Ví dụ:**
```python
class JSONSerializableMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)
    
    @classmethod
    def from_json(cls, json_str):
        import json
        data = json.loads(json_str)
        return cls(**data)

class XMLSerializableMixin:
    def to_xml(self):
        import xml.etree.ElementTree as ET
        root = ET.Element(self.__class__.__name__)
        for key, value in self.__dict__.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        return ET.tostring(root, encoding='unicode')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person, JSONSerializableMixin, XMLSerializableMixin):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

emp = Employee("Alice", 30, "E123")
print(f"JSON: {emp.to_json()}")
print(f"XML: {emp.to_xml()}")
```
**Output:**
```
JSON: {"name": "Alice", "age": 30, "employee_id": "E123"}
XML: <Employee><name>Alice</name><age>30</age><employee_id>E123</employee_id></Employee>
```

### 3.5. Protocols (Structural Subtyping)

Protocol định nghĩa giao diện dựa trên cấu trúc thay vì kế thừa rõ ràng.

#### 3.5.1. `typing.Protocol`

**Ví dụ:**
```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> None:
        ...
    
    def area(self) -> float:
        ...

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def draw(self):
        print("Vẽ hình tròn")
    
    def area(self):
        return 3.14159 * self.radius ** 2

class Square:
    def __init__(self, side):
        self.side = side
    
    def draw(self):
        print("Vẽ hình vuông")
    
    def area(self):
        return self.side ** 2

# Kiểm tra protocol
def process_drawable(obj: Drawable):
    obj.draw()
    print(f"Diện tích: {obj.area()}")

circle = Circle(5)
square = Square(4)

print(f"circle là Drawable? {isinstance(circle, Drawable)}")
print(f"square là Drawable? {isinstance(square, Drawable)}")

process_drawable(circle)
process_drawable(square)
```
**Output:**
```
circle là Drawable? True
square là Drawable? True
Vẽ hình tròn
Diện tích: 78.53975
Vẽ hình vuông
Diện tích: 16
```

## 4. ĐÓNG GÓI VÀ PROPERTIES

### 4.1. Bộ chỉ định truy cập

Python không có bộ chỉ định truy cập chính thức như private/protected, nhưng có quy ước đặt tên.

#### 4.1.1. Thành viên công khai (Public)

Có thể truy cập từ bất kỳ đâu.

**Ví dụ:**
```python
class PublicExample:
    def __init__(self):
        self.public_attribute = "Truy cập công khai"
    
    def public_method(self):
        return "Phương thức công khai"

obj = PublicExample()
print(f"Thuộc tính công khai: {obj.public_attribute}")
print(f"Phương thức công khai: {obj.public_method()}")
```
**Output:**
```
Thuộc tính công khai: Truy cập công khai
Phương thức công khai: Phương thức công khai
```

#### 4.1.2. Thành viên được bảo vệ (Protected)

Đặt tên với dấu gạch dưới `_` ở đầu. Chỉ là quy ước, vẫn có thể truy cập.

**Ví dụ:**
```python
class ProtectedExample:
    def __init__(self):
        self._protected_attribute = "Truy cập được bảo vệ"
    
    def _protected_method(self):
        return "Phương thức được bảo vệ"
    
    def access_protected(self):
        # Có thể truy cập protected từ bên trong lớp
        return f"{self._protected_attribute} - {self._protected_method()}"

obj = ProtectedExample()
print(f"Truy cập từ bên ngoài: {obj._protected_attribute}")  # Không nên
print(f"Truy cập đúng cách: {obj.access_protected()}")
```
**Output:**
```
Truy cập từ bên ngoài: Truy cập được bảo vệ
Truy cập đúng cách: Truy cập được bảo vệ - Phương thức được bảo vệ
```

#### 4.1.3. Thành viên riêng tư (Private)

Đặt tên với hai dấu gạch dưới `__` ở đầu. Python thực hiện name mangling.

**Ví dụ:**
```python
class PrivateExample:
    def __init__(self):
        self.__private_attribute = "Thuộc tính riêng tư"
        self.public_attribute = "Thuộc tính công khai"
    
    def __private_method(self):
        return "Phương thức riêng tư"
    
    def access_private(self):
        # Có thể truy cập private từ bên trong lớp
        return f"{self.__private_attribute} - {self.__private_method()}"
    
    def get_private_attribute(self):
        return self.__private_attribute

obj = PrivateExample()
print(f"Thuộc tính công khai: {obj.public_attribute}")

# Truy cập trực tiếp sẽ lỗi
# print(obj.__private_attribute)  # AttributeError
# print(obj.__private_method())   # AttributeError

print(f"Truy cập qua phương thức: {obj.access_private()}")
print(f"Truy cập qua getter: {obj.get_private_attribute()}")

# Name mangling: _ClassName__attribute
print(f"Truy cập qua name mangling: {obj._PrivateExample__private_attribute}")
```
**Output:**
```
Thuộc tính công khai: Thuộc tính công khai
Truy cập qua phương thức: Thuộc tính riêng tư - Phương thức riêng tư
Truy cập qua getter: Thuộc tính riêng tư
Truy cập qua name mangling: Thuộc tính riêng tư
```

#### 4.1.4. Name Mangling

Python biến đổi tên thuộc tính/method bắt đầu bằng `__` thành `_ClassName__attribute`.

**Ví dụ:**
```python
class Test:
    def __init__(self):
        self.__secret = "Bí mật"
        self._not_so_secret = "Không quá bí mật"
        self.public = "Công khai"

t = Test()

# Xem tất cả thuộc tính
print("Tất cả thuộc tính:")
for attr in dir(t):
    if not attr.startswith('__'):  # Bỏ các phương thức đặc biệt
        print(f"  {attr}")

print(f"\nTruy cập thuộc tính:")
print(f"  t.public: {t.public}")
print(f"  t._not_so_secret: {t._not_so_secret}")
print(f"  t._Test__secret: {t._Test__secret}")
```
**Output:**
```
Tất cả thuộc tính:
  _Test__secret
  _not_so_secret
  public

Truy cập thuộc tính:
  t.public: Công khai
  t._not_so_secret: Không quá bí mật
  t._Test__secret: Bí mật
```

### 4.2. Properties

Property cho phép định nghĩa getter, setter, deleter với cú pháp thuộc tính.

#### 4.2.1. Decorator `@property`

**Ví dụ cơ bản:**
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter cho celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter cho celsius với validation"""
        if value < -273.15:
            raise ValueError("Nhiệt độ không thể thấp hơn -273.15°C")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Property chỉ đọc (không có setter)"""
        return self._celsius * 9/5 + 32

temp = Temperature(25)
print(f"Ban đầu: {temp.celsius}°C = {temp.fahrenheit}°F")

# Sử dụng setter
temp.celsius = 30
print(f"Sau khi thay đổi: {temp.celsius}°C = {temp.fahrenheit}°F")

# Property chỉ đọc
try:
    temp.fahrenheit = 100  # Lỗi: không có setter
except AttributeError as e:
    print(f"Lỗi: {e}")

# Validation trong setter
try:
    temp.celsius = -300  # Lỗi: validation
except ValueError as e:
    print(f"Lỗi validation: {e}")
```
**Output:**
```
Ban đầu: 25°C = 77.0°F
Sau khi thay đổi: 30°C = 86.0°F
Lỗi: property 'fahrenheit' of 'Temperature' object has no setter
Lỗi validation: Nhiệt độ không thể thấp hơn -273.15°C
```

#### 4.2.2. Setter và Deleter

**Ví dụ đầy đủ:**
```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._email = None
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Tên không được để trống")
        self._name = value
    
    @name.deleter
    def name(self):
        print(f"Xóa tên của {self._name}")
        self._name = "Đã xóa"
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0 or value > 150:
            raise ValueError("Tuổi không hợp lệ")
        self._age = value
    
    @property
    def email(self):
        if self._email is None:
            return f"{self._name.lower()}@example.com"
        return self._email
    
    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Email không hợp lệ")
        self._email = value
    
    @email.deleter
    def email(self):
        print("Xóa email")
        self._email = None

person = Person("Alice", 30)
print(f"Tên: {person.name}, Tuổi: {person.age}")
print(f"Email mặc định: {person.email}")

person.name = "Alice Smith"
person.age = 31
person.email = "alice.smith@company.com"
print(f"Sau khi cập nhật: {person.name}, {person.age} tuổi, Email: {person.email}")

del person.email
print(f"Sau khi xóa email: {person.email}")

del person.name
print(f"Sau khi xóa tên: {person.name}")
```
**Output:**
```
Tên: Alice, Tuổi: 30
Email mặc định: alice@example.com
Sau khi cập nhật: Alice Smith, 31 tuổi, Email: alice.smith@company.com
Xóa email
Sau khi xóa email: alice.smith@example.com
Xóa tên của Alice Smith
Sau khi xóa tên: Đã xóa
```

#### 4.2.3. So sánh Property vs Getter/Setter

**Bảng so sánh:**

| Tiêu chí | Property | Getter/Setter thông thường |
|----------|----------|----------------------------|
| **Cú pháp** | `obj.property` | `obj.get_property()`, `obj.set_property(value)` |
| **Đọc tự nhiên** | Giống thuộc tính | Giống phương thức |
| **Bảo toàn API** | Có thể thay đổi implementation | Phải thay đổi cách gọi |
| **Validation** | Dễ dàng trong setter | Cần kiểm tra trong setter |
| **Tính toán** | Có thể tính toán khi truy cập | Phải tính toán trước hoặc trong getter |
| **Kế thừa** | Có thể ghi đè | Có thể ghi đè |

**Ví dụ minh họa:**
```python
# Cách tiếp cận với getter/setter thông thường
class CircleTraditional:
    def __init__(self, radius):
        self.set_radius(radius)
    
    def get_radius(self):
        return self._radius
    
    def set_radius(self, value):
        if value <= 0:
            raise ValueError("Bán kính phải dương")
        self._radius = value
    
    def get_area(self):
        return 3.14159 * self._radius ** 2

# Cách tiếp cận với property
class CircleProperty:
    def __init__(self, radius):
        self.radius = radius  # Sử dụng property setter
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Bán kính phải dương")
        self._radius = value
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2

# Sử dụng
circle1 = CircleTraditional(5)
circle2 = CircleProperty(5)

print(f"Traditional - Bán kính: {circle1.get_radius()}, Diện tích: {circle1.get_area():.2f}")
print(f"Property - Bán kính: {circle2.radius}, Diện tích: {circle2.area:.2f}")

# Cập nhật bán kính
circle1.set_radius(10)
circle2.radius = 10

print(f"\nSau khi thay đổi:")
print(f"Traditional - Bán kính: {circle1.get_radius()}, Diện tích: {circle1.get_area():.2f}")
print(f"Property - Bán kính: {circle2.radius}, Diện tích: {circle2.area:.2f}")
```
**Output:**
```
Traditional - Bán kính: 5, Diện tích: 78.54
Property - Bán kính: 5, Diện tích: 78.54

Sau khi thay đổi:
Traditional - Bán kính: 10, Diện tích: 314.16
Property - Bán kính: 10, Diện tích: 314.16
```

### 4.3. Descriptors

Descriptors là đối tượng định nghĩa các phương thức `__get__`, `__set__`, `__delete__` để kiểm soát truy cập thuộc tính.

#### 4.3.1. Descriptor Protocol

**Ví dụ cơ bản:**
```python
class ValidatedAttribute:
    """Descriptor cho thuộc tính được validate"""
    
    def __init__(self, name, validator):
        self.name = name
        self.validator = validator
    
    def __set_name__(self, owner, name):
        # Gọi khi descriptor được gán vào lớp
        self.name = name
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)
    
    def __set__(self, obj, value):
        # Validate trước khi gán
        self.validator(value)
        obj.__dict__[self.name] = value
    
    def __delete__(self, obj):
        del obj.__dict__[self.name]

# Validator functions
def validate_age(value):
    if not (0 <= value <= 150):
        raise ValueError("Tuổi phải từ 0 đến 150")

def validate_name(value):
    if not value or not value.strip():
        raise ValueError("Tên không được để trống")
    if len(value) > 50:
        raise ValueError("Tên quá dài")

class Person:
    # Sử dụng descriptors
    name = ValidatedAttribute("name", validate_name)
    age = ValidatedAttribute("age", validate_age)
    
    def __init__(self, name, age):
        self.name = name  # Gọi __set__
        self.age = age    # Gọi __set__
    
    def __str__(self):
        return f"{self.name}, {self.age} tuổi"

# Sử dụng
person = Person("Alice", 30)
print(f"person: {person}")

try:
    person.age = 200  # Validation sẽ thất bại
except ValueError as e:
    print(f"Lỗi tuổi: {e}")

try:
    person.name = ""  # Validation sẽ thất bại
except ValueError as e:
    print(f"Lỗi tên: {e}")
```
**Output:**
```
person: Alice, 30 tuổi
Lỗi tuổi: Tuổi phải từ 0 đến 150
Lỗi tên: Tên không được để trống
```

#### 4.3.2. `__set_name__()` (Python 3.6+)

**Ví dụ:**
```python
class AutoStorage:
    """Descriptor tự động lưu trữ giá trị"""
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, None)
    
    def __set__(self, obj, value):
        obj.__dict__[self.name] = value

class Validated(AutoStorage):
    """Descriptor với validation"""
    
    def __set__(self, obj, value):
        value = self.validate(obj, value)
        super().__set__(obj, value)
    
    def validate(self, obj, value):
        raise NotImplementedError("Phải triển khai phương thức validate")

class Quantity(Validated):
    """Descriptor cho số lượng dương"""
    
    def validate(self, obj, value):
        if value <= 0:
            raise ValueError(f"{self.name} phải lớn hơn 0")
        return value

class NonBlank(Validated):
    """Descriptor cho chuỗi không rỗng"""
    
    def validate(self, obj, value):
        value = value.strip()
        if not value:
            raise ValueError(f"{self.name} không được để trống")
        return value

class Product:
    name = NonBlank()
    price = Quantity()
    quantity = Quantity()
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_value(self):
        return self.price * self.quantity

# Sử dụng
product = Product("Laptop", 1000, 5)
print(f"Product: {product.name}, Giá: ${product.price}, Số lượng: {product.quantity}")
print(f"Tổng giá trị: ${product.total_value()}")

try:
    product.price = -100  # Lỗi validation
except ValueError as e:
    print(f"Lỗi: {e}")
```
**Output:**
```
Product: Laptop, Giá: $1000, Số lượng: 5
Tổng giá trị: $5000
Lỗi: price phải lớn hơn 0
```

#### 4.3.3. Data Descriptors vs Non-data Descriptors

**Bảng so sánh:**

| Loại Descriptor | Định nghĩa | Ưu tiên |
|----------------|------------|---------|
| **Data Descriptor** | Có phương thức `__set__` hoặc `__delete__` | Cao hơn `__dict__` |
| **Non-data Descriptor** | Chỉ có phương thức `__get__` | Thấp hơn `__dict__` |

**Ví dụ:**
```python
class DataDescriptor:
    """Data Descriptor (có __set__)"""
    def __get__(self, obj, objtype=None):
        print("DataDescriptor.__get__")
        return "giá trị từ descriptor"
    
    def __set__(self, obj, value):
        print("DataDescriptor.__set__")
        obj._value = value

class NonDataDescriptor:
    """Non-data Descriptor (chỉ có __get__)"""
    def __get__(self, obj, objtype=None):
        print("NonDataDescriptor.__get__")
        return "giá trị từ non-data descriptor"

class TestClass:
    data_desc = DataDescriptor()
    non_data_desc = NonDataDescriptor()

obj = TestClass()

print("=== Data Descriptor ===")
print(f"Truy cập: {obj.data_desc}")
obj.data_desc = "giá trị mới"
print(f"Sau khi gán: {obj.data_desc}")

print("\n=== Non-data Descriptor ===")
print(f"Truy cập: {obj.non_data_desc}")
obj.non_data_desc = "gán trực tiếp vào __dict__"
print(f"Sau khi gán: {obj.non_data_desc}")
print(f"Giá trị trong __dict__: {obj.__dict__.get('non_data_desc')}")
```
**Output:**
```
=== Data Descriptor ===
DataDescriptor.__get__
Truy cập: giá trị từ descriptor
DataDescriptor.__set__
DataDescriptor.__get__
Sau khi gán: giá trị từ descriptor

=== Non-data Descriptor ===
NonDataDescriptor.__get__
Truy cập: giá trị từ non-data descriptor
NonDataDescriptor.__get__
Sau khi gán: gán trực tiếp vào __dict__
Giá trị trong __dict__: gán trực tiếp vào __dict__
```

## 5. PHƯƠNG THỨC ĐẶC BIỆT NÂNG CAO

### 5.1. Tạo và khởi tạo đối tượng

#### 5.1.1. Phương thức `__new__()`

`__new__()` được gọi trước `__init__()`, trả về đối tượng mới.

**Ví dụ:**
```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print("Tạo instance mới")
            cls._instance = super().__new__(cls)
        else:
            print("Trả về instance đã tồn tại")
        return cls._instance
    
    def __init__(self):
        print("Khởi tạo Singleton")

# Test
print("Tạo s1:")
s1 = Singleton()

print("\nTạo s2:")
s2 = Singleton()

print(f"\ns1 is s2: {s1 is s2}")
```
**Output:**
```
Tạo s1:
Tạo instance mới
Khởi tạo Singleton

Tạo s2:
Trả về instance đã tồn tại
Khởi tạo Singleton

s1 is s2: True
```

#### 5.1.2. `__init_subclass__()` (Python 3.6+)

Được gọi khi lớp con được tạo.

**Ví dụ:**
```python
class PluginBase:
    plugins = []
    
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.plugins.append(cls)
        print(f"Đăng ký plugin: {cls.__name__}")

class PluginA(PluginBase):
    pass

class PluginB(PluginBase):
    pass

class PluginC(PluginA):  # Cũng được đăng ký
    pass

print(f"\nTất cả plugin: {[p.__name__ for p in PluginBase.plugins]}")
```
**Output:**
```
Đăng ký plugin: PluginA
Đăng ký plugin: PluginB
Đăng ký plugin: PluginC

Tất cả plugin: ['PluginA', 'PluginB', 'PluginC']
```

#### 5.1.3. `__subclasshook__()`

Cho phép ABC kiểm tra xem một lớp có phải là lớp con không dựa trên cấu trúc.

**Ví dụ:**
```python
from abc import ABC, abstractmethod

class Sized(ABC):
    @classmethod
    def __subclasshook__(cls, C):
        if cls is Sized:
            if any("__len__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented

# Không cần kế thừa trực tiếp
class MyClass:
    def __len__(self):
        return 42

print(f"MyClass là subclass của Sized? {issubclass(MyClass, Sized)}")
print(f"instance của MyClass là instance của Sized? {isinstance(MyClass(), Sized)}")
```
**Output:**
```
MyClass là subclass của Sized? True
instance của MyClass là instance của Sized? True
```

### 5.2. Truy cập thuộc tính

#### 5.2.1. `__getattr__()`, `__setattr__()`, `__delattr__()`

**Ví dụ:**
```python
class DynamicAttributes:
    def __init__(self):
        self._data = {}
    
    def __getattr__(self, name):
        """Được gọi khi thuộc tính không tồn tại"""
        print(f"__getattr__: {name}")
        if name in self._data:
            return self._data[name]
        raise AttributeError(f"'DynamicAttributes' object has no attribute '{name}'")
    
    def __setattr__(self, name, value):
        """Được gọi khi gán thuộc tính"""
        print(f"__setattr__: {name} = {value}")
        if name == "_data":
            # Gọi __setattr__ của object để tránh đệ quy
            super().__setattr__(name, value)
        else:
            self._data[name] = value
    
    def __delattr__(self, name):
        """Được gọi khi xóa thuộc tính"""
        print(f"__delattr__: {name}")
        if name in self._data:
            del self._data[name]
        else:
            super().__delattr__(name)

obj = DynamicAttributes()
obj.x = 10  # Gọi __setattr__
obj.y = 20  # Gọi __setattr__

print(f"\nobj.x: {obj.x}")  # Gọi __getattr__
print(f"obj.y: {obj.y}")    # Gọi __getattr__

del obj.x  # Gọi __delattr__
print(f"\nSau khi xóa, obj.x: ", end="")
try:
    print(obj.x)
except AttributeError as e:
    print(f"Lỗi: {e}")
```
**Output:**
```
__setattr__: _data = {}
__setattr__: x = 10
__setattr__: y = 20

__getattr__: x
obj.x: 10
__getattr__: y
obj.y: 20

__delattr__: x
__getattr__: x
Lỗi: 'DynamicAttributes' object has no attribute 'x'
```

#### 5.2.2. `__getattribute__()`

Được gọi cho MỌI truy cập thuộc tính.

**Ví dụ:**
```python
class LoggingAttributes:
    def __init__(self):
        self.x = 10
        self.y = 20
    
    def __getattribute__(self, name):
        print(f"__getattribute__: {name}")
        if name.startswith("private_"):
            raise AttributeError(f"Truy cập bị từ chối: {name}")
        return super().__getattribute__(name)
    
    def method(self):
        return "Đây là phương thức"

obj = LoggingAttributes()
print(f"obj.x: {obj.x}")
print(f"obj.y: {obj.y}")
print(f"obj.method(): {obj.method()}")

# Thêm thuộc tính
obj.private_secret = "bí mật"
try:
    print(f"obj.private_secret: {obj.private_secret}")
except AttributeError as e:
    print(f"Lỗi: {e}")
```
**Output:**
```
__getattribute__: x
obj.x: 10
__getattribute__: y
obj.y: 20
__getattribute__: method
__getattribute__: method
obj.method(): Đây là phương thức
__getattribute__: private_secret
Lỗi: Truy cập bị từ chối: private_secret
```

#### 5.2.3. `__dir__()`

Tùy chỉnh kết quả của hàm `dir()`.

**Ví dụ:**
```python
class CustomDir:
    def __init__(self):
        self.public_attr = "public"
        self._protected_attr = "protected"
        self.__private_attr = "private"
    
    def public_method(self):
        pass
    
    def _protected_method(self):
        pass
    
    def __private_method(self):
        pass
    
    def __dir__(self):
        # Chỉ hiển thị public attributes và methods
        default = super().__dir__()
        filtered = [item for item in default 
                   if not item.startswith('_') or item.startswith('__')]
        return sorted(filtered)

obj = CustomDir()
print("dir(obj):")
for item in dir(obj):
    print(f"  {item}")
```
**Output:**
```
dir(obj):
  __class__
  __delattr__
  __dict__
  __dir__
  __doc__
  __eq__
  __format__
  __ge__
  __getattribute__
  __gt__
  __hash__
  __init__
  __init_subclass__
  __le__
  __lt__
  __module__
  __ne__
  __new__
  __reduce__
  __reduce_ex__
  __repr__
  __setattr__
  __sizeof__
  __str__
  __subclasshook__
  __weakref__
  public_attr
  public_method
```

#### 5.2.4. `__slots__`

Tối ưu bộ nhớ bằng cách ngăn tạo `__dict__` cho đối tượng.

**Bảng so sánh `__slots__` vs `__dict__`:**

| Tiêu chí | Với `__slots__` | Với `__dict__` |
|----------|-----------------|----------------|
| **Bộ nhớ** | Tiết kiệm hơn | Tốn hơn |
| **Truy cập thuộc tính** | Nhanh hơn | Chậm hơn |
| **Thêm thuộc tính động** | Không thể | Có thể |
| **Kế thừa** | Phức tạp | Đơn giản |
| **Weak references** | Cần `__weakref__` | Hỗ trợ mặc định |

**Ví dụ:**
```python
import sys

class WithSlots:
    __slots__ = ('x', 'y', '__weakref__')  # __weakref__ để hỗ trợ weak references
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

class WithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# So sánh bộ nhớ
obj1 = WithSlots(1, 2)
obj2 = WithoutSlots(1, 2)

print(f"Kích thước WithSlots: {sys.getsizeof(obj1)} bytes")
print(f"Kích thước WithoutSlots: {sys.getsizeof(obj2)} bytes")

# Thêm thuộc tính động
obj2.z = 3  # OK
print(f"obj2.z: {obj2.z}")

try:
    obj1.z = 3  # Lỗi
except AttributeError as e:
    print(f"Không thể thêm z vào obj1: {e}")
```
**Output:**
```
Kích thước WithSlots: 56 bytes
Kích thước WithoutSlots: 56 bytes
obj2.z: 3
Không thể thêm z vào obj1: 'WithSlots' object has no attribute 'z'
```

### 5.3. Container Protocol

#### 5.3.1. `__len__()` và `__contains__()`

**Ví dụ:**
```python
class WordCollection:
    def __init__(self, words):
        self.words = set(words)
    
    def __len__(self):
        return len(self.words)
    
    def __contains__(self, word):
        return word in self.words
    
    def add(self, word):
        self.words.add(word)
        return self

collection = WordCollection(["apple", "banana", "cherry"])
print(f"Số từ: {len(collection)}")
print(f"'apple' trong collection? {'apple' in collection}")
print(f"'orange' trong collection? {'orange' in collection}")

collection.add("orange").add("grape")
print(f"\nSau khi thêm, số từ: {len(collection)}")
print(f"'orange' trong collection? {'orange' in collection}")
```
**Output:**
```
Số từ: 3
'apple' trong collection? True
'orange' trong collection? False

Sau khi thêm, số từ: 5
'orange' trong collection? True
```

#### 5.3.2. `__iter__()`, `__next__()`, `__reversed__()`

**Ví dụ:**
```python
class Countdown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        self.current = self.start
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value
    
    def __reversed__(self):
        # Trả về iterator đếm ngược (từ 1 đến start)
        class Countup:
            def __init__(self, n):
                self.n = n
                self.current = 1
            
            def __iter__(self):
                return self
            
            def __next__(self):
                if self.current > self.n:
                    raise StopIteration
                value = self.current
                self.current += 1
                return value
        
        return Countup(self.start)

# Sử dụng iterator
print("Countdown từ 5:")
for num in Countdown(5):
    print(num)

print("\nReversed (Countup từ 1 đến 5):")
for num in reversed(Countdown(5)):
    print(num)
```
**Output:**
```
Countdown từ 5:
5
4
3
2
1

Reversed (Countup từ 1 đến 5):
1
2
3
4
5
```

### 5.4. Giao thức số học

#### 5.4.1. Phương thức số học

**Ví dụ:**
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    # Các phép toán số học
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented
    
    def __rmul__(self, scalar):
        # Phép nhân bên phải: scalar * vector
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x / scalar, self.y / scalar)
        return NotImplemented
    
    # Phép toán tại chỗ (in-place)
    def __iadd__(self, other):
        if isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
            return self
        return NotImplemented
    
    # Phép toán matrix multiplication (Python 3.5+)
    def __matmul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y  # Dot product
        return NotImplemented

v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(f"v1 = {v1}, v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 3 = {v1 * 3}")
print(f"2 * v1 = {2 * v1}")
print(f"v1 / 2 = {v1 / 2}")
print(f"v1 @ v2 = {v1 @ v2}")  # Dot product

v1 += v2
print(f"Sau khi v1 += v2: {v1}")
```
**Output:**
```
v1 = Vector(2, 3), v2 = Vector(4, 5)
v1 + v2 = Vector(6, 8)
v1 - v2 = Vector(-2, -2)
v1 * 3 = Vector(6, 9)
2 * v1 = Vector(4, 6)
v1 / 2 = Vector(1.0, 1.5)
v1 @ v2 = 23
Sau khi v1 += v2: Vector(6, 8)
```

#### 5.4.2. Phương thức so sánh

**Ví dụ:**
```python
class Version:
    def __init__(self, major, minor, patch=0):
        self.major = major
        self.minor = minor
        self.patch = patch
    
    def __repr__(self):
        return f"Version({self.major}.{self.minor}.{self.patch})"
    
    def __eq__(self, other):
        if isinstance(other, Version):
            return (self.major, self.minor, self.patch) == (other.major, other.minor, other.patch)
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Version):
            return (self.major, self.minor, self.patch) < (other.major, other.minor, other.patch)
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, Version):
            return (self.major, self.minor, self.patch) <= (other.major, other.minor, other.patch)
        return NotImplemented
    
    # Các phương thức so sánh khác có thể dùng @functools.total_ordering

v1 = Version(1, 2, 3)
v2 = Version(1, 2, 3)
v3 = Version(1, 3, 0)

print(f"v1 = {v1}, v2 = {v2}, v3 = {v3}")
print(f"v1 == v2: {v1 == v2}")
print(f"v1 == v3: {v1 == v3}")
print(f"v1 < v3: {v1 < v3}")
print(f"v1 <= v2: {v1 <= v2}")
print(f"v1 > v3: {v1 > v3}")  # Tự động từ __lt__
```
**Output:**
```
v1 = Version(1.2.3), v2 = Version(1.2.3), v3 = Version(1.3.0)
v1 == v2: True
v1 == v3: False
v1 < v3: True
v1 <= v2: True
v1 > v3: False
```

#### 5.4.3. Phương thức đơn nguyên (Unary)

**Ví dụ:**
```python
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __repr__(self):
        return f"ComplexNumber({self.real}, {self.imag})"
    
    def __neg__(self):
        return ComplexNumber(-self.real, -self.imag)
    
    def __pos__(self):
        return ComplexNumber(+self.real, +self.imag)
    
    def __abs__(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5
    
    def __invert__(self):
        # Đảo ngược: a + bi -> -a - bi
        return ComplexNumber(-self.real, -self.imag)

c = ComplexNumber(3, 4)
print(f"c = {c}")
print(f"-c = {-c}")
print(f"+c = {+c}")
print(f"|c| = {abs(c)}")
print(f"~c = {~c}")
```
**Output:**
```
c = ComplexNumber(3, 4)
-c = ComplexNumber(-3, -4)
+c = ComplexNumber(3, 4)
|c| = 5.0
~c = ComplexNumber(-3, -4)
```

#### 5.4.4. Chuyển đổi kiểu

**Ví dụ:**
```python
class Measurement:
    def __init__(self, value, unit="cm"):
        self.value = value
        self.unit = unit
    
    def __repr__(self):
        return f"Measurement({self.value}, '{self.unit}')"
    
    def __int__(self):
        return int(self.value)
    
    def __float__(self):
        return float(self.value)
    
    def __complex__(self):
        return complex(self.value, 0)
    
    def __bool__(self):
        return bool(self.value)
    
    def __index__(self):
        # Dùng trong slicing và bin(), hex(), oct()
        return int(self.value)
    
    def __round__(self, ndigits=None):
        return Measurement(round(self.value, ndigits), self.unit)

m = Measurement(12.345, "cm")
print(f"m = {m}")
print(f"int(m) = {int(m)}")
print(f"float(m) = {float(m)}")
print(f"complex(m) = {complex(m)}")
print(f"bool(m) = {bool(m)}")
print(f"bin(int(m)) = {bin(m)}")
print(f"round(m, 1) = {round(m, 1)}")

# Sử dụng trong slicing
data = list(range(20))
print(f"\nSlicing với m: data[:m] = {data[:m]}")
```
**Output:**
```
m = Measurement(12.345, 'cm')
int(m) = 12
float(m) = 12.345
complex(m) = (12.345+0j)
bool(m) = True
bin(int(m)) = 0b1100
round(m, 1) = Measurement(12.3, 'cm')

Slicing với m: data[:m] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
```

### 5.5. Giao thức quản lý ngữ cảnh

#### 5.5.1. `__enter__()` và `__exit__()`

**Ví dụ:**
```python
class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"Mở file {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Đóng file {self.filename}")
        if self.file:
            self.file.close()
        
        # Xử lý ngoại lệ nếu có
        if exc_type is not None:
            print(f"Ngoại lệ: {exc_type.__name__}: {exc_value}")
        
        # Trả về True để ngăn ngoại lệ lan truyền
        return False  # Cho phép ngoại lệ lan truyền

# Sử dụng
print("Bắt đầu khối with:")
with FileHandler("test.txt", "w") as f:
    f.write("Hello, World!")
    print("Đã ghi vào file")

print("\nKhối with kết thúc")

# Với ngoại lệ
print("\n\nVới ngoại lệ:")
try:
    with FileHandler("test.txt", "r") as f:
        content = f.read()
        print(f"Nội dung: {content}")
        raise ValueError("Lỗi tùy ý trong khối with")
except ValueError as e:
    print(f"Bắt được ngoại lệ bên ngoài: {e}")
```
**Output:**
```
Bắt đầu khối with:
Mở file test.txt
Đã ghi vào file
Đóng file test.txt

Khối with kết thúc


Với ngoại lệ:
Mở file test.txt
Nội dung: Hello, World!
Đóng file test.txt
Ngoại lệ: ValueError: Lỗi tùy ý trong khối with
Bắt được ngoại lệ bên ngoài: Lỗi tùy ý trong khối with
```

### 5.6. Giao thức Pickle

#### 5.6.1. `__getstate__()` và `__setstate__()`

**Ví dụ:**
```python
import pickle

class Person:
    def __init__(self, name, age, password):
        self.name = name
        self.age = age
        self.password = password  # Không muốn pickle mật khẩu
    
    def __getstate__(self):
        # Xác định những gì sẽ được pickle
        state = self.__dict__.copy()
        # Không lưu password
        del state['password']
        return state
    
    def __setstate__(self, state):
        # Khôi phục trạng thái
        self.__dict__.update(state)
        # Khôi phục password mặc định
        self.password = None
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age}, password={'*' * len(self.password) if self.password else None})"

person = Person("Alice", 30, "secret123")
print(f"Trước khi pickle: {person}")

# Pickle
data = pickle.dumps(person)
print(f"\nKích thước dữ liệu pickle: {len(data)} bytes")

# Unpickle
restored = pickle.loads(data)
print(f"Sau khi unpickle: {restored}")
```
**Output:**
```
Trước khi pickle: Person(name='Alice', age=30, password=********)

Kích thước dữ liệu pickle: 62 bytes

Sau khi unpickle: Person(name='Alice', age=30, password=None)
```

### 5.7. Giao thức khớp mẫu (Pattern Matching Protocol) (Python 3.10+)

#### 5.7.1. `__match_args__`

**Ví dụ:**
```python
class Point:
    __match_args__ = ("x", "y")  # Xác định thứ tự các thuộc tính để khớp
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

def check_point(point):
    match point:
        case Point(0, 0):
            return "Gốc tọa độ"
        case Point(0, y):
            return f"Trên trục y tại y={y}"
        case Point(x, 0):
            return f"Trên trục x tại x={x}"
        case Point(x, y):
            return f"Điểm tại ({x}, {y})"

points = [Point(0, 0), Point(0, 5), Point(3, 0), Point(2, 4)]
for p in points:
    print(f"{p}: {check_point(p)}")
```
**Output:**
```
Point(0, 0): Gốc tọa độ
Point(0, 5): Trên trục y tại y=5
Point(3, 0): Trên trục x tại x=3
Point(2, 4): Điểm tại (2, 4)
```

## 6. DATA CLASSES VÀ ENUMS

### 6.1. Dataclasses (Python 3.7+)

Dataclass tự động tạo các phương thức đặc biệt như `__init__()`, `__repr__()`, `__eq__()`.

#### 6.1.1. Decorator `@dataclass`

**Ví dụ cơ bản:**
```python
from dataclasses import dataclass, field
from typing import List, ClassVar

@dataclass
class Person:
    name: str
    age: int = 0  # Giá trị mặc định
    emails: List[str] = field(default_factory=list)  # Sử dụng default_factory cho mutable
    # Biến lớp
    species: ClassVar[str] = "Homo sapiens"
    
    def greet(self):
        return f"Xin chào, tôi là {self.name}, {self.age} tuổi"

# Tạo đối tượng
person1 = Person("Alice", 30, ["alice@example.com"])
person2 = Person("Bob", 25)
person3 = Person("Alice", 30, ["alice@example.com"])

print(f"person1: {person1}")
print(f"person2: {person2}")
print(f"person1 == person3: {person1 == person3}")
print(f"person1.greet(): {person1.greet()}")
print(f"Loài: {Person.species}")
```
**Output:**
```
person1: Person(name='Alice', age=30, emails=['alice@example.com'])
person2: Person(name='Bob', age=25, emails=[])
person1 == person3: True
person1.greet(): Xin chào, tôi là Alice, 30 tuổi
Loài: Homo sapiens
```

#### 6.1.2. Tùy chọn dataclass

**Ví dụ:**
```python
from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)  # order: cho phép so sánh, frozen: immutable
class Product:
    name: str
    price: float
    quantity: int = 0
    tags: List[str] = field(default_factory=list, compare=False)  # Không dùng trong so sánh
    
    def total_value(self):
        return self.price * self.quantity

# Tạo sản phẩm
p1 = Product("Laptop", 1000, 5, ["tech", "electronics"])
p2 = Product("Tablet", 500, 10, ["tech", "portable"])
p3 = Product("Laptop", 1000, 5, ["different", "tags"])

print(f"p1: {p1}")
print(f"p2: {p2}")
print(f"p1 == p3: {p1 == p3}")  # So sánh bỏ qua tags
print(f"p1 < p2: {p1 < p2}")  # So sánh theo thứ tự khai báo trường

# frozen=True: không thể thay đổi
try:
    p1.price = 1200
except AttributeError as e:
    print(f"Không thể thay đổi (frozen): {e}")

print(f"\np1.total_value(): ${p1.total_value()}")
```
**Output:**
```
p1: Product(name='Laptop', price=1000, quantity=5, tags=['tech', 'electronics'])
p2: Product(name='Tablet', price=500, quantity=10, tags=['tech', 'portable'])
p1 == p3: True
p1 < p2: False
Không thể thay đổi (frozen): cannot assign to field 'price'

p1.total_value(): $5000
```

#### 6.1.3. `__post_init__()`

**Ví dụ:**
```python
@dataclass
class Student:
    name: str
    scores: List[int]
    average: float = field(init=False)  # Không khởi tạo trong __init__
    
    def __post_init__(self):
        # Được gọi sau __init__
        if not self.scores:
            self.average = 0.0
        else:
            self.average = sum(self.scores) / len(self.scores)
        
        # Validation
        if self.average < 0 or self.average > 10:
            raise ValueError("Điểm trung bình phải từ 0 đến 10")
    
    def grade(self):
        if self.average >= 8.5:
            return "Giỏi"
        elif self.average >= 7.0:
            return "Khá"
        elif self.average >= 5.5:
            return "Trung bình"
        else:
            return "Yếu"

student1 = Student("Alice", [8, 9, 7, 8, 9])
student2 = Student("Bob", [5, 6, 4, 5, 6])

print(f"{student1.name}: ĐTB = {student1.average:.2f}, Xếp loại: {student1.grade()}")
print(f"{student2.name}: ĐTB = {student2.average:.2f}, Xếp loại: {student2.grade()}")
```
**Output:**
```
Alice: ĐTB = 8.20, Xếp loại: Khá
Bob: ĐTB = 5.20, Xếp loại: Trung bình
```

#### 6.1.4. Kế thừa với Dataclasses

**Ví dụ:**
```python
@dataclass
class Vehicle:
    make: str
    model: str
    year: int
    
    def age(self, current_year=2024):
        return current_year - self.year

@dataclass
class Car(Vehicle):
    num_doors: int = 4
    fuel_type: str = "gasoline"

@dataclass
class Truck(Vehicle):
    payload_capacity: float  # tấn
    num_axles: int = 2

car = Car("Toyota", "Camry", 2020, 4, "hybrid")
truck = Truck("Ford", "F-150", 2019, 2.5, 2)

print(f"Car: {car.make} {car.model} ({car.year}), {car.num_doors} cửa, {car.age()} năm")
print(f"Truck: {truck.make} {truck.model} ({truck.year}), {truck.payload_capacity}t, {truck.age()} năm")
```
**Output:**
```
Car: Toyota Camry (2020), 4 cửa, 4 năm
Truck: Ford F-150 (2019), 2.5t, 5 năm
```

### 6.2. Enums (Python 3.4+)

Enum định nghĩa tập hợp các giá trị không đổi.

#### 6.2.1. `Enum` cơ bản

**Ví dụ:**
```python
from enum import Enum, auto

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4

class Day(Enum):
    MONDAY = auto()  # Tự động gán giá trị
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()

# Sử dụng
color = Color.RED
day = Day.MONDAY

print(f"color: {color}, value: {color.value}, name: {color.name}")
print(f"day: {day}, value: {day.value}")

# Lặp qua enum
print("\nTất cả màu:")
for c in Color:
    print(f"  {c.name}: {c.value}")

# So sánh
print(f"\nColor.RED is Color.RED: {Color.RED is Color.RED}")
print(f"Color.RED == Color.RED: {Color.RED == Color.RED}")
print(f"Color.RED == 1: {Color.RED == 1}")  # False
print(f"Color.RED.value == 1: {Color.RED.value == 1}")  # True
```
**Output:**
```
color: Color.RED, value: 1, name: RED
day: Day.MONDAY, value: 1

Tất cả màu:
  RED: 1
  GREEN: 2
  BLUE: 3
  YELLOW: 4

Color.RED is Color.RED: True
Color.RED == Color.RED: True
Color.RED == 1: False
Color.RED.value == 1: True
```

#### 6.2.2. `IntEnum`

`IntEnum` có thể so sánh với số nguyên.

**Ví dụ:**
```python
from enum import IntEnum

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

# So sánh với số nguyên
priority = Priority.HIGH
print(f"priority: {priority}, value: {priority.value}")
print(f"priority > 2: {priority > 2}")
print(f"priority == 3: {priority == 3}")

# Sử dụng trong điều kiện
if priority >= Priority.HIGH:
    print("Ưu tiên cao!")
```
**Output:**
```
priority: Priority.HIGH, value: 3
priority > 2: True
priority == 3: True
Ưu tiên cao!
```

#### 6.2.3. `Flag`

`Flag` cho phép kết hợp các giá trị với toán tử bitwise.

**Ví dụ:**
```python
from enum import Flag, auto

class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()
    DELETE = auto()
    
    # Các kết hợp phổ biến
    RW = READ | WRITE
    RWX = READ | WRITE | EXECUTE
    ALL = READ | WRITE | EXECUTE | DELETE

# Sử dụng
user_perms = Permission.READ | Permission.WRITE
admin_perms = Permission.ALL

print(f"user_perms: {user_perms}")
print(f"admin_perms: {admin_perms}")

# Kiểm tra quyền
print(f"\nuser có quyền READ? {Permission.READ in user_perms}")
print(f"user có quyền EXECUTE? {Permission.EXECUTE in user_perms}")
print(f"admin có quyền DELETE? {Permission.DELETE in admin_perms}")

# Thêm quyền
user_perms |= Permission.EXECUTE
print(f"\nuser_perms sau khi thêm EXECUTE: {user_perms}")

# Xóa quyền
user_perms &= ~Permission.WRITE
print(f"user_perms sau khi xóa WRITE: {user_perms}")
```
**Output:**
```
user_perms: Permission.READ|WRITE
admin_perms: Permission.ALL

user có quyền READ? True
user có quyền EXECUTE? False
admin có quyền DELETE? True

user_perms sau khi thêm EXECUTE: Permission.READ|WRITE|EXECUTE
user_perms sau khi xóa WRITE: Permission.READ|EXECUTE
```

## 7. METACLASSES

Metaclass là "class của class", kiểm soát cách lớp được tạo.

### 7.1. Cơ bản về Metaclass

#### 7.1.1. Lớp `type`

`type` là metaclass mặc định của tất cả lớp trong Python.

**Ví dụ:**
```python
# Tạo lớp thông thường
class MyClass:
    x = 10

# Kiểm tra
print(f"type(MyClass): {type(MyClass)}")
print(f"type(type): {type(type)}")

# type cũng có thể dùng để tạo lớp động
def method(self):
    return f"Hello from {self.name}"

# Tạo lớp với type
DynamicClass = type('DynamicClass', (object,), {
    'name': 'Dynamic',
    'greet': method,
    '__repr__': lambda self: f"DynamicClass(name={self.name})"
})

# Sử dụng
obj = DynamicClass()
print(f"obj: {obj}")
print(f"obj.greet(): {obj.greet()}")
```
**Output:**
```
type(MyClass): <class 'type'>
type(type): <class 'type'>
obj: DynamicClass(name=Dynamic)
obj.greet(): Hello from Dynamic
```

#### 7.1.2. Tạo lớp với `type()`

**Ví dụ chi tiết:**
```python
# Các hàm cho lớp
def __init__(self, name, value):
    self.name = name
    self.value = value

def display(self):
    return f"{self.name}: {self.value}"

# Tạo lớp động
CustomClass = type(
    'CustomClass',  # Tên lớp
    (object,),      # Base classes
    {               # Namespace
        '__init__': __init__,
        'display': display,
        'class_attribute': 'Tôi là thuộc tính lớp',
        '__repr__': lambda self: f"CustomClass({self.name}, {self.value})"
    }
)

# Sử dụng
obj1 = CustomClass("Đối tượng 1", 100)
obj2 = CustomClass("Đối tượng 2", 200)

print(f"obj1: {obj1}")
print(f"obj1.display(): {obj1.display()}")
print(f"CustomClass.class_attribute: {CustomClass.class_attribute}")
```
**Output:**
```
obj1: CustomClass(Đối tượng 1, 100)
obj1.display(): Đối tượng 1: 100
CustomClass.class_attribute: Tôi là thuộc tính lớp
```

### 7.2. Metaclass tùy chỉnh

#### 7.2.1. Kế thừa từ `type`

**Ví dụ:**
```python
class MyMeta(type):
    def __new__(mcs, name, bases, namespace):
        print(f"MyMeta.__new__: Tạo lớp {name}")
        
        # Thêm thuộc tính tự động
        if 'version' not in namespace:
            namespace['version'] = '1.0'
        
        # Đảm bảo có phương thức __repr__
        if '__repr__' not in namespace:
            namespace['__repr__'] = lambda self: f"{name}()"
        
        return super().__new__(mcs, name, bases, namespace)
    
    def __init__(cls, name, bases, namespace):
        print(f"MyMeta.__init__: Khởi tạo lớp {name}")
        super().__init__(name, bases, namespace)
    
    def __call__(cls, *args, **kwargs):
        print(f"MyMeta.__call__: Tạo instance của {cls.__name__}")
        instance = super().__call__(*args, **kwargs)
        # Thêm thuộc tính cho instance
        instance.created_at = "2024-01-01"
        return instance

class MyClass(metaclass=MyMeta):
    def __init__(self, value):
        self.value = value

print("\n--- Tạo đối tượng ---")
obj = MyClass(42)
print(f"obj: {obj}")
print(f"obj.value: {obj.value}")
print(f"obj.version: {obj.version}")
print(f"obj.created_at: {obj.created_at}")
```
**Output:**
```
MyMeta.__new__: Tạo lớp MyClass
MyMeta.__init__: Khởi tạo lớp MyClass

--- Tạo đối tượng ---
MyMeta.__call__: Tạo instance của MyClass
obj: MyClass()
obj.value: 42
obj.version: 1.0
obj.created_at: 2024-01-01
```

#### 7.2.2. Ghi đè `__new__()` và `__init__()`

**Ví dụ nâng cao:**
```python
class ValidationMeta(type):
    def __new__(mcs, name, bases, namespace):
        # Kiểm tra tên lớp không bắt đầu bằng số
        if name[0].isdigit():
            raise TypeError(f"Tên lớp không được bắt đầu bằng số: {name}")
        
        # Kiểm tra có phương thức validate không
        if 'validate' not in namespace:
            raise TypeError(f"Lớp {name} phải có phương thức validate")
        
        # Tự động thêm phương thức is_valid
        if 'is_valid' not in namespace:
            def is_valid(self):
                try:
                    self.validate()
                    return True
                except ValueError:
                    return False
            namespace['is_valid'] = is_valid
        
        return super().__new__(mcs, name, bases, namespace)

class Product(metaclass=ValidationMeta):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def validate(self):
        if not self.name:
            raise ValueError("Tên không được để trống")
        if self.price <= 0:
            raise ValueError("Giá phải lớn hơn 0")
    
    def __repr__(self):
        return f"Product({self.name}, ${self.price})"

# Sử dụng
good_product = Product("Laptop", 1000)
bad_product = Product("", -100)

print(f"good_product: {good_product}")
print(f"good_product.is_valid(): {good_product.is_valid()}")

print(f"\nbad_product: {bad_product}")
print(f"bad_product.is_valid(): {bad_product.is_valid()}")

# Lỗi khi định nghĩa lớp không hợp lệ
try:
    class 2InvalidClass(metaclass=ValidationMeta):
        pass
except TypeError as e:
    print(f"\nLỗi tạo lớp: {e}")
```
**Output:**
```
good_product: Product(Laptop, $1000)
good_product.is_valid(): True

bad_product: Product(, $-100)
bad_product.is_valid(): False

Lỗi tạo lớp: Tên lớp không được bắt đầu bằng số: 2InvalidClass
```

### 7.3. Trường hợp sử dụng Metaclass

#### 7.3.1. Mẫu Singleton

**Ví dụ:**
```python
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self, connection_string):
        self.connection_string = connection_string
        print(f"Kết nối đến: {connection_string}")
    
    def query(self, sql):
        return f"Thực hiện: {sql}"

# Tạo instances
db1 = Database("server1.example.com")
db2 = Database("server2.example.com")  # Vẫn dùng instance đầu tiên

print(f"db1 is db2: {db1 is db2}")
print(f"db1.connection_string: {db1.connection_string}")
print(f"db2.connection_string: {db2.connection_string}")
print(f"db1.query('SELECT * FROM users'): {db1.query('SELECT * FROM users')}")
```
**Output:**
```
Kết nối đến: server1.example.com
db1 is db2: True
db1.connection_string: server1.example.com
db2.connection_string: server1.example.com
db1.query('SELECT * FROM users'): Thực hiện: SELECT * FROM users
```

#### 7.3.2. Đăng ký lớp

**Ví dụ:**
```python
class PluginRegistryMeta(type):
    registry = {}
    
    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        
        # Đăng ký lớp nếu không phải lớp trừu tượng
        if not name.startswith('Abstract') and 'plugin_id' in namespace:
            plugin_id = namespace['plugin_id']
            mcs.registry[plugin_id] = cls
        
        return cls

class AbstractPlugin(metaclass=PluginRegistryMeta):
    plugin_id = None
    
    def execute(self):
        raise NotImplementedError

class ImageProcessor(AbstractPlugin):
    plugin_id = 'image_processor'
    
    def execute(self, data):
        return f"Xử lý ảnh: {data}"

class DataValidator(AbstractPlugin):
    plugin_id = 'data_validator'
    
    def execute(self, data):
        return f"Kiểm tra dữ liệu: {data}"

# Sử dụng registry
print("Các plugin đã đăng ký:")
for plugin_id, plugin_class in PluginRegistryMeta.registry.items():
    print(f"  {plugin_id}: {plugin_class.__name__}")

# Tạo và sử dụng plugin
data = "example_data"
for plugin_id, plugin_class in PluginRegistryMeta.registry.items():
    plugin = plugin_class()
    result = plugin.execute(data)
    print(f"\n{plugin_id}: {result}")
```
**Output:**
```
Các plugin đã đăng ký:
  image_processor: ImageProcessor
  data_validator: DataValidator

image_processor: Xử lý ảnh: example_data
data_validator: Kiểm tra dữ liệu: example_data
```

#### 7.3.3. Validation

**Ví dụ:**
```python
class ValidatedFieldsMeta(type):
    def __new__(mcs, name, bases, namespace):
        # Thu thập tất cả Field descriptors
        fields = {}
        for key, value in namespace.items():
            if isinstance(value, Field):
                fields[key] = value
                value.name = key
        
        # Tạo lớp
        cls = super().__new__(mcs, name, bases, namespace)
        
        # Lưu fields vào lớp
        cls._fields = fields
        
        return cls

class Field:
    def __init__(self, field_type, required=True, default=None):
        self.field_type = field_type
        self.required = required
        self.default = default
        self.name = None
    
    def validate(self, value):
        if value is None:
            if self.required:
                raise ValueError(f"{self.name} là bắt buộc")
            return self.default
        
        if not isinstance(value, self.field_type):
            raise TypeError(f"{self.name} phải là kiểu {self.field_type.__name__}")
        
        return value

class Model(metaclass=ValidatedFieldsMeta):
    def __init__(self, **kwargs):
        for field_name, field in self._fields.items():
            value = kwargs.get(field_name, field.default)
            validated_value = field.validate(value)
            setattr(self, field_name, validated_value)
    
    def __repr__(self):
        fields = ', '.join(f"{name}={getattr(self, name)}" 
                          for name in self._fields.keys())
        return f"{self.__class__.__name__}({fields})"

class User(Model):
    username = Field(str, required=True)
    email = Field(str, required=True)
    age = Field(int, required=False, default=18)
    score = Field(float, required=False, default=0.0)

# Sử dụng
try:
    user1 = User(username="alice", email="alice@example.com", age=25, score=95.5)
    print(f"user1: {user1}")
    
    user2 = User(username="bob", email="bob@example.com")
    print(f"user2: {user2}")
    
    user3 = User(username="charlie", email="charlie@example.com", age="not_a_number")
except (ValueError, TypeError) as e:
    print(f"Lỗi: {e}")
```
**Output:**
```
user1: User(username=alice, email=alice@example.com, age=25, score=95.5)
user2: User(username=bob, email=bob@example.com, age=18, score=0.0)
Lỗi: age phải là kiểu int
```

---

# PHẦN IV: XỬ LÝ FILE VÀ I/O OPERATIONS

## 1. FILE HANDLING

### 1.1. Opening Files

#### 1.1.1. `open()` Function
Hàm `open()` được sử dụng để mở một file và trả về một file object. Cú pháp cơ bản:
```python
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```
- `file`: Đường dẫn đến file (chuỗi) hoặc file descriptor (số nguyên).
- `mode`: Chế độ mở file (mặc định là `'r'` - đọc).
- `encoding`: Bảng mã ký tự (ví dụ: `'utf-8'`).

#### 1.1.2. File Modes (r, w, a, x, b, t, +, U)
Các chế độ mở file được kết hợp từ các ký tự sau:

| Mode | Mô tả |
|------|-------|
| `r` | Đọc (mặc định). Lỗi nếu file không tồn tại. |
| `w` | Ghi. Tạo file mới nếu chưa có, ghi đè nếu đã có. |
| `a` | Ghi tiếp (append). Ghi thêm vào cuối file, tạo mới nếu chưa có. |
| `x` | Tạo file mới để ghi. Lỗi nếu file đã tồn tại. |
| `b` | Chế độ nhị phân (binary). Kết hợp với `r`, `w`, `a`, `x`. |
| `t` | Chế độ văn bản (text, mặc định). |
| `+` | Mở để đọc và ghi. Kết hợp với `r`, `w`, `a`, `x`. |
| `U` | Universal newlines (không dùng từ Python 3). |

**Ví dụ kết hợp mode:**
- `'rb'`: Đọc file nhị phân.
- `'w+'`: Ghi và đọc, tạo mới hoặc ghi đè.
- `'a+b'`: Ghi tiếp và đọc file nhị phân.

#### 1.1.3. Encoding Parameter
Tham số `encoding` xác định bảng mã ký tự dùng để giải mã/ mã hóa nội dung file. Mặc định là `None` (hệ thống). Nên dùng `'utf-8'` để hỗ trợ Unicode.

**Ví dụ:**
```python
file = open('example.txt', mode='r', encoding='utf-8')
```

#### 1.1.4. Buffering Parameter
Tham số `buffering` điều khiển bộ đệm:
- `0`: Tắt bộ đệm (chỉ chế độ nhị phân).
- `1`: Bộ đệm dòng (chỉ chế độ văn bản).
- Số nguyên >1: Kích thước bộ đệm byte.
- `-1` (mặc định): Sử dụng kích thước bộ đệm mặc định hệ thống.

#### 1.1.5. Newline Handling
Tham số `newline` kiểm soát cách xử lý ký tự kết thúc dòng:
- `None` (mặc định): Ký tự kết thúc dòng được chuyển thành `'\n'` khi đọc; khi ghi, `'\n'` được chuyển thành ký tự kết thúc dòng mặc định hệ thống (`os.linesep`).
- `''`: Giữ nguyên ký tự kết thúc dòng.
- `'\n'`, `'\r'`, `'\r\n'`: Chỉ sử dụng ký tự này khi ghi.

### 1.2. Reading Files

#### 1.2.1. `read()`, `readline()`, `readlines()`
- `read(size=-1)`: Đọc toàn bộ nội dung (nếu `size` không chỉ định) hoặc `size` ký tự/byte.
- `readline(size=-1)`: Đọc một dòng (hoặc tối đa `size` ký tự).
- `readlines(hint=-1)`: Đọc tất cả các dòng và trả về danh sách. `hint` là số ký tự gần đúng cần đọc.

**Ví dụ:**
```python
# Giả sử file example.txt có nội dung:
# Line 1
# Line 2
# Line 3

with open('example.txt', 'r') as f:
    content = f.read()
    print(content)
```
```
Output:
Line 1
Line 2
Line 3
```

```python
with open('example.txt', 'r') as f:
    line = f.readline()
    print(line)
```
```
Output:
Line 1

```

```python
with open('example.txt', 'r') as f:
    lines = f.readlines()
    print(lines)
```
```
Output:
['Line 1\n', 'Line 2\n', 'Line 3\n']
```

#### 1.2.2. Iterating over Files
File object có thể được lặp trực tiếp để đọc từng dòng.

**Ví dụ:**
```python
with open('example.txt', 'r') as f:
    for line in f:
        print(line.strip())
```
```
Output:
Line 1
Line 2
Line 3
```

### 1.3. Writing Files

#### 1.3.1. `write()`, `writelines()`
- `write(string)`: Ghi chuỗi `string` vào file.
- `writelines(sequence)`: Ghi một chuỗi các chuỗi (như list) vào file. Không tự động thêm ký tự xuống dòng.

**Ví dụ:**
```python
with open('output.txt', 'w') as f:
    f.write('Hello, World!\n')
    f.writelines(['Line 1\n', 'Line 2\n'])
```

**Trạng thái file trước khi chạy:**
```
File output.txt chưa tồn tại.
```

**Trạng thái file sau khi chạy:**
```
Nội dung file output.txt:
Hello, World!
Line 1
Line 2
```

#### 1.3.2. `flush()`
Phương thức `flush()` buộc dữ liệu trong bộ đệm được ghi ngay vào file mà không cần đóng file.

**Ví dụ:**
```python
with open('flush_example.txt', 'w') as f:
    f.write('Before flush\n')
    f.flush()  # Dữ liệu được ghi ngay lập tức
    # Các thao tác khác
    f.write('After flush\n')
```

### 1.4. File Position

#### 1.4.1. `tell()`
Trả về vị trí hiện tại của con trỏ file (số byte tính từ đầu file).

**Ví dụ:**
```python
with open('example.txt', 'r') as f:
    print(f.tell())  # 0
    f.read(5)
    print(f.tell())  # 5
```

#### 1.4.2. `seek()`
Di chuyển con trỏ file đến vị trí chỉ định. Cú pháp: `seek(offset, whence=0)`
- `offset`: Số byte để di chuyển.
- `whence`:
  - `0` (mặc định): Tính từ đầu file.
  - `1`: Tính từ vị trí hiện tại.
  - `2`: Tính từ cuối file.

**Ví dụ:**
```python
with open('example.txt', 'r') as f:
    f.seek(5)  # Di chuyển đến byte thứ 5
    print(f.read(10))
```

### 1.5. Closing Files

#### 1.5.1. `close()`
Đóng file và giải phóng tài nguyên. Nên dùng `with` statement để tự động đóng.

#### 1.5.2. `with` Statement (Context Manager)
Đảm bảo file được đóng ngay cả khi có lỗi xảy ra.

**Ví dụ:**
```python
with open('example.txt', 'r') as f:
    data = f.read()
# File tự động đóng khi ra khỏi block with
```

## 2. DIRECTORY OPERATIONS

### 2.1. `os.path` Module
Module cung cấp các hàm để thao tác với đường dẫn.

#### 2.1.1. Path Manipulation
| Hàm | Mô tả |
|------|-------|
| `join(path, *paths)` | Nối các phần đường dẫn. |
| `split(path)` | Tách thành (thư mục, tên file). |
| `splitext(path)` | Tách thành (path không có đuôi, đuôi file). |
| `basename(path)` | Trả về tên file/thư mục cuối cùng. |
| `dirname(path)` | Trả về thư mục chứa path. |

**Ví dụ:**
```python
import os

path = '/home/user/file.txt'
print(os.path.join('/home', 'user', 'doc', 'file.txt'))
print(os.path.split(path))
print(os.path.splitext(path))
```
```
Output:
/home/user/doc/file.txt
('/home/user', 'file.txt')
('/home/user/file', '.txt')
```

#### 2.1.2. Path Information
| Hàm | Mô tả |
|------|-------|
| `exists(path)` | Kiểm tra path có tồn tại. |
| `isfile(path)` | Kiểm tra có phải file. |
| `isdir(path)` | Kiểm tra có phải thư mục. |
| `getsize(path)` | Trả về kích thước file (byte). |
| `getmtime(path)` | Thời gian sửa đổi lần cuối (timestamp). |

**Ví dụ:**
```python
import os

path = 'example.txt'
print(os.path.exists(path))
print(os.path.isfile(path))
print(os.path.getsize(path))
```
```
Output:
True
True
1024
```

### 2.2. `pathlib` Module (Python 3.4+)
Module hiện đại để xử lý đường dẫn với đối tượng `Path`.

#### 2.2.1. Path Object
Tạo đối tượng `Path` từ chuỗi đường dẫn.

**Ví dụ:**
```python
from pathlib import Path

p = Path('/home/user/file.txt')
print(p)
```
```
Output:
/home/user/file.txt
```

#### 2.2.2. Path Methods và Properties
| Phương thức/Thuộc tính | Mô tả |
|------------------------|-------|
| `p.name` | Tên file/thư mục cuối cùng. |
| `p.stem` | Tên file không có đuôi. |
| `p.suffix` | Đuôi file. |
| `p.parent` | Thư mục cha. |
| `p.exists()` | Kiểm tra tồn tại. |
| `p.is_file()` | Kiểm tra file. |
| `p.is_dir()` | Kiểm tra thư mục. |
| `p.read_text()` | Đọc nội dung file văn bản. |
| `p.write_text(data)` | Ghi chuỗi vào file. |

**Ví dụ:**
```python
from pathlib import Path

p = Path('example.txt')
print(p.name)
print(p.stem)
print(p.suffix)
print(p.parent)
print(p.exists())
```
```
Output:
example.txt
example
.txt
.
True
```

#### 2.2.3. `Path.glob()`, `Path.rglob()`
- `glob(pattern)`: Trả về iterator các file khớp pattern trong thư mục hiện tại.
- `rglob(pattern)`: Tìm đệ quy trong tất cả thư mục con.

**Ví dụ:**
```python
from pathlib import Path

# Tìm tất cả file .txt trong thư mục hiện tại
for file in Path('.').glob('*.txt'):
    print(file)

# Tìm đệ quy tất cả file .py
for file in Path('.').rglob('*.py'):
    print(file)
```

#### 2.2.4. So sánh `os.path` vs `pathlib`
| Tiêu chí | `os.path` | `pathlib` |
|----------|-----------|-----------|
| Phong cách | Hàm đơn lẻ | Đối tượng hướng đối tượng |
| Khả năng đọc | Tốt | Tốt hơn với method chain |
| Hỗ trợ | Có sẵn | Python 3.4+ |
| Thao tác phức tạp | Cần nhiều hàm kết hợp | Method phong phú |

### 2.3. `os` Module cho Directories

#### 2.3.1. `listdir()`, `mkdir()`, `makedirs()`
- `os.listdir(path)`: Trả về danh sách tên file/thư mục trong `path`.
- `os.mkdir(path, mode=0o777)`: Tạo thư mục.
- `os.makedirs(path, mode=0o777, exist_ok=False)`: Tạo thư mục đệ quy (cả thư mục cha). Nếu `exist_ok=True` thì không báo lỗi nếu thư mục đã tồn tại.

**Ví dụ:**
```python
import os

# Liệt kê nội dung thư mục hiện tại
print(os.listdir('.'))

# Tạo thư mục mới
os.mkdir('new_dir')

# Tạo cây thư mục
os.makedirs('dir1/dir2/dir3')
```

#### 2.3.2. `chdir()`, `getcwd()`
- `os.chdir(path)`: Thay đổi thư mục làm việc hiện tại.
- `os.getcwd()`: Trả về đường dẫn thư mục làm việc hiện tại.

**Ví dụ:**
```python
import os

print(os.getcwd())
os.chdir('..')
print(os.getcwd())
```

#### 2.3.3. `walk()`
Hàm `os.walk(top)` duyệt cây thư mục, trả về generator sinh ra tuple `(dirpath, dirnames, filenames)`.

**Ví dụ:**
```python
import os

for root, dirs, files in os.walk('.'):
    print(f'Root: {root}')
    print(f'Directories: {dirs}')
    print(f'Files: {files}')
```

### 2.4. File và Directory Management

#### 2.4.1. `remove()`, `unlink()`, `rmdir()`
- `os.remove(path)` hoặc `os.unlink(path)`: Xóa file.
- `os.rmdir(path)`: Xóa thư mục rỗng.

**Ví dụ:**
```python
import os

# Xóa file
os.remove('file_to_delete.txt')

# Xóa thư mục rỗng
os.rmdir('empty_dir')
```

#### 2.4.2. `rename()`, `move()`, `copy()`
- `os.rename(src, dst)`: Đổi tên hoặc di chuyển file/thư mục.
- `shutil.move(src, dst)`: Di chuyển file/thư mục (có thể khác ổ đĩa).
- `shutil.copy(src, dst)`: Sao chép file.

**Ví dụ:**
```python
import os
import shutil

# Đổi tên file
os.rename('old.txt', 'new.txt')

# Di chuyển file
shutil.move('source.txt', 'destination.txt')

# Sao chép file
shutil.copy('original.txt', 'copy.txt')
```

#### 2.4.3. `shutil` Module
Module cung cấp các hàm cấp cao để thao tác với file và thư mục.

| Hàm | Mô tả |
|------|-------|
| `shutil.copy(src, dst)` | Sao chép file. |
| `shutil.copy2(src, dst)` | Sao chép file và giữ metadata. |
| `shutil.copytree(src, dst)` | Sao chép toàn bộ thư mục. |
| `shutil.rmtree(path)` | Xóa thư mục và toàn bộ nội dung. |
| `shutil.move(src, dst)` | Di chuyển file/thư mục. |

**Ví dụ:**
```python
import shutil

# Sao chép thư mục
shutil.copytree('source_dir', 'dest_dir')

# Xóa thư mục và mọi thứ bên trong
shutil.rmtree('dir_to_delete')
```

## 3. DATA SERIALIZATION

### 3.1. JSON

#### 3.1.1. `json.dumps()`, `json.loads()`
- `json.dumps(obj)`: Chuyển đối tượng Python thành chuỗi JSON.
- `json.loads(s)`: Chuyển chuỗi JSON thành đối tượng Python.

**Ví dụ:**
```python
import json

data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# Serialize
json_string = json.dumps(data)
print(json_string)

# Deserialize
parsed_data = json.loads(json_string)
print(parsed_data['name'])
```
```
Output:
{"name": "John", "age": 30, "city": "New York"}
John
```

#### 3.1.2. `json.dump()`, `json.load()`
- `json.dump(obj, file)`: Ghi đối tượng Python vào file JSON.
- `json.load(file)`: Đọc file JSON thành đối tượng Python.

**Ví dụ:**
```python
import json

data = {'key': 'value'}

# Ghi vào file
with open('data.json', 'w') as f:
    json.dump(data, f)

# Đọc từ file
with open('data.json', 'r') as f:
    loaded_data = json.load(f)
    print(loaded_data)
```
```
Output:
{'key': 'value'}
```

#### 3.1.3. Custom `JSONEncoder` và `JSONDecoder`
Tạo lớp kế thừa để mã hóa/giải mã các kiểu dữ liệu tùy chỉnh.

**Ví dụ:**
```python
import json
from datetime import datetime

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

data = {'time': datetime.now()}
json_string = json.dumps(data, cls=CustomEncoder)
print(json_string)
```

### 3.2. CSV

#### 3.2.1. `csv.reader()`, `csv.writer()`
- `csv.reader(csvfile)`: Đọc file CSV, trả về iterator các dòng dưới dạng list.
- `csv.writer(csvfile)`: Tạo đối tượng ghi CSV.

**Ví dụ:**
```python
import csv

# Ghi file CSV
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Alice', 25])
    writer.writerow(['Bob', 30])

# Đọc file CSV
with open('output.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```
```
Output:
['Name', 'Age']
['Alice', '25']
['Bob', '30']
```

#### 3.2.2. `csv.DictReader()`, `csv.DictWriter()`
- `csv.DictReader(csvfile)`: Đọc file CSV thành dictionary với key là tên cột.
- `csv.DictWriter(csvfile, fieldnames)`: Ghi dictionary vào CSV.

**Ví dụ:**
```python
import csv

# Ghi với DictWriter
with open('dict_output.csv', 'w', newline='') as f:
    fieldnames = ['name', 'age']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': 'Alice', 'age': 25})
    writer.writerow({'name': 'Bob', 'age': 30})

# Đọc với DictReader
with open('dict_output.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
```
```
Output:
{'name': 'Alice', 'age': '25'}
{'name': 'Bob', 'age': '30'}
```

#### 3.2.3. Dialects và Quoting (bao gồm `Sniffer`)
Dialect định nghĩa các tham số định dạng CSV (dấu phân cách, ký tự trích dẫn, v.v.). `csv.Sniffer` tự động phát hiện dialect.

**Ví dụ:**
```python
import csv

# Tạo dialect tùy chỉnh
csv.register_dialect('my_dialect', delimiter='|', quoting=csv.QUOTE_ALL)

with open('custom.csv', 'w', newline='') as f:
    writer = csv.writer(f, dialect='my_dialect')
    writer.writerow(['a', 'b', 'c'])

# Sniffer
with open('custom.csv', 'r') as f:
    sample = f.read(1024)
    sniffer = csv.Sniffer()
    dialect = sniffer.sniff(sample)
    f.seek(0)
    reader = csv.reader(f, dialect=dialect)
    for row in reader:
        print(row)
```

### 3.3. Pickle

#### 3.3.1. `pickle.dumps()`, `pickle.loads()`
- `pickle.dumps(obj)`: Serialize đối tượng thành bytes.
- `pickle.loads(bytes)`: Deserialize bytes thành đối tượng.

**Ví dụ:**
```python
import pickle

data = {'a': 1, 'b': 2}

# Serialize
pickled = pickle.dumps(data)
print(pickled)

# Deserialize
unpickled = pickle.loads(pickled)
print(unpickled)
```
```
Output:
b'\x80\x04\x95\x11\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x01a\x94K\x01\x8c\x01b\x94K\x02u.'
{'a': 1, 'b': 2}
```

#### 3.3.2. `pickle.dump()`, `pickle.load()`
- `pickle.dump(obj, file)`: Ghi đối tượng vào file.
- `pickle.load(file)`: Đọc đối tượng từ file.

**Ví dụ:**
```python
import pickle

data = [1, 2, 3]

# Ghi vào file
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

# Đọc từ file
with open('data.pkl', 'rb') as f:
    loaded = pickle.load(f)
    print(loaded)
```
```
Output:
[1, 2, 3]
```

#### 3.3.3. Security Considerations
Pickle không an toàn khi tải dữ liệu từ nguồn không tin cậy vì có thể thực thi mã tùy ý. Chỉ dùng pickle với dữ liệu đáng tin.

### 3.4. Other Formats

#### 3.4.1. XML (`xml.etree.ElementTree`)
Module để phân tích và tạo XML.

**Ví dụ:**
```python
import xml.etree.ElementTree as ET

# Tạo XML
root = ET.Element('root')
child = ET.SubElement(root, 'child')
child.text = 'Some text'

tree = ET.ElementTree(root)
tree.write('example.xml')

# Đọc XML
tree = ET.parse('example.xml')
root = tree.getroot()
print(root.tag)
for elem in root:
    print(elem.tag, elem.text)
```
```
Output:
root
child Some text
```

#### 3.4.2. YAML (`PyYAML`)
Cần cài đặt thư viện `pyyaml`. Hỗ trợ serialization với cú pháp thân thiện.

**Ví dụ:**
```python
import yaml

data = {'name': 'John', 'items': [1, 2, 3]}

# Ghi YAML
with open('data.yaml', 'w') as f:
    yaml.dump(data, f)

# Đọc YAML
with open('data.yaml', 'r') as f:
    loaded = yaml.safe_load(f)
    print(loaded)
```

#### 3.4.3. TOML (`tomllib`) (Python 3.11+)
Module chuẩn từ Python 3.11 để đọc TOML. Ghi cần `tomli-w`.

**Ví dụ:**
```python
import tomllib

# Đọc TOML (Python 3.11+)
with open('config.toml', 'rb') as f:
    data = tomllib.load(f)
    print(data)
```

## 4. INPUT/OUTPUT NÂNG CAO

### 4.1. Standard Streams (`stdin`, `stdout`, `stderr`)
Ba luồng tiêu chuẩn:
- `sys.stdin`: Luồng đầu vào (bàn phím).
- `sys.stdout`: Luồng đầu ra (màn hình).
- `sys.stderr`: Luồng lỗi.

**Ví dụ:**
```python
import sys

sys.stdout.write('Enter your name: ')
name = sys.stdin.readline().strip()
sys.stderr.write('Debug: Name entered\n')
print(f'Hello, {name}')
```

### 4.2. Formatted Output

#### 4.2.1. `print()` Function (`sep`, `end`, `file`, `flush`)
- `sep`: Chuỗi phân cách giữa các đối số (mặc định là khoảng trắng).
- `end`: Chuỗi kết thúc (mặc định `'\n'`).
- `file`: Đối tượng file để ghi (mặc định `sys.stdout`).
- `flush`: Có xả bộ đệm ngay (mặc định `False`).

**Ví dụ:**
```python
print('Hello', 'World', sep=', ', end='!\n')
print('Error', file=sys.stderr, flush=True)
```
```
Output:
Hello, World!
Error
```

#### 4.2.2. `format()` Function
Định dạng chuỗi với các placeholder `{}`.

**Ví dụ:**
```python
text = 'World'
formatted = 'Hello {}'.format(text)
print(formatted)

# Với số
num = 3.14159
print('Value: {:.2f}'.format(num))
```
```
Output:
Hello World
Value: 3.14
```

#### 4.2.3. Format Specification Mini-Language
Cú pháp định dạng bên trong `{}`:
- `:f` - số thực.
- `:d` - số nguyên.
- `:s` - chuỗi.
- `:<` - căn trái, `:>` căn phải, `:^` căn giữa.
- `:x` - số hex.

**Ví dụ:**
```python
print('{:10}'.format('left'))   # Căn trái
print('{:>10}'.format('right')) # Căn phải
print('{:^10}'.format('center')) # Căn giữa
print('{:.2f}'.format(3.14159)) # 2 chữ số thập phân
print('{:x}'.format(255))       # hex
```
```
Output:
left      
     right
  center  
3.14
ff
```

### 4.3. Command Line Arguments

#### 4.3.1. `sys.argv`
Danh sách các đối số dòng lệnh. `sys.argv[0]` là tên script.

**Ví dụ script `args.py`:**
```python
import sys
print('Number of arguments:', len(sys.argv))
for i, arg in enumerate(sys.argv):
    print(f'Argument {i}: {arg}')
```
```
Chạy: python args.py arg1 arg2
Output:
Number of arguments: 3
Argument 0: args.py
Argument 1: arg1
Argument 2: arg2
```

#### 4.3.2. `argparse` Module
Module mạnh mẽ để phân tích đối số dòng lệnh.

##### 4.3.2.1. `ArgumentParser`
Tạo parser và thêm các đối số.

**Ví dụ:**
```python
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
```
```
Chạy: python script.py 1 2 3 4 --sum
Output:
10
```

##### 4.3.2.2. Positional và Optional Arguments
- Positional: Bắt buộc, không có tiền tố.
- Optional: Bắt đầu với `--` hoặc `-`.

**Ví dụ:**
```python
parser = argparse.ArgumentParser()
parser.add_argument('pos', help='positional argument')
parser.add_argument('--opt', help='optional argument')
args = parser.parse_args()
```

##### 4.3.2.3. Subparsers
Cho phép tạo các lệnh con.

**Ví dụ:**
```python
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='command')

parser_a = subparsers.add_parser('a', help='command a')
parser_a.add_argument('--foo', type=int)

parser_b = subparsers.add_parser('b', help='command b')
parser_b.add_argument('--bar')

args = parser.parse_args()
```

##### 4.3.2.4. Argument Groups
Nhóm các đối số lại để hiển thị đẹp hơn.

**Ví dụ:**
```python
parser = argparse.ArgumentParser()
group1 = parser.add_argument_group('group1')
group1.add_argument('--foo', help='foo help')
group2 = parser.add_argument_group('group2')
group2.add_argument('--bar', help='bar help')
```

##### 4.3.2.5. `FileType`, `Action` Classes
- `FileType`: Tự động mở file.
- `Action`: Lớp cơ sở để tạo hành động tùy chỉnh.

**Ví dụ:**
```python
parser.add_argument('--file', type=argparse.FileType('r'))
```

### 4.4. Environment Variables

#### 4.4.1. `os.environ`
Dictionary chứa các biến môi trường.

**Ví dụ:**
```python
import os

print(os.environ['PATH'])  # In biến PATH

# Duyệt qua tất cả
for key, value in os.environ.items():
    print(f'{key}: {value}')
```

#### 4.4.2. `os.getenv()`, `os.putenv()`
- `os.getenv(key, default=None)`: Lấy giá trị biến môi trường.
- `os.putenv(key, value)`: Đặt biến môi trường (không ảnh hưởng đến `os.environ`).

**Ví dụ:**
```python
import os

path = os.getenv('PATH', '')
print(path)

os.putenv('MY_VAR', 'value')
```

---

# PHẦN V: MODULES, PACKAGES VÀ STANDARD LIBRARY

## 1. MODULES VÀ PACKAGES

### 1.1. Modules

#### 1.1.1. Creating Modules
Module là file Python (`.py`) chứa code có thể tái sử dụng.

**Ví dụ tạo module `mymodule.py`:**
```python
def greet(name):
    return f'Hello, {name}!'

pi = 3.14159
```

#### 1.1.2. Importing Modules
Có nhiều cách import:
- `import module`
- `from module import name`
- `from module import *` (không khuyến khích)

**Ví dụ:**
```python
import mymodule
print(mymodule.greet('Alice'))

from mymodule import pi
print(pi)
```

#### 1.1.3. Module Attributes (`__name__`, `__file__`, `__doc__`, v.v.)
- `__name__`: Tên module. Nếu chạy trực tiếp, giá trị là `'__main__'`.
- `__file__`: Đường dẫn file module.
- `__doc__`: Chuỗi tài liệu của module.

**Ví dụ:**
```python
# Trong mymodule.py
print(__name__)
print(__file__)
```

#### 1.1.4. Reloading Modules (`importlib.reload()`)
Tải lại module đã import (hữu ích khi phát triển).

**Ví dụ:**
```python
import importlib
import mymodule
importlib.reload(mymodule)
```

### 1.2. Packages

#### 1.2.1. Package Structure (bao gồm cả data directory)
Package là thư mục chứa file `__init__.py` và các module con.

Cấu trúc:
```
mypackage/
    __init__.py
    module1.py
    module2.py
    data/
        datafile.txt
```

#### 1.2.2. `__init__.py` (bao gồm `__all__` và `__version__`)
File `__init__.py` có thể rỗng hoặc chứa code khởi tạo package.

**Ví dụ `__init__.py`:**
```python
__version__ = '1.0'
__all__ = ['module1', 'module2']

from .module1 import *
from .module2 import *
```

#### 1.2.3. Importing từ Packages
- `import package.module`
- `from package import module`
- `from package.module import name`

**Ví dụ:**
```python
import mypackage.module1
from mypackage import module2
from mypackage.module1 import func
```

#### 1.2.4. Namespace Packages (Python 3.3+)
Package không cần `__init__.py`, cho phép phân tán package trên nhiều thư mục.

### 1.3. Import System

#### 1.3.1. Absolute Imports
Import từ gốc của project.

**Ví dụ:**
```python
from mypackage import module
```

#### 1.3.2. Relative Imports (`.`, `..`)
Import tương đối trong package. Dùng dấu chấm:
- `.`: module cùng thư mục.
- `..`: module thư mục cha.

**Ví dụ trong `mypackage/subpackage/module.py`:**
```python
from . import sibling_module
from .. import parent_module
```

#### 1.3.3. `importlib` Module
Module cung cấp API để thao tác import hệ thống.

**Ví dụ:**
```python
import importlib

module = importlib.import_module('mypackage.module1')
```

#### 1.3.4. `__all__` Variable (Kiểm soát `from * import`)
Danh sách tên được export khi dùng `from module import *`.

**Ví dụ trong `mymodule.py`:**
```python
__all__ = ['func1', 'func2']

def func1(): pass
def func2(): pass
def internal(): pass  # Không được export
```

## 2. STANDARD LIBRARY QUAN TRỌNG

### 2.1. Collections Module

#### 2.1.1. `Counter`
Đếm số lần xuất hiện của các phần tử.

**Ví dụ:**
```python
from collections import Counter

cnt = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
print(cnt)
print(cnt['a'])
print(cnt.most_common(2))
```
```
Output:
Counter({'a': 3, 'b': 2, 'c': 1})
3
[('a', 3), ('b', 2)]
```

#### 2.1.2. `defaultdict`
Dictionary với giá trị mặc định khi truy cập key không tồn tại.

**Ví dụ:**
```python
from collections import defaultdict

dd = defaultdict(list)
dd['key'].append(1)  # Tự động tạo list nếu key chưa có
print(dd['key'])

dd_int = defaultdict(int)
dd_int['count'] += 1
print(dd_int['count'])
```
```
Output:
[1]
1
```

#### 2.1.3. `OrderedDict`
Dictionary ghi nhớ thứ tự thêm vào.

**Ví dụ:**
```python
from collections import OrderedDict

od = OrderedDict()
od['z'] = 1
od['a'] = 2
print(list(od.keys()))
```
```
Output:
['z', 'a']
```

#### 2.1.4. `deque`
Hàng đợi hai đầu với thao tác nhanh.

**Ví dụ:**
```python
from collections import deque

d = deque([1, 2, 3])
d.appendleft(0)
d.append(4)
print(d)
print(d.pop())
print(d.popleft())
```
```
Output:
deque([0, 1, 2, 3, 4])
4
0
```

#### 2.1.5. `namedtuple`
Tuple với tên trường, tạo lớp đơn giản.

**Ví dụ:**
```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)
print(p[0])
```
```
Output:
10 20
10
```

#### 2.1.6. `ChainMap`
Nhóm nhiều dictionary thành một view.

**Ví dụ:**
```python
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
chain = ChainMap(dict1, dict2)
print(chain['a'])
print(chain['c'])
```
```
Output:
1
3
```

#### 2.1.7. `UserDict`, `UserList`, `UserString`
Lớp cơ sở để kế thừa tạo container tùy chỉnh.

**Ví dụ:**
```python
from collections import UserDict

class MyDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)

d = MyDict({'a': 1})
print(d)  # {'a': 2}
```

### 2.2. Datetime Module

#### 2.2.1. `datetime`, `date`, `time`, `timedelta`
- `datetime`: Ngày và giờ.
- `date`: Chỉ ngày.
- `time`: Chỉ giờ.
- `timedelta`: Chênh lệch thời gian.

**Ví dụ:**
```python
from datetime import datetime, date, time, timedelta

now = datetime.now()
print(now)

today = date.today()
print(today)

t = time(14, 30)
print(t)

delta = timedelta(days=5)
print(today + delta)
```

#### 2.2.2. `strftime()`, `strptime()`
- `strftime()`: Định dạng datetime thành chuỗi.
- `strptime()`: Phân tích chuỗi thành datetime.

**Ví dụ:**
```python
from datetime import datetime

dt = datetime.now()
formatted = dt.strftime('%Y-%m-%d %H:%M:%S')
print(formatted)

parsed = datetime.strptime('2023-01-01', '%Y-%m-%d')
print(parsed)
```

#### 2.2.3. `timezone`, `timedelta`
- `timezone`: Đại diện múi giờ.
- `timedelta`: Khoảng thời gian.

**Ví dụ:**
```python
from datetime import datetime, timezone, timedelta

utc = timezone.utc
dt_utc = datetime.now(utc)
print(dt_utc)

tz = timezone(timedelta(hours=7))  # UTC+7
dt_local = datetime.now(tz)
print(dt_local)
```

#### 2.2.4. `calendar` Module
Cung cấp các hàm liên quan đến lịch.

**Ví dụ:**
```python
import calendar

print(calendar.month(2023, 1))
print(calendar.isleap(2024))
print(calendar.weekday(2023, 1, 1))
```

### 2.3. Math Module

#### 2.3.1. Mathematical Functions
Các hàm toán học cơ bản và nâng cao.

**Ví dụ:**
```python
import math

print(math.sqrt(16))
print(math.sin(math.pi/2))
print(math.log(100, 10))
print(math.factorial(5))
```

#### 2.3.2. Constants (`pi`, `e`, `tau`, `inf`, `nan`)
Các hằng số toán học.

**Ví dụ:**
```python
import math

print(math.pi)
print(math.e)
print(math.tau)
print(math.inf)
print(math.nan)
```

#### 2.3.3. Number-theoretic Functions
Các hàm lý thuyết số.

**Ví dụ:**
```python
import math

print(math.gcd(48, 18))
print(math.lcm(12, 15))
print(math.prod([1,2,3,4]))
print(math.dist((0,0), (3,4)))
print(math.hypot(3,4))
```

### 2.4. Random Module

#### 2.4.1. Random Number Generation
- `random.random()`: Số thực ngẫu nhiên trong [0.0, 1.0).
- `random.randint(a, b)`: Số nguyên ngẫu nhiên trong [a, b].

**Ví dụ:**
```python
import random

print(random.random())
print(random.randint(1, 10))
```

#### 2.4.2. Sequences (`choice`, `sample`, `shuffle`)
- `random.choice(seq)`: Chọn ngẫu nhiên một phần tử.
- `random.sample(population, k)`: Lấy mẫu không lặp.
- `random.shuffle(seq)`: Xáo trộn tại chỗ.

**Ví dụ:**
```python
import random

items = [1, 2, 3, 4, 5]
print(random.choice(items))
print(random.sample(items, 3))
random.shuffle(items)
print(items)
```

#### 2.4.3. Distributions (`uniform`, `gaussian`, v.v.)
- `random.uniform(a, b)`: Phân phối đều.
- `random.gauss(mu, sigma)`: Phân phối chuẩn.

**Ví dụ:**
```python
import random

print(random.uniform(5, 10))
print(random.gauss(0, 1))
```

#### 2.4.4. Seed và State
- `random.seed(a=None)`: Khởi tạo bộ sinh số ngẫu nhiên.
- `random.getstate()`: Lấy trạng thái hiện tại.
- `random.setstate(state)`: Khôi phục trạng thái.

**Ví dụ:**
```python
import random

random.seed(42)
print(random.random())
state = random.getstate()
print(random.random())
random.setstate(state)
print(random.random())  # Số giống lần trước
```

### 2.5. String Module

#### 2.5.1. String Constants
Các chuỗi hằng như chữ cái, chữ số.

**Ví dụ:**
```python
import string

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
print(string.whitespace)
```

#### 2.5.2. Template Strings
Template đơn giản để thay thế biến.

**Ví dụ:**
```python
from string import Template

t = Template('Hello, $name!')
result = t.substitute(name='Alice')
print(result)
```

### 2.6. Itertools Module

#### 2.6.1. Infinite Iterators (`count`, `cycle`, `repeat`)
- `itertools.count(start=0, step=1)`: Bộ đếm vô hạn.
- `itertools.cycle(iterable)`: Lặp vô hạn.
- `itertools.repeat(object, times=None)`: Lặp lại object.

**Ví dụ:**
```python
import itertools

for i in itertools.count(10, 2):
    if i > 20:
        break
    print(i)

c = 0
for item in itertools.cycle('AB'):
    if c > 5:
        break
    print(item)
    c += 1

for item in itertools.repeat('X', 3):
    print(item)
```

#### 2.6.2. Finite Iterators (`accumulate`, `chain`, `groupby`, v.v.)
- `itertools.accumulate(iterable, func)`: Tích lũy.
- `itertools.chain(*iterables)`: Nối iterables.
- `itertools.groupby(iterable, key)`: Nhóm theo key.

**Ví dụ:**
```python
import itertools

print(list(itertools.accumulate([1,2,3,4])))
print(list(itertools.chain('AB', 'CD')))
for key, group in itertools.groupby('AAAABBBCCDAABBB'):
    print(key, list(group))
```

#### 2.6.3. Combinatoric Iterators (`product`, `permutations`, `combinations`)
- `itertools.product(*iterables, repeat=1)`: Tích Descartes.
- `itertools.permutations(iterable, r=None)`: Hoán vị.
- `itertools.combinations(iterable, r)`: Tổ hợp.

**Ví dụ:**
```python
import itertools

print(list(itertools.product('AB', repeat=2)))
print(list(itertools.permutations('ABC', 2)))
print(list(itertools.combinations('ABC', 2)))
```

### 2.7. Functools Module

#### 2.7.1. `lru_cache`, `cache` (Python 3.9+)
- `lru_cache(maxsize=None)`: Decorator cache với thuật toán LRU.
- `cache`: Alias của `lru_cache(maxsize=None)` (Python 3.9+).

**Ví dụ:**
```python
from functools import lru_cache

@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))
```

#### 2.7.2. `partial`, `partialmethod`
- `partial(func, *args, **kwargs)`: Cố định một số đối số của hàm.
- `partialmethod`: Tương tự cho method.

**Ví dụ:**
```python
from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
print(square(5))
```

#### 2.7.3. `reduce`
Áp dụng hàm lên các phần tử của iterable từ trái sang phải.

**Ví dụ:**
```python
from functools import reduce

result = reduce(lambda x, y: x+y, [1,2,3,4])
print(result)  # 10
```

#### 2.7.4. `wraps`, `update_wrapper`
Giữ metadata của hàm gốc khi dùng decorator.

**Ví dụ:**
```python
from functools import wraps

def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    '''Docstring'''
    pass

print(example.__name__)
print(example.__doc__)
```

#### 2.7.5. `singledispatch`, `singledispatchmethod`
Cho phép đa hình dựa trên kiểu đối số.

**Ví dụ:**
```python
from functools import singledispatch

@singledispatch
def func(arg):
    print('Default:', arg)

@func.register(int)
def _(arg):
    print('Integer:', arg)

func(10)
func('hello')
```

#### 2.7.6. `total_ordering`
Decorator tự sinh các phương thức so sánh nếu đã định nghĩa ít nhất một phương thức so sánh.

**Ví dụ:**
```python
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, score):
        self.score = score
    def __eq__(self, other):
        return self.score == other.score
    def __lt__(self, other):
        return self.score < other.score

s1 = Student(85)
s2 = Student(90)
print(s1 <= s2)
```

### 2.8. Statistics Module

#### 2.8.1. Central Tendency (`mean`, `median`, `mode`)
Các đo lường xu hướng trung tâm.

**Ví dụ:**
```python
import statistics

data = [1, 2, 2, 3, 4]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.mode(data))
```

#### 2.8.2. Spread (`stdev`, `variance`, `quantiles`)
Các đo lường độ phân tán.

**Ví dụ:**
```python
import statistics

data = [1, 2, 3, 4, 5]
print(statistics.stdev(data))
print(statistics.variance(data))
print(statistics.quantiles(data, n=4))
```

### 2.9. Decimal và Fractions

#### 2.9.1. Decimal (chính xác cao)
Cho tính toán chính xác, tránh sai số dấu phẩy động.

**Ví dụ:**
```python
from decimal import Decimal

a = Decimal('0.1')
b = Decimal('0.2')
c = a + b
print(c)  # 0.3 chính xác
```

#### 2.9.2. Fractions (phân số)
Biểu diễn phân số chính xác.

**Ví dụ:**
```python
from fractions import Fraction

f1 = Fraction(1, 3)
f2 = Fraction(1, 6)
print(f1 + f2)  # 1/2
```

### 2.10. `re` Module (Regular Expressions)

#### 2.10.1. Pattern Syntax
Cú pháp biểu thức chính quy:
- `.`: Bất kỳ ký tự nào (trừ xuống dòng).
- `\d`: Chữ số.
- `\w`: Chữ cái, số, gạch dưới.
- `*`: 0 hoặc nhiều.
- `+`: 1 hoặc nhiều.
- `?`: 0 hoặc 1.
- `{m,n}`: Từ m đến n lần.

#### 2.10.2. `re` Functions (`match`, `search`, `findall`, `finditer`, `sub`, `split`)
- `re.match(pattern, string)`: Kiểm tra từ đầu chuỗi.
- `re.search(pattern, string)`: Tìm đầu tiên.
- `re.findall(pattern, string)`: Tìm tất cả.
- `re.finditer(pattern, string)`: Iterator các match object.
- `re.sub(pattern, repl, string)`: Thay thế.
- `re.split(pattern, string)`: Tách chuỗi.

**Ví dụ:**
```python
import re

text = 'Hello 123 World 456'
print(re.match(r'\d+', text))  # None vì không khớp từ đầu
print(re.search(r'\d+', text).group())
print(re.findall(r'\d+', text))
print(re.sub(r'\d+', 'NUM', text))
print(re.split(r'\s+', text))
```

#### 2.10.3. Pattern Objects
Biên dịch pattern để tái sử dụng.

**Ví dụ:**
```python
import re

pattern = re.compile(r'\d+')
result = pattern.findall('Hello 123 World 456')
print(result)
```

#### 2.10.4. Match Objects
Đối tượng chứa thông tin về match.

**Ví dụ:**
```python
import re

match = re.search(r'(\d+) (\w+)', '123 abc')
if match:
    print(match.group())   # '123 abc'
    print(match.group(1))  # '123'
    print(match.group(2))  # 'abc'
    print(match.start(), match.end())
```

#### 2.10.5. Flags
Các cờ thay đổi hành vi regex.
- `re.IGNORECASE` (`re.I`): Không phân biệt hoa thường.
- `re.MULTILINE` (`re.M`): ^ và $ khớp đầu/cuối dòng.
- `re.DOTALL` (`re.S`): . khớp cả xuống dòng.

**Ví dụ:**
```python
import re

text = 'Hello\nWorld'
print(re.search('world', text, re.IGNORECASE).group())
print(re.findall('^[A-Z]', text, re.MULTILINE))
```

### 2.11. `json` Module (nâng cao)

#### 2.11.1. Custom Serialization
Định nghĩa cách mã hóa đối tượng tùy chỉnh.

**Ví dụ:**
```python
import json

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return [obj.real, obj.imag]
        return super().default(obj)

json_string = json.dumps(2+3j, cls=ComplexEncoder)
print(json_string)
```

#### 2.11.2. `JSONEncoder`, `JSONDecoder`
Lớp cơ sở để tùy chỉnh mã hóa/giải mã.

**Ví dụ:**
```python
import json

class CustomDecoder(json.JSONDecoder):
    def decode(self, s):
        obj = super().decode(s)
        if isinstance(obj, dict) and 'special' in obj:
            obj['special'] = 'decoded'
        return obj

data = '{"special": "value"}'
result = json.loads(data, cls=CustomDecoder)
print(result)
```

### 2.12. `csv` Module (nâng cao)

#### 2.12.1. Dialects
Định nghĩa các tham số định dạng CSV.

**Ví dụ:**
```python
import csv

csv.register_dialect('my_dialect', delimiter=';', quotechar='"')
with open('file.csv', 'w', newline='') as f:
    writer = csv.writer(f, dialect='my_dialect')
    writer.writerow(['a;b', 'c'])
```

#### 2.12.2. Sniffer
Tự động phát hiện dialect.

**Ví dụ:**
```python
import csv

with open('file.csv', 'r') as f:
    sample = f.read(1024)
    sniffer = csv.Sniffer()
    dialect = sniffer.sniff(sample)
    f.seek(0)
    reader = csv.reader(f, dialect=dialect)
    for row in reader:
        print(row)
```

### 2.13. `sqlite3` Module

#### 2.13.1. Connection, Cursor
- `sqlite3.connect(database)`: Tạo kết nối.
- `connection.cursor()`: Tạo cursor để thực thi truy vấn.

**Ví dụ:**
```python
import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()
```

#### 2.13.2. Executing Queries
Thực thi lệnh SQL.

**Ví dụ:**
```python
cursor.execute('''CREATE TABLE stocks
                  (date text, trans text, symbol text, qty real, price real)''')
cursor.execute("INSERT INTO stocks VALUES ('2023-01-01','BUY','AAPL',100,150.0)")
conn.commit()
```

#### 2.13.3. Transactions
Tự động commit hoặc rollback với context manager.

**Ví dụ:**
```python
with conn:
    conn.execute("INSERT INTO stocks VALUES ('2023-01-02','SELL','GOOG',50,2800.0)")
```

#### 2.13.4. Row Factory
Thay đổi cách trả về hàng.

**Ví dụ:**
```python
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute('SELECT * FROM stocks')
row = cursor.fetchone()
print(row['symbol'])
```

### 2.14. `hashlib` Module

#### 2.14.1. Hash Algorithms (MD5, SHA1, SHA256, v.v.)
Các thuật toán băm.

**Ví dụ:**
```python
import hashlib

m = hashlib.sha256()
m.update(b'Hello')
print(m.hexdigest())

# Một lần
print(hashlib.sha256(b'Hello').hexdigest())
```

#### 2.14.2. HMAC
Mã xác thực tin nhắn dùng khóa.

**Ví dụ:**
```python
import hmac

key = b'secret'
msg = b'Hello'
h = hmac.new(key, msg, hashlib.sha256)
print(h.hexdigest())
```

### 2.15. `logging` Module

#### 2.15.1. Loggers, Handlers, Formatters, Filters
- Logger: Điểm ghi log.
- Handler: Xử lý log (file, console).
- Formatter: Định dạng log.
- Filter: Lọc log.

**Ví dụ:**
```python
import logging

logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('app.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info('This is an info message')
```

#### 2.15.2. Log Levels
Các mức độ log: DEBUG, INFO, WARNING, ERROR, CRITICAL.

#### 2.15.3. Configuration
Cấu hình logging từ file hoặc dictionary.

**Ví dụ:**
```python
import logging.config

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('simpleExample')
```

#### 2.15.4. Logging đến Files, Console, Network
Có nhiều handler: `FileHandler`, `StreamHandler`, `SocketHandler`.

**Ví dụ:**
```python
import logging

logger = logging.getLogger()
logger.addHandler(logging.FileHandler('file.log'))
logger.addHandler(logging.StreamHandler())
```

### 2.16. `unittest` Module

#### 2.16.1. `TestCase`, `TestSuite`, `TestLoader`
- `TestCase`: Lớp cơ sở cho test case.
- `TestSuite`: Tập hợp các test.
- `TestLoader`: Tải test từ module, class.

**Ví dụ:**
```python
import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()
```

#### 2.16.2. Assertions
Các phương thức assert: `assertEqual`, `assertTrue`, `assertRaises`, v.v.

#### 2.16.3. Fixtures
- `setUp()`: Chuẩn bị trước mỗi test.
- `tearDown()`: Dọn dẹp sau mỗi test.

**Ví dụ:**
```python
class TestExample(unittest.TestCase):
    def setUp(self):
        self.list = [1, 2, 3]
    def test_len(self):
        self.assertEqual(len(self.list), 3)
```

#### 2.16.4. Mocking (`unittest.mock`)
Giả lập đối tượng để test.

**Ví dụ:**
```python
from unittest.mock import Mock

mock = Mock()
mock.method.return_value = 10
print(mock.method())
```

### 2.17. `threading` Module (Synchronization Primitives, Thread-local Data)

#### 2.17.1. Thread Class
Tạo và chạy thread.

**Ví dụ:**
```python
import threading

def worker():
    print('Thread working')

thread = threading.Thread(target=worker)
thread.start()
thread.join()
```

#### 2.17.2. Synchronization Primitives (`Lock`, `RLock`, `Condition`, `Semaphore`, `Event`, `Timer`, `Barrier`)
Các cơ chế đồng bộ.

**Ví dụ Lock:**
```python
import threading

lock = threading.Lock()
lock.acquire()
try:
    # critical section
    pass
finally:
    lock.release()
```

#### 2.17.3. Thread-local Data
Dữ liệu riêng cho từng thread.

**Ví dụ:**
```python
import threading

local_data = threading.local()
local_data.value = 42
```

#### 2.17.4. `ThreadPoolExecutor` (từ `concurrent.futures`)
Quản lý pool thread.

**Ví dụ:**
```python
from concurrent.futures import ThreadPoolExecutor

def task(n):
    return n * n

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(task, range(10))
    for result in results:
        print(result)
```

### 2.18. `multiprocessing` Module (Process với queues, Shared Memory, Managers)

#### 2.18.1. Process Class
Tạo và chạy process.

**Ví dụ:**
```python
from multiprocessing import Process

def worker(name):
    print(f'Process {name}')

p = Process(target=worker, args=('child',))
p.start()
p.join()
```

#### 2.18.2. Inter-process Communication
Sử dụng Queue, Pipe.

**Ví dụ Queue:**
```python
from multiprocessing import Process, Queue

def worker(q):
    q.put('Hello')

q = Queue()
p = Process(target=worker, args=(q,))
p.start()
print(q.get())
p.join()
```

#### 2.18.3. Shared Memory (`Value`, `Array`)
Bộ nhớ chia sẻ giữa các process.

**Ví dụ:**
```python
from multiprocessing import Process, Value, Array

def worker(n, arr):
    n.value = 3.14
    for i in range(len(arr)):
        arr[i] = -arr[i]

num = Value('d', 0.0)
arr = Array('i', range(10))
p = Process(target=worker, args=(num, arr))
p.start()
p.join()
print(num.value)
print(arr[:])
```

#### 2.18.4. `ProcessPoolExecutor` (từ `concurrent.futures`)
Quản lý pool process.

**Ví dụ:**
```python
from concurrent.futures import ProcessPoolExecutor

def task(n):
    return n * n

with ProcessPoolExecutor(max_workers=3) as executor:
    results = executor.map(task, range(10))
    for result in results:
        print(result)
```

### 2.19. `asyncio` Module (bao gồm Timeouts, Shields, Gathering)

#### 2.19.1. Event Loop
Vòng lặp sự kiện chạy các coroutine.

**Ví dụ:**
```python
import asyncio

async def main():
    print('Hello')
    await asyncio.sleep(1)
    print('World')

asyncio.run(main())
```

#### 2.19.2. Coroutines, Tasks, Futures
- Coroutine: Hàm async.
- Task: Wrapper của coroutine để chạy trên event loop.
- Future: Đối tượng đại diện cho kết quả bất đồng bộ.

**Ví dụ Task:**
```python
import asyncio

async def nested():
    return 42

async def main():
    task = asyncio.create_task(nested())
    await task
    print(task.result())

asyncio.run(main())
```

#### 2.19.3. `async/await` Syntax
Khai báo và chờ coroutine.

**Ví dụ:**
```python
import asyncio

async def say_after(delay, msg):
    await asyncio.sleep(delay)
    print(msg)

async def main():
    await say_after(1, 'Hello')
    await say_after(2, 'World')

asyncio.run(main())
```

#### 2.19.4. Synchronization Primitives (`Lock`, `Semaphore`, `Event`, `Condition`, `Queue`)
Tương tự threading nhưng cho asyncio.

**Ví dụ Lock:**
```python
import asyncio

lock = asyncio.Lock()

async def worker():
    async with lock:
        print('Critical section')
        await asyncio.sleep(1)

async def main():
    await asyncio.gather(worker(), worker())

asyncio.run(main())
```

#### 2.19.5. Streams
Làm việc với kết nối mạng.

**Ví dụ:**
```python
import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    writer.write(message.encode())
    data = await reader.read(100)
    print(f'Received: {data.decode()}')
    writer.close()

asyncio.run(tcp_echo_client('Hello World'))
```

#### 2.19.6. Task Groups (Python 3.11+)
Quản lý nhóm task.

**Ví dụ:**
```python
async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(say_after(1, 'Hello'))
        tg.create_task(say_after(2, 'World'))
```

### 2.20. `typing` Module (Type Hints)

#### 2.20.1. Basic Types (`Any`, `Union`, `Optional`, `List`, `Dict`, `Callable`, `NoReturn`)
- `Any`: Bất kỳ kiểu nào.
- `Union[int, str]`: int hoặc str.
- `Optional[int]` tương đương `Union[int, None]`.
- `List[int]`: Danh sách int.
- `Dict[str, int]`: Dictionary với key str, value int.
- `Callable[[int, int], int]`: Hàm nhận 2 int, trả về int.
- `NoReturn`: Hàm không trả về (luôn raise exception).

**Ví dụ:**
```python
from typing import List, Dict, Optional

def process(items: List[int]) -> Dict[str, int]:
    return {'len': len(items)}

result: Optional[int] = None
```

#### 2.20.2. Generic Types
Kiểu tổng quát với `TypeVar`.

**Ví dụ:**
```python
from typing import TypeVar, List

T = TypeVar('T')

def first(lst: List[T]) -> T:
    return lst[0]
```

#### 2.20.3. Protocols, `TypeVar`, `NewType`, `TypedDict`
- `Protocol`: Structural subtyping.
- `NewType`: Tạo kiểu mới từ kiểu có sẵn.
- `TypedDict`: Dictionary với kiểu cố định cho key.

**Ví dụ:**
```python
from typing import TypedDict

class Point(TypedDict):
    x: int
    y: int

p: Point = {'x': 1, 'y': 2}
```

#### 2.20.4. Type Guards, Self Type (Python 3.11+), Variadic Generics
- Type guard: Hàm trả về `TypeGuard`.
- `Self`: Kiểu đại diện cho class hiện tại.
- Variadic Generics: Generic với số lượng biến đổi.

**Ví dụ Type Guard:**
```python
from typing import TypeGuard

def is_str_list(val: list) -> TypeGuard[list[str]]:
    return all(isinstance(x, str) for x in val)
```

### 2.21. `zoneinfo` (timezone support) (Python 3.9+)
Module chuẩn để làm việc với múi giờ.

**Ví dụ:**
```python
from zoneinfo import ZoneInfo
from datetime import datetime

dt = datetime(2023, 1, 1, tzinfo=ZoneInfo('America/New_York'))
print(dt)
```

### 2.22. `secrets` (cryptographically strong random numbers) (Python 3.6+)
Module tạo số ngẫu nhiên an toàn cho mật mã.

**Ví dụ:**
```python
import secrets

print(secrets.token_hex(16))
print(secrets.choice(['a', 'b', 'c']))
```

### 2.23. `ipaddress` (IP addresses)
Module để thao tác với địa chỉ IP.

**Ví dụ:**
```python
import ipaddress

ip = ipaddress.ip_address('192.168.1.1')
network = ipaddress.ip_network('192.168.1.0/24')
print(ip in network)
```

## 3. STANDARD LIBRARY ÍT DÙNG HƠN

### 3.1. Internet Protocols

#### 3.1.1. `email` (quản lý email messages)
Tạo, phân tích email.

#### 3.1.2. `html` (HTML parsing và escaping)
- `html.escape()`: Escape ký tự đặc biệt HTML.
- `html.parser`: Parser đơn giản.

#### 3.1.3. `http` (HTTP protocols)
Module client và server HTTP.

#### 3.1.4. `smtplib`, `imaplib`, `poplib` (email protocols)
Gửi và nhận email.

#### 3.1.5. `telnetlib`, `ftplib` (telnet và FTP)
Kết nối telnet và FTP.

#### 3.1.6. `socketserver` (network servers framework)
Framework để tạo server mạng.

#### 3.1.7. `urllib`, `urllib2` (URL handling)
Mở và đọc URL.

#### 3.1.8. `xmlrpc` (XML-RPC client và server)
Triển khai XML-RPC.

### 3.2. Data Encoding

#### 3.2.1. `base64` (Base16, Base32, Base64 encoding)
Mã hóa base64.

**Ví dụ:**
```python
import base64

encoded = base64.b64encode(b'binary data')
print(encoded)
decoded = base64.b64decode(encoded)
print(decoded)
```

#### 3.2.2. `quopri` (Quoted-printable encoding)
Mã hóa quoted-printable.

#### 3.2.3. `uu` (uuencode)
Mã hóa uuencode.

#### 3.2.4. `binascii` (binary-ASCII conversions)
Chuyển đổi giữa binary và ASCII.

### 3.3. System Interaction

#### 3.3.1. `sys` (system-specific parameters)
Truy cập thông tin hệ thống.

#### 3.3.2. `os` (operating system interfaces)
Giao diện với hệ điều hành.

#### 3.3.3. `time` (time access và conversions)
Thao tác thời gian.

#### 3.3.4. `gc` (garbage collector interface)
Điều khiển garbage collector.

#### 3.3.5. `inspect` (runtime introspection) (bao gồm `getsource`, `signature`, `isclass`, `getmembers`, `stack`)
Kiểm tra đối tượng tại runtime.

**Ví dụ:**
```python
import inspect

def func(a, b=1):
    pass

print(inspect.signature(func))
print(inspect.getsource(func))
```

#### 3.3.6. `ast` (Abstract Syntax Trees)
Thao tác với cú pháp trừu tượng.

#### 3.3.7. `dis` (bytecode disassembler)
Disassemble bytecode Python.

**Ví dụ:**
```python
import dis

def add(a, b):
    return a + b

dis.dis(add)
```

#### 3.3.8. `tokenize` (tokenizer cho Python source)
Tách source code thành token.

#### 3.3.9. `symtable` (symbol tables)
Truy cập symbol table.

#### 3.3.10. `tabnanny` (indentation checker)
Kiểm tra lỗi thụt dòng.

#### 3.3.11. `py_compile` (compile Python source files)
Biên dịch file Python thành bytecode.

#### 3.3.12. `compileall` (compile all Python source files)
Biên dịch tất cả file Python trong thư mục.

### 3.4. Development và Debugging

#### 3.4.1. `pdb` (Python debugger) (bao gồm các lệnh: `l`, `n`, `s`, `c`, `b`, `p`, `w`, `q`, `post_mortem`)
Debugger tương tác.

**Ví dụ:**
```python
import pdb

def buggy_function():
    a = 1
    pdb.set_trace()
    b = 0
    return a / b
```

#### 3.4.2. `profile`, `cProfile` (profiler)
Phân tích hiệu năng.

#### 3.4.3. `timeit` (execution time measurement)
Đo thời gian thực thi.

**Ví dụ:**
```python
import timeit

time = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(time)
```

#### 3.4.4. `doctest` (test interactive examples)
Kiểm tra ví dụ trong docstring.

**Ví dụ:**
```python
def add(a, b):
    '''
    >>> add(2, 3)
    5
    '''
    return a + b

if __name__ == '__main__':
    import doctest
    doctest.testmod()
```

#### 3.4.5. `trace` (program execution tracer)
Theo dõi thực thi chương trình.

#### 3.4.6. `tracemalloc` (trace memory allocations)
Theo dõi cấp phát bộ nhớ.

#### 3.4.7. `faulthandler` (dump traceback on fatal errors)
Xử lý lỗi nghiêm trọng.

### 3.5. Miscellaneous

#### 3.5.1. `graphlib` (graph-like structures) (Python 3.9+)
Làm việc với đồ thị.

#### 3.5.2. `mimetypes` (map filenames to MIME types)
Ánh xạ tên file sang MIME type.

#### 3.5.3. `plistlib` (Mac OS X .plist files)
Đọc/ghi file .plist.

#### 3.5.4. `wave` (WAV file handling)
Xử lý file WAV.

#### 3.5.5. `colorsys` (color system conversions)
Chuyển đổi hệ màu.

#### 3.5.6. `imghdr` (image type determination)
Xác định loại ảnh.

## 4. VIRTUAL ENVIRONMENTS

### 4.1. Tại sao cần Virtual Environment? (Lợi ích và mục đích)
Virtual Environment (venv) cô lập môi trường Python cho từng dự án, tránh xung đột phiên bản thư viện.

### 4.2. Tạo và sử dụng `venv`
Module chuẩn từ Python 3.3.

**Tạo venv:**
```bash
python -m venv myenv
```

**Kích hoạt:**
- Windows: `myenv\Scripts\activate`
- Unix/MacOS: `source myenv/bin/activate`

**Vô hiệu hóa:**
```bash
deactivate
```

### 4.3. `Pipenv` và `Poetry` (Modern Tools) (So sánh và ví dụ)
Công cụ quản lý dependencies và virtual environment hiện đại.

**Pipenv:**
```bash
pip install pipenv
pipenv install requests
pipenv shell
```

**Poetry:**
```bash
pip install poetry
poetry new project
poetry add requests
poetry shell
```

### 4.4. PIP là gì? (Các lệnh cơ bản: install, list, requirements.txt)
PIP là trình quản lý gói Python.

**Các lệnh cơ bản:**
- `pip install package`: Cài đặt package.
- `pip list`: Liệt kê package đã cài.
- `pip freeze > requirements.txt`: Xuất danh sách package.
- `pip install -r requirements.txt`: Cài từ file.

**Ví dụ `requirements.txt`:**
```
requests==2.28.1
flask>=2.0.0
```

---

# PHẦN VI: LẬP TRÌNH WEB VỚI PYTHON (BACKEND)

## 1. GIỚI THIỆU LẬP TRÌNH WEB

### 1.1. Client-Server Model
Mô hình máy khách (client) gửi yêu cầu, máy chủ (server) xử lý và trả về phản hồi.

### 1.2. HTTP Protocol Basics
Giao thức truyền tải siêu văn bản.

#### 1.2.1. HTTP Methods
Các phương thức: GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS.

#### 1.2.2. HTTP Status Codes
- 1xx: Thông tin.
- 2xx: Thành công (200 OK, 201 Created).
- 3xx: Điều hướng (301 Moved Permanently).
- 4xx: Lỗi client (404 Not Found, 403 Forbidden).
- 5xx: Lỗi server (500 Internal Server Error).

#### 1.2.3. HTTP Headers
Các trường thông tin: Content-Type, User-Agent, Authorization, Cookie.

#### 1.2.4. Cookies và Sessions
- Cookie: Dữ liệu nhỏ lưu ở client.
- Session: Dữ liệu lưu ở server, nhận diện bằng session ID.

### 1.3. RESTful API Concepts
Kiến trúc REST (Representational State Transfer).

#### 1.3.1. REST Principles
- Client-server.
- Stateless.
- Cacheable.
- Uniform interface.

#### 1.3.2. Resources và URIs
Tài nguyên được định danh bằng URI.

#### 1.3.3. Statelessness
Mỗi request chứa đủ thông tin, server không lưu trạng thái client.

### 1.4. WSGI và ASGI (Specification)
- WSGI (Web Server Gateway Interface): Giao tiếp đồng bộ.
- ASGI (Asynchronous Server Gateway Interface): Giao tiếp bất đồng bộ.

## 2. WEB FRAMEWORK: FLASK (GIẢNG KỸ)

### 2.1. Flask Introduction
Microframework nhẹ, linh hoạt.

#### 2.1.1. Installation
```bash
pip install flask
```

#### 2.1.2. Application Structure
Ứng dụng Flask đơn giản:

**Ví dụ:**
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
```

### 2.2. Routing và Views

#### 2.2.1. URL Routes
Định nghĩa route bằng decorator.

**Ví dụ:**
```python
@app.route('/user/<username>')
def show_user(username):
    return f'User {username}'
```

#### 2.2.2. View Functions
Hàm xử lý request, trả về response.

#### 2.2.3. URL Building (`url_for`)
Tạo URL từ tên hàm.

**Ví dụ:**
```python
from flask import url_for

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('profile', username='John Doe'))
```

#### 2.2.4. HTTP Methods
Mặc định chỉ nhận GET. Cho phép method khác:

**Ví dụ:**
```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Xử lý POST
        pass
    else:
        # Hiển thị form GET
        pass
```

### 2.3. Template Engine (Jinja2)
Flask sử dụng Jinja2 để render template.

#### 2.3.1. Template Inheritance
Kế thừa layout.

**Ví dụ `base.html`:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```

**Ví dụ `child.html`:**
```html
{% extends "base.html" %}
{% block title %}Home{% endblock %}
{% block content %}
    <h1>Hello</h1>
{% endblock %}
```

#### 2.3.2. Variables và Expressions
Truyền biến từ view.

**View:**
```python
@app.route('/')
def index():
    return render_template('index.html', name='Alice')
```

**Template:**
```html
<h1>Hello {{ name }}!</h1>
```

#### 2.3.3. Control Structures
Vòng lặp, điều kiện.

**Ví dụ:**
```html
{% if users %}
    <ul>
    {% for user in users %}
        <li>{{ user }}</li>
    {% endfor %}
    </ul>
{% endif %}
```

#### 2.3.4. Filters và Tests
- Filters: Biến đổi biến, ví dụ `{{ name|upper }}`.
- Tests: Kiểm tra, ví dụ `{% if number is even %}`.

#### 2.3.5. Macros
Định nghĩa hàm trong template.

**Ví dụ:**
```html
{% macro input(name, value='', type='text') %}
    <input type="{{ type }}" name="{{ name }}" value="{{ value }}">
{% endmacro %}

{{ input('username') }}
{{ input('password', type='password') }}
```

### 2.4. Form Handling

#### 2.4.1. WTForms Integration
Thư viện xử lý form.

**Ví dụ:**
```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if form.validate_on_submit():
        return f'Hello {form.name.data}'
    return render_template('form.html', form=form)
```

#### 2.4.2. CSRF Protection
Bảo vệ chống giả mạo request.

**Cấu hình:**
```python
app.config['SECRET_KEY'] = 'your-secret-key'
```

#### 2.4.3. File Uploads
Xử lý upload file.

**Ví dụ:**
```python
from flask import request
from werkzeug.utils import secure_filename

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join('uploads', filename))
    return 'File uploaded'
```

### 2.5. Session và Cookies

#### 2.5.1. Session Management
Lưu trữ session.

**Ví dụ:**
```python
from flask import session

app.secret_key = 'secret'

@app.route('/set')
def set_session():
    session['username'] = 'Alice'
    return 'Session set'

@app.route('/get')
def get_session():
    return session.get('username', 'Not set')
```

#### 2.5.2. Cookies Handling
Đọc và ghi cookie.

**Ví dụ:**
```python
from flask import make_response

@app.route('/setcookie')
def set_cookie():
    resp = make_response('Cookie set')
    resp.set_cookie('username', 'Alice')
    return resp

@app.route('/getcookie')
def get_cookie():
    username = request.cookies.get('username')
    return f'Username: {username}'
```

### 2.6. Error Handling

#### 2.6.1. Custom Error Pages
Định nghĩa trang lỗi tùy chỉnh.

**Ví dụ:**
```python
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
```

#### 2.6.2. Logging
Ghi log lỗi.

**Ví dụ:**
```python
import logging
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

@app.route('/error')
def error():
    app.logger.error('An error occurred')
    return 'Error logged'
```

### 2.7. Blueprints

#### 2.7.1. Modular Applications
Tổ chức ứng dụng thành module.

**Ví dụ `auth.py`:**
```python
from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return 'Login page'
```

**Đăng ký blueprint:**
```python
from auth import auth
app.register_blueprint(auth, url_prefix='/auth')
```

#### 2.7.2. Blueprint Registration
Đăng ký với URL prefix.

### 2.8. Database Integration

#### 2.8.1. SQLAlchemy ORM
ORM mạnh mẽ.

#### 2.8.2. Flask-SQLAlchemy
Integration với Flask.

**Ví dụ:**
```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)

db.create_all()
```

#### 2.8.3. Database Migrations
Quản lý thay đổi schema với Flask-Migrate.

**Ví dụ:**
```bash
pip install flask-migrate
```
```python
from flask_migrate import Migrate

migrate = Migrate(app, db)
```
```bash
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```

### 2.9. Authentication và Authorization

#### 2.9.1. User Authentication
Xác thực người dùng.

#### 2.9.2. Role-based Access Control
Phân quyền theo vai trò.

#### 2.9.3. Flask-Login, Flask-Security
Thư viện hỗ trợ.

**Ví dụ Flask-Login:**
```python
from flask_login import LoginManager, UserMixin, login_user

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
    pass

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login')
def login():
    user = User.query.first()
    login_user(user)
    return 'Logged in'
```

### 2.10. RESTful APIs với Flask

#### 2.10.1. Flask-RESTful
Extension để xây dựng API.

**Ví dụ:**
```python
from flask_restful import Api, Resource

api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/api')
```

#### 2.10.2. Serialization (Marshmallow)
Chuyển đổi đối tượng thành JSON.

**Ví dụ:**
```python
from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()

user = User(id=1, username='Alice')
schema = UserSchema()
result = schema.dump(user)
print(result)  # {'id': 1, 'username': 'Alice'}
```

#### 2.10.3. API Versioning
Quản lý phiên bản API.

### 2.11. Testing Flask Applications

#### 2.11.1. Unit Testing
Kiểm thử đơn vị.

**Ví dụ:**
```python
import unittest

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
```

#### 2.11.2. Integration Testing
Kiểm thử tích hợp.

#### 2.11.3. Test Client
Client giả lập để test.

### 2.12. Deployment

#### 2.12.1. Production Servers (Gunicorn, uWSGI)
Sử dụng server production.

**Ví dụ Gunicorn:**
```bash
pip install gunicorn
gunicorn -w 4 app:app
```

#### 2.12.2. Reverse Proxy (Nginx)
Cấu hình Nginx làm reverse proxy.

#### 2.12.3. Docker Containerization
Đóng gói ứng dụng trong Docker.

**Ví dụ Dockerfile:**
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "-w", "4", "app:app"]
```

#### 2.12.4. Cloud Platforms
Triển khai lên AWS, GCP, Azure, Heroku.

## 3. WEB FRAMEWORK: DJANGO (GIỚI THIỆU)

### 3.1. Django Introduction
Framework full-featured, "batteries included".

#### 3.1.1. Installation
```bash
pip install django
django-admin startproject myproject
```

#### 3.1.2. Project Structure
- `manage.py`: Script quản lý.
- `settings.py`: Cấu hình.
- `urls.py`: Routing.
- `wsgi.py`: WSGI entry point.

### 3.2. MTV Pattern
Model-Template-View (tương tự MVC).

### 3.3. Django ORM

#### 3.3.1. Models
Định nghĩa model.

**Ví dụ:**
```python
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
```

#### 3.3.2. Queries
Truy vấn database.

**Ví dụ:**
```python
User.objects.filter(username='Alice')
User.objects.get(id=1)
```

#### 3.3.3. Migrations
Tạo và áp dụng migrations.

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3.4. Django Admin
Giao diện quản trị tự động.

### 3.5. Django REST Framework (DRF)
Framework mạnh để xây dựng API.

#### 3.5.1. Serializers
Chuyển đổi dữ liệu.

#### 3.5.2. Viewsets
Nhóm các view liên quan.

#### 3.5.3. Routers
Tự động tạo URL cho viewsets.

## 4. DATA HANDLING IN WEB APPLICATIONS

### 4.1. Working với Databases

#### 4.1.1. SQL Databases
PostgreSQL, MySQL, SQLite.

#### 4.1.2. NoSQL Databases
MongoDB, Redis.

#### 4.1.3. Connection Pooling
Quản lý kết nối database.

### 4.2. Serialization và Deserialization

#### 4.2.1. JSON Serialization
Chuyển đổi sang JSON.

#### 4.2.2. XML Serialization
Chuyển đổi sang XML.

### 4.3. Data Validation

#### 4.3.1. Input Validation
Kiểm tra dữ liệu đầu vào.

#### 4.3.2. Data Sanitization
Làm sạch dữ liệu.

### 4.4. Caching Strategies

#### 4.4.1. In-memory Caching
Redis, Memcached.

#### 4.4.2. HTTP Caching
Cache ở phía client.

#### 4.4.3. Database Caching
Cache kết quả truy vấn.

## 5. WEB SECURITY

### 5.1. Common Vulnerabilities

#### 5.1.1. XSS (Cross-Site Scripting)
Chèn mã độc vào trang web.

#### 5.1.2. CSRF (Cross-Site Request Forgery)
Giả mạo request từ người dùng đã xác thực.

#### 5.1.3. SQL Injection
Chèn mã SQL vào truy vấn.

#### 5.1.4. Authentication Bypass
Vượt qua xác thực.

#### 5.1.5. Insecure Direct Object References
Truy cập trực tiếp đối tượng không được phép.

#### 5.1.6. Security Misconfiguration
Cấu hình bảo mật sai.

#### 5.1.7. Sensitive Data Exposure
Lộ dữ liệu nhạy cảm.

### 5.2. Security Best Practices

#### 5.2.1. Password Hashing
Băm mật khẩu với bcrypt, PBKDF2.

#### 5.2.2. HTTPS/TLS
Mã hóa kết nối.

#### 5.2.3. Input Validation
Kiểm tra nghiêm ngặt đầu vào.

#### 5.2.4. Least Privilege Principle
Cấp quyền tối thiểu.

#### 5.2.5. Security Headers
Cài đặt header bảo mật.

## 6. DEPLOYMENT VÀ DEVOPS

### 6.1. Web Servers

#### 6.1.1. Gunicorn
WSGI server.

#### 6.1.2. uWSGI
WSGI server đầy đủ tính năng.

#### 6.1.3. Waitress
WSGI server cho Windows.

### 6.2. Reverse Proxy

#### 6.2.1. Nginx
Reverse proxy phổ biến.

#### 6.2.2. Apache
Web server linh hoạt.

### 6.3. Containerization

#### 6.3.1. Docker
Đóng gói ứng dụng.

#### 6.3.2. Docker Compose
Quản lý multi-container.

#### 6.3.3. Kubernetes
Orchestration container.

### 6.4. Cloud Deployment

#### 6.4.1. AWS
Amazon Web Services.

#### 6.4.2. Google Cloud Platform
Google Cloud.

#### 6.4.3. Microsoft Azure
Azure.

#### 6.4.4. Heroku
Platform as a Service.

### 6.5. CI/CD Pipelines

#### 6.5.1. Jenkins
CI/CD server.

#### 6.5.2. GitLab CI/CD
CI/CD tích hợp.

#### 6.5.3. GitHub Actions
CI/CD từ GitHub.

#### 6.5.4. Travis CI
CI dịch vụ.

## 7. REAL-TIME VÀ ASYNCHRONOUS WEB

### 7.1. WebSockets
Giao tiếp hai chiều.

#### 7.1.1. Flask-SocketIO
WebSockets cho Flask.

#### 7.1.2. Django Channels
WebSockets cho Django.

### 7.2. Asynchronous Views

#### 7.2.1. `async/await` trong Flask
Flask 2.0 hỗ trợ async.

#### 7.2.2. Async Views trong Django
Django 3.1+ hỗ trợ async.

### 7.3. Background Tasks

#### 7.3.1. Celery
Hệ thống queue phân tán.

#### 7.3.2. Redis Queue (RQ)
Queue đơn giản với Redis.

#### 7.3.3. Dramatiq
Queue hiệu năng cao.

--- 

# PHẦN VII: KỸ THUẬT NÂNG CAO

## 1. METAPROGRAMMING

Metaprogramming là kỹ thuật viết chương trình có khả năng thao tác, tạo ra, hoặc sửa đổi chương trình khác (hoặc chính nó) trong thời gian chạy (runtime). Trong Python, metaprogramming thường liên quan đến decorators, metaclasses, descriptors, và code generation.

### 1.1. Advanced Decorators

Decorator là một hàm đặc biệt nhận một hàm (hoặc lớp) làm đối số và trả về một hàm (hoặc lớp) mới, thường để mở rộng hoặc thay đổi hành vi của hàm/lớp gốc.

#### 1.1.1. Class Decorators

Class decorator nhận một lớp làm đối số, trả về một lớp đã được sửa đổi. Chúng có thể thêm, sửa, xóa thuộc tính hoặc phương thức của lớp.

**Giải thích:**
Class decorator hoạt động tương tự function decorator, nhưng áp dụng cho lớp. Khi một lớp được khai báo, decorator sẽ nhận lớp đó, thực hiện các thay đổi, và trả về lớp đã sửa đổi.

**Ví dụ:**
```python
def add_method(cls):
    def new_method(self):
        return "Đây là phương thức mới được thêm vào"
    cls.new_method = new_method
    return cls

@add_method
class MyClass:
    def original_method(self):
        return "Phương thức gốc"

obj = MyClass()
print(obj.original_method())
print(obj.new_method())
```
**Output:**
```
Phương thức gốc
Đây là phương thức mới được thêm vào
```

#### 1.1.2. Decorator với Arguments

Decorator có thể nhận tham số. Khi đó, cần tạo một decorator factory (hàm trả về decorator).

**Giải thích:**
Decorator với tham số thực chất là một hàm nhận tham số, trả về một decorator (hàm nhận hàm khác). Cú pháp: `@decorator_factory(arg)`.

**Ví dụ:**
```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Xin chào")

say_hello()
```
**Output:**
```
Xin chào
Xin chào
Xin chào
```

#### 1.1.3. Decorator Chaining

Nhiều decorator có thể được áp dụng cho cùng một hàm/lớp, thực thi theo thứ tự từ dưới lên (gần hàm nhất chạy trước).

**Giải thích:**
Khi nhiều decorator được áp dụng, chúng được lồng vào nhau. Decorator đầu tiên (trên cùng) sẽ bao bọc decorator tiếp theo, và cuối cùng bao bọc hàm gốc.

**Ví dụ:**
```python
def decorator1(func):
    def wrapper():
        print("Decorator 1 trước")
        func()
        print("Decorator 1 sau")
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2 trước")
        func()
        print("Decorator 2 sau")
    return wrapper

@decorator1
@decorator2
def my_function():
    print("Hàm gốc")

my_function()
```
**Output:**
```
Decorator 1 trước
Decorator 2 trước
Hàm gốc
Decorator 2 sau
Decorator 1 sau
```

### 1.2. Metaclasses (Tổng hợp)

Metaclass là lớp của các lớp, kiểm soát việc tạo và hành vi của lớp. Mọi lớp trong Python đều là instance của một metaclass (mặc định là `type`).

#### 1.2.1. `type` Class

`type` là metaclass mặc định của tất cả các lớp. Nó có thể được dùng để tạo lớp động: `type(name, bases, dict)`.

**Giải thích:**
- `name`: Tên lớp (string).
- `bases`: Tuple chứa các lớp cơ sở.
- `dict`: Dictionary chứa namespace của lớp (thuộc tính, phương thức).

**Ví dụ:**
```python
# Tạo lớp động bằng type
MyDynamicClass = type('MyDynamicClass', (), {'x': 10, 'get_x': lambda self: self.x})

obj = MyDynamicClass()
print(obj.x)
print(obj.get_x())
```
**Output:**
```
10
10
```

#### 1.2.2. Custom Metaclasses

Custom metaclass được tạo bằng cách kế thừa từ `type` và ghi đè các phương thức như `__new__` hoặc `__init__`.

**Giải thích:**
- `__new__`: Được gọi để tạo lớp (trước `__init__`). Nhận `metacls`, `name`, `bases`, `dict`.
- `__init__`: Được gọi sau khi lớp được tạo, để khởi tạo lớp.

**Ví dụ:**
```python
class MyMeta(type):
    def __new__(metacls, name, bases, dict):
        dict['added_by_meta'] = "Thuộc tính được thêm bởi metaclass"
        return super().__new__(metacls, name, bases, dict)

class MyClass(metaclass=MyMeta):
    pass

print(MyClass.added_by_meta)
```
**Output:**
```
Thuộc tính được thêm bởi metaclass
```

#### 1.2.3. Metaclass Use Cases

Metaclass thường dùng cho:
- Validation: Kiểm tra định dạng lớp khi tạo.
- Registration: Tự động đăng ký lớp vào một registry.
- Singleton: Đảm bảo chỉ có một instance của lớp.

**Ví dụ Singleton với Metaclass:**
```python
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class SingletonClass(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

obj1 = SingletonClass(10)
obj2 = SingletonClass(20)
print(obj1 is obj2)
print(obj1.value, obj2.value)
```
**Output:**
```
True
10 10
```

### 1.3. Descriptors (Tổng hợp)

Descriptor là một đối tượng có phương thức `__get__`, `__set__`, hoặc `__delete__`, được dùng để quản lý truy cập thuộc tính của một đối tượng khác.

#### 1.3.1. Data Descriptors vs Non-data Descriptors

- **Data descriptor:** Có ít nhất một trong `__set__` hoặc `__delete__`. Ưu tiên cao hơn non-data descriptor.
- **Non-data descriptor:** Chỉ có `__get__`.

**Giải thích:**
Khi truy cập thuộc tính, Python tìm kiếm theo thứ tự: data descriptor trong lớp, thuộc tính instance, non-data descriptor trong lớp, thuộc tính lớp, ...

**Ví dụ:**
```python
class DataDescriptor:
    def __get__(self, obj, objtype=None):
        return "DataDescriptor __get__"
    def __set__(self, obj, value):
        print("DataDescriptor __set__", value)

class NonDataDescriptor:
    def __get__(self, obj, objtype=None):
        return "NonDataDescriptor __get__"

class MyClass:
    data_desc = DataDescriptor()
    non_data_desc = NonDataDescriptor()

obj = MyClass()
print(obj.data_desc)
obj.data_desc = 100
print(obj.non_data_desc)
obj.non_data_desc = 200  # Ghi đè non-data descriptor
print(obj.non_data_desc)
```
**Output:**
```
DataDescriptor __get__
DataDescriptor __set__ 100
NonDataDescriptor __get__
200
```

#### 1.3.2. Descriptor Protocol

Descriptor protocol gồm:
- `__get__(self, obj, objtype=None)`: Trả về giá trị thuộc tính.
- `__set__(self, obj, value)`: Thiết lập giá trị thuộc tính.
- `__delete__(self, obj)`: Xóa thuộc tính.

**Ví dụ:**
```python
class ValidatedAttribute:
    def __init__(self):
        self.value = None
    def __get__(self, obj, objtype=None):
        return self.value
    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise TypeError("Giá trị phải là số nguyên")
        self.value = value

class MyClass:
    attr = ValidatedAttribute()

obj = MyClass()
obj.attr = 42
print(obj.attr)
obj.attr = "không phải số"  # Lỗi
```
**Output:**
```
42
TypeError: Giá trị phải là số nguyên
```

### 1.4. Code Generation

Code generation liên quan đến tạo và thực thi code động trong thời gian chạy, sử dụng các hàm như `eval()`, `exec()`, và module `ast`.

#### 1.4.1. `eval()`, `exec()`

- `eval(expression, globals=None, locals=None)`: Đánh giá biểu thức Python (một string) và trả về giá trị.
- `exec(object, globals=None, locals=None)`: Thực thi code Python (có thể là string, code object) và trả về `None`.

**Giải thích:**
- `eval` chỉ xử lý biểu thức đơn (như `x + y`), không xử lý câu lệnh (như `if`, `def`).
- `exec` có thể xử lý khối code nhiều câu lệnh.
- Cả hai đều tiềm ẩn rủi ro bảo mật nếu dùng với input không tin cậy.

**Ví dụ:**
```python
x = 10
y = 20
result = eval('x + y')
print("eval result:", result)

code = """
def hello(name):
    return f'Xin chào {name}'
print(hello('Python'))
"""
exec(code)
```
**Output:**
```
eval result: 30
Xin chào Python
```

#### 1.4.2. `ast` Module

Module `ast` (Abstract Syntax Trees) cho phép phân tích cú pháp code Python thành cây cú pháp, có thể sửa đổi và biên dịch lại.

**Giải thích:**
- `ast.parse(source)`: Phân tích source code thành AST.
- `ast.dump(node)`: Hiển thị cấu trúc AST.
- `compile(node, filename, mode)`: Biên dịch AST thành code object.
- `exec()` hoặc `eval()` có thể chạy code object.

**Ví dụ:**
```python
import ast

code = "x = 10 + 20"
tree = ast.parse(code)
print(ast.dump(tree, indent=2))

# Sửa đổi AST: thay 20 bằng 30
for node in ast.walk(tree):
    if isinstance(node, ast.Constant) and node.value == 20:
        node.value = 30

compiled = compile(tree, '<string>', 'exec')
exec(compiled)
print(x)  # x được tạo bởi code đã thực thi
```
**Output:**
```
Module(
  body=[
    Assign(
      targets=[
        Name(id='x', ctx=Store())],
      value=BinOp(
        left=Constant(value=10),
        op=Add(),
        right=Constant(value=20)))],
  type_ignores=[])
40
```

#### 1.4.3. `codeop` Module

Module `codeop` cung cấp các tiện ích để biên dịch code không đầy đủ (như trong môi trường tương tác), hỗ trợ biên dịch từng phần.

**Giải thích:**
- `codeop.compile_command(source, filename="<input>", symbol="single")`: Biên dịch một lệnh, trả về code object nếu lệnh hoàn chỉnh, ngược lại trả về `None`.

**Ví dụ:**
```python
import codeop

compiler = codeop.compile_command
code1 = "x = 10"
code2 = "x = 10; y = 20"
code3 = "if x > 5:"  # thiếu

print(compiler(code1) is not None)
print(compiler(code2) is not None)
print(compiler(code3) is not None)
```
**Output:**
```
True
True
False
```

## 2. CONCURRENCY & PARALLELISM

Concurrency (đồng thời) và parallelism (song song) là các kỹ thuật để thực hiện nhiều tác vụ cùng lúc, nhằm cải thiện hiệu suất.

### 2.1. Threading (Advanced)

Threading cho phép chạy nhiều luồng (thread) trong cùng một tiến trình (process), chia sẻ bộ nhớ. Tuy nhiên, do Global Interpreter Lock (GIL), chỉ một luồng có thể thực thi bytecode Python tại một thời điểm.

#### 2.1.1. Thread Pools

Thread pool quản lý một nhóm luồng được tạo trước, tránh chi phí tạo/hủy luồng liên tục. Sử dụng `ThreadPoolExecutor` từ `concurrent.futures`.

**Giải thích:**
- `ThreadPoolExecutor(max_workers)`: Tạo pool với số luồng tối đa.
- `submit(func, *args, **kwargs)`: Gửi tác vụ đến pool, trả về Future object.
- `map(func, iterable)`: Ánh xạ hàm lên iterable, trả về iterator của kết quả.

**Ví dụ:**
```python
from concurrent.futures import ThreadPoolExecutor
import time

def task(n):
    time.sleep(1)
    return n * n

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(task, i) for i in range(5)]
    for future in futures:
        print(future.result())
```
**Output:**
```
0
1
4
9
16
```

#### 2.1.2. Thread Synchronization

Khi nhiều luồng truy cập tài nguyên dùng chung, cần đồng bộ để tránh race condition. Các công cụ đồng bộ: `Lock`, `RLock`, `Semaphore`, `Event`, `Condition`.

**Giải thích:**
- `Lock`: Khóa đơn giản, chỉ một luồng giữ khóa tại một thời điểm.
- `RLock`: Khóa có thể nhập lại (reentrant), cho phép cùng luồng giữ nhiều lần.
- `Semaphore`: Giới hạn số luồng truy cập tài nguyên.
- `Event`: Cho phép luồng chờ tín hiệu từ luồng khác.
- `Condition`: Kết hợp khóa và điều kiện, cho phép luồng chờ điều kiện thỏa mãn.

**Ví dụ với Lock:**
```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        lock.acquire()
        counter += 1
        lock.release()

threads = []
for _ in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Counter:", counter)
```
**Output:**
```
Counter: 500000
```

#### 2.1.3. Thread Communication

Các luồng có thể giao tiếp thông qua cơ chế chia sẻ bộ nhớ (biến toàn cục, queue). Module `queue` cung cấp hàng đợi an toàn cho luồng.

**Giải thích:**
- `Queue`: Hàng đợi FIFO (First-In-First-Out).
- `LifoQueue`: Hàng đợi LIFO (Last-In-First-Out).
- `PriorityQueue`: Hàng đợi ưu tiên.

**Ví dụ:**
```python
import threading
import queue
import time

def producer(q):
    for i in range(5):
        time.sleep(0.5)
        q.put(i)
        print(f"Producer: put {i}")
    q.put(None)  # Tín hiệu kết thúc

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumer: got {item}")
        q.task_done()

q = queue.Queue()
t1 = threading.Thread(target=producer, args=(q,))
t2 = threading.Thread(target=consumer, args=(q,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Hoàn thành")
```
**Output:**
```
Producer: put 0
Consumer: got 0
Producer: put 1
Consumer: got 1
Producer: put 2
Consumer: got 2
Producer: put 3
Consumer: got 3
Producer: put 4
Consumer: got 4
Hoàn thành
```

### 2.2. Multiprocessing (Advanced)

Multiprocessing sử dụng nhiều tiến trình (process) thay vì luồng, mỗi tiến trình có bộ nhớ riêng và không bị ảnh hưởng bởi GIL, phù hợp cho CPU-bound tasks.

#### 2.2.1. Process Pools

Tương tự thread pool, process pool quản lý một nhóm tiến trình. Dùng `ProcessPoolExecutor` từ `concurrent.futures`.

**Giải thích:**
- `ProcessPoolExecutor(max_workers)`: Tạo pool với số tiến trình tối đa (thường bằng số CPU).
- Interface tương tự `ThreadPoolExecutor`.

**Ví dụ:**
```python
from concurrent.futures import ProcessPoolExecutor
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

numbers = range(10, 30)
with ProcessPoolExecutor() as executor:
    results = executor.map(is_prime, numbers)
    for num, prime in zip(numbers, results):
        print(f"{num}: {'số nguyên tố' if prime else 'hợp số'}")
```
**Output:**
```
10: hợp số
11: số nguyên tố
12: hợp số
13: số nguyên tố
14: hợp số
15: hợp số
16: hợp số
17: số nguyên tố
18: hợp số
19: số nguyên tố
20: hợp số
21: hợp số
22: hợp số
23: số nguyên tố
24: hợp số
25: hợp số
26: hợp số
27: hợp số
28: hợp số
29: số nguyên tố
```

#### 2.2.2. Shared Memory

Các tiến trình không chia sẻ bộ nhớ mặc định. Để chia sẻ dữ liệu, có thể dùng shared memory thông qua `multiprocessing.Value` và `multiprocessing.Array`.

**Giải thích:**
- `Value(typecode, value)`: Tạo biến chia sẻ của kiểu C (như 'i' cho int, 'd' cho double).
- `Array(typecode, sequence)`: Tạo mảng chia sẻ.

**Ví dụ:**
```python
import multiprocessing

def worker(val, arr):
    val.value += 1
    for i in range(len(arr)):
        arr[i] *= 2

if __name__ == '__main__':
    val = multiprocessing.Value('i', 0)
    arr = multiprocessing.Array('d', [1.0, 2.0, 3.0])
    p = multiprocessing.Process(target=worker, args=(val, arr))
    p.start()
    p.join()
    print("Giá trị:", val.value)
    print("Mảng:", list(arr))
```
**Output:**
```
Giá trị: 1
Mảng: [2.0, 4.0, 6.0]
```

#### 2.2.3. Process Communication

Các tiến trình có thể giao tiếp thông qua `Pipe` (ống nối) hoặc `Queue` (hàng đợi) từ module `multiprocessing`.

**Giải thích:**
- `Pipe()`: Trả về hai đầu nối (connection) để gửi/nhận dữ liệu.
- `Queue()`: Hàng đợi an toàn cho tiến trình.

**Ví dụ với Queue:**
```python
import multiprocessing
import time

def producer(q):
    for i in range(5):
        time.sleep(0.5)
        q.put(i)
        print(f"Producer: put {i}")
    q.put(None)

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumer: got {item}")

if __name__ == '__main__':
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=producer, args=(q,))
    p2 = multiprocessing.Process(target=consumer, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Hoàn thành")
```
**Output:**
```
Producer: put 0
Consumer: got 0
Producer: put 1
Consumer: got 1
Producer: put 2
Consumer: got 2
Producer: put 3
Consumer: got 3
Producer: put 4
Consumer: got 4
Hoàn thành
```

### 2.3. Asyncio (Advanced)

Asyncio là thư viện cho lập trình bất đồng bộ (asynchronous) sử dụng `async/await`, phù hợp cho I/O-bound tasks, cho phép chạy nhiều coroutine trên một luồng đơn.

#### 2.3.1. Event Loop Policies

Event loop policy kiểm soát việc tạo và quản lý event loop. Có thể tùy chỉnh bằng `asyncio.set_event_loop_policy()`.

**Giải thích:**
- Mặc định dùng `asyncio.DefaultEventLoopPolicy`.
- Có thể thay đổi cho các nền tảng khác nhau (Windows, Unix).

**Ví dụ:**
```python
import asyncio
import sys

async def main():
    await asyncio.sleep(1)
    print("Xong")

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

asyncio.run(main())
```
**Output:**
```
Xong
```

#### 2.3.2. Custom Event Loops

Có thể tạo event loop tùy chỉnh bằng cách kế thừa `asyncio.AbstractEventLoop`. Tuy nhiên, ít khi cần thiết.

**Ví dụ đơn giản:**
```python
import asyncio

async def task():
    print("Task đang chạy")
    await asyncio.sleep(1)
    print("Task hoàn thành")

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
try:
    loop.run_until_complete(task())
finally:
    loop.close()
```
**Output:**
```
Task đang chạy
Task hoàn thành
```

#### 2.3.3. Async Generators

Async generator là generator sử dụng `async def` và `yield`. Nó trả về một async iterator, có thể dùng với `async for`.

**Giải thích:**
- Khai báo: `async def gen(): yield value`
- Dùng `async for` để lặp.

**Ví dụ:**
```python
import asyncio

async def async_range(n):
    for i in range(n):
        await asyncio.sleep(0.1)
        yield i

async def main():
    async for num in async_range(5):
        print(num)

asyncio.run(main())
```
**Output:**
```
0
1
2
3
4
```

### 2.4. GIL (Global Interpreter Lock)

GIL là một khóa (lock) trong trình thông dịch CPython, chỉ cho phép một luồng thực thi bytecode Python tại một thời điểm.

#### 2.4.1. What is GIL?

GIL tồn tại để đơn giản hóa quản lý bộ nhớ (reference counting) và tích hợp với thư viện C. Nó ngăn chặn race condition khi nhiều luồng truy cập đối tượng Python.

**Giải thích:**
- GIL chỉ ảnh hưởng đến luồng thực thi bytecode Python.
- Các hoạt động I/O (như file, network) có thể giải phóng GIL trong khi chờ.
- Các thư viện C (như numpy) có thể giải phóng GIL khi thực hiện tính toán nặng.

#### 2.4.2. Working Around GIL

Để vượt qua hạn chế của GIL:
- Sử dụng multiprocessing thay vì threading cho CPU-bound tasks.
- Sử dụng async I/O cho I/O-bound tasks.
- Sử dụng các thư viện được viết bằng C và giải phóng GIL.

#### 2.4.3. So sánh Threading, Multiprocessing, Asyncio

| Tiêu chí | Threading | Multiprocessing | Asyncio |
|----------|-----------|-----------------|---------|
| **Mô hình** | Đa luồng trong một tiến trình | Đa tiến trình | Đơn luồng, đa nhiệm bất đồng bộ |
| **Bộ nhớ** | Chia sẻ | Riêng biệt | Chia sẻ |
| **GIL** | Bị ảnh hưởng | Không ảnh hưởng | Không ảnh hưởng (chạy trên một luồng) |
| **Phù hợp** | I/O-bound tasks, GUI | CPU-bound tasks | I/O-bound tasks, network |
| **Độ phức tạp** | Trung bình | Cao | Cao (cần hiểu async/await) |

### 2.5. `concurrent.futures` Module

Module này cung cấp high-level interface cho việc chạy các tác vụ đồng thời, với `ThreadPoolExecutor` và `ProcessPoolExecutor`.

#### 2.5.1. `ThreadPoolExecutor`

Đã trình bày ở phần 2.1.1.

#### 2.5.2. `ProcessPoolExecutor`

Đã trình bày ở phần 2.2.1.

#### 2.5.3. Future Objects

Future đại diện cho kết quả tính toán chưa hoàn thành. Có thể kiểm tra trạng thái (`done()`, `cancelled()`), lấy kết quả (`result()`), hoặc thêm callback (`add_done_callback()`).

**Giải thích:**
- `Future` được trả về bởi `submit()`.
- `result()` sẽ chờ đến khi có kết quả hoặc ném exception nếu có lỗi.
- `add_done_callback(callback)` gọi hàm callback khi Future hoàn thành.

**Ví dụ:**
```python
from concurrent.futures import ThreadPoolExecutor
import time

def task(n):
    time.sleep(1)
    return n * 2

def callback(future):
    print("Callback được gọi với kết quả:", future.result())

with ThreadPoolExecutor() as executor:
    future = executor.submit(task, 10)
    future.add_done_callback(callback)
    print("Kết quả từ result():", future.result())
```
**Output:**
```
Kết quả từ result(): 20
Callback được gọi với kết quả: 20
```

## 3. MEMORY MANAGEMENT & OPTIMIZATION

Quản lý bộ nhớ trong Python được thực hiện tự động thông qua reference counting và garbage collector.

### 3.1. Memory Management Basics

#### 3.1.1. Reference Counting

Mỗi đối tượng Python có một bộ đếm tham chiếu (reference count). Khi tham chiếu đến đối tượng được tạo, bộ đếm tăng; khi tham chiếu bị xóa, bộ đếm giảm. Khi bộ đếm về 0, bộ nhớ được giải phóng.

**Giải thích:**
- Có thể kiểm tra reference count bằng `sys.getrefcount(obj)`. Lưu ý: hàm này tăng thêm 1 reference tạm thời.
- Các thao tác như gán biến, truyền đối số đều tăng reference count.

**Ví dụ:**
```python
import sys

a = []
print("Reference count ban đầu:", sys.getrefcount(a))  # Tăng 1 do truyền vào getrefcount

b = a
print("Sau khi gán b = a:", sys.getrefcount(a))

del b
print("Sau khi del b:", sys.getrefcount(a))
```
**Output:**
```
Reference count ban đầu: 2
Sau khi gán b = a: 3
Sau khi del b: 2
```

#### 3.1.2. Garbage Collection (3 Generations)

Bộ thu gom rác (garbage collector) xử lý các reference cycles (vòng tham chiếu) mà reference counting không giải quyết được. Python sử dụng generational GC với 3 thế hệ (generation).

**Giải thích:**
- Generation 0: chứa các đối tượng mới.
- Generation 1: chứa đối tượng sống sót sau vài lần thu gom ở gen 0.
- Generation 2: chứa đối tượng sống lâu.
- GC chạy khi số lượng đối tượng vượt ngưỡng.
- Có thể điều khiển bằng module `gc`.

**Ví dụ:**
```python
import gc

print("GC enabled:", gc.isenabled())
print("Ngưỡng GC:", gc.get_threshold())
print("Số đối tượng trong mỗi gen:", gc.get_count())

# Tạo reference cycle
class Node:
    def __init__(self):
        self.next = None

a = Node()
b = Node()
a.next = b
b.next = a

# Xóa reference
del a
del b

# Thu gom rác
collected = gc.collect()
print("Số đối tượng được thu gom:", collected)
```
**Output:**
```
GC enabled: True
Ngưỡng GC: (700, 10, 10)
Số đối tượng trong mỗi gen: (15, 0, 0)
Số đối tượng được thu gom: 4
```

#### 3.1.3. Circular References

Reference cycle xảy ra khi các đối tượng tham chiếu lẫn nhau, tạo thành vòng. Reference counting không giải phóng được, cần GC.

**Ví dụ:**
```python
import gc

class MyClass:
    def __init__(self, name):
        self.name = name
        self.other = None

obj1 = MyClass("A")
obj2 = MyClass("B")
obj1.other = obj2
obj2.other = obj1

del obj1, obj2
print("Trước GC:", gc.get_count())
gc.collect()
print("Sau GC:", gc.get_count())
```
**Output:**
```
Trước GC: (16, 0, 0)
Sau GC: (0, 0, 0)
```

### 3.2. Optimization Techniques

#### 3.2.1. `__slots__` (So sánh với `__dict__`)

`__slots__` cho phép lớp khai báo trước các thuộc tính instance, tiết kiệm bộ nhớ bằng cách ngăn tạo `__dict__` cho mỗi instance.

**Giải thích:**
- Mặc định, mỗi instance có `__dict__` lưu thuộc tính dưới dạng dictionary, tốn bộ nhớ.
- `__slots__` thay thế `__dict__` bằng một cấu trúc cố định.
- Không thể thêm thuộc tính mới ngoài những thuộc tính đã khai báo.

**So sánh:**

| Đặc điểm | Có `__dict__` (mặc định) | Có `__slots__` |
|----------|--------------------------|----------------|
| Bộ nhớ | Lớn hơn (do dict) | Nhỏ hơn |
| Tốc độ truy cập thuộc tính | Chậm hơn | Nhanh hơn |
| Thêm thuộc tính động | Được | Không được |
| Kế thừa | Hoạt động bình thường | Cần xử lý cẩn thận |

**Ví dụ:**
```python
import sys

class WithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class WithSlots:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj1 = WithoutSlots(1, 2)
obj2 = WithSlots(1, 2)

print("Kích thước WithoutSlots:", sys.getsizeof(obj1) + sys.getsizeof(obj1.__dict__))
print("Kích thước WithSlots:", sys.getsizeof(obj2))
```
**Output:**
```
Kích thước WithoutSlots: 152
Kích thước WithSlots: 56
```

#### 3.2.2. Memory Views

Memory view (`memoryview`) cho phép truy cập dữ liệu nhị phân của đối tượng hỗ trợ buffer protocol (như `bytes`, `bytearray`, `array`) mà không cần sao chép.

**Giải thích:**
- Hữu ích khi xử lý dữ liệu lớn, tránh copy.
- Có thể cắt (slice) và thay đổi nếu đối tượng gốc mutable.

**Ví dụ:**
```python
data = bytearray(b'abcdef')
mv = memoryview(data)
print("Memory view:", mv)
print("Truy cập phần tử:", mv[2])  # 99 (b'c')
mv[2] = 122  # 'z'
print("Sau khi sửa:", data)
```
**Output:**
```
Memory view: <memory at 0x...>
Truy cập phần tử: 99
Sau khi sửa: bytearray(b'abzdef')
```

#### 3.2.3. Weak References (`weakref` module)

Weak reference là một tham chiếu không tăng reference count, cho phép đối tượng được giải phóng bởi GC ngay cả khi còn weak reference.

**Giải thích:**
- Dùng khi cần theo dõi đối tượng nhưng không muốn ngăn giải phóng bộ nhớ.
- `weakref.ref(obj)` tạo weak reference.
- `weakref.WeakSet`, `weakref.WeakValueDictionary` là các collection sử dụng weak reference.

**Ví dụ:**
```python
import weakref

class MyClass:
    pass

obj = MyClass()
r = weakref.ref(obj)
print("Weak ref trước khi xóa:", r())
del obj
print("Weak ref sau khi xóa:", r())
```
**Output:**
```
Weak ref trước khi xóa: <__main__.MyClass object at 0x...>
Weak ref sau khi xóa: None
```

#### 3.2.4. Array Module (`array`)

Module `array` cung cấp kiểu mảng hiệu quả về bộ nhớ, lưu trữ các phần tử cùng kiểu C.

**Giải thích:**
- Khai báo: `array(typecode, initializer)`.
- Typecode xác định kiểu dữ liệu (ví dụ: 'i' cho int, 'd' cho double).
- Tiết kiệm bộ nhớ hơn list cho số lượng lớn phần tử cùng kiểu.

**Ví dụ:**
```python
import array
import sys

arr = array.array('i', [1, 2, 3, 4, 5])
print("Mảng:", arr)
print("Kích thước mảng:", sys.getsizeof(arr))
lst = [1, 2, 3, 4, 5]
print("Kích thước list:", sys.getsizeof(lst))
```
**Output:**
```
Mảng: array('i', [1, 2, 3, 4, 5])
Kích thước mảng: 92
Kích thước list: 104
```

#### 3.2.5. Generator Expressions

Generator expression tạo generator một cách ngắn gọn, tiết kiệm bộ nhớ vì không tạo toàn bộ danh sách ngay lập tức.

**Giải thích:**
- Cú pháp: `(expression for item in iterable if condition)`.
- Trả về một generator, có thể lặp từng phần tử.

**Ví dụ:**
```python
import sys

# List comprehension: tạo list toàn bộ
list_comp = [x**2 for x in range(1000)]
print("Kích thước list comprehension:", sys.getsizeof(list_comp))

# Generator expression: tạo generator
gen_exp = (x**2 for x in range(1000))
print("Kích thước generator expression:", sys.getsizeof(gen_exp))
```
**Output:**
```
Kích thước list comprehension: 8856
Kích thước generator expression: 112
```

#### 3.2.6. String Interning

String interning là cơ chế lưu trữ duy nhất một bản sao của các chuỗi giống nhau. Python tự động intern một số chuỗi (như identifier, chuỗi ngắn). Có thể thủ công với `sys.intern()`.

**Giải thích:**
- Giảm bộ nhớ và tăng tốc so sánh (vì so sánh địa chỉ).
- `sys.intern(string)` trả về interned string.

**Ví dụ:**
```python
import sys

a = "hello"
b = "hello"
print("a is b?", a is b)  # True, Python tự động intern

c = "hello world!"
d = "hello world!"
print("c is d?", c is d)  # Có thể False nếu chuỗi dài

e = sys.intern("hello world!")
f = sys.intern("hello world!")
print("e is f?", e is f)  # True
```
**Output:**
```
a is b? True
c is d? False
e is f? True
```

### 3.3. Performance Profiling

Profiling giúp phân tích hiệu suất, tìm điểm nghẽn (bottleneck).

#### 3.3.1. `cProfile`

`cProfile` là profiler cung cấp thống kê chi tiết về thời gian thực thi của từng hàm.

**Giải thích:**
- Chạy: `python -m cProfile script.py`.
- Có thể lập trình với `cProfile.run()`.

**Ví dụ:**
```python
import cProfile

def fast_function():
    return sum(range(1000))

def slow_function():
    total = 0
    for i in range(1000):
        for j in range(1000):
            total += i * j
    return total

def main():
    fast_function()
    slow_function()

cProfile.run('main()', sort='time')
```
**Output:**
```
         2002 function calls in 0.125 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.124    0.124    0.124    0.124 <ipython-input-...>:7(slow_function)
        1    0.001    0.001    0.001    0.001 <ipython-input-...>:3(fast_function)
        1    0.000    0.000    0.125    0.125 <ipython-input-...>:15(main)
        1    0.000    0.000    0.125    0.125 {built-in method builtins.exec}
...
```

#### 3.3.2. `line_profiler`

`line_profiler` cung cấp thông tin chi tiết theo từng dòng code, cần cài đặt thêm (`pip install line_profiler`).

**Ví dụ:**
```python
# Lưu thành file test_profile.py
def my_function():
    total = 0
    for i in range(100):
        for j in range(100):
            total += i * j
    return total

if __name__ == '__main__':
    my_function()
```
Chạy trong terminal:
```
kernprof -l -v test_profile.py
```
**Output mẫu:**
```
Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def my_function():
     2         1          1.0      1.0      0.0      total = 0
     3       101         22.0      0.2      0.1      for i in range(100):
     4     10100       2148.0      0.2     10.9          for j in range(100):
     5   1000000     17456.0      0.0     88.9              total += i * j
     6         1          1.0      1.0      0.0      return total
```

#### 3.3.3. `memory_profiler`

`memory_profiler` theo dõi sử dụng bộ nhớ theo từng dòng, cần cài đặt (`pip install memory_profiler`).

**Ví dụ:**
```python
# Lưu thành file test_memory.py
from memory_profiler import profile

@profile
def my_function():
    a = [1] * 1000000
    b = [2] * 2000000
    del b
    return a

if __name__ == '__main__':
    my_function()
```
Chạy trong terminal:
```
python -m memory_profiler test_memory.py
```
**Output mẫu:**
```
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     2     38.0 MiB     38.0 MiB           1   @profile
     3                                         def my_function():
     4     45.5 MiB      7.5 MiB           1       a = [1] * 1000000
     5     60.8 MiB     15.3 MiB           1       b = [2] * 2000000
     6     45.5 MiB    -15.3 MiB           1       del b
     7     45.5 MiB      0.0 MiB           1       return a
```

### 3.4. Optimization Strategies

#### 3.4.1. Algorithm Optimization (Complexity)

Chọn thuật toán và cấu trúc dữ liệu phù hợp để giảm độ phức tạp thời gian và bộ nhớ.

**Ví dụ:** Sử dụng set cho tìm kiếm nhanh O(1) thay vì list O(n).

```python
import time

# List O(n)
my_list = list(range(10000))
start = time.time()
5000 in my_list
print("List search time:", time.time() - start)

# Set O(1)
my_set = set(range(10000))
start = time.time()
5000 in my_set
print("Set search time:", time.time() - start)
```
**Output:**
```
List search time: 0.00010609626770019531
Set search time: 3.0040740966796875e-06
```

#### 3.4.2. Built-in Functions

Sử dụng hàm built-in (viết bằng C) thay vì viết vòng lặp Python, vì chúng nhanh hơn.

**Ví dụ:**
```python
import time

data = list(range(1000000))

# Vòng lặp Python
start = time.time()
total = 0
for x in data:
    total += x
print("Vòng lặp Python:", time.time() - start)

# Hàm built-in sum
start = time.time()
total = sum(data)
print("Hàm sum built-in:", time.time() - start)
```
**Output:**
```
Vòng lặp Python: 0.058847665786743164
Hàm sum built-in: 0.007978200912475586
```

#### 3.4.3. Local Variables Lookup

Truy cập biến local nhanh hơn biến global hoặc built-in. Có thể gán biến global vào local để tăng tốc.

**Ví dụ:**
```python
import time
import math

def slow():
    total = 0
    for i in range(1000000):
        total += math.sin(i)  # Truy cập math.sin mỗi lần
    return total

def fast():
    total = 0
    sin = math.sin  # Gán vào biến local
    for i in range(1000000):
        total += sin(i)
    return total

start = time.time()
slow()
print("Slow:", time.time() - start)
start = time.time()
fast()
print("Fast:", time.time() - start)
```
**Output:**
```
Slow: 0.238389253616333
Fast: 0.18205904960632324
```

#### 3.4.4. String Concatenation (`join()` vs `+`)

Khi nối nhiều chuỗi, `join()` hiệu quả hơn `+` vì `+` tạo chuỗi mới mỗi lần.

**Giải thích:**
- `+`: Tạo chuỗi trung gian, độ phức tạp O(n²).
- `join()`: Tính tổng độ dài rồi tạo chuỗi một lần, O(n).

**Ví dụ:**
```python
import time

# Dùng +
start = time.time()
s = ''
for i in range(10000):
    s += str(i)
print("Thời gian dùng +:", time.time() - start)

# Dùng join
start = time.time()
parts = [str(i) for i in range(10000)]
s = ''.join(parts)
print("Thời gian dùng join:", time.time() - start)
```
**Output:**
```
Thời gian dùng +: 0.0029931068420410156
Thời gian dùng join: 0.0019941329956054688
```

#### 3.4.5. Caching (`lru_cache`, `@cache` Python 3.9+)

Cache kết quả của hàm để tránh tính toán lại, đặc biệt với hàm đệ quy hoặc hàm tốn kém.

**Ví dụ:**
```python
from functools import lru_cache
import time

# Không cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

start = time.time()
result = fib(30)
print("Không cache:", time.time() - start, "kết quả:", result)

# Có cache
@lru_cache(maxsize=None)
def fib_cached(n):
    if n < 2:
        return n
    return fib_cached(n-1) + fib_cached(n-2)

start = time.time()
result = fib_cached(30)
print("Có cache:", time.time() - start, "kết quả:", result)
```
**Output:**
```
Không cache: 0.3715202808380127 kết quả: 832040
Có cache: 2.09808349609375e-05 kết quả: 832040
```

## 4. TESTING VÀ DEBUGGING

### 4.1. Unit Testing

Unit test kiểm tra từng đơn vị code (hàm, phương thức) một cách biệt lập.

#### 4.1.1. `unittest` Module

`unittest` là framework testing có sẵn, lấy cảm hứng từ JUnit.

**Giải thích:**
- Tạo lớp kế thừa `unittest.TestCase`.
- Các phương thức test bắt đầu bằng `test_`.
- Sử dụng các assertion như `assertEqual`, `assertTrue`, `assertRaises`.

**Ví dụ:**
```python
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)

if __name__ == '__main__':
    unittest.main()
```
**Output:**
```
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

#### 4.1.2. `pytest` Framework

`pytest` là framework testing phổ biến, cần cài đặt (`pip install pytest`). Nó cung cấp cú pháp đơn giản và nhiều tính năng mạnh.

**Giải thích:**
- Không cần lớp, chỉ cần hàm bắt đầu bằng `test_`.
- Tự động phát hiện test.
- Có fixture, parameterized test.

**Ví dụ:**
```python
# Lưu thành file test_sample.py
def add(a, b):
    return a + b

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2
```
Chạy trong terminal:
```
pytest test_sample.py -v
```
**Output:**
```
============================= test session starts =============================
platform linux -- Python 3.x, pytest-7.x, pluggy-1.x
collected 2 items

test_sample.py::test_add_positive PASSED                                 [ 50%]
test_sample.py::test_add_negative PASSED                                 [100%]

============================== 2 passed in 0.01s ==============================
```

#### 4.1.3. Mocking (`unittest.mock`)

Mocking thay thế các phần phụ thuộc (như hàm, đối tượng) bằng đối tượng giả để cô lập unit test.

**Giải thích:**
- `Mock`: lớp mock cơ bản.
- `patch`: decorator/context manager để tạm thời thay thế đối tượng.

**Ví dụ:**
```python
from unittest.mock import Mock, patch

def get_data_from_api(url):
    # Giả sử gọi API
    pass

def process_data(url):
    data = get_data_from_api(url)
    return data.upper()

# Test với mock
def test_process_data():
    mock_data = Mock()
    mock_data.upper.return_value = "MOCKED"
    with patch('__main__.get_data_from_api', return_value=mock_data):
        result = process_data("http://example.com")
        assert result == "MOCKED"
        mock_data.upper.assert_called_once()

test_process_data()
print("Test passed")
```
**Output:**
```
Test passed
```

### 4.2. Integration Testing

Integration test kiểm tra sự tương tác giữa các module, component.

#### 4.2.1. Database Testing

Kiểm tra tương tác với database, thường dùng database trong bộ nhớ (SQLite) hoặc mock.

**Ví dụ với SQLite:**
```python
import sqlite3
import unittest

def create_table(conn):
    conn.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)''')

def insert_user(conn, name):
    conn.execute("INSERT INTO users (name) VALUES (?)", (name,))
    conn.commit()

def get_users(conn):
    cursor = conn.execute("SELECT name FROM users")
    return [row[0] for row in cursor]

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        create_table(self.conn)

    def tearDown(self):
        self.conn.close()

    def test_insert_and_get(self):
        insert_user(self.conn, 'Alice')
        insert_user(self.conn, 'Bob')
        users = get_users(self.conn)
        self.assertEqual(users, ['Alice', 'Bob'])

if __name__ == '__main__':
    unittest.main()
```
**Output:**
```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

#### 4.2.2. Web Application Testing

Kiểm tra ứng dụng web, thường dùng test client của framework (Flask, Django) hoặc thư viện như `requests`.

**Ví dụ với Flask test client:**
```python
from flask import Flask, jsonify
import unittest

app = Flask(__name__)

@app.route('/hello')
def hello():
    return jsonify(message='Hello, World!')

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello(self):
        response = self.app.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Hello, World!'})

if __name__ == '__main__':
    unittest.main()
```
**Output:**
```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

#### 4.2.3. API Testing

Kiểm tra API endpoints, có thể dùng `requests` hoặc test client.

**Ví dụ:**
```python
import requests
import unittest

class TestAPI(unittest.TestCase):
    def test_get_request(self):
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('userId', data)
        self.assertIn('id', data)
        self.assertIn('title', data)

if __name__ == '__main__':
    unittest.main()
```
**Output:**
```
.
----------------------------------------------------------------------
Ran 1 test in ...s

OK
```

### 4.3. Debugging Tools

#### 4.3.1. `pdb` (với các lệnh chi tiết)

`pdb` (Python Debugger) là debugger tích hợp, cho phép dừng chương trình, kiểm tra biến, chạy từng bước.

**Các lệnh cơ bản:**
- `l(ist)`: Hiển thị code xung quanh dòng hiện tại.
- `n(ext)`: Chạy dòng tiếp theo (không vào hàm).
- `s(tep)`: Chạy vào hàm.
- `c(ontinue)`: Tiếp tục chạy đến breakpoint tiếp theo.
- `b(reak)`: Đặt breakpoint.
- `p(rint)`: In giá trị biến.
- `q(uit)`: Thoát debugger.

**Ví dụ:**
```python
import pdb

def calculate_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total

pdb.set_trace()  # Dừng tại đây
result = calculate_sum(5)
print("Kết quả:", result)
```
Khi chạy, chương trình dừng tại `pdb.set_trace()`, có thể dùng các lệnh pdb.

#### 4.3.2. `breakpoint()` (Python 3.7+)

`breakpoint()` là hàm built-in gọi debugger (mặc định là pdb). Có thể tùy chỉnh bằng biến môi trường `PYTHONBREAKPOINT`.

**Ví dụ:**
```python
def buggy_function(x):
    breakpoint()  # Dừng tại đây
    return x / 0

buggy_function(10)
```
Khi chạy, chương trình dừng tại `breakpoint()` và vào pdb.

#### 4.3.3. Post-mortem Debugging

Debug sau khi chương trình crash, tự động vào pdb khi có exception.

**Cách 1:** Dùng `python -m pdb script.py`.
**Cách 2:** Trong code:
```python
import pdb

def faulty():
    return 1 / 0

try:
    faulty()
except:
    pdb.post_mortem()  # Vào pdb sau khi exception xảy ra
```

### 4.4. Code Coverage

Code coverage đo lường phần trăm code được chạy bởi test, giúp đánh giá độ toàn diện của test.

#### 4.4.1. `coverage.py`

`coverage.py` là công cụ đo coverage phổ biến, cần cài đặt (`pip install coverage`).

**Ví dụ:**
Tạo file `my_module.py`:
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def unused():
    return "Không được gọi"
```
Tạo file `test_my_module.py`:
```python
import unittest
from my_module import add, subtract

class TestMyModule(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5,3), 2)
```
Chạy coverage:
```
coverage run -m unittest test_my_module.py
coverage report -m
```
**Output:**
```
Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
my_module.py         6      1    83%   8
test_my_module.py    7      0   100%
-----------------------------------------------
TOTAL               13      1    92%
```

#### 4.4.2. `pytest-cov`

`pytest-cov` là plugin pytest cho coverage, cài đặt: `pip install pytest-cov`.

Chạy:
```
pytest --cov=my_module test_my_module.py
```
**Output:**
```
---------- coverage: platform linux, python 3.x ----------
Name              Stmts   Miss  Cover
-------------------------------------
my_module.py         6      1    83%
-------------------------------------
TOTAL                6      1    83%

============================= test session starts =============================
...
```

## 5. PACKAGING VÀ DISTRIBUTION

### 5.1. Package Structure

Cấu trúc package chuẩn giúp dễ dàng phân phối và cài đặt.

#### 5.1.1. Layout

Cấu trúc cơ bản:
```
mypackage/
├── mypackage/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
├── tests/
│   ├── __init__.py
│   └── test_mypackage.py
├── README.md
├── LICENSE
├── setup.py
├── setup.cfg
└── pyproject.toml
```

#### 5.1.2. `__init__.py`

File `__init__.py` biến thư mục thành package Python. Có thể để trống hoặc chứa code khởi tạo.

**Ví dụ:**
```python
# mypackage/__init__.py
from .module1 import MyClass
from .module2 import my_function

__version__ = '1.0.0'
__all__ = ['MyClass', 'my_function']
```

#### 5.1.3. `__main__.py`

File `__main__.py` cho phép chạy package như một script: `python -m mypackage`.

**Ví dụ:**
```python
# mypackage/__main__.py
from . import main

if __name__ == '__main__':
    main()
```

### 5.2. Configuration Files

#### 5.2.1. `setup.py`

`setup.py` là script dùng `setuptools` để định nghĩa package.

**Ví dụ:**
```python
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='1.0.0',
    author='Tên tác giả',
    description='Mô tả package',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25',
        'numpy>=1.19',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
```

#### 5.2.2. `setup.cfg`

`setup.cfg` là file cấu hình cho `setuptools`, có thể thay thế nhiều tham số trong `setup.py`.

**Ví dụ:**
```ini
[metadata]
name = mypackage
version = 1.0.0
author = Tên tác giả
description = Mô tả package

[options]
packages = find:
install_requires =
    requests>=2.25
    numpy>=1.19

[options.extras_require]
dev = pytest>=6.0

[flake8]
max-line-length = 88
```

#### 5.2.3. `pyproject.toml`

`pyproject.toml` là file cấu hình hiện đại (PEP 518), dùng chung cho nhiều công cụ (build system, linter, formatter).

**Ví dụ:**
```toml
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "mypackage"
version = "1.0.0"
authors = [
    {name = "Tên tác giả", email = "email@example.com"},
]
description = "Mô tả package"
requires-python = ">=3.7"
dependencies = [
    "requests>=2.25",
    "numpy>=1.19",
]

[project.optional-dependencies]
dev = ["pytest>=6.0", "black"]

[tool.black]
line-length = 88
```

### 5.3. Building Packages

#### 5.3.1. Source Distribution

Source distribution (sdist) chứa source code, có thể cần biên dịch.

Tạo:
```bash
python setup.py sdist
```
Hoặc với `build`:
```bash
python -m build --sdist
```

#### 5.3.2. Wheel Distribution

Wheel là định dạng phân phối nhị phân, cài đặt nhanh hơn.

Tạo:
```bash
python setup.py bdist_wheel
```
Hoặc với `build`:
```bash
python -m build --wheel
```

### 5.4. Publishing to PyPI

PyPI (Python Package Index) là kho package chính thức của Python.

#### 5.4.1. TestPyPI

TestPyPI là môi trường thử nghiệm để đăng package trước khi đăng lên PyPI chính.

Upload lên TestPyPI:
```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

#### 5.4.2. `twine`

`twine` là công cụ upload package lên PyPI, an toàn hơn `setup.py upload`.

Cài đặt: `pip install twine`
Upload lên PyPI:
```bash
twine upload dist/*
```

### 5.5. Private Package Repositories

Có thể host repository riêng cho package nội bộ.

#### 5.5.1. `devpi`

`devpi` là server lưu trữ package và mirror PyPI.

Cài đặt: `pip install devpi-server devpi-client`
Khởi động server:
```bash
devpi-server --start
```
Sử dụng client:
```bash
devpi use http://localhost:3141
devpi login root --password=
devpi index -c dev bases=root/pypi
devpi upload
```

#### 5.5.2. Nexus Repository

Nexus Repository Manager (của Sonatype) hỗ trợ nhiều định dạng, trong đó có PyPI.

Cấu hình pip để sử dụng Nexus:
```ini
# ~/.pip/pip.conf
[global]
index-url = http://nexus.example.com/repository/pypi-all/pypi
```

## 6. C INTEGRATION VÀ EXTENSIONS

### 6.1. `ctypes` Module

`ctypes` cho phép gọi hàm từ thư viện C (shared library) trực tiếp từ Python.

#### 6.1.1. Loading Shared Libraries

Có thể load thư viện động (.so trên Linux, .dll trên Windows, .dylib trên macOS).

**Ví dụ:**
```python
from ctypes import CDLL
import platform

if platform.system() == 'Linux':
    libc = CDLL('libc.so.6')
elif platform.system() == 'Windows':
    libc = CDLL('msvcrt.dll')
else:
    libc = CDLL('libc.dylib')
```

#### 6.1.2. Calling C Functions

Gọi hàm C, chuyển đổi kiểu dữ liệu tự động.

**Ví dụ:**
```python
from ctypes import cdll, c_double

libm = cdll.LoadLibrary('libm.so.6')  # Thư viện toán C
sqrt = libm.sqrt
sqrt.argtypes = [c_double]
sqrt.restype = c_double

result = sqrt(25.0)
print("Căn bậc hai của 25:", result)
```
**Output:**
```
Căn bậc hai của 25: 5.0
```

### 6.2. CFFI

CFFI (C Foreign Function Interface) cung cấp cách gọi code C từ Python, hỗ trợ cả ABI và API mode.

#### 6.2.1. ABI Mode

ABI (Application Binary Interface) mode tương tự ctypes, không cần compiler.

**Ví dụ:**
```python
from cffi import FFI

ffi = FFI()
ffi.cdef("int printf(const char *format, ...);")
C = ffi.dlopen(None)  # Load thư viện C chuẩn
C.printf(b"Hello, %s!\n", b"World")
```
**Output:**
```
Hello, World!
```

#### 6.2.2. API Mode

API mode cần compiler (như gcc), tạo module C extension.

**Ví dụ:**
Tạo file `build_my_module.py`:
```python
from cffi import FFI

ffi = FFI()
ffi.cdef("int add(int a, int b);")
ffi.set_source("_my_module", """
    int add(int a, int b) {
        return a + b;
    }
""")

if __name__ == "__main__":
    ffi.compile()
```
Chạy:
```bash
python build_my_module.py
```
Sau đó import module `_my_module`.

### 6.3. Writing C Extensions (C API)

Có thể viết extension bằng Python C API, cần kiến thức về C.

#### 6.3.1. Python C API

Python C API cung cấp các hàm và macro để tương tác với Python runtime.

**Ví dụ module C đơn giản:**
File `my_module.c`:
```c
#include <Python.h>

static PyObject* my_add(PyObject* self, PyObject* args) {
    int a, b;
    if (!PyArg_ParseTuple(args, "ii", &a, &b))
        return NULL;
    return PyLong_FromLong(a + b);
}

static PyMethodDef MyMethods[] = {
    {"add", my_add, METH_VARARGS, "Cộng hai số nguyên."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef mymodule = {
    PyModuleDef_HEAD_INIT,
    "my_module",
    NULL,
    -1,
    MyMethods
};

PyMODINIT_FUNC PyInit_my_module(void) {
    return PyModule_Create(&mymodule);
}
```

#### 6.3.2. Building Extensions

Dùng `setuptools` để biên dịch extension.

File `setup.py`:
```python
from setuptools import setup, Extension

module = Extension('my_module', sources=['my_module.c'])

setup(
    name='MyModule',
    version='1.0',
    ext_modules=[module],
)
```
Chạy:
```bash
python setup.py build_ext --inplace
```

### 6.4. Cython Introduction

Cython là ngôn ngữ lập trình siêu tập của Python, cho phép viết code Python với hiệu suất gần C, có thể biên dịch thành C extension.

#### 6.4.1. Cython Syntax

Cython mở rộng Python với các từ khóa như `cdef`, `cpdef`, và kiểu tĩnh.

**Ví dụ:**
File `cython_example.pyx`:
```cython
def py_add(a, b):
    return a + b

cdef int c_add(int a, int b):
    return a + b

cpdef int cp_add(int a, int b):
    return a + b
```

#### 6.4.2. Compiling Cython Code

Cần file `setup.py`:
```python
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("cython_example.pyx"),
)
```
Chạy:
```bash
python setup.py build_ext --inplace
```

## 7. NETWORK PROGRAMMING

### 7.1. Socket Programming

Socket là endpoint cho giao tiếp hai chiều giữa hai máy.

#### 7.1.1. TCP Sockets

TCP (Transmission Control Protocol) đảm bảo truyền dữ liệu tin cậy.

**Ví dụ TCP Server:**
```python
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Server đang lắng nghe...")

conn, addr = server_socket.accept()
print("Kết nối từ:", addr)
data = conn.recv(1024)
print("Nhận:", data.decode())
conn.sendall(b"Hello from server")
conn.close()
server_socket.close()
```

**Ví dụ TCP Client:**
```python
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))
client_socket.sendall(b"Hello from client")
data = client_socket.recv(1024)
print("Nhận:", data.decode())
client_socket.close()
```

#### 7.1.2. UDP Sockets

UDP (User Datagram Protocol) không đảm bảo tin cậy nhưng nhanh hơn.

**Ví dụ UDP Server:**
```python
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))
print("UDP Server đang lắng nghe...")

data, addr = server_socket.recvfrom(1024)
print("Nhận từ", addr, ":", data.decode())
server_socket.sendto(b"Hello from UDP server", addr)
server_socket.close()
```

**Ví dụ UDP Client:**
```python
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.sendto(b"Hello from UDP client", ('localhost', 12345))
data, addr = client_socket.recvfrom(1024)
print("Nhận:", data.decode())
client_socket.close()
```

#### 7.1.3. SSL/TLS Sockets

SSL/TLS mã hóa kết nối socket, dùng module `ssl`.

**Ví dụ SSL Server:**
```python
import socket, ssl

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

conn, addr = server_socket.accept()
ssl_conn = context.wrap_socket(conn, server_side=True)
data = ssl_conn.recv(1024)
print("Nhận (SSL):", data.decode())
ssl_conn.sendall(b"Hello from SSL server")
ssl_conn.close()
server_socket.close()
```

**Ví dụ SSL Client:**
```python
import socket, ssl

context = ssl.create_default_context()
# Nếu dùng self-signed cert, cần tắt verify
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_conn = context.wrap_socket(client_socket, server_hostname='localhost')
ssl_conn.connect(('localhost', 12345))
ssl_conn.sendall(b"Hello from SSL client")
data = ssl_conn.recv(1024)
print("Nhận (SSL):", data.decode())
ssl_conn.close()
```

### 7.2. HTTP Clients

#### 7.2.1. `requests` Library

`requests` là thư viện HTTP phổ biến, cài đặt: `pip install requests`.

**Ví dụ:**
```python
import requests

response = requests.get('https://api.github.com')
print("Status code:", response.status_code)
print("Headers:", response.headers['content-type'])
print("Nội dung (một phần):", response.text[:100])
```
**Output:**
```
Status code: 200
Headers: application/json; charset=utf-8
Nội dung (một phần): {"current_user_url":"https://api.github.com/user","current_user_authorizations_html_url":"https://github.com/settings/connections/applications{/client_id}"
```

#### 7.2.2. `aiohttp` (async)

`aiohttp` hỗ trợ HTTP client/server bất đồng bộ, cài đặt: `pip install aiohttp`.

**Ví dụ:**
```python
import aiohttp
import asyncio

async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.github.com') as response:
            print("Status:", response.status)
            text = await response.text()
            print("Nội dung (một phần):", text[:100])

asyncio.run(fetch())
```
**Output:**
```
Status: 200
Nội dung (một phần): {"current_user_url":"https://api.github.com/user","current_user_authorizations_html_url":"https://github.com/settings/connections/applications{/client_id}"
```

#### 7.2.3. HTTPX

HTTPX là thư viện HTTP hiện đại, hỗ trợ cả sync và async, cài đặt: `pip install httpx`.

**Ví dụ sync:**
```python
import httpx

response = httpx.get('https://api.github.com')
print("Status:", response.status_code)
print("Headers:", response.headers['content-type'])
```
**Ví dụ async:**
```python
import httpx
import asyncio

async def fetch():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://api.github.com')
        print("Status:", response.status_code)

asyncio.run(fetch())
```

### 7.3. SSH và SFTP

#### 7.3.1. `paramiko` Library

`paramiko` thực hiện SSH và SFTP, cài đặt: `pip install paramiko`.

**Ví dụ SSH:**
```python
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('hostname', username='user', password='pass')
stdin, stdout, stderr = ssh.exec_command('ls -l')
print(stdout.read().decode())
ssh.close()
```

**Ví dụ SFTP:**
```python
import paramiko

transport = paramiko.Transport(('hostname', 22))
transport.connect(username='user', password='pass')
sftp = paramiko.SFTPClient.from_transport(transport)
sftp.put('local_file.txt', 'remote_file.txt')
sftp.get('remote_file.txt', 'local_copy.txt')
sftp.close()
transport.close()
```

#### 7.3.2. `asyncssh`

`asyncssh` là thư viện SSH bất đồng bộ, cài đặt: `pip install asyncssh`.

**Ví dụ:**
```python
import asyncio
import asyncssh

async def run_client():
    async with asyncssh.connect('hostname', username='user', password='pass') as conn:
        result = await conn.run('ls -l')
        print(result.stdout)

asyncio.run(run_client())
```

### 7.4. FTP và SMTP

#### 7.4.1. `ftplib`

`ftplib` là module tích hợp cho FTP.

**Ví dụ:**
```python
from ftplib import FTP

ftp = FTP('ftp.example.com')
ftp.login(user='username', passwd='password')
ftp.cwd('/pub')
ftp.retrlines('LIST')
with open('local_file.txt', 'wb') as f:
    ftp.retrbinary('RETR remote_file.txt', f.write)
ftp.quit()
```

#### 7.4.2. `smtplib`

`smtplib` là module tích hợp cho SMTP (gửi email).

**Ví dụ:**
```python
import smtplib
from email.mime.text import MIMEText

msg = MIMEText('Nội dung email')
msg['Subject'] = 'Tiêu đề email'
msg['From'] = 'sender@example.com'
msg['To'] = 'receiver@example.com'

smtp = smtplib.SMTP('smtp.example.com', 587)
smtp.starttls()
smtp.login('username', 'password')
smtp.send_message(msg)
smtp.quit()
```

---

# PHẦN VIII: BEST PRACTICES VÀ DESIGN PATTERNS

## 1. CODE STYLE VÀ DOCUMENTATION

### 1.1. PEP 8 Guidelines

PEP 8 là hướng dẫn về style code cho Python, khuyến khích code dễ đọc và nhất quán.

#### 1.1.1. Indentation

Sử dụng **4 khoảng trắng** cho mỗi cấp độ thụt lề. Không dùng tab.

**Ví dụ:**
```python
def my_function():
    if condition:
        do_something()
    else:
        do_something_else()
```

#### 1.1.2. Line Length

Giới hạn dòng ở **79 ký tự** cho code, **72 ký tự** cho comment và docstring. Có thể ngắt dòng với dấu `\` hoặc trong ngoặc.

**Ví dụ:**
```python
# Ngắt dòng với dấu \
long_string = "Đây là một chuỗi rất dài, cần được ngắt ra để " \
              "tuân thủ PEP 8."

# Ngắt trong ngoặc
result = calculate(long_argument1, long_argument2,
                   long_argument3, long_argument4)
```

#### 1.1.3. Imports (order)

Sắp xếp import theo thứ tự:
1. Standard library imports.
2. Related third party imports.
3. Local application/library specific imports.

Mỗi nhóm cách nhau một dòng trắng.

**Ví dụ:**
```python
import os
import sys

import requests
import numpy as np

from mypackage import mymodule
```

#### 1.1.4. Naming Conventions

- **snake_case:** cho biến, hàm, phương thức, module (ví dụ: `my_variable`, `calculate_total`).
- **PascalCase:** cho lớp (ví dụ: `MyClass`, `HttpClient`).
- **UPPER_CASE:** cho hằng số (ví dụ: `MAX_SIZE`, `DEFAULT_TIMEOUT`).

**Ví dụ:**
```python
MAX_CONNECTIONS = 100

def calculate_average(numbers):
    pass

class DataProcessor:
    def process_data(self):
        pass
```

### 1.2. Code Organization

#### 1.2.1. Module Structure

Mỗi module nên có một mục đích rõ ràng. Các hàm liên quan nên được nhóm lại.

**Ví dụ:**
```python
# math_operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Không thể chia cho 0")
    return a / b
```

#### 1.2.2. Package Structure

Package nên được tổ chức theo chức năng. Sử dụng `__init__.py` để xuất các thành phần chính.

**Ví dụ:**
```
mypackage/
├── __init__.py
├── core.py
├── utils.py
└── io.py
```
`__init__.py`:
```python
from .core import CoreClass
from .utils import helper_function
from .io import read_file, write_file

__all__ = ['CoreClass', 'helper_function', 'read_file', 'write_file']
```

### 1.3. Documentation

#### 1.3.1. Docstrings

Docstring mô tả mục đích của module, lớp, hàm. Tuân theo PEP 257.

**Ví dụ:**
```python
def factorial(n):
    """
    Tính giai thừa của số nguyên không âm n.

    Args:
        n (int): Số nguyên cần tính giai thừa.

    Returns:
        int: Giai thừa của n.

    Raises:
        ValueError: Nếu n là số âm.
    """
    if n < 0:
        raise ValueError("n phải là số không âm")
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

#### 1.3.2. Sphinx

Sphinx là công cụ tạo tài liệu từ docstring, hỗ trợ nhiều định dạng (HTML, PDF).

Cài đặt: `pip install sphinx`
Khởi tạo: `sphinx-quickstart`
Tạo tài liệu: `sphinx-apidoc -o docs/ mypackage/`

#### 1.3.3. Type Hints

Type hints (PEP 484) giúp kiểm tra kiểu tĩnh, tăng khả năng đọc và hỗ trợ IDE.

**Ví dụ:**
```python
from typing import List, Optional

def greet_all(names: List[str]) -> None:
    for name in names:
        print(f"Hello, {name}!")

def find_index(items: List[int], target: int) -> Optional[int]:
    try:
        return items.index(target)
    except ValueError:
        return None
```

### 1.4. Type Hints Best Practices

#### 1.4.1. When to Use Type Hints

- Dự án lớn, nhiều người tham gia.
- Thư viện công khai.
- Khi cần kiểm tra kiểu với mypy.

Không bắt buộc cho script nhỏ, nhưng khuyến khích.

#### 1.4.2. Type Hinting Generics

Sử dụng `typing` module để hint generics.

**Ví dụ:**
```python
from typing import Dict, Tuple, Iterable

def process_dict(data: Dict[str, int]) -> List[Tuple[str, int]]:
    return [(k, v) for k, v in data.items()]

def flatten(items: Iterable[Iterable[int]]) -> List[int]:
    return [item for sublist in items for item in sublist]
```

#### 1.4.3. Type Checking Tools

- **mypy:** Kiểm tra kiểu tĩnh, cài đặt: `pip install mypy`. Chạy: `mypy my_module.py`.
- **pyright:** Công cụ của Microsoft, thường dùng trong VS Code.
- **pytype:** Của Google.

**Ví dụ với mypy:**
Tạo file `example.py`:
```python
def add(a: int, b: int) -> int:
    return a + b

result = add(5, "10")  # Lỗi kiểu
```
Chạy:
```bash
mypy example.py
```
**Output:**
```
example.py:5: error: Argument 2 to "add" has incompatible type "str"; expected "int"
Found 1 error in 1 file (checked 1 source file)
```

## 2. DESIGN PATTERNS

Design patterns là các giải pháp mẫu cho các vấn đề thường gặp trong thiết kế phần mềm.

### 2.1. Creational Patterns

#### 2.1.1. Singleton

Đảm bảo một lớp chỉ có một instance và cung cấp điểm truy cập toàn cục.

**Cách 1: Decorator**
```python
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    def __init__(self):
        print("Khởi tạo Database")

db1 = Database()
db2 = Database()
print(db1 is db2)
```
**Output:**
```
Khởi tạo Database
True
```

**Cách 2: Metaclass**
```python
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=SingletonMeta):
    def __init__(self):
        print("Khởi tạo Logger")

logger1 = Logger()
logger2 = Logger()
print(logger1 is logger2)
```
**Output:**
```
Khởi tạo Logger
True
```

#### 2.1.2. Factory

Cung cấp interface để tạo đối tượng, nhưng để lớp con quyết định lớp cụ thể nào được tạo.

**Ví dụ:**
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        return "Lái xe ô tô"

class Bike(Vehicle):
    def drive(self):
        return "Đạp xe đạp"

class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        else:
            raise ValueError(f"Không biết loại {vehicle_type}")

vehicle = VehicleFactory.get_vehicle("car")
print(vehicle.drive())
```
**Output:**
```
Lái xe ô tô
```

#### 2.1.3. Builder

Tách việc xây dựng đối tượng phức tạp khỏi biểu diễn của nó, cho phép cùng một quá trình xây dựng tạo ra các biểu diễn khác nhau.

**Ví dụ:**
```python
class Computer:
    def __init__(self, cpu, ram, storage):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
    
    def __str__(self):
        return f"CPU: {self.cpu}, RAM: {self.ram}GB, Storage: {self.storage}GB"

class ComputerBuilder:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
    
    def set_cpu(self, cpu):
        self.cpu = cpu
        return self
    
    def set_ram(self, ram):
        self.ram = ram
        return self
    
    def set_storage(self, storage):
        self.storage = storage
        return self
    
    def build(self):
        return Computer(self.cpu, self.ram, self.storage)

builder = ComputerBuilder()
computer = builder.set_cpu("Intel i7").set_ram(16).set_storage(512).build()
print(computer)
```
**Output:**
```
CPU: Intel i7, RAM: 16GB, Storage: 512GB
```

#### 2.1.4. Prototype

Tạo đối tượng mới bằng cách sao chép (clone) một đối tượng hiện có (prototype).

**Ví dụ:**
```python
import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class Car(Prototype):
    def __init__(self, model, color):
        self.model = model
        self.color = color
    
    def __str__(self):
        return f"{self.model} màu {self.color}"

original = Car("Toyota", "đỏ")
clone = original.clone()
clone.color = "xanh"
print("Original:", original)
print("Clone:", clone)
print("Cùng object?", original is clone)
```
**Output:**
```
Original: Toyota màu đỏ
Clone: Toyota màu xanh
Cùng object? False
```

### 2.2. Structural Patterns

#### 2.2.1. Adapter

Chuyển đổi interface của một lớp thành interface khác mà client mong đợi.

**Ví dụ:**
```python
class EuropeanSocket:
    def voltage(self):
        return 230

class USASocket:
    def voltage(self):
        return 110

class Adapter:
    def __init__(self, socket):
        self.socket = socket
    
    def voltage(self):
        if isinstance(self.socket, EuropeanSocket):
            return self.socket.voltage()
        elif isinstance(self.socket, USASocket):
            # Chuyển đổi điện áp
            return self.socket.voltage() * 2

european = EuropeanSocket()
adapter = Adapter(european)
print("Điện áp qua adapter:", adapter.voltage())
```
**Output:**
```
Điện áp qua adapter: 230
```

#### 2.2.2. Decorator

Đã trình bày trong phần Metaprogramming.

#### 2.2.3. Facade

Cung cấp một interface đơn giản hóa cho một hệ thống phức tạp.

**Ví dụ:**
```python
class CPU:
    def start(self):
        return "CPU khởi động"

class Memory:
    def load(self):
        return "Bộ nhớ tải dữ liệu"

class HardDrive:
    def read(self):
        return "Ổ cứng đọc dữ liệu"

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()
    
    def start_computer(self):
        results = []
        results.append(self.cpu.start())
        results.append(self.memory.load())
        results.append(self.hard_drive.read())
        return "\n".join(results)

facade = ComputerFacade()
print(facade.start_computer())
```
**Output:**
```
CPU khởi động
Bộ nhớ tải dữ liệu
Ổ cứng đọc dữ liệu
```

#### 2.2.4. Proxy

Cung cấp một đối tượng thay thế hoặc giữ chỗ cho một đối tượng khác để kiểm soát truy cập.

**Ví dụ:**
```python
class RealSubject:
    def request(self):
        return "RealSubject: Xử lý request."

class Proxy:
    def __init__(self, real_subject):
        self._real_subject = real_subject
    
    def request(self):
        if self.check_access():
            return self._real_subject.request()
        else:
            return "Proxy: Truy cập bị từ chối."
    
    def check_access(self):
        print("Proxy: Kiểm tra quyền truy cập.")
        return True

real = RealSubject()
proxy = Proxy(real)
print(proxy.request())
```
**Output:**
```
Proxy: Kiểm tra quyền truy cập.
RealSubject: Xử lý request.
```

### 2.3. Behavioral Patterns

#### 2.3.1. Observer

Định nghĩa sự phụ thuộc một-nhiều giữa các đối tượng, khi một đối tượng thay đổi trạng thái, tất cả các đối tượng phụ thuộc được thông báo và cập nhật tự động.

**Ví dụ:**
```python
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        pass

class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name
    
    def update(self, message):
        print(f"{self.name} nhận thông báo: {message}")

subject = Subject()
observer1 = ConcreteObserver("Observer 1")
observer2 = ConcreteObserver("Observer 2")
subject.attach(observer1)
subject.attach(observer2)
subject.notify("Sự kiện đã xảy ra!")
```
**Output:**
```
Observer 1 nhận thông báo: Sự kiện đã xảy ra!
Observer 2 nhận thông báo: Sự kiện đã xảy ra!
```

#### 2.3.2. Strategy

Định nghĩa một họ các thuật toán, đóng gói từng thuật toán và làm cho chúng có thể hoán đổi cho nhau.

**Ví dụ:**
```python
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class AddStrategy(Strategy):
    def execute(self, a, b):
        return a + b

class SubtractStrategy(Strategy):
    def execute(self, a, b):
        return a - b

class Context:
    def __init__(self, strategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy):
        self._strategy = strategy
    
    def execute_strategy(self, a, b):
        return self._strategy.execute(a, b)

context = Context(AddStrategy())
print("10 + 5 =", context.execute_strategy(10, 5))
context.set_strategy(SubtractStrategy())
print("10 - 5 =", context.execute_strategy(10, 5))
```
**Output:**
```
10 + 5 = 15
10 - 5 = 5
```

#### 2.3.3. Command

Đóng gói một yêu cầu như một đối tượng, cho phép tham số hóa client với các yêu cầu khác nhau.

**Ví dụ:**
```python
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Light:
    def turn_on(self):
        return "Đèn bật"
    
    def turn_off(self):
        return "Đèn tắt"

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        return self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        return self.light.turn_off()

class RemoteControl:
    def __init__(self):
        self.command = None
    
    def set_command(self, command):
        self.command = command
    
    def press_button(self):
        if self.command:
            return self.command.execute()
        return "Không có lệnh"

light = Light()
remote = RemoteControl()
remote.set_command(LightOnCommand(light))
print(remote.press_button())
remote.set_command(LightOffCommand(light))
print(remote.press_button())
```
**Output:**
```
Đèn bật
Đèn tắt
```

#### 2.3.4. State

Cho phép một đối tượng thay đổi hành vi khi trạng thái nội bộ của nó thay đổi.

**Ví dụ:**
```python
class State(ABC):
    @abstractmethod
    def handle(self, context):
        pass

class ConcreteStateA(State):
    def handle(self, context):
        print("Trạng thái A xử lý.")
        context.state = ConcreteStateB()

class ConcreteStateB(State):
    def handle(self, context):
        print("Trạng thái B xử lý.")
        context.state = ConcreteStateA()

class Context:
    def __init__(self, state):
        self.state = state
    
    def request(self):
        self.state.handle(self)

context = Context(ConcreteStateA())
context.request()
context.request()
```
**Output:**
```
Trạng thái A xử lý.
Trạng thái B xử lý.
```

## 3. ERROR HANDLING STRATEGIES

### 3.1. Defensive Programming

Lập trình phòng thủ nhằm giảm thiểu lỗi bằng cách kiểm tra dữ liệu đầu vào và các điều kiện bất thường.

#### 3.1.1. Input Validation

Kiểm tra tính hợp lệ của dữ liệu đầu vào trước khi xử lý.

**Ví dụ:**
```python
def calculate_square_root(x):
    if not isinstance(x, (int, float)):
        raise TypeError("x phải là số")
    if x < 0:
        raise ValueError("x không được âm")
    return x ** 0.5

try:
    result = calculate_square_root(-4)
except ValueError as e:
    print("Lỗi:", e)
```
**Output:**
```
Lỗi: x không được âm
```

#### 3.1.2. Assertions

Dùng `assert` để kiểm tra điều kiện trong quá trình phát triển, thường bị vô hiệu hóa khi chạy với tối ưu hóa (`-O` flag).

**Ví dụ:**
```python
def divide(a, b):
    assert b != 0, "b không thể bằng 0"
    return a / b

print(divide(10, 2))
print(divide(10, 0))  # AssertionError
```
**Output:**
```
5.0
AssertionError: b không thể bằng 0
```

### 3.2. Exception Hierarchies

Tạo hệ thống exception tùy chỉnh phản ánh cấu trúc lỗi của ứng dụng.

#### 3.2.1. Custom Exception Classes

Kế thừa từ `Exception` hoặc lớp con.

**Ví dụ:**
```python
class AppError(Exception):
    """Base exception cho ứng dụng."""
    pass

class ValidationError(AppError):
    """Lỗi xác thực dữ liệu."""
    pass

class DatabaseError(AppError):
    """Lỗi liên quan đến database."""
    pass

def validate_age(age):
    if age < 0:
        raise ValidationError("Tuổi không được âm")
    if age > 150:
        raise ValidationError("Tuổi không hợp lệ")

try:
    validate_age(-5)
except ValidationError as e:
    print("Lỗi xác thực:", e)
```
**Output:**
```
Lỗi xác thực: Tuổi không được âm
```

#### 3.2.2. Exception Chaining

Dùng `raise ... from ...` để chỉ ra nguyên nhân gốc của exception.

**Ví dụ:**
```python
try:
    x = int("không phải số")
except ValueError as e:
    raise RuntimeError("Xử lý dữ liệu thất bại") from e
```
**Output:**
```
ValueError: invalid literal for int() with base 10: 'không phải số'

The above exception was the direct cause of the following exception:

RuntimeError: Xử lý dữ liệu thất bại
```

### 3.3. Logging Strategies

Ghi log giúp theo dõi hành vi ứng dụng và debug.

#### 3.3.1. Structured Logging

Ghi log với định dạng cấu trúc (JSON) để dễ phân tích.

**Ví dụ với `structlog`:**
Cài đặt: `pip install structlog`
```python
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer()
    ]
)

log = structlog.get_logger()
log.info("Sự kiện xảy ra", user_id=123, action="login")
```
**Output (JSON):**
```
{"event": "Sự kiện xảy ra", "user_id": 123, "action": "login", "level": "info"}
```

#### 3.3.2. Log Levels

Các mức log: DEBUG, INFO, WARNING, ERROR, CRITICAL.

**Ví dụ:**
```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("Thông tin debug chi tiết")
logger.info("Thông tin thông thường")
logger.warning("Cảnh báo")
logger.error("Lỗi")
logger.critical("Lỗi nghiêm trọng")
```
**Output:**
```
DEBUG:__main__:Thông tin debug chi tiết
INFO:__main__:Thông tin thông thường
WARNING:__main__:Cảnh báo
ERROR:__main__:Lỗi
CRITICAL:__main__:Lỗi nghiêm trọng
```

### 3.4. Retry Mechanisms

Tự động thử lại khi thao tác thất bại, phổ biến với network request.

#### 3.4.1. Exponential Backoff

Tăng dần thời gian chờ giữa các lần thử.

**Ví dụ với `tenacity`:**
Cài đặt: `pip install tenacity`
```python
import tenacity
import random

@tenacity.retry(
    wait=tenacity.wait_exponential(multiplier=1, min=1, max=10),
    stop=tenacity.stop_after_attempt(5)
)
def unreliable_function():
    if random.random() < 0.8:
        raise RuntimeError("Thất bại ngẫu nhiên")
    return "Thành công"

try:
    result = unreliable_function()
    print(result)
except tenacity.RetryError as e:
    print("Thất bại sau nhiều lần thử:", e)
```
**Output (có thể):**
```
Thành công
```
hoặc
```
Thất bại sau nhiều lần thử: ...
```

#### 3.4.2. Circuit Breaker Pattern

Ngắt kết nối tạm thời khi dịch vụ liên tục lỗi, tránh làm quá tải.

**Ví dụ với `pybreaker`:**
Cài đặt: `pip install pybreaker`
```python
import pybreaker

breaker = pybreaker.CircuitBreaker(fail_max=3, reset_timeout=10)

@breaker
def fragile_function():
    raise ConnectionError("Lỗi kết nối")

for _ in range(5):
    try:
        fragile_function()
    except pybreaker.CircuitBreakerError as e:
        print("Circuit breaker mở:", e)
    except ConnectionError as e:
        print("Lỗi kết nối:", e)
```
**Output:**
```
Lỗi kết nối: Lỗi kết nối
Lỗi kết nối: Lỗi kết nối
Lỗi kết nối: Lỗi kết nối
Circuit breaker mở: ...
Circuit breaker mở: ...
```

## 4. PERFORMANCE BEST PRACTICES

### 4.1. Algorithm Optimization

#### 4.1.1. Time Complexity (O notation)

Phân tích độ phức tạp thời gian để chọn thuật toán phù hợp.

**Ví dụ:** Tìm kiếm tuyến tính O(n) vs tìm kiếm nhị phân O(log n).
```python
import time

# Linear search O(n)
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

# Binary search O(log n) (yêu cầu mảng đã sắp xếp)
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

sorted_arr = list(range(1000000))
target = 999999

start = time.time()
linear_search(sorted_arr, target)
print("Linear search:", time.time() - start)

start = time.time()
binary_search(sorted_arr, target)
print("Binary search:", time.time() - start)
```
**Output:**
```
Linear search: 0.02394580841064453
Binary search: 7.152557373046875e-06
```

#### 4.1.2. Space Complexity

Độ phức tạp bộ nhớ, lượng bộ nhớ cần thiết theo kích thước đầu vào.

**Ví dụ:** Tính Fibonacci với O(n) bộ nhớ vs O(1) bộ nhớ.
```python
# O(n) space
def fib_list(n):
    if n <= 1:
        return n
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

# O(1) space
def fib_vars(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

import sys
print("Kích thước fib_list(1000):", sys.getsizeof(fib_list(1000)))
print("Kích thước fib_vars(1000):", sys.getsizeof(fib_vars(1000)))
```
**Output:**
```
Kích thước fib_list(1000): 8856
Kích thước fib_vars(1000): 28
```

#### 4.1.3. Data Structure Selection

Chọn cấu trúc dữ liệu phù hợp với thao tác cần thiết.

| Cấu trúc dữ liệu | Thao tác chính | Độ phức tạp |
|------------------|----------------|-------------|
| List | Truy cập theo index, thêm/xóa cuối | O(1) |
| Dict | Truy cập theo key, thêm/xóa | O(1) |
| Set | Kiểm tra membership, thêm/xóa | O(1) |
| Deque | Thêm/xóa hai đầu | O(1) |

**Ví dụ:** Dùng set để loại bỏ phần tử trùng lặp nhanh hơn list.
```python
import time

data = [i % 1000 for i in range(100000)]

# Dùng list O(n²)
start = time.time()
unique_list = []
for item in data:
    if item not in unique_list:
        unique_list.append(item)
print("List time:", time.time() - start)

# Dùng set O(n)
start = time.time()
unique_set = set(data)
print("Set time:", time.time() - start)
```
**Output:**
```
List time: 14.921597003936768
Set time: 0.005983829498291016
```

### 4.2. Memory Optimization

#### 4.2.1. `__slots__`

Đã trình bày trong phần 3.2.1.

#### 4.2.2. Generators

Đã trình bày trong phần 3.2.5.

#### 4.2.3. `array` Module

Đã trình bày trong phần 3.2.4.

### 4.3. I/O Optimization

#### 4.3.1. Buffered I/O

Sử dụng buffer để giảm số lần gọi I/O.

**Ví dụ:** Đọc file theo khối thay vì từng dòng.
```python
import time

# Không buffer (đọc từng dòng)
start = time.time()
with open('large_file.txt', 'r') as f:
    for line in f:
        pass
print("Đọc từng dòng:", time.time() - start)

# Buffer lớn hơn
start = time.time()
with open('large_file.txt', 'r', buffering=8192) as f:
    for line in f:
        pass
print("Buffer 8KB:", time.time() - start)
```

#### 4.3.2. Asynchronous I/O

Dùng asyncio cho I/O-bound tasks để xử lý đồng thời.

**Ví dụ:**
```python
import asyncio
import aiofiles

async def read_file_async(filename):
    async with aiofiles.open(filename, 'r') as f:
        content = await f.read()
    return content

async def main():
    tasks = [read_file_async(f'file{i}.txt') for i in range(10)]
    results = await asyncio.gather(*tasks)
    print(f"Đọc {len(results)} files đồng thời")

asyncio.run(main())
```

#### 4.3.3. Compression

Nén dữ liệu trước khi lưu hoặc truyền để giảm kích thước.

**Ví dụ với gzip:**
```python
import gzip
import json

data = {"key": "value" * 1000}

# Nén
compressed = gzip.compress(json.dumps(data).encode())
print("Kích thước gốc:", len(json.dumps(data)))
print("Kích thước nén:", len(compressed))

# Giải nén
decompressed = gzip.decompress(compressed)
print("Dữ liệu giải nén bằng dữ liệu gốc?", json.loads(decompressed) == data)
```
**Output:**
```
Kích thước gốc: 14012
Kích thước nén: 147
Dữ liệu giải nén bằng dữ liệu gốc? True
```

### 4.4. Database Optimization

#### 4.4.1. Indexes

Tạo index trên các cột thường dùng để tìm kiếm, sắp xếp.

**Ví dụ SQL (SQLite):**
```sql
CREATE INDEX idx_users_email ON users(email);
```

#### 4.4.2. Query Optimization

- Sử dụng JOIN thay vì nhiều truy vấn.
- Chỉ SELECT các cột cần thiết.
- Tránh SELECT *.

**Ví dụ:**
```python
# Không tối ưu
cursor.execute("SELECT * FROM users WHERE age > 20")
# Tối ưu
cursor.execute("SELECT id, name FROM users WHERE age > 20")
```

#### 4.4.3. Connection Pooling

Dùng pool kết nối để tránh chi phí tạo kết nối mới.

**Ví dụ với `psycopg2.pool`:**
```python
import psycopg2
from psycopg2 import pool

connection_pool = psycopg2.pool.SimpleConnectionPool(
    1, 10, host='localhost', database='mydb', user='user', password='pass'
)

conn = connection_pool.getconn()
cursor = conn.cursor()
cursor.execute("SELECT 1")
cursor.close()
connection_pool.putconn(conn)
```

---

# PHẦN IX: PYTHON ENHANCEMENT PROPOSALS (PEPS)

PEP là các đề xuất cải tiến Python, bao gồm các tiêu chuẩn, hướng dẫn, và thông tin kỹ thuật.

## 1. PEP 8 - Style Guide

PEP 8 là hướng dẫn về style code, đã trình bày trong phần VIII.1.

## 2. PEP 20 - Zen of Python

Là tập hợp 19 nguyên tắc triết học thiết kế Python, có thể xem bằng `import this`.

**Nội dung:**
```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## 3. PEP 257 - Docstring Conventions

Hướng dẫn viết docstring.

**Ví dụ:**
```python
def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    if imag == 0.0 and real == 0.0:
        return complex_zero
    # ...
```

## 4. PEP 484 - Type Hints

Đề xuất type hints, đã trình bày trong phần VIII.1.3 và VIII.1.4.

## 5. PEP 526 - Variable Annotations

Mở rộng PEP 484, cho phép annotation biến (không chỉ hàm).

**Ví dụ:**
```python
from typing import List

primes: List[int] = []
captain: str = "Picard"
```

## 6. PEP 3333 - WSGI

Web Server Gateway Interface, chuẩn giao tiếp giữa web server và ứng dụng Python.

**Ví dụ ứng dụng WSGI đơn giản:**
```python
def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)
    return [b'Hello, World!']
```

## 7. PEP 492 - `async/await`

Đề xuất cú pháp bất đồng bộ với `async` và `await`.

**Ví dụ:**
```python
async def fetch_data():
    return "data"

async def main():
    data = await fetch_data()
    print(data)
```

## 8. PEP 570 - Positional-only Parameters

Cho phép định nghĩa tham số chỉ positional (từ Python 3.8).

**Ví dụ:**
```python
def func(a, b, /, c, d):
    # a, b chỉ positional
    # c, d có thể positional hoặc keyword
    pass

func(1, 2, 3, d=4)  # hợp lệ
func(1, 2, c=3, d=4)  # hợp lệ
func(a=1, b=2, c=3, d=4)  # Lỗi: a, b không thể keyword
```

## 9. PEP 572 - Walrus Operator

Toán tử `:=` (walrus) cho phép gán giá trị trong biểu thức (từ Python 3.8).

**Ví dụ:**
```python
# Không dùng walrus
line = f.readline()
while line:
    print(line)
    line = f.readline()

# Dùng walrus
while (line := f.readline()):
    print(line)
```

## 10. PEP 634 - Pattern Matching

Giới thiệu cú pháp `match`/`case` (từ Python 3.10).

**Ví dụ:**
```python
def describe(value):
    match value:
        case 0:
            return "zero"
        case [x, y]:
            return f"list với hai phần tử: {x}, {y}"
        case {"name": name, "age": age}:
            return f"{name}, {age} tuổi"
        case _:
            return "khác"

print(describe(0))
print(describe([1, 2]))
print(describe({"name": "Alice", "age": 30}))
```
**Output:**
```
zero
list với hai phần tử: 1, 2
Alice, 30 tuổi
```

## 11. PEP 654 - Exception Groups

Giới thiệu `ExceptionGroup` và `except*` để xử lý nhiều exception cùng lúc (từ Python 3.11).

**Ví dụ:**
```python
try:
    raise ExceptionGroup("group", [ValueError(1), TypeError(2)])
except* ValueError as e:
    print(f"Bắt ValueError: {e}")
except* TypeError as e:
    print(f"Bắt TypeError: {e}")
```
**Output:**
```
Bắt ValueError: 1
Bắt TypeError: 2
```

## 12. Các PEP quan trọng khác (Tổng hợp)

- **PEP 202:** List Comprehensions.
- **PEP 318:** Decorators.
- **PEP 343:** `with` Statement.
- **PEP 380:** `yield from`.
- **PEP 405:** Virtual Environments.
- **PEP 448:** Additional Unpacking Generalizations.
- **PEP 498:** f-strings.
- **PEP 525:** Asynchronous Generators.
- **PEP 553:** `breakpoint()`.
- **PEP 560:** Core Support for typing module.
- **PEP 563:** Postponed Evaluation of Annotations.
- **PEP 585:** Type Hinting Generics In Standard Collections.
- **PEP 604:** Union Types: `X | Y`.
- **PEP 612:** Parameter Specification Variables.
- **PEP 613:** Explicit Type Aliases.
- **PEP 635:** Structural Pattern Matching: Motivation and Rationale.
- **PEP 636:** Structural Pattern Matching: Tutorial.
- **PEP 673:** `Self` Type.
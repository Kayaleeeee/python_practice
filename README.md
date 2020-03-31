# Python Basic ⚡️

#

### **1. Arithmetic Opertators**

| Operator | Name                   | Example |
| -------- | ---------------------- | ------- |
| +        | addition               | x+y     |
| -        | subtraction            | x-y     |
| \*       | Multiplication         | x\*y    |
| /        | Division               | x/y     |
| %        | Modulus(나머지)        | x%y     |
| \*\*     | Exponentiation(지수승) | x\*\*y  |
| //       | Floor division(몫)     | x//y    |

#

### **2. Assignment Operators**
| Operator | Example | Same as |
|-|-|-|
|=| x = 5 | x = 5 |
|+=| x+= 3 | x = x+3 |
|-=| x-= 3 | x = x-3 |
|_=| x_=3 | x = x\*3 |
|/=| x/=3 | x = x/3 |

#

### **3. 자료형**

- **Boolean(불리언)**
  True, False (참, 거짓)

###

- **Number(숫자)**
  int, float(정수형, 실수형)
  ex) 1, 1.56

###

- **string(문자열)**
  ex) 'Hello World'

###

- **List & Tuple & Dictionary**

| **List = ['a', 'b', 1, 1, 123 ]** | **Tuple = ('a', 'b', 'True')** | **Dictionary = {key:value}** |
| --------------------------------- | ------------------------------ | ---------------------------- |
| 순서 있음                         | 순서 있음                      | 순서 없음                    |
| 변화가능한 자료모음               | 변하지 않는 값                 | 변화가능                     |
| 같은 값 중복 허용                 | 중복 불허                      | 키 값 중복 불허              |

- **출력법**

```python
A = [1, 2, True, 3, 'pizza']
B = ('Hello', 1, 123, False)
C = {'name': 'Kaya', 'age': 25, }

print(A[0])
print(B[2])
print(C['name'])


>> 1
>> 123
>> kaya
```

#

### **4. 조건문**

- **if** + 조건1
- **elif** + 조건2 (앞의 조건1이 거짓일 경우 조건2 실행)
- **else** :
  이 전의 조건문이 모두 거짓일 시 실행

#

### **5. 반복문**

- **for**:
  Tuple, Lust, Dictionary 등을 순서에따라 반복

  ###

  ```python
  A = [1, 2, 3, 4]
  for i in A:
      print(i)
  ```

  ```python
  grades = [100, 92, 82, 80, 74, 70, 40]

  for grade in grades:
      if grade >= 90 and grade < 100:
          print(str(grade) + '점의 학점은 A입니다.')

      elif grade >= 80 and grade < 90:
          print(str(grade) + '점의 학점은 B입니다.')

      elif grade >= 70 and grade < 80:
          print(str(grade) + '점의 학점은 C입니다.')

      else:
          print(str(grade) + '점의 학점은 D입니다.')
  ```

        *str을 안넣으면 print불가

##

- **while**:
  조건이 참인 동안 조건문 반복 실행

  ###

  ```python
  a=1
  while(k<10>):
      print(k)
      k+=2
  ```

  ```python
  treeHit = 0
  while treeHit < 10:
    print('나무가 %d번 찍혔습니다.' % treeHit)
    treeHit += 1

  if treeHit == 10:
    print('나무가 넘어갑니다.')

    <!-- String Formatting (%d): 문자열 내부에 다른 자료형을 쓰고 싶을 경우. -->
    %s: String
    %c: Character
    %d: integer
    %f: floating point

  ```

#

### **6. Function 함수**

- 호출 할 때만 실행되는 코드블록
- 함수 코드에 따라서 데이터 반환

```python
  def functionName(params1, params2):
    params1 = params1 + '_vn'
    params2 = params2 + ' world'
    return(params1, params2)

output = functionName('Likelion', 'Hello')
print(output)

>>>('Likelion_vn', 'Hello World')
```

### **7. Class 객체**

- 내부에 변수와 함수 포함
- 코드를 더 유기적으로 활용 가능, 재사용성 높음
- 클래스는 다양한 동작을(함수를 통해) 구현하는 하나의 객체
- 하지만, 객체의 유니크한 성질은 *인스턴스 설정 후 *메소드를 호출하여 결정한다.

```python
class Cat:
  def meow(self): #meow() 메소드 정의
    print('야옹')

cat1 = Cat() #인스턴스 생성
cat1.meow() #메소드 호출

>>야옹

```

#

- **self**

  1. 클래스에서 만든 인스턴스를 지칭
  2. **_self._** 를 통해 클래스 메소드와 속성에 접근

  ```python

  class Cat:

    def __init__(self, name='나비', color='black'):
      self.name = name
      self.color = color

    def info(self):
      print('고양이 이름은', self.name, '색은', self.color)

  cat1 = Cat('네로', '검정')
  cat2 = Cat('미미', '갈색')

  cat1.info()
  cat2.info()

  >>고양이 이름은 네로 색은 검정
  >>고양이 이름은 미미 색은 갈색

  ```

출처: https://www.youtube.com/watch?v=QCNkJ3SaZ

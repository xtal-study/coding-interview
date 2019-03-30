# 해시 테이블

## Hash Table

__Hash Table__ 은, __Hash__ 라는 자료를 이용하여 특정한 __키(Key)__ 와 그에 대응하는 __값(Value)__ 을 묶어 저장하는 자료 구조이다. 이 대응은 __Hash Function__ 이라는 놈을 통해서 이루어진다. Hash Function은 키를 입력받으면 그에 맞는 Hash를 뱉어낸다. 그리고 이 Hash가 가리키는 곳에 저장되어 있는 정보를 탐색하면 입력된 Key에 대응하는 Value 값을 구할 수 있게 된다는 아이디어이다. Hash를 통해서 Key와 Value가 묶인다고 생각하면 편할 듯 싶다.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Hash_table_3_1_1_0_1_0_0_SP.svg/1280px-Hash_table_3_1_1_0_1_0_0_SP.svg.png" alt="alt text" width="500" height="400">

위의 그림은 간단한 해시 테이블의 구조를 설명한다. 사람의 이름과 전화번호를 Key와 Value로 하여 해시 테이블을 구성하는데, 이 Key-Value 쌍들을 미리 배열에 저장해 놓는다. 보통 이렇게 Key-Value 쌍들이 저장된 공간을 __Bucket__ 이라고 한다. 

Hash function에 이름을 Key로 입력하면 그 이름에 해당하는 Hash value가 반환된다. 그리고 Bucket에서 Hash value에 해당하는 index를 찾으면, 입력된 Key와 그에 대응하는 Value가 묶인 쌍을 가져올 수 있다.

정말 이상적으로는, 하나의 키에 하나의 해시만 대응시키는게 최고다. 하지만 실제로는 메모리 문제 등 여러 제약 사항 때문에, 보통 Key의 수보다 Hash의 수가 적은 Hash table을 운용한다. 이렇게 될 경우 두 개 이상의 Key가 하나의 Hash에 연결되어 __해시 충돌(Collision)__ 이 일어날 수 있다. 이를 해결하기 위해 __체이닝(Chaining)__ 과 같은 방법들이 고안되었다.

체이닝은 이름은 거창한데 생각보다 간단한 아이디어다. 어차피 Bucket에 Key랑 Value를 같이 저장하니까, 하나의 Hash value 위치에 두 개 이상의 Key-Value 쌍을 리스트 형태로 이어서 저장하자는 아이디어다. Hash value를 찾아 Bucket의 해당 위치를 찾은 후, 그 위치의 리스트를 순차적으로 탐색하여 입력된 Key를 찾으면 되는 것이다. 이는 보통 Linked List로 구현된다. 위와 같은 예시를 든 이미지로 보면 아래와 같은 모습이다.

<img src="https://i.imgur.com/7PTT8dT.png" alt="" width="500" height="400">

해시 테이블의 성능에는, 해시를 얼마나 효율적으로 적절한 갯수를 이용하는지가 큰 영향을 미친다. 그래서 해시 테이블을 구현할 때는 적절한 해시 함수의 디자인이 필수다.

위에서는 이해를 위해 Key에 이름이라는 String을 사용했지만, 보통 해시 테이블을 다룰 때는 키가 정수형인 경우가 많다. 정수형의 Key를 다를 때 생각할 수 있는 대표적인 해시 함수는 __Division Method__ 이다. 정말 간단하게, Key 값을 Bucket의 길이로 나눈 나머지를 Hash value로 취한다. 아래와 같은 모습이다.

![](https://latex.codecogs.com/gif.latex?v%20%3D%20k%5Cbmod%7Bl%7D)
 
여기서 ![](https://latex.codecogs.com/gif.latex?k)는 Key 값, ![](https://latex.codecogs.com/gif.latex?l)은 Bucket의 길이, ![](https://latex.codecogs.com/gif.latex?v)는 Hash value이다.

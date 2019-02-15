# Big-O Notation

알고리즘의 시간 / 공간 복잡도를 계산하기 위해 __Big-O Notation__ 을 사용한다.

![](https://latex.codecogs.com/gif.latex?O%28n%29)은 ![](https://latex.codecogs.com/gif.latex?n) 크기의 자료가 알고리즘에 입력되었을 때의 시간이 ![](https://latex.codecogs.com/gif.latex?O%28n%29)만큼 걸린다 / 메모리를 ![](https://latex.codecogs.com/gif.latex?O%28n%29)만큼 사용한다는 의미이다.

예를 들어, 어떤 알고리즘의 시간 복잡도가 ![](https://latex.codecogs.com/gif.latex?O%281%29)일 경우, 입력의 크기에 상관 없이 알고리즘의 수행 시간은 1로 동일하다. 또한 ![](https://latex.codecogs.com/gif.latex?O%28n%29)일 경우, 입력의 크기에 따라 알고리즘의 수행 시간이 선형적으로 증가한다.

복잡도의 표기에는 다양한 변수가 포함될 수도 있다. 어떤 알고리즘이 높이가 ![](https://latex.codecogs.com/gif.latex?h)이고 너비가 ![](https://latex.codecogs.com/gif.latex?w)인 모든 픽셀의 값을 더하는 작업을 한다면, 이 알고리즘의 수행 시간은 ![](https://latex.codecogs.com/gif.latex?O%28wh%29)일 것이다.

어떤 알고리즘의 시간 복잡도를 이야기할 때는 보통 그 알고리즘이 동작하는 __최악의 경우__ 의 복잡도를 이야기한다.

### 공간 복잡도의 계산
공간 복잡도는 보통 알고리즘의 __메모리 사용량__ 을 나타낸다. 어떤 알고리즘이 길이가 ![](https://latex.codecogs.com/gif.latex?n)인 배열을 만들어야 한다면 공간 복잡도는 ![](https://latex.codecogs.com/gif.latex?O%28n%29)일 것이고, ![](https://latex.codecogs.com/gif.latex?%28n%20%5Ctimes%20m%29) 크기의 2차원 배열을 만들어야 한다면 ![](https://latex.codecogs.com/gif.latex?O%28nm%29)이 될 것이다.

또한 함수의 호출 스택도 공간 복잡도 계산에 포함된다. 예를 들어 아래와 같은 재귀 함수는, 마지막 재귀의 반환 전까지 모든 함수의 호출이 스택에 쌓여 있는다.

```
int sum(int n) {
    if(n <= 0) {
        return 0;
    }
    return n + sum(n - 1);
}
```

`sum` 함수는 `n`이 0이 되어 재귀를 탈출할 때까지 `n`번 호출되며, 마지막 재귀에서 순차적으로 반환하므로 `n`개의 호출이 모두 스택에 쌓인다. 따라서 공간 복잡도는 ![](https://latex.codecogs.com/gif.latex?O%28n%29)이다.

중요한것은 __호출 스택에 쌓이는가__ 이다. 따라서 아래와 같은 함수는 공간 복잡도가 ![](https://latex.codecogs.com/gif.latex?O%281%29)이다.

```
int SumDoubles(int n) {
    int total = 0;
    int i;
    for(i = 0; i < n; ++i) {
        total += Doubler(i);
    }
}

int Doubler(int k) {
    return 2 * k;
}
```

### 복잡도 계산시 유의할 점
#### 상수 또는 상수항은 무시하라
![](https://latex.codecogs.com/gif.latex?O%282n%29)은 ![](https://latex.codecogs.com/gif.latex?O%28n%29)과 같다고 볼 수 있다. 이는 Big-O Notation이 정확한 실행 시간이 아닌, __실행 시간이 증가하는 비율__ 관점을 보기 때문이다.
- ![](https://latex.codecogs.com/gif.latex?O%283n%5E2%20&plus;%20n%29%20%5C%20%5C%20%3D%20%5C%20%5C%20O%28n%5E2%29)
- ![](https://latex.codecogs.com/gif.latex?O%28n%5E3%20&plus;%20n%5E3%29%20%5C%20%5C%20%3D%20%5C%20%5C%20O%28n%5E3%29)

#### 지배적이지 않은 항은 무시하라
한 마디로, __제일 수행 시간에 영향이 큰 항__ 만 남기라는 뜻이다. 예를 들면 아래와 같은 것들이다.
- ![](https://latex.codecogs.com/gif.latex?O%28n%5E2%20&plus;%20n%29%20%5C%20%5C%20%3D%20%5C%20%5C%20O%28n%5E2%29)
- ![](https://latex.codecogs.com/gif.latex?O%28n%20&plus;%20%5Clog%20n%29%20%5C%20%5C%20%3D%20%5C%20%5C%20O%28n%29)
- ![](https://latex.codecogs.com/gif.latex?O%283n%20&plus;%202n%5E2%20&plus;%20n%29%20%5C%20%5C%20%3D%20%5C%20%5C%20O%28n%5E2%29)
- ![](https://latex.codecogs.com/gif.latex?O%281000n%5E%7B100%7D%20&plus;%202%5En%29%20%5C%20%5C%20%3D%20%5C%20%5C%20O%282%5En%29)

#### 관계가 명확하지 않은 변수는 남겨라
서로 관계를 알 수 없는 변수가 둘 이상 있을 경우, 해당 항을 상수 취급하면 안 된다. 아래와 같은 경우, ![](https://latex.codecogs.com/gif.latex?a)와 ![](https://latex.codecogs.com/gif.latex?b)의 관계가 종속적임을 아는 상황이 아니면 둘 다 상수 취급할 수 없다.
- ![](https://latex.codecogs.com/gif.latex?O%28a%5E2%20&plus;%20b%29)

#### ![](https://latex.codecogs.com/gif.latex?%5Clarge%20O%28%5Clog%20n%29) 수행 시간
보통 어떤 알고리즘에서 연산을 수행할 때마다 __이용하는 데이터의 수가 반씩 줄어든다면,__ 시간 복잡도는 ![](https://latex.codecogs.com/gif.latex?O%28%5Clog%20n%29)이 될 가능성이 크다. 대표적인 예가 __이진 탐색__ 이다. 이 알고리즘은 한번 Iteration이 수행될 때마다, 다음 탐색할 데이터의 양이 반씩 줄어든다. 입력 데이터가 ![](https://latex.codecogs.com/gif.latex?N)개라고 가정하면, 한 번의 탐색 과정을 거친 후 다음 탐색 과정에서는 ![](https://latex.codecogs.com/gif.latex?N/2)만큼의 데이터를 탐색할 것이다. 세 번째는 ![](https://latex.codecogs.com/gif.latex?N/4)일 거고, 이렇게 원하는 값을 찾을 때 까지 반복한다. 이 경우의 관계식을 살펴보면, 총 탐색 횟수(Iteration)을 ![](https://latex.codecogs.com/gif.latex?K)라고 할 때, ![](https://latex.codecogs.com/gif.latex?2%5EK%20%3D%20N)이 성립할 것이다. 로그의 성질에 의해 ![](https://latex.codecogs.com/gif.latex?K%20%3D%20%5Clog%20N)으로 볼 수 있다(로그의 밑은 무시된다). 따라서 이 경우 이진 탐색 알고리즘의 시간 복잡도는 ![](https://latex.codecogs.com/gif.latex?O%28%5Clog%20N%29)이 된다.

#### 재귀적인 수행 시간
아래의 코드는 ![](https://latex.codecogs.com/gif.latex?O%282%5EN%29)의 시간 복잡도를 가지고 있다.
```
int f(int n) {
    if(n <= 1) {
        return 1;
    }
    return f(n - 1) + f(n - 1)
}
```
함수 `f`가 한 번 호출될 때마다, 재귀적으로 두 개의 'f'를 다시 호출하고 있다. 따라서 호출을 반복할수록 시간 복잡도는 2의 제곱으로 늘어날 것이다. 만약 'f'의 내부에서 'f'를 세 번씩 호출한다면, 복잡도는 ![](https://latex.codecogs.com/gif.latex?O%283%5EN%29)이 될 것이다.


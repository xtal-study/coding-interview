# 연결 리스트
__연결 리스트(Linked List)__ 는 리스트형 자료구조이다. 순차적으로 저장되는 데이터를 담을 수 있다.

컨셉은 간단하다. 링크드 리스트에서 각각의 데이터들을 저장할 단위 자료구조를 __노드(Node)__ 라고 하자. Node는 저장된 데이터만을 가지고 있는 것이 아니라, 다음으로 연결되어야 할 노드의 메모리상 주소 값을 같이 가지고 있다. Head 노드부터 시작해서 각 노드가 가지고 있는 다음 노드 주소 값을 따라 탐색하면 리스트 내부를 모두 탐색할 수 있게 된다는 아이디어이다. 그림으로 보면 아래와 같은 모양일 것이다.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Singly-linked-list.svg/612px-Singly-linked-list.svg.png" width="500" height="50">

각 화살표의 원점이 가리키는 상자가 각 노드에서 다음 노드의 주소 값을 저장한 필드라고 생각할 수 있다.

#### 새로운 노드의 삽입
링크드 리스트에 새로운 노드를 삽입할 때는, 새로운 노드를 '다음 노드'로 가질 이전 노드의 정보가 필요하다. __A->B->C__ 순서의 링크드 리스트가 있을 때, B와 C 노드 사이에 D라는 노드를 추가하려면, 아래와 같은 시퀀스가 필요하다.  
1. 새로운 데이터가 담긴 D 노드를 생성한다.
2. D 노드의 '다음 노드'를 B 노드의 '다음 노드'인 C로 설정한다.
3. B 노드의 '다음 노드'를 새로 생성된 노드인 D로 설정한다.

그림으로는 아래와 같은 모습일 것이다.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/CPT-LinkedLists-addingnode.svg/711px-CPT-LinkedLists-addingnode.svg.png" width="550" height="140">

#### 노드의 삭제
링크드 리스트에서 노드를 삭제할 때는, 자신의 이전 노드가 자신의 다음 노드를 가리킬 수 있도록 처리를 해 주어야 한다. __A->B->C->D__ 순서의 링크드 리스트가 있을 때, C 노드를 삭제하려면, 아래와 같은 시퀀스가 필요하다.
1. B 노드의 '다음 노드'를 D 노드로 설정한다.
2. C 노드의 메모리를 해제한다.

그림으로는 아래와 같은 모습일 것이다.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/CPT-LinkedLists-deletingnode.svg/570px-CPT-LinkedLists-deletingnode.svg.png" width="400" height="200">

#### 이중 연결 리스트
단방향 연결 리스트는 각 노드가 자신의 다음 노드 정보만을 가지고 있었지만, __이중 연결 리스트(Doubly Linked List)__ 는 자신의 이전 노드 정보도 같이 가지고 있는다. 따라서 '이전 노드' 와 관련된 탐색이 조금 더 편리해진다.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Doubly-linked-list.svg/915px-Doubly-linked-list.svg.png" width="700" height="50">

#### 원형 연결 리스트
__원형 연결 리스트(Circular Linked List)__ 는 모든 노드가 다음 노드와 이전 노드를 가지고 있는 링크드 리스트이다.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Circularly-linked-list.svg/525px-Circularly-linked-list.svg.png" width="400" height="70">

만약 원형 이중 연결 리스트라면, 첫 번째 노드와 마지막 노드가 서로 가리키고 있을 것이다.

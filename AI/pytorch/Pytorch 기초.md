

# Pytorch 기초

### 1.  Tensor

- 3D Tensor
  - 대체로 |t|=(batch size, width, height) 와 유사한 형식

- 3차원 Tensor라면 3차원 배열이라고 생각하는 것이 편함



### 2. Numpy

- import numpy
- 텐서 생성
  - ex) t = np.array([0., 1., ...])
- 명령어
  - t.ndim -> t의 차원 ex) 1 -- 1차원 배열
  - t.shape -> t의 크기 출력 ex) (7,) -- 1차원 배열의 길이 
- index는 0부터 시작
- slice 가능



### 3. Pytorch Tensor 선언

- import torch
- 생성
  - t = torch.FloatTensor([0., 1., ...])
- 명령어
  - t.dim -> t의 차원
  - t.shape -> t의 size
  - t.size() -> t의 size
    - shape과 size의 차이는 sorted와 sort의 차이와 같은 듯
  - t. view -> t의 shape을 바꿀 때 사용

- BroadCasting

  - 크기가 다른 두 텐서의 연산을 할 때에 자동으로 크기를 맞춰서 연산을 수행하게 하는 기능

  - ```python
    m1 = torch.FloatTensor([[1,2]])
    m2 = torch.FloatTensor([[3],[4]])
    print(m1 + m2)
    => tensor([4., 5.],
              [5., 6.])
    ```

- 곱셈

  - matmul

    - 행렬의 곱셈(내적)과 같음 => 2 x 2 matmul 2 x 1 => 2 x 1
    - ex) m1.matmul(m2)

  - mul

    - 동일한 위치에 있는 원소끼리의 곱

    - 텐서 * 텐서와 같다

    - broadcasting 적용 가능

    - ```python
      m1 = torch.FloatTensor([[1, 2], [3, 4]])
      m2 = torch.FloatTensor([[1], [2]])
      print('Shape of Matrix 1: ', m1.shape) # 2 x 2
      print('Shape of Matrix 2: ', m2.shape) # 2 x 1
      print(m1 * m2) # 2 x 2
      print(m1.mul(m2))
      Shape of Matrix 1:  torch.Size([2, 2])
      Shape of Matrix 2:  torch.Size([2, 1])
      tensor([[1., 2.],
              [6., 8.]])
      tensor([[1., 2.],
              [6., 8.]])
      ```

    - mul() 안에 인자로 상수를 넣을 수도 있음



#### Tensor 조작 명령어

- View: 원소의 수를 유지하면서 텐서의 크기 변경, 매우 중요!

  - ex) t.view([-1,3])
    - t 텐서의 차원을 2차원으로 만들고 첫번째 차원은 파이토치에게 맡기는 의미로 -1을 하였다.

- squeeze: 크기가 1인 차원을 제거

  - t.squeeze()를 하면 크기가 1인 차원을 삭제하고 병합된다.

  - ```python
    # squeeze 예시
    t = torch.FloatTensor([[0],[1],[2]]) # 일 때
    t.squeeze()
    => tensor([0., 1., 2.,])
       torch.Size([3])
    ```

- unsqueeze: 특정 위치에 크기가 1인 차원을 추가

  - ex) t.unsqueeze(차원 인덱스)

- 타입 캐스팅

  - ![image-20220303131733473](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220303131733473.png)

- concatenate(연결하기)

  - 두 텐서를 합친다고 이해하면 편하다

  - dimension을 지시해서 해당 차원에 더해지게 선택할 수 있다.

  - ```python
    x = torch.FloatTensor([[1, 2], [3, 4]])
    y = torch.FloatTensor([[5, 6], [7, 8]])
    print(torch.cat([x, y], dim=0))
    => tensor([[1., 2.],
            [3., 4.],
            [5., 6.],
            [7., 8.]])
    ```

-  stacking

  - 쌓는다. 연결과 유사하며 더 편할 떄가 있음

  - 스택킹은 실제 많은 연산(cat을 이용한)을 포함하고 있다.

  - ```python
    x = torch.FloatTensor([1, 4])
    y = torch.FloatTensor([2, 5])
    z = torch.FloatTensor([3, 6])
    print(torch.stack([x, y, z]))
    => tensor([[1., 4.],
            [2., 5.],
            [3., 6.]])
    ```

- ones_like와 zeros_like
  - torch.ones_like 처럼 명령어를 사용하면 동일한 크기이며 값이 1로만 채워진 텐서를 생성



#### Numpy Axis

```python
>>> arr = np.arange(0, 32)
>>> len(arr)
32
>>> arr
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])
>>> v = arr.reshape([4,2,4])

# axis = None으로 하면 (default값임) 그냥 총합 더함
# axis = 0
>>> res01=v.sum(axis=0) ## axis=0 기준 합계
>>> res01.shape
(2, 4)
>>> res01
array([[48, 52, 56, 60],
       [64, 68, 72, 76]])

# axis = 1
>>> res02=v.sum(axis=1)  ## axis=1 기준 합계
>>> res02.shape
(4, 4)
>>> res02
array([[ 4,  6,  8, 10],
       [20, 22, 24, 26],
       [36, 38, 40, 42],
       [52, 54, 56, 58]])
>>>

# axis = 2
>>> res03=v.sum(axis=2)  ## axis=2 기준 합계
>>> res03.shape
(4, 2)
>>> res03
array([[  6,  22],
       [ 38,  54],
       [ 70,  86],
       [102, 118]])
>>>
```

- sum 사용 시 axis=0 처럼 axis의 값을 줄 땐 해당 axis를 제거한다고 생각하면 쉽다.

![image-20220303115826427](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220303115826427.png)

출처: http://taewan.kim/post/numpy_sum_axis/



#### Pandas

- height = torch.tensor(data.height)
  - pandas를 이용한 데이터를 tensor로 바꾸기
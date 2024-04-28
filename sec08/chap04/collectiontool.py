# 기본 컬렉션보다 강력한 기능들을 제공하는 특수 컨테이너 타입들을 갖습니다.

from collections import Counter

# Counter : 딕셔너리의 서브클래스로
# 주어진 컬렉션의 요소의 개수를 세는데 유용

fruits = ["apple", "orange", "apple", "pear", "orange", "banana", "orange"]
fruit_counter = Counter(fruits) #fruit리스트의 자료값을 카운트해줌 (중복된 값도 몇개인지 알려줌)
apples = fruit_counter.get("apple") #Counter(fruits)하고나서 apple이 몇개인지 .get을 이용해서 출력

most_common_fruit = fruit_counter.most_common(2) #Counter(fruits)하고나서 제일 많을 것들을 알기 위해서 .most_common()을 해줌
# ()안에 1~n 기재해주면  1~n위까지 출력해줌


from collections import deque

# deque : 데이터를 양쪽 끝에서 처리해야 하는 용도에 유용

dq = deque([4, 5, 6, 7, 8]) #deque()함수안에 [4,5,6,7,8]이라는 리스트를 넣음
dq.append(9) # 🔴 오른쪽 끝에 요소 추가
dq.appendleft(3) # 왼쪽 끝에 요소 추가

dq.pop()  # 오른쪽 끝의 요소 제거
dq.popleft()  # 왼쪽 끝의 요소 제거

dq.extend([9, 10]) # 오른쪽 끝에 이터러블 요소들 추가
dq.extendleft([3, 2, 1]) # 왼쪽 끝에 이터러블 요소들 역순으로 추가  즉, 추가되면 1,2,3으로 추가됨

dq.rotate(2) # 오른쪽 끝에 있는 요소 (2)개가 앞으로 이동함
dq.rotate(-5) # 왼쪽 끝에 있는 요소 (5)개가 뒤로 이동함



from collections import namedtuple

# namedtuple : 각 항목에 이름이 있는 튜플
# 튜플과 마찬가지로 내용을 바꿀 수 없음

# 아래와 같이 [클래스]를 생성하여 사용
Person = namedtuple("Person", ["name", "age", "city"])

# 인스턴스 생성
p1 = Person("Alice", 30, "New York") #field_names 에 순서에 맞게 이름, 나이, 도시에 맞춰서 들어감
p2 = Person(name="Bob", age=25, city="Paris") #p1과 다르게 순서와 상관없이 요소값에 맞춰서 들어감

# 필드에 접근
p1_name, p1_age = p1.name, p1.age
p2_city_a = p2.city

#인스턴스의 자료값을 수정할 수 는 없음
# p2.city = "Seoul" # 💡 오류 발생

#인스턴스의 자료를 수정 할 수 없지만 새로운 인스턴스를 만들 수 는 있음
# _replace 메소드로 새로운 인스턴스를 만드는 건 가능
# p1 city 는 New York 이지만 p3 객체를 p1처럼 만들지만 city만 수정하게됨
p3 = p1._replace(city="Seoul")



from collections import defaultdict

# defaultdict : 존재하지 않는 키에 대한 기본값 생성
# 인자로 특정 값(기본값으로 쓸)을 반환하는 함수를 받음

# int를 기본값으로 하는 defaultdict 생성
# int() 호출 시 0을 반환하므로, 새 키의 기본값은 0

my_int = int() #int() 라는 함수는 0을 반환하게끔 설정되어 있다.

# dd_int = defaultdict(int) #defaultdict(int) 주어지지 않는 키워드에 대해서 0을 반환하는 딕셔너리가 생성됨
dd_int = defaultdict(lambda: 5) # 이와 같이 바꿔 볼 것

dd_int_a = dd_int["a"] #dd_int["a"] 또한 0을 반환하게 되어 있다.

dd_int["a"] += 1
dd_int["b"] += 2

dd_int_b = dd_int["b"]

dd_int["c"] = "hello"
dd_int_c = dd_int["c"]


pass
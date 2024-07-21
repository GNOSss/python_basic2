import pickle

# pickle 파일로부터 데이터 불러오기
# rb 는 read binary , 즉 binary 형식 데이터를 읽어줘라 라는 뜻
# 변수명 = pickle.loda(with open 을 참조하는 변수명) <<여기서는 f
with open('my_data.pickle', 'rb') as f:
    loaded_list = pickle.load(f)
    loaded_dict = pickle.load(f)

## 주의 사항은 pickle.dump 했을때 먼저 실행한 것들은 pickle.load 할때 먼저 나오니
## 어떤것들이 몇번째 들어갔는지 알고 있어야 함






pass
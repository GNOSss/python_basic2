import os
import shutil

# 파일 복사
# shutil.copy() 로 파일 복사 가능
# ("복사할 파일명" , "복사해 붙여 넣을 경로")
# shutil.copy("Tiger.txt", "./animal")   # "./animal"은 현재 경로의 animal 디렉토리 라는 뜻


# 파일 다른 이름으로 복사
# shutil.copy() 로 파일 복사 가능
# ("복사할 파일명" , "복사해 붙여 넣을 경로/새로운 이름.파일형식")
# shutil.copy("Tiger.txt", "./animal/Tigers_copy.txt")    # 기존은 Tiger.txt 이고 바뀐 이름은 Tiger_copy.txt 이다.


# 디렉토리 생성
# os.makedirs("beast", exist_ok=True)

# 파일 이동
# shutil.move() 로 파일 이동 가능
# ("이동 시킬 경로와 파일명" , "옮겨 놓을 곳의 경로")
# shutil.move("Tiger.txt", "./beast")


# 이름 변경에도 사용 가능
# shutil.move() 파일의 이름을 변경 시킬 수 있음 shutil.copy 와 비슷
# ("변경 할 주소와 파일명" , "변경 될 주소와 파일명")
# shutil.move("./animal/Tigers_copy.txt", "./animal/Tigers_2.txt")



# os.makedirs("./fruit/tropic", exist_ok=True)        #fruits 디렉토리에 tropic이라는 하위 디렉토리 생성
# shutil.move("./fruit/Banana.txt", "./fruit/tropic")         #fruits 디렉토리에 있는 Banana.txt 를 tropic 디렉토리로 이동
# os.makedirs("plant", exist_ok=True)         #현재 경로에 plant 디렉토리 생성



# 폴더 내용을 [재귀적]으로 복사
# 재귀적인 말이 어려우므로 전체 복사(디렉토리, 파일등)한다.
# 참고사항 !!  복사 당할 해당 디렉토리도 복사됨 , 복사 당할 디렉토리의 하위 파일,디렉토리만 되는게 아님
# shutil.copytree("복사 당할 디렉토리 경로" , "붙여 넣을 디렉토리 경로")
# shutil.copytree("./fruit", "./plant/fruit")


# 폴더를 재귀적으로 삭제
# shutil.rmtree("전체 삭제할 디렉토리 경로")
# shutil.rmtree("./plant")



# zipped 이라는 폴더 생성
# os.makedirs("./zipped", exist_ok=True)


# 폴더 압축
#shutil.make_archive() 는

shutil.make_archive("./zipped1/fruit1", "zip", "./fruit")
#첫 번째 매개변수("./zipped/fruit"): 압축 파일의 저장 경로 및 파일의 기본 이름을 지정합니다.
#여기서는 "./zipped/fruit"이므로, 현재 작업 디렉토리의 zipped 폴더 내에 fruit.zip 파일로 저장됩니다.
#만약 zipped 디렉토리가 존재하지 않으면, 이 디렉토리도 생성됩니다.
# ./zipped1/fruit1 이라고 내가 임의대로 적어서 실행함

#두 번째 매개변수("zip"): 생성될 압축 파일의 형식을 지정합니다.
#이 경우 "zip" 형식을 사용하므로, ZIP 압축 파일이 생성됩니다.
#다른 형식으로는 "tar", "gztar", "bztar", "xztar" 등이 있습니다.

#세 번째 매개변수("./fruit"): 압축할 디렉토리의 경로입니다.
#여기서는 현재 디렉토리 내의 fruit 폴더를 압축 대상으로 지정합니다.
# 이 폴더 내의 모든 파일과 하위 디렉토리가 포함되어 압축됩니다.


#unpacked이라는 디렉토리 생성
# os.makedirs("./zipped/unpacked", exist_ok=True)


# 압축 풀기
# shutil.unpack_archinve()로 압축풀기 가능
# 첫번째 변수에 압축 해제 할 대상의 파일 경로를 입력 ("./zipped1/fruit1.zip")
# 두번째 변수에 압축 해제하여 붙여 넣은 경로를 입력한다. ("./zipped/unpacked")
# 세번째 변수에는 압축 해제 할 대상의 파일 형식을 입력한다.
shutil.unpack_archive("./zipped1/fruit1.zip", "./zipped/unpacked", "zip")


# 정리하자면 해당 chapter에서
# fruit 폴더를 zipped1 폴더 하위에 zip형식으로 압축하였고
# zipped1 폴더에 zip형식으로 압축된 fruit1 (이름 변경함) 을
# zipped 폴더에 하위 unpacked 폴더 안에 압축을 해제 했음
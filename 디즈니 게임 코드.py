#게임 시작과 함께 미키마우스로 환영하기
print("디즈니 게임에 오신 것을 환영합니다!")

import turtle

t=turtle.Turtle()
t.width(3)
word="♥ Welcome to Disney! ♥"

def mickey():
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.begin_fill()
    t.goto(-95,140)
    t.circle(60)
    t.goto(95,140)
    t.circle(60)
    t.end_fill()
    t.pencolor("violet")
    t.write(str(word), font=("Times New Roman", 20, "bold"))

mickey()


#게임 설명
print("게임을 통해 당신이 얼마나 디즈니를 사랑하는지 알 수 있습니다!")
print("** 1단계는 20점, 2단계는 30점, 3단계는 50점을 획득할 수 있습니다! **")
print("")
print("그럼 시작해볼까요~? 시작하려면 엔터를 눌러주세요.")
input("")
print("---------------------------------------------------------------------------------")

#필요한 변수 설정 및 리스트 작성
from random import randint

movie_list=["Elsa", "Olaf", "Rapunzel", "Jasmin", "Troy"]
movie_name=["주먹왕 OO", "겨울OO", "하이스쿨 OOO", "프린세스 OOOO", "라이온 O"]
i=randint(0,4)
m=randint(0,4)
n=randint(0,2)
good=("와! 정답입니다! 다음 단계로 넘어가볼까요? 엔터를 눌러주세요.")
bad=("땡 아쉽네요ㅠ 다음 단계는 꼭 맞추시길 바래요~ 다음 단계를 위해 엔터를 눌러주세요.")
correct=0

#1단계
print("<1단계 문제입니다>")
print("")
print("1단계 문제는 등장인물을 보고 영화 제목을 맞추는 문제입니다! 단, '영어'로 답하셔야 해요~!")
print("")
print("등장인물은,", movie_list[i], "입니다. 무슨 영화일까요?")
print("")
answer1=input("정답은?")
print("")

if movie_list[i]=="Elsa":
    if answer1=="frozen":
        print(good)
        correct=correct+20
    else:
        print(bad)
        print("정답은, Frozen 이었습니다!")

if movie_list[i]=="Olaf":
    if answer1=="frozen":
        print(good)
        correct=correct+20
    else:
        print(bad)
        print("정답은, Frozen 이었습니다!")
        
if movie_list[i]=="Rapunzel":
    if answer1=="tangled":
        print(good)
        correct=correct+20
    else:
        print(bad)
        print("정답은, Tangled 였습니다!")
        
if movie_list[i]=="Jasmin":
    if answer1=="aladdin":
        print(good)
        correct=correct+20
    else:
        print(bad)
        print("정답은, Aladdin 이었습니다!")
    
if movie_list[i]=="Troy":
    if answer1=="high school musical":
        print(good)
        correct=correct+20   
    else:
        print(bad)
        print("정답은, High School Musical 이었습니다!")   

print("현재까지의 점수는", correct, "점 입니다.")        
input("")
        
#2단계
print("---------------------------------------------------------------------------------")
print("<2단계 문제입니다>")
print("")
print("2단계에서는 완성되지 않은 디즈니 영화 제목이 나올거에요! '제목의 풀네임'을 완성 시켜주세요~")
print("")
print("영화제목은,", movie_name[m], "입니다. 영화 제목은 무엇일일까요?")
print("")
answer2=input("정답은?")
print("")

if movie_name[m]=="주먹왕 OO":
    if answer2=="주먹왕 랄프":
        print(good)
        correct=correct+30
    else:
        print("땡! 정답은, '주먹왕 랄프' 였습니다!")

if movie_name[m]=="겨울OO":
    if answer2=="겨울왕국":
        print(good)
        correct=correct+30
    else:
        print("땡! 정답은, '겨울왕국' 이었습니다!")

if movie_name[m]=="하이스쿨 OOO":
    if answer2=="하이스쿨 뮤지컬":
        print(good)
        correct=correct+30
    else:
        print("땡! 정답은, '하이스쿨 뮤지컬' 이었습니다!")

if movie_name[m]=="프린세스 OOOO":
    if answer2=="프린세스 다이어리":
        print(good)
        correct=correct+30
    else:
        print("정답은, '프린세스 다이어리' 였습니다!")

if movie_name[m]=="라이온 O":
    if answer2=="라이온 킹":
        print(good)
        correct=correct+30
    else:
        print("정답은, '라이온 킹' 였습니다!")

print("현재까지의 점수는", correct, "점 입니다.")        
input("")

#3단계
print("---------------------------------------------------------------------------------")
print("<3단계 마지막 문제입니다>")
print("")
print("3단계에서는 등장인물의 특징을 보고 등장인물이 누구인지 '한글'로 답을 적어주세요!")
print("")

if n==0:
    print("1. 긴 머리카락")
    print("2. 초록 카멜레온")
    print("3, 높은 탑")    

elif n==1:
    print("1. 마법")
    print("2. 눈사람")
    print("3. 겨울")

else:
    print("1. 일곱 난쟁이")
    print("2. 독사과")
    print("3. 빨간 리본")

print("")
answer3=input("정답은?")
print("")

if n==0:
    if answer3=="라푼젤":
        print("와! 정답입니다!")
        correct=correct+50
    else:
        print("땡! 정답은, '라푼젤'이었습니다~")

if n==1:
    if answer3=="엘사":
        print("와! 정답입니다!")
        correct=correct+50
    else:
        print("땡! 정답은, '엘사'였습니다~")

if n==2:
    if answer3=="백설공주":
        print("와! 정답입니다!")
        correct=correct+50
    else:
        print("땡! 정답은, '백설공주'였습니다~")

print("현재까지의 점수는", correct, "점 입니다.")        

#게임 종료
print("")
print("이렇게 디즈니 게임이 종료되었습니다~! 결과를 한번 볼까요? 엔터를 눌러주세요")
input("")
print("---------------------------------------------------------------------------------")
if correct<=20:
    print(correct, "점 이시네요ㅠㅠ 조금만 더 노력하면 디즈니에 매력에 빠지실거에요~")
elif correct<=50:
    print(correct, "점 이네요! 디즈니 비기너시군요~?")
elif correct<=80:
    print(correct, "점이라니! 디즈니 팬이시군요~?")
else:
    print(correct, "점이나!? 디즈니 러버시군요!")

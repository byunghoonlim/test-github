# for 값 in 리스트

상자 = ["사과", "배", "콩", "두부"] #리스트

for 값 in 상자:
    print(값)

'''
상자안에 물건을 전부 까서
사과는 냉장실에
아이스크림은 냉동실에 넣어 주시고,
나머지는 폐기처분 해주세요.
'''

상자 = ["사과", "배", "콩", "두부", "아이스크림"] #리스트
냉장실 = []
냉동실 = []

for 값 in 상자:
    if 값 == "사과":
        print(f"'{값}' 냉장실에 넣기")
    elif 값 == "아이스크림":
        print(f"'{값}' 냉동실에 넣기")
    else:
        print(f"'{값}'은 폐기 처분")

#f-string
#문자와 변수를 혼재해서 문자열로 바꾸고 싶을때!
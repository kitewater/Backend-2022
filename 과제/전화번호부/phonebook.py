phonebook = []

while True:
    print("----------멋쟁이 사자처럼 전화번호부----------")
    print("------1)추가 2)조회 3)수정 4)삭제 q)종료------")
    print("----------------------------------------------")


    menu = input("원하시는 메뉴를 입력해주세요: ")
    
    if menu == "q":
        print("Process finished with exit code 0")
        break;

    elif menu == "1":
        name = input("이름을 입력해주세요: ")
        phone = input(name+"님의 번호를 입력해주세요: ")
        mail = input(name+"님의 메일을 입력해주세요: ")
        phonebook.append({"이름":name, "전화번호":phone, "메일":mail})
    
    elif menu == "2":
        name = input("조회를 원하는 이름을 입력해주세요: ")
        for i in phonebook:
            if i["이름"] == name:
                print(i)
            else:
                print("목록에 이름이 존재하지 않습니다.")

    elif menu == "3":
        name = input("수정을 원하는 이름을 입력해주세요: ")
        item, content = input("수정을 원하는 항목과 내용을 입력해주세요: ").split()
        for i in phonebook:
            if i["이름"] == name:
                i[item] = content
    
    elif menu == "4":
        name = input("삭제를 원하는 이름을 입력해주세요: ")
        for i in phonebook:
            if i["이름"] == name:
                phonebook.remove(i)

    else:
        print("없는 메뉴입니다. 다시 선택해주세요. ")


elif1 = 0
elif2 = 0
elif3 = 0

while True:
    ans = input("あなたはツイ廃ですか？y/N:")

    if ans == "y":
        print("インターネットやめろ")
        break
    elif ans == "N":
        if elif1 <= 9:
            print("嘘つけ")
            elif1 += 1
        else:
            print("現実みろ^^")
    elif ans == "n":
        if elif2 <=9:
            print("Please enter N instead of n")
            elif2 += 1
        else:
            print("Nだっつってんだろ！！")
    else:
        if elif3 <= 19:
            print("yかNって言ってんだろ")
            elif3 += 1
        elif elif3 <= 29:
            print("答えろ")
            elif3 += 1
        elif elif3 <= 99:
            print("...")
            elif3 += 1
        else:
            print("お前の勝ちだ")
            break

        
end = input()
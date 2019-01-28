"""HangmanProgram"""
def hangman():
    """"Choose your topic"""
    print("1. Moblie Popular Game")
    print("2. Serie A Team Footballer (2018/2019)")
    print("3. Onepiece Character")
    words = ""
    answer = []
    score = 0
    picked = ""
    wrong = 10
    picked_wrong = ""
    check_first_time = 0
    #เลือกหัวข้อ
    choose = input("Please Choose 1-3 : ")
    if(check_first_time == 0):
        if(choose == "1"):
            print("Hint: \"ETERNAL MMORPG!!\"")
            file = open("Moblie Popular Game.txt", "r") #เปิดไฟล์หมวดหมู่ของคำ และอ่านคำ
            lines = file.readlines()
            file.close()
            for line in lines:
                print(line)
                if(line.find( "Ragnarok" ) != -1):
                    words = words + "Ragnarok"
            for i in range(len(words)):
                answer.append("_")
                # print("_", end = " ")
            i = 0 #reset i
            for x in answer:
                print(x, end = " ") # โชว์คำตอบปัจจุบัน
            x = 0 #reset x
            print("score " +"{}".format(score) +", remaining wrong guess " + "{}".format(wrong))
            while(wrong != 0):
                pickwords = input("Pick a word: ") #pick a word
                if(pickwords is "R" ):
                    if(picked.find("R") == -1):
                        score += 12.5
                        answer[0] = "R" #ใส่คำที่ถูกต้องลงใน List
                        picked = picked + "R"
                        for x in answer:
                            print(x, end = " ") # โชว์คำตอบปัจจุบัน
                        x = 0 #reset x
                    else:
                        for x in answer:
                            print(x, end = " ") # โชว์คำตอบปัจจุบัน
                        x = 0 #reset x
                    print("score " +"{}".format(score) + ", remainng wrong guess "  + "{}".format(wrong))
                elif(pickwords is "a"):
                    if(picked.find("a") == -1):
                        score += 25
                        answer[1] = "a" #ใส่คำที่ถูกต้องลงใน List
                        answer[4] = "a" #ใส่คำที่ถูกต้องลงใน List
                        picked = picked + "a"
                        for x in answer:
                                print(x, end = " ") # โชว์คำตอบปัจจุบัน
                        x = 0 #reset
                    else:
                        for x in answer:
                            print(x, end = " ") # โชว์คำตอบปัจจุบัน
                        x = 0 #reset x
                    print("score " +"{}".format(score) + ", remainng wrong guess "  + "{}".format(wrong))
                elif(pickwords is "g"):
                    if(picked.find("g") == -1):
                        score += 12.5
                        answer[2] = "g" #ใส่คำที่ถูกต้องลงใน List
                        picked = picked + "g"
                        for x in answer:
                            print(x, end = " ") # โชว์คำตอบปัจจุบัน
                        x = 0 #reset
                    else:
                        for x in answer:
                            print(x, end = " ") # โชว์คำตอบปัจจุบัน
                        x = 0 #reset x
                    print("score " +"{}".format(score) + ", remainng wrong guess "  + "{}".format(wrong))
                elif(pickwords is "n"):
                    if(picked.find("n") == -1):
                        score += 12.5
                        answer[3] = "n" #ใส่คำที่ถูกต้องลงใน List
                        picked = picked + "n"
                        for x in answer:
                            print(x, end = " ") # โชว์คำตอบปัจจุบัน
                        x = 0 #reset
                    else:
                        for x in answer:
                            print(x, end = " ") # โชว์คำตอบปัจจุบัน
                        x = 0 #reset x
                    print("score " +"{}".format(score) + ", remainng wrong guess "  + "{}".format(wrong))
                elif(pickwords is "r"):
                    if(picked.find("r") == -1):
                        score += 12.5
                        answer[5] = "r" #ใส่คำที่ถูกต้องลงใน List
                        picked = picked + "r"
                        for x in answer:
                            print(x, end = " ") # โชว์คำตอบปัจจุบัน
                        x = 0 #reset
                    else:
                        for x in answer:
                            print(x, end = " ") # โชว์คำตอบปัจจุบัน
                        x = 0 #reset x
                    print("score " +"{}".format(score) + ", remainng wrong guess "  + "{}".format(wrong))
                elif(pickwords is "o"):
                    if(picked.find("o") == -1):
                        score += 12.5
                        answer[6] = "o" #ใส่คำที่ถูกต้องลงใน List
                        picked = picked + "o"
                        for x in answer:
                            print(x, end = " ") # โชว์คำตอบปัจจุบัน
                        x = 0 #reset
                    else:
                        for x in answer:
                            print(x, end = " ") # โชว์คำตอบปัจจุบัน
                        x = 0 #reset x
                    print("score " +"{}".format(score) + ", remainng wrong guess "  + "{}".format(wrong))
                elif(pickwords is "k"):
                    if(picked.find("k") == -1):
                        score += 12.5
                        answer[7] = "k" #ใส่คำที่ถูกต้องลงใน List
                        picked = picked + "k"
                        for x in answer:
                            print(x, end = " ") # โชว์คำตอบปัจจุบัน
                        x = 0 #reset
                    else:
                        for x in answer:
                            print(x, end = " ") # โชว์คำตอบปัจจุบัน
                        x = 0 #reset x
                    print("score " +"{}".format(score) + ", remainng wrong guess "  + "{}".format(wrong))
                elif(pickwords is ""):
                    print("Please pick some word.")
                else:
                    wrong -= 1
                    if picked_wrong.find(pickwords) == -1 :
                        picked_wrong = picked_wrong + pickwords + " "
                    else:
                        pass
                    for x in answer:
                        print(x, end = " ") # โชว์คำตอบปัจจุบัน
                    x = 0 #reset x
                    print("score " +"{}".format(score) + ", remainng wrong guess "  + "{}".format(wrong) + ", wrong guessed: " + picked_wrong)
        else:
            print("score " +"{}".format(score) + ", remainng wrong guess "  + "{}".format(wrong) + ", wrong guessed: " + picked_wrong)
# ###########################################################################################################################################
#     if(choose == "2"):
#         print("Hint: \"Zebra\"")
#         file = open("Serie A Team Footballer.txt")
#         lines = file.readlines()
#         file.close()
#         for line in lines:
#             if line.find( "Juventus" ) != -1:
#                 words = words + "Juventus"
#
# ###########################################################################################################################################
#     if(choose == "3"):
#         print("Hint: \"One of Emperors\"")
#         file = open("Onepiece Character.txt")
#         lines = file.readlines()
#         file.close()
#         for line in lines:
#             if line.find( "Kaido" ) != -1:
#                 words = words + "Kaido"







hangman()

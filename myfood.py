import random
# 화면에 음식 리스트를 추가하는 기능 
def print_list(foodlist):
    str = ""
    for i, food in enumerate(foodlist):
        # print(f"{i+1}. {food})
        str = str + f"{i+1}. {food} "

    print(str) # 위에서 더해진 문자열을 여기서 출력 

# 음식 리스트중에서 하나를 추천해주는 기능 
def print_rand_list(foodlist): 
    for i in range(5):
        food = random.choice(foodlist)
        print(f"{i+1}. {food}")



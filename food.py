# 음식 리스트 중에서 
# 그중 하나를 추천
import random

# 음식 리스트 중에서 
foodlist = ["짜장면", "짬뽕","탕슉","우동","돈까스"]
#print(foodlist[2])
# 그중 하나를 추천
food = random.choice(foodlist)
print(food)

# 5번을 연속으로 추천해보자
for i in range(5):
    # print(i+1)
    food = random.choice(foodlist)
    # print(i+1 + ". " + food)
    print(f"{i+1}. {food}")
    
print("종료")
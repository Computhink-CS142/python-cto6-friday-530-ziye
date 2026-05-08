# import random
# first_num=random.randint(1,6)
# second_num=random.randint(1,6)
# third_num=random.randint(1,6)
# print("1st number",str(first_num))
# print("2st number",str(second_num))
# print("3st number",str(third_num))
# first_even=first_num%2
# second_even=second_num%2
# third_even=third_num%2
# all_even_or_odd=first_even==second_even==third_even
# print("all numbers are even/odd:",str(all_even_or_odd))

# user=input("how much day mr whatever")
# if user<25:
#     print("return ya book")
# else:
#     print("byebye")

# user=input("how many apples you wanna buy")
# if user>10:
#     print("you will get 10% persent discount secret event until april!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#     price=user-0.01
#     print("pls pay$",price)
# else:
#     print(user,"this is your amt you need to pay")

######################fruitifresh#######################
num_apple=input("how much apples")
num_orange=input("how much oranges")
if num_apple>5:
    print("you will have a 10% discount for all the apples")
    apple_price=0.60*num_apple
    apple_price=apple_price-0.1
    print("you'll pay",apple_price)
else:
    apple_price=0.60*num_apple
    print("you'll pay",apple_price)
num_apple=input("how much apples")
num_orange=input("how much apples")
if num_orange>5:
    print("you will have a 10% discount for all the apples")
    orange_price=0.60*num_orange
    orange_price=orange_price-0.1
    print("you'll pay",apple_price)
else:
    orange_price=0.60*num_orange
    print("you'll pay",orange_price)

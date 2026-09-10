# To print hello world.

#   start 
#     print "Hello World"
#   stop

print("Hello World", end="\t")
print("Thank you :)")


# # To find whether the no is even or odd.

#    start
#     input number n
#     if n mod 2 == 0:
#         print n,"even"
#     else:
#         print n,"odd"
#    stop

n = 4
if n % 2 == 0:
    print("Even")
else:
    print("Odd")



# To find the greatest among 3 nos.

#   start 
#      input number n1,n2,n3
#      if n1 > n2 and n1 > n3:
#         print n1,"greatest"
#      elif n2 > n1 and n2 > n3:
#         print n2,"greatest"
#      else:
#         print n3,"greatest"
#    stop

pos, neg, zero = 0, 0, 0
input = [1, 2, 0, -4]
for num in input:
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zero += 1
print("Positive: ", pos, "\n", "Negative: ", neg, "\n", "Zeros: ", zero)


# To find the number is positive or negative or zero.

#  start 
#    input number n
#    if n > 0:
#      print n,"positive"
#    elif n < 0:
#      print n,"negative"
#    else:
#      print n,"zero"
#   stop 

num1 = 12
num2 = 23
num3 = 34
print("Greatest: ", end="")
if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 > num3:
        print(num2)
    else:
        print(num3)




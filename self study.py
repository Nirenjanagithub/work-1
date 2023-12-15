#number =input("Enter the number: ")
#x=int(number)
#if x % 2==0:
#    print(x,"is an Even number")
#else:
#    print(x,"is an Odd number")

    # prob 2#
#number = input("Enter the number: ")
#x=float(number)
#if x<0:
#    print(x,"is a negative numer")  
#elif x==0:
#    print(x,"is nither positive nor negative")
#else:
#    print(x,"is a positive number")
#num_1= input("Enter number= ")
#num_2= input ("Enter another number= ")
#sum = float(num_1) + float(num_2)
#print(sum)
# arr = ['x','y','z']
# letter = input("Enter :")
# for letter in arr:
#     if letter == arr:
#         print(letter)
# else:
#     print(False)
# r1=int(input("Enter the number : "))
# r2=int(input("Enter another number : "))
# n= range(r1,r2)
# for i  in n:
#     print(i)

# r1=int(input("Enter the number : "))
# r2=int(input("Enter another number : "))
# n= range(r1,r2)
# for i in n:
#     if i % 2== 0:
#         print(i)
    
# sum=0
# r2=int(input("Enter number : "))
# n= range(1,r2+1)
# for i in n:
#     sum+=i
# print(sum)

# sum = 0
# number_one = int(input("Eneter first number : "))
# number_two = int(input("Enter another number : "))
# r = range(number_one, number_two)
# for i in r:
#     if i%2 !=0:
#         x = i
#         sum+=x
# print(sum)
# start_number = int(input("Enter the first number : "))
# end_number = int(input("Enter another number : "))
# number = int(input("Enter the number: "))
# n = range(start_number,end_number)
# for i in n:
#     mul= i * number
#     print(i, "x" ,number, "=" ,mul)

# lts = [1,2,3,4,5,6,7,8,9,9,10]
# for i in  lts:
#     print(i)
# number = str(input("Enter a number: "))
# count = 0
# for i in number:
#     count+=1
# print(count)
    
# given_string = str(input("Enter a string: "))
# reverse_string = ""
# for i in given_string:
#     reverse_string = i + reverse_string
#     if reverse_string == given_string:
#         print("Its is a palindrome")

#         break
# else:
#     print("not a palindrome")

# given_string = str(input("Enter a string: "))
# reverse_string = ""
# for i in given_string:
#     reverse_string = i + reverse_string

# print(reverse_string)

# number = str(input("Enter a number : "))
# length = len(number)
# armstrong_number =0
# convert_length = int(length)
# for i in number:
#     convert_number = int(i)
#     armstrong_number+=pow(convert_number, convert_length)
#     converted_armstrong = str(armstrong_number)
# if converted_armstrong== number:
#     print("It is an Armstrong number")
    
# else: 
#     print("It is NOT an Armstrong number")

number_one = int(input("Enter a number: "))
number_two = int(input("Enter another number: "))
lst = range(number_one, number_two)
even =""
odd =""
for i in lst:
    if i%2==0:
        x=str(i)
        even = x + even
        len_one=len(even)
    elif i%2 != 0:
        y=str(i)
        odd = y + odd
        len_two = len(odd)
print(len_one, "is length of Even number")
print(len_two, "length of Odd number" )
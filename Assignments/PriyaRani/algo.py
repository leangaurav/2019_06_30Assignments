# def find_in_range(lnum,start,end):
#     print(lnum,start,end)
#     list_result_num=[]
#     for i in lnum:
#         if i >=start and i <=end:
#             print(i)
#             list_result_num.append(i)
#     print("New resultant list are:",list_result_num)
# find_in_range([3,5,10,24,28,8,2,7],5,24)

# find_in_range([3,10, 5, 8, 2, 7], 5, 9)
# List of numbers = [3,10, 5, 8, 2, 7]
# start = 5
# end = 9
# list returned should be [5, 8, 7]


def mean(a):
    print(a)
    sum=0
    # for i in a:
    #     sum +=i
    # print(sum)
    # avg=sum//len(a)
    # print(avg)
    [sum + i for i in a ]
    print(list(map(lambda num: sum+num, a)))
    #result=list(filter(lambda num:sum(num)//len(a),a))
    print(sum)
mean([10,203,40,560])








# def second_maximum(a):
#     if(len(a)>2):
#         if a[0] > a[1]:
#             f_max=a[0]
#             s_max=a[1]
#         else:
#             f_max=a[1]
#             s_max=a[0]
#         for i in range(2,len(a)):
#             if a[i]> f_max:
#                 s_max=f_max
#                 f_max=a[i]
#
#             if a[i]>s_max:
#                 s_max=a[i]
#         f_s = f_max, s_max
#         return f_s
#     else:
#         print("Enter the list wiht atleast 3 number")
# print(second_maximum([3,5,67,54,78]))
# print(second_maximum([354,813,67,15,267]))
# print(second_maximum([38,59,627,524,378]))




# def maximum(a):
#     result=list(max max=i if max <i,for i in a)
#     result=[ max=i for i in a if max<i]
# maximum([2,3,4,5,67,1])


# def maximum(a):
#     print(a)
#     max=0
#     for i in a:
#         if max < i:
#             max=i
#     print(max)
# maximum([2,3,4,5,6,7])






# def count_even_odd(seq):
#     resulteven=list(filter(lambda num:num%2==0,seq))
#     print(len(resulteven))
#     print(resulteven)
#     resultodd=list(filter(lambda num: num%2!=0,seq))
#     print(len(resultodd))
#     print(resultodd)
# count_even_odd([10,20,3,5,7,8,9])

        #OR


# def count_even_odd(seq):
#     resulteven=list(filter(lambda num:num%2==0,seq))
#     print(len(resulteven))
#     resultodd=list(filter(lambda num: num%2!=0,seq))
#     print(len(resultodd))
#     return resulteven,resultodd
# print(count_even_odd([10,20,3,5,7,8,9]))





# def reverse_list(a):
#     l=len(a) - 1
#     for i in range(0,l):
#         if i < l:
#             temp=a[l]
#             a[l]=a[i]
#             a[i]=temp
#             print("a[i]==",a[i])
#             print("l=", l)
#             print("i=",i)
#             i+=1
#             l-=1
#         print(a)
# reverse_list([10,20,30,40])

# def reverse_list(a):
#     reversel=[]
#     for i in range(len(a)-1,-1,-1):
#         reversel.append(a[i])
#     print(reversel)
# reverse_list([10,20,30,40])
# def reverse_list(a):
#     reversel=[]
#     list(map(lambda i:reversel.append(a[i]),range(len(a)-1,-1,-1)))
#     print(reversel)
# reverse_list([10,20,30,50])


#question 1
#What is the time, space complexity of following code:
#int a = 0, b = 0;
#for (i = 0; i < N; i++) {
#a = a + 1;
#}
#for (j = 0; j < M; j++) {
#b = b + j;
#}

#ANSWER:
  #The first loop O(n)and the second loop is O(m).We don't know which one is bigger so we can say
# O(n+m) also O(max(n,m)). The space complexity is constant/O(1) as no additional space utilized.

#What does it mean when we say that an algorithm X is asymptotically more efficient than Y?
#a)X will be a better choice for all inputs
#b)X will be a better choice for all inputs except possibly small inputs
#c)X will be a better choice for all inputs except possibly large inputs
#d)Y will be a better choice for small inputs

#ANSWER:
# In asympotic we consider growth of algorithm in terms of input size. An algorithm X is said to
# be asympotically better than Y if X takes smaller time than Y for all input sizes n larger than a value n0 where n0>0.
#Therefore option b.



#Write a Python program to print even numbers in a list.
list1=[1,2,3,4,5,6,7,8,9,10]
for no in list1:
    if no%2==0:
        print("Even number from list are ",no)

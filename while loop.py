# #print all the numbers rom 1 to 10 using loops 
count =1 
while count <= 10:
    print(count)
    count += 1


# # Input from user
answer=""
while answer !="yes" :
    answer = input("What do you want : yes or no ? ")
print(answer)

#3 attempt 
#yes on the 3 attempt , " print -Glad we are on same page"
#Otherwise : 3 strikes "You are out "

attempt =0
while attempt<3:
    answer = input("What do you want : yes or no ? ")
    if answer =="yes":
        print("Glad we are on same page")
        break
    attempt =+1
else:
  print("3 sttrikes, You arre out")

 


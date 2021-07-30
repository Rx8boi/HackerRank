def print_factors(x, p):
  arr=[]


  print("The factors of",x,"are:")
   
  for i in range(1, x + 1):
       if x % i == 0:
         arr.append(i)

  print(arr, p)
  print(arr[p-1])

num = 320
p = 1
print_factors(num, p)
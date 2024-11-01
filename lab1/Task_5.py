def remove(source,size,idx):
  k= idx

  for i in range(k,size):
    source[i]= source[i+1]
    source[i+1]=0
  return source
source=[10,20,30,40,50,0,0]
remove(source,5,2)
print(source)


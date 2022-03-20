N = int(input())
inList = list(map(int,input().split()))
inList.sort()
#print(inList)
result = 0 #총 그룹 수
count = 0 #현재 그룹에 포함된 모험가의 수
for i in inList:
  count+=1 #현재 그룹에 하나씩 포함시키기
  if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상
    result+=1
    count = 0
print(result)
    
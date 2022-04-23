import csv
import time

with open('processes1.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(len(data))
length = len(data)

print(data)
list_check = 1
while list_check == 1:
    if(len(data)==0):
        list_check = 0
    for i in range(0,length):
        for j in range(0, 3):
            # print(" ")
            # print(j)
            try:
                print(f"Proessing: {data[i][0]}")
                time.sleep(1)
                data[i][1] = int(data[i][1]) - 1
                if(data[i][1] !=0):
                    print(f"Requiring {data[i][0]}")
                    data.append(data[i])
                    del data[i]
            except Exception as ex:
                pass

            try:
                if(data[i][1] == 0):
                    
                    print(f"{data[i][0]} finished!")
                    del data[i]
                    print(f"Presses lef in the queue: {len(data)}")
            except Exception as ex:
                pass
                # print(f"after processing: {data[i][1]}")
        # print("    ")
    
        

print(data)


 
 
# from queue import Queue
 
# # Initializing a queue
# q = Queue(maxsize = 3)
 
# # qsize() give the maxsize
# # of the Queue
# print(q.qsize())
 
# # Adding of element to queue
# q.put('a')
# q.put('b')
# q.put('c')
 
# # Return Boolean for Full
# # Queue
# print("\nFull: ", q.full())
 
# # Removing element from queue
# print("\nElements dequeued from the queue")
# print(q.get())
# print(q.get())
# print(q.get())
 
# # Return Boolean for Empty
# # Queue
# print("\nEmpty: ", q.empty())
 
# q.put(1)
# print("\nEmpty: ", q.empty())
# print("Full: ", q.full())
 
# This would result into Infinite
# Loop as the Queue is empty.
# print(q.get())
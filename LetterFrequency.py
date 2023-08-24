
first_input = input("First input: ")
second_input = input("Second input: ")

length_of_first_input = len(first_input)
count = 0

for i in first_input:
  # print(i)
  if second_input in i:
    count = count + 1
    
frequency = (count / length_of_first_input) * 100

print(int(frequency))
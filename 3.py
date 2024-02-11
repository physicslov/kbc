import time
rs = 0
print('WELCOME TO KBC\n')
print('you get 4 questions and for each, you get four options and get 20 rs. for every correct option in 10 seconds')

questions = ['Who is the Prime Minister of America:', 'What is the capital of Bihar:', 'In which year did corona come to India:', 'Who invented the electric bulb:']
options1 = ['joe biden', 'patna', '2019', 'thomas alva edison']

for i in range(0,4):
    print(questions[i])
    
    start_time = time.time()  # Record the start time
    
    ans = input("Enter your answer: ").lower()
    
    elapsed_time = time.time() - start_time  # Calculate the elapsed time
    
    if elapsed_time > 10:
        print("TIME'S UP!")
        exit()

    if ans == options1[i]:
        print('SAHI JAWAB')
        rs += 20
    else:
        print('GALAT JAWAB')
        break

print("You have won", rs, 'rupees')




  
            
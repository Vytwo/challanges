
start = input()
start= start.split(" ")
number = int(start[0])
total_steps = int(start[1])

sample = []
#    "."" or "*"

for i in range(number):
    line = input()
    sample.append(line)

matrix =[]
for i in range(number):
    matrix.append(str(i) + sample[i])


def function(steps,list):
    global number
    global sample

    if steps > 1:
        alt = list
        list = []

        for i in range(len(alt) * number):
            list.append(f"{i}")
        firsts = list
        for newline in alt:
            for character in newline:
                if character == ".":
                    for i in range(number):
                        list[alt.index(newline) * number + i] += sample[i]

                if character == "*":
                    for i in range(number):
                        list[alt.index(newline) * number + i] += number * "*"
                
        
        steps -= 1
        function(steps,list)
    else:
        for line in list:
            print(line[1::])
        
    

function(total_steps, matrix)



"""
2 3
.*
..

c0mpleted

---------->

.*
..

.***
..**
.*.*
....

.*******
..******
.*.*****
....****
.***.***
..**..**
.*.*.*.*
........



"""
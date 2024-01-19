
time=0
def name(n):
    global time
    if(time<n):
        print('shash')
        time+=1
        name(n)  #recursive calling

name(5)

def name(n, count=0):
    if count < n:
        print('shash')
        name(n, count + 1)  # Recursive call

# Call the function with an argument
name(5)

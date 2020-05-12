"""

Attempting to do some datascience on a dumb prng vs C rand()

"""

import matplotlib.pyplot as plt

def avg(nums):
    return sum(nums) / len(nums)

def fill_map(m, nums):
    for x in nums:
        m[x//1000]+=1
        
def fill_digits(m, nums):
    for x in nums:
        while x > 0:
            digit = x%10
            m[digit] += 1
            x//=10
            
def do_erat(arr):
    arr[0] = False
    for x in range(2, len(arr)):
        if x:
            for y in range(2*x, len(arr), x):
                arr[y] = False
            

def get_pows(n, max_el):
    res = []
    n_copy = n
    while n < max_el:
        res.append(n)
        n*=n_copy
    return res


#reading rands from files
                
c_rands = []
with open('c_rand.txt') as c_rand_out:
    line = c_rand_out.readline()
    while line != "":
        num = line.split()
        for x in num:
            c_rands.append(int(x))
        line = c_rand_out.readline()

my_dummy_rands = []

with open('dummy_rand.txt') as dummy_rand_out:
    line = dummy_rand_out.readline()
    while line != "":
        num = line.split()
        for x in num:
            my_dummy_rands.append(int(x))
        line = dummy_rand_out.readline()

#min/max/avg
        
c_max = max(c_rands)
my_max = max(my_dummy_rands)
c_min = min(c_rands)
my_min = min(my_dummy_rands)
c_avg = avg(c_rands)
my_avg = avg(my_dummy_rands)


#distribution in thousands

c_map = {i : 0 for i in range(0, c_max//1000+1)}
fill_map(c_map, c_rands)

my_map = {i : 0 for i in range(0, my_max//1000+1)}
fill_map(my_map, my_dummy_rands)

cx, cy = [],[]
for k, v in c_map.items():
    cx.append(k)
    cy.append(v)

plt.figure()
plt.bar(cx,cy)
plt.title('c rand()')
plt.xlabel('thousands')
plt.ylabel('numbers in thousand')
plt.show()

my_x, my_y = [],[]
for k, v in my_map.items():
    my_x.append(k)
    my_y.append(v)

plt.figure()
plt.bar(my_x,my_y)
plt.title('my dummy rand()')
plt.xlabel('thousands')
plt.ylabel('numbers in thousand')
plt.show()


#digit frequency

c_digits = {i : 0 for i in range(10)}
fill_digits(c_digits, c_rands)

plt.figure()
plt.bar(c_digits.keys(), c_digits.values())
plt.title('c rand() digit frequency')
plt.xlabel('digits')
plt.ylabel('freqs')
plt.show()

my_digits = {i : 0 for i in range(10)}
fill_digits(my_digits, my_dummy_rands)

plt.figure()
plt.bar(my_digits.keys(), my_digits.values())
plt.title('my dummy rand() digit frequency')
plt.xlabel('digits')
plt.ylabel('freqs')
plt.show()

#primes

c_primes = {'prime' : 0,
            'composite' : 0}

my_primes = {'prime' : 0,
            'composite' : 0}

erat = [True for i in range (max(c_max, my_max) + 1)]
do_erat(erat)

for x in c_rands:
    if erat[x]:
        c_primes['prime']+=1
    else:
        c_primes['composite'] += 1
        
for x in my_dummy_rands:
    if erat[x]:
        my_primes['prime']+=1
    else:
        my_primes['composite'] += 1
        
plt.figure()
plt.bar(c_primes.keys(), c_primes.values())
plt.title('c rand() primes')
plt.show()

plt.figure()
plt.bar(my_primes.keys(), my_primes.values())
plt.title('my dummy rand() primes')
plt.show()

#2^n
pows_of_2 = get_pows(2, max(c_max, my_max))
c_pow = 0
for x in c_rands:
    if x in pows_of_2:
        c_pow+=1
        
my_pow = 0
for x in my_dummy_rands:
    if x in pows_of_2:
        my_pow+=1
        
plt.figure()
plt.bar(['c rand', 'my dummy rand'], [c_pow, my_pow])
plt.title('num of elements = 2^n')
plt.show()
          

#even vs odd
c_pairity = {'even': 0, 'odd':0}
for x in c_rands:
    if x % 2:
        c_pairity['odd']+=1
    else:
        c_pairity['even']+=1
        

my_pairity = {'even': 0, 'odd':0}
for x in my_dummy_rands:
    if x % 2:
        my_pairity['odd']+=1
    else:
        my_pairity['even']+=1
             
        
plt.figure()
plt.bar(['c rand() evens', 'c rand ()odds', 'my rand() evens', 'my rand() odds'],
          [c_pairity['even'], c_pairity['odd'],my_pairity['even'],
          my_pairity['odd']])
plt.title('even vs odd')
plt.show()          

         
#Duplicates
c_same = 0
s = set()
for x in c_rands:
    if x in s:
        c_same+=1
    else:
        s.add(x)

print(c_same, len(s))


sizes = [c_same, len(s)]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels = ('Duplicates', 'Uniques'), autopct='%1.1f%%')
ax1.axis('equal')
ax1.set(title='c rand()')
plt.show()

my_same = 0
s.clear()

for x in my_dummy_rands:
    if x in s:
        my_same+=1
    else:
        s.add(x)
        
print(my_same, len(s))    
          
sizes = [my_same, len(s)]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels = ('Duplicates', 'Uniques'), autopct='%1.1f%%')
ax1.axis('equal')
ax1.set(title='my dummy rand')
plt.show()

#sequence
s.clear()
c_seq = []
curr_seq = 0
for x in c_rands:
    if x in s:
        s.clear()
        c_seq.append(curr_seq)
        curr_seq = 0
    else:
        curr_seq+=1
        s.add(x)
print(c_seq)

s.clear()
my_seq = []
curr_seq = 0
for x in my_dummy_rands:
    if x in s:
        s.clear()
        my_seq.append(curr_seq)
        curr_seq = 0
    else:
        curr_seq +=1
        s.add(x)

print(my_seq)

plt.figure()
plt.plot(my_seq)
plt.plot(c_seq)
plt.show()

print(f'longest seq my dummy prng: {max(my_seq)}\nlongest seq c rand(): \
{max(c_seq)}')
          
          
        
          
          
          
          
          
          
          
          
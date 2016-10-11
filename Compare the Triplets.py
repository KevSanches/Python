import sys
anna_result = 0
bob_result = 0

anna = sys.stdin.readline()
bob = sys.stdin.readline()

anna = anna.split()
bob = bob.split()

for i in range(3):
	if int(anna[i]) > int(bob[i]):
		anna_result += 1
	elif int(anna[i]) < int(bob[i]):
		bob_result += 1

print (anna_result, bob_result)


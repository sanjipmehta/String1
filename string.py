#write a program for following requirement?
#-->a4k3b2
#ans-->aeknbd
s='a4k3b2'
output=''
for x in s:
	if x.isalpha():
		output+=x
		ch=x
	else:
		new=chr(ord(ch)+int(x))
		output+=new
print(output)
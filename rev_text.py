import re, colorama, os
text = input("\033[35m\033[1mТекст: \033[36m")
text = re.split(r' ', text)
#col_text = len.text
if len(text) == 2:
	var1 = text[0]
	var2 = text[1]
	var1_bk = re.findall(r'\w', var1)
	var2_bk = re.findall(r'\w', var2)
	up_tx = var2_bk[0].upper()
	down_tx = var1_bk[0].lower()
	print("\033[32m" + str(up_tx) + "\033[37m" + var1[1:30] + " \033[32m" + str(down_tx) + "\033[37m" + var2[1:30])
	os.system("python rev_text.py")
else:
	print("\033[31mДля корректного вывода вводите не больше, не меньше двух слов!")
	os.system("python rev_text.py")
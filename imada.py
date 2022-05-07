#初心者だから変なコードだと思う
import random
imada = 50
kougeki = 0
nurunuru = 100
kaifuku = 0
ryou = 0
syurui = 0
sousa = 1
hananoa = 5
int(ryou)
int(hananoa)
int(kaifuku)
int(syurui)
int(kougeki)
int(imada)
int(sousa)
print("入れ歯のヌルヌル HP100")
print("今田耕司　HP50")
while True:
	print("入れ歯のヌルヌルの体力")
	print(nurunuru)
	damage = random.randint(1, 5)
	int(damage)
	imada -= damage
	print("入れ歯のヌルヌルの攻撃")
	print(damage)
	print("今田耕司ののこり体力")
	print(imada)
	print("攻撃a 回復b")
	sousa = input(">_")
	if sousa == "a":
		kougeki = random.randint(3, 10)
		print("今田耕司の攻撃")
		print(kougeki)
		nurunuru -= kougeki
	elif sousa == "b":
		print("ハナノア(水):a ハナノア(ハナノア液):b")
		print("ハナノア液の残り(水は無制限)")
		print(hananoa)
		kaifuku = input("ハナノアの種類: ")
		if kaifuku == "a":
			ryou = random.randint(0, 2)
			imada += ryou
			print("回復した体力")
			print(ryou)
		elif kaifuku == "b":
			hananoa -= 1
			if hananoa <  0:
				print("ハナノアが足りない!")
			elif hananoa > 1:
				ryou = random.randint(5, 15)
				print("回復した体力")
				print(ryou)
				imada += ryou
	if nurunuru <= 0:
		print("入れ歯のヌルヌルを倒した")
		break
	if imada <= 0:
		print("今田耕司死亡...")
		break		
	
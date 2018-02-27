number=485
result= int(number/60)
remainder= number%60
print("saat= " + str(result))
print("dakika= " + str(remainder))

result= int(number/30)
remainder= number%30
print("ay= " + str(result))
print("gün= " + str(remainder))

result= int(number/365)
remainder= number%30
print("yıl= " + str(result))
print("ay= " + str(remainder))

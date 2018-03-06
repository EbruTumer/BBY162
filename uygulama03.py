__author__ = "Ebru Tümer"
#Şehir plakalarını liste ve sözlük şeklinde gösterme ve üzerinde birkaç işlem yapma.
plakalar= {"Ankara":"06", "Adana":"01", "Samsun":"55", "Çanakkale":"18", "Kayseri" : "38", "Ordu": "52", "Trabzon": "61"}
print(plakalar)
plakalar["Çankırı"]=17
print(plakalar)
del plakalar['Adana']
print(plakalar)
print(plakalar.keys())
print(plakalar.values())
print("İzmir" in plakalar)
plakalar["İzmir"]=35
print(plakalar)
print("İzmir" in plakalar)
print(len(plakalar))
print(plakalar["Ankara"])
print(plakalar.clear())







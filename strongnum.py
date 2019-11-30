def faktorial(x):
    fakt = 1
    while x >= 1:
        fakt = fakt * x
        x = x - 1
    return fakt

n = int(input("Input n = "))
nCopy = n
jumlah = 0
while nCopy > 0:
    nMod = nCopy % 10
    jumlah = jumlah + faktorial(nMod)
    nCopy = nCopy // 10
if jumlah == n:
    print("Strong number")
else:
    print("Bukan strong number")
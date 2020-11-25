class Sportag:
  def __init__(self, sor):
    self.nev = sor[0]
    self.napok = sor[1:len(sor)]
    for i in range(len(self.napok)):
      self.napok[i] = int(self.napok[i])

datumok = [28, 29, 30, 31, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#1. feladat
sportagak = []
for sor in open("London2012.txt", encoding="UTF-8-sig"):
  sportagak.append(Sportag(sor.strip().split(';')))

#2. feladat:
i = 0
while sportagak[i].nev != "Atlétika": i += 1
c = 0
for n in sportagak[i].napok:
  if n > 0: c += 1

print(f"2. feladat:\n\tDöntős napok száma atlétika sportágban: {c} db")

#3. feladat:
i = 0
while sportagak[i].nev != "Úszás": i += 1
c = 0
for n in sportagak[i].napok:
  c += n
print(f"3. feladat:\n\tAranyérmek száma úszásban: {c} db")

#4. feladat:
npd = sportagak[0].napok

for s in sportagak[1:len(sportagak)]:
  i = 0
  for n in s.napok:
    npd[i] += n
    i += 1

maxi = 0
for i in range(len(npd)):
  if npd[i] > npd[maxi]: maxi = i

print(f"4. feladat:\n\tA legtöbb döntő ({npd[maxi]} db) {datumok[maxi]}.-án/én volt")

#5. feladat
sum = 0
for s in sportagak: 
  for n in s.napok:
    sum += n

print(f"5. feladat:\n\t{sum} db aranyérmet osztottak ki az olimpián")

#6. feladat
kn = 29
i = 0
while (datumok[i] != kn): i += 1
c = 0
for s in sportagak:
  c += s.napok[i]

print(f"6. feladat:\n\t{kn}-án/én {c} db döntő volt")
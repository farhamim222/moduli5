def onko_alkuluku(luku):
  """Tarkistaa, onko annettu luku alkuluku.

  Args:
    luku: Tarkistettava kokonaisluku.

  Returns:
    True, jos luku on alkuluku, muuten False.
  """

  if luku <= 1:
    return False
  if luku <= 3:
    return True
  if luku % 2 == 0 or luku % 3 == 0:
    return False

  i = 5
  while i * i <= luku:
    if luku % i == 0 or luku % (i + 2) == 0:
      return False
    i += 6

  return True

luku = int(input("Anna kokonaisluku: "))

if onko_alkuluku(luku):
  print(luku, "on alkuluku.")
else:
  print(luku, "ei ole alkuluku.")
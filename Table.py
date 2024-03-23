# tablice

# glavna funkcija
def main():
  plate = input()
  if is_valid(plate):
    print ("OK")
  else:
     print ("ERROR")

# vidi valja li
def is_valid(tabla):
# Ovo mi treba kao brojac
  pozicija = 0
  if len(tabla) < 2 or len(tabla) >6:
    return False
  if tabla[0:2].isalpha() is False:
    return False
  for i in tabla:
    if not (i.isalpha() or i.isdigit()):
      return False
  for i in tabla:
    if i.isdigit():
      if i == "0":
        return False
      elif not (tabla[pozicija:].isdigit()):
        return False
      else:
        return True
    pozicija += 1
  else:
    return True

# Pokreni program
main()
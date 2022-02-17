players = ["Kevin", "Jim", "Rasul", "Ronaldo"]
lucky_numbers = [21, 44, 22, 66, 19, 47]
print(players)
print(players[1])
print(players[1:])      # starts from position 1 and everything after that
print(players[1:3])   # takes elements 1 and 2

players[2] = "Raul"     # changing
print(players[2])

players.extend(lucky_numbers)
print(players)

q = ["Tom", "Jim", "John"]
q.insert(1, "Robert")          # adding adding an element "Robert" on position 1
print(q)
q.remove("John")
print(q)
q.pop()                        # remuves the last element
print(q)

e = ["Barris", "Figo", "Raul", "Alberto", "Dudek"]
e.sort()                       # sort the list alfabetical order
print(e)

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

pl = e.copy()                  # copying values from "e"
print(pl)

rows = raw_input('How many rows do you want? ')
if rows.isdigit():
    rows = int(rows)
else:
    rows = 6

col= raw_input('How many columns do you want? ')

if col.isdigit():
    col = int(col)
else:
    col = 6

for i in range(rows):
    for j in range (col):
        if i % 2 == 0:
            print '*',
    else:
        print '$',
    print

                     

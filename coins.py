# name of student: Shane Boer
# number of student: 99042114
# purpose of program: wisselgeld berekenen
# function of program: waarden herkennen en uitrekenen
# structure of program: variable if, elif, else en while statements

toPay = int(float(input('Amount to pay: '))* 100) # variabele toPay is een getal die met decimale kan werken waar je in kan vullen wat je moet betalen x 100
paid = int(float(input('Paid amount: ')) * 100) # variabele paid is een getal die met decimale kan werken waar je in kan vullen wat er betaald is x 100
change = paid - toPay # variabele bereken paid en toPay en dat is dan de variabele van change
betaald = []

if change > 0: # als change groter is dan 0 voer de code onder de if uit
  coinValue = 500 # variabele coinValue waarde is 500
  
  while change > 0 and coinValue > 0: # zolang change groter is dan 0 en coinValue ook groter is dan 0
    nrCoins = change // coinValue # nrCoins word de gehele waarden van change en coinValue


    if nrCoins > 0: # als nrCoins groter is dan 0
      print('return maximal ', nrCoins, ' coins of ', float(coinValue/100), ' euro!' ) # print de text plus de variabele nrCoins en coinValue gedeeld door 100
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue/100) +  ' euro did you return? ')) # laat de aantal munten zien die ze moeten betalen en geef een input waar ze het aantal in kunnen vullen
      change -= nrCoinsReturned * coinValue # doe change - nrCoinsReturned x coinValue en dat word de nieuwe waarde van de variabele
      betaald.append('je hebt {} munten van {} euro terug gegeven' .format(nrCoinsReturned, coinValue/100))


# comment on code below: als coinValue 500 is maak het dan 300 als het 300 is maak het 200 etc.
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0
    


if change > 0: # als change groter is dan 0 print de text hieronder
  print('Change not returned: ', str(float(change/100)) + ' cents')
else:
  print('done')
  for x in betaald:
    print(x)
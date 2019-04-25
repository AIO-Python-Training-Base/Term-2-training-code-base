with open('sitin.txt') as fileIn:
  dataInList = fileIn.read().splitlines()
  configList = dataInList[0].split(' ')
  r = int(configList[0])
  s = int(configList[1])
  ticketsNum = int(dataInList[1])

  
with open('sitout.txt','w') as fileOut:
  fileOut.write(str(sittingNum) + ' ' + str(standingNum))

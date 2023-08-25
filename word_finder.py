#complexity 7.35 against 3.0
#exec(open("./word_finder.py").read())
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Pattern == Text[i:i+len(Pattern)]:
            count = count + 1
    return count

#Nrighe = input('Num righe:')
#Ncolonne = input('Num colonne:')

#for i in range(int(Nrighe)):
#  print(i)

word_table = open('C:\LavoroOrnella\Studio\Python_test\word_table.txt', 'r')
word_rows = word_table.readlines()

count = 0
word_table = []
for line in word_rows:
    count += 1
    line = line.strip()
    word_table_list = line.split(' ')
    word_table.append(word_table_list)
	
###print(len(word_table))

word = input('Parola da cercare:')
founded = 0
tableIndexes = []
for i in range(len(word)):
   print('***')
   print(word[i])
   for row in range(len(word_table)):
   ###   print(word_table[j])
      indexes = [j for j in range(len(word_table[0])) if word_table[row][j] == word[i]]
      tableIndexes[row] = [indexes]
      #print(indexes)


#path = "";
#appo = 0;
#for h in range(len(tableIndexes)):
 #  for k in range(len(tableIndexes[0])):      
  #    if tableIndexes[h][k] > 0:       
   #      if appo == tableIndexes[h, k]:
    #        path = path + ";(" + h + "," + k + ")";
     #       continue
      #   else:
       #     appo = tableIndexes[h, k];
   
#print(path)
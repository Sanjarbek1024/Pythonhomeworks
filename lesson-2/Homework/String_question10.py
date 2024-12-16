# Write a program that asks the user for a sentence and prints the number of words in it

sentance = str(input("Write a sentance :")) 

words = sentance.split() # bo'sh joy orqali so'zlarni ajratib oldim
words2 = len(words)      # so'zlarni sonini len orqali aniqladim
print(words2)            # Va print qildim
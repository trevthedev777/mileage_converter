print('How many Kilometers did you run/cycle/swim today?')
kms = float(input())
miles = float(kms) / 1.60934
miles = round(miles, 2) #takes take value of miles and rounds it to 2 decimal points
print(f'Congratulations,your {kms} is equal to {miles} miles') 


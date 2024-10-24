# 2)დაწერე პროგრამა, რომელიც შეამოწმებს, არის თუ არა მოცემული ცვლადი float ტიპის.

def check_if_Float(x): # შექმენი ფუნქცია რომ შეამოწმოს თუ არის x float
  if type(x) == type(1.5): 
    return True
  else:
    return False
  
print(check_if_Float(1.5)) # true
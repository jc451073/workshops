__author__ = 'jc451073'
def tax_return(income):
 if income <= 16000:
    return 0
 else:
      return (income - 16000) * 0.3
print(tax_return(100000))
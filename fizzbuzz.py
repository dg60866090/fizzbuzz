
def do_fizzbuzz():
  """
  Do fizzbuzz with for and if 
  While i goes up 1 to 15, 
  print 'fizz' if i is time of 3 
  print 'buzz' if i is times of 5
  print 'fizzbuzz' if i is times of 15
  else, print i (string)
  """


   for i in ragne(1,15+1):
    if i%3==0:
        print('fizz')
    else:
       print ('{}'.format(i))
   return True


if __name__=='__main__':
    do_fizzbuzz()

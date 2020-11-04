#GEORGIOS DIMOPOULOS A.M. 2964
def kl():
    print('+------+')
    print('|')
    print('|')
    print('|')
def kl1():
    print('+------+')
    print('|      O')
    print('|')
    print('|')
def kl2():
    print('+------+')
    print('|      O')
    print('|    --+')
    print('|')
def kl3():
    print('+------+')
    print('|      O')
    print('|    --+--')
    print('|         ')
def kl4():
    print('+------+')
    print('|      O')
    print('|    --+--')
    print('|     / ')
def kl5():
    print('+------+')
    print('|      O')
    print('|    --+--')
    print('|     / \ ' )
def printhanger(tries,maxtries):
    if tries==0:
        kl()
        print('5 προσπάθειες σας μένουν')
    elif tries==1:
        kl1()
        print('4 προσπάθειες σας μένουν')
    elif tries==2:
        kl2()
        print('3 προσπάθειες σας μένουν')
    elif tries==3:
        kl3()
        print('2 προσπάθειες σας μένουν')
    elif tries==4:
        kl4()
        print('1 προσπάθεια σας μένει')
    elif tries==5:
        kl5()
        print('Λυπάμαι χάσατε')
print('*****Καλωσόρισες στην Κρεμάλα!!!*****')
j='p'
while j=='p' or j=='P':
 asd=['ς','ε','ρ','τ','υ','θ','ι','ο','π','α','σ','δ','φ','γ','η','ξ','κ','λ','ζ','χ','ψ','ω','β','ν','μ']
 jkl=[' ','"','' ,'0,''1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','-','=','_','/','+','[',']','{','}','~','`','¨',';',':',"'",',','<','.','>','?']
 k=list()
 p=0
 pp=0
 import random
 po=open('WORDS.txt')
 f=po.readlines()
 counter=-1
 for i in f:
    counter=counter+1
    f[counter]=f[counter][:-1]
 x=input("Αν θες να παίξεις με άλλον παίχτη πληκτρολόγησε g ή G:")
 if x=='G' or x=='g':
  y=input('Πληκτρολόγησε την λέξη χωρίς να κοιτάει ο 2ος παίκτης(η λέξη πρέπει να είναι στα αγγλικά και μπορεί να περιέχει από 3 έως 20 γράμματα):').lower()
  while y not in f:
   print('Αυτή η λέξη δεν υπάρχει στο λεξιλόγιο!') 
   y=input('Πληκτρολόγησε την λέξη χωρίς να κοιτάει ο 2ος παίκτης(η λέξη πρέπει να είναι στα αγγλικά και μπορεί να περιέχει από 3 έως 20 γράμματα):').lower()
  import os
  os.system('clear')        
  m=(len(y))*'-'
  while pp==0:
    printhanger(p,5)
    print(m)
    print('Επιλεγμένα γράμματα:',k)
    z=input('Μάντεψε γράμμα:').lower()
    while len(z)>1 or z in jkl or z in asd:
        print('Μην γίνεσαι σε παρακαλώ τόσο πολύ ηλίθιος!')
        z=input('Μάντεψε γράμμα:').lower()
    for q in k:
        v=q.upper()
        while z.upper()==v:
            print('Αυτό το γράμμα το έχεις ξαναδώσει!')
            z=input('Μάντεψε γράμμα:').lower()
    k.append(z.upper())
    if z in y:
        for i in range(len(y)):
            if z in y[i]:
                l=y[i].upper()
                m=m[:i] + l + m[i+1:]
    if z not in y:
        p=p+1
    if '-' not in m:
        pp=1
        print(m)
        print('Συγχαρητήρια κερδίσατε! βρήκατε την λέξη:',y)
    if p==5:
        pp=1
        printhanger(5,5)
        print('Η λέξη ήταν:',y)
 else:
  z=input("Πληκτρολόγησε r ή R εάν θέλεις μία λέξη τυχαίου μήκους αλλιώς δώσε το μήκος της λέξης που επιθυμείς από 3-20:")
  qw=['r','R','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
  while z not in qw:
   print('Είσαι ηλίθιος κοίτα τι σου ζητάω!')
   z=input("Πληκτρολόγησε r ή R εάν θέλεις μία λέξη τυχαίου μήκους αλλιώς δώσε το μήκος της λέξης που επιθυμείς από 3-20:")
  if z=='r' or z=='R':
   y=random.choice(f)        
   m=(len(y))*'-'
   while pp==0:
    printhanger(p,5)
    print(m)
    print('Επιλεγμένα γράμματα:',k)
    z=input('Μάντεψε γράμμα:').lower()
    while len(z)>1 or z in jkl or z in asd:
        print('Μην γίνεσαι σε παρακαλώ τόσο πολύ ηλίθιος!')
        z=input('Μάντεψε γράμμα:').lower()
    for q in k:
        v=q.upper()
        while z.upper()==v:
            print('Αυτό το γράμμα το έχεις ξαναδώσει!')
            z=input('Μάντεψε γράμμα:').lower()
    k.append(z.upper())
    if z in y:
        for i in range(len(y)):
            if z in y[i]:
                l=y[i].upper()
                m=m[:i] + l + m[i+1:]
    if z not in y:
        p=p+1
    if '-' not in m:
        pp=1
        print(m)
        print('Συγχαρητήρια κερδίσατε! βρήκατε την λέξη:',y)
    if p==5:
        pp=1
        printhanger(5,5)
        print('Η λέξη ήταν:',y)
  else:
   y=random.choice(f)
   while len(y) != eval(z):
    y=random.choice(f)
   m=(len(y))*'-'
   while pp==0:
    printhanger(p,5)
    print(m)
    print('Επιλεγμένα γράμματα:',k)
    z=input('Μάντεψε γράμμα:').lower()
    while len(z)>1 or z in jkl or z in asd:
        print('Μην γίνεσαι σε παρακαλώ τόσο πολύ ηλίθιος!')
        z=input('Μάντεψε γράμμα:').lower()
    for q in k:
        v=q.upper()
        while z.upper()==v:
            print('Αυτό το γράμμα το έχεις ξαναδώσει!')
            z=input('Μάντεψε γράμμα:').lower()
    k.append(z.upper())
    if z in y:
        for i in range(len(y)):
            if z in y[i]:
                l=y[i].upper()
                m=m[:i] + l + m[i+1:]
    if z not in y:
        p=p+1
    if '-' not in m:
        pp=1
        print(m)
        print('Συγχαρητήρια κερδίσατε! βρήκατε την λέξη:',y)
    if p==5:
        pp=1
        printhanger(5,5)
        print('Η λέξη ήταν:',y)
 j=input("Αν θέλεις να ξαναπαίξεις πληκτρολόγησε P ή p:")
questions = [
  [
    "Which language was used to create Facebook?",
    "Python","Java",
    "C++","PHP", 4
  ],
  [
  "Who developed Python Programming Language?", "Wick van Rossum", "Rasmus Lerdorf",
    "Guido van Rossum","Niene Stom",3
  ],
  [
    "Which type of Programming does Python support?", " object-oriented programming",
    "structured programming",
    "functional programming","all of the mentioned",4
  ],
  [
    "Is Python case sensitive when dealing with identifiers?" ,"no", "yes","machine dependent",
    "none of the mentioned",2
  ],
  [
    "Which of the following is the correct extension of the Python file?",
    ".python",
    ".pl",
    ".py",
    ".p",
    3
  ],
  [
    "Which of the following character is used to give single-line comments in Python?",
    "//",
    "#",
    "!",
    "/*",
    2
  ],
  [
    "Python supports the creation of anonymous functions at runtime, using a construct called ?",
    "pi",
    "anonymous",
    "lambda",
    "none of the mentioned",
    3
  ],
  [
    "Which of the following is not a core data type in Python programming?","Tuples",
    "Lists",
    "Class","Dictionary",3
  ],
  [
    "Which one of the following is not a keyword in Python language?","pass","eval",
    "assert","nonlocal",2
  ],
  [
    "What will be the output of the following Python expression if x=56.236?",
    "56.236",
    "56.23",
    "56.0000",
    "56.24",
    4
  ]
]

levels = [1000,2000,3000,30000,60000,120000,240000,360000,6400000,100000000]
money =0

print("Welcome to Kaun Banega Crorepati Game !")
for i in range(0, len(questions)):
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"Your Question is {questions[i][0]}")  
  print(f"a. {question[1]}")
  print(f"b. {question[2]}")
  print(f"c. {question[3]}")
  print(f"d. {question[4]}")
  reply= int(input("Enter your answer (1-4):"))
  if (reply == question[-1]):
    print(f"Correct answer, you have won Rs.{levels[i]}")
    if(i== 1):
      money== 1000
    elif(i== 2):
      money== 2000
    elif(i== 3):
      money== 3000
    elif(i== 4):
      money== 30000
    elif(i== 5):
      money== 60000
    elif(i== 6):
      money== 120000
    elif(i== 7):
      money== 240000
    elif(i== 8):
      money== 360000
    elif(i== 9):
     money== 6400000
    elif(i== 10):
     money== 10000000
     print(f"Congratulations You are a Crorepati Now !\nYou will take home: Rs 10000000 ")

  else:
    print("Wrong answer!")
    print(f"You will take home: {money}")
    break

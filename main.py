import json
import random

with open("flashcards.json", "r") as f:
  flashcards = json.load(f)
list_of_keys = list(flashcards.keys())

print("Welcome to the Unit Circle Flashcards! In this excercise, the computer output a triganometric function with a radian value inside. Your task is to answer the value of the prompt. \n\n**Note: if your answer has a √ (square root) in it, then the format of your response should be root2/2 (if the answer you want is √2/2. Once again, the format is root_/_. \n\nBest of luck to you and math away!")

def flashcards_game():
  long_list = list_of_keys
  short_list = []
  # read stats json file
  # loop through dictionary (see slides for how to loop through dictionaries)
  # each question, check if you've gotten it right 3 times in a row recently.

  # value = stats[key]
  # for value in stats:
  
  #if not, add it to short_list
  #   if value == "true, true, true":
  #     flashcards.append()
  
  #build short_list so it's all the ones we haven't gotten right 3 times in a row
  big_list = long_list + short_list*2
  random.shuffle(big_list)
  for key in big_list:
    value = flashcards[key]
    user_response = input(f"What is the value of {key} ?")
    if user_response == value:
      correct = True
      print("You're correct!")
    elif user_response != value:
      correct = False
      print("Your answer is not correct. I will note this so we can drill this moving forward.")

    with open('stats.json', 'r') as f:
      stats = json.load(f)
      stats[key].append(correct)

    with open('stats.json', 'w') as f:
      json.dump(stats,f)

  flashcards_game()

# #test trial for randomness
# for correct in stats:
#   if 

flashcards_game()
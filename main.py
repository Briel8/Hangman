import random, time, json

class Hangman:
    def __init__(self):
        self.eligible_words = []
        self.result = []
        self.wrong = []
        self.generate_rand()
        self.saved_progress = False
    def generate_rand(self):
        """Continue the game from last memory.
        Or Generates the word to be guessed in the game.
        """
        with open("progress.json", 'r') as progress_file:
            data = json.load(progress_file)
            if data["master_word"]:
                self.master_word = data["master_word"]
                self.result = data["result"]
                self.wrong = data["wrong"]
                self.life = data["life"]
                print(f"from json: master_word is {self.master_word} ")
            else:
                file_obj = open("google-10000-english-no-swears.txt")
                english_words = file_obj.read().split()
                for word in english_words:
                    if len(word) >= 5 and len(word) <= 12:
                        self.eligible_words.append(word)

                random_word = random.choice(self.eligible_words)
                self.master_word = random_word
                self.make_result()
                self.life = len(self.master_word)
    
    def make_result(self):
        for i in range(len(self.master_word)):
            self.result.append("_")

    def guess_char(self):
        self.guess = input("Please enter a guess: ").lower()
    
    def check_guess(self):
        if self.guess in self.master_word:
            for i in range(len(self.master_word)):
                if self.master_word[i] == self.guess:
                    self.result[i] = self.guess
        elif self.guess == 'bb':
            self.save_progress(self.master_word, self.result, self.wrong, self.life)
            self.saved_progress = True
        else:
            self.wrong.append(self.guess)
            self.life -= 1

    def display(self):
        print(f"Progress: {self.result}")
        print(f"Missed: {self.wrong}")
        print(f"Chances left: {self.life}")
        print("---HangMan---")
        print()

    def won(self):
        for i in range(len(self.master_word)):
            if self.master_word[i] != self.result[i]:
                return False
        return True
    
    def congratulations(self):
        print("Congratulations! You have won")
        print(self.result)

    def save_progress(self, word, result, wrong, life):
        """Returns True after saving."""
        data = {"master_word":word, "result":result, "wrong": wrong, "life":life}

        with open("progress.json", 'w') as progress_file:
            json.dump(data, progress_file)
    
    def clear_progress(self):
        with open("progress.json", 'w') as progres_file:
            data = {"master_word": None, "result":None, "wrong":None, "life":None}
            json.dump(data, progres_file)


    def play(self):
        print("WELCOME TO THE GAME OF HANGMAN!")
        print(self.master_word)
        self.display()
        time.sleep(2)
        while(self.life > 0):
            self.guess_char()
            self.check_guess()
            # if player want to save file and exit
            if self.saved_progress:
                print()
                print("---HANGMAN---")
                print("Saved progress.")
                print()
                break
            if self.won():
                self.congratulations()
                self.clear_progress()

                break
            self.display()

        # At this point the player lost
        if self.won() != True and self.saved_progress != True:
            print("You Loose!")
            self.clear_progress()

    def test(self):
        with open("progress.json", 'r') as test_file:
            data = json.load(test_file)
            print(data)

game = Hangman()
game.play()
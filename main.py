import random, time

class Hangman:
    def __init__(self):
        self.eligible_words = []
        self.master_word = self.generate_rand()
        self.result = []
        self.wrong = []
        self.life = len(self.master_word)
        self.make_result()

    def generate_rand(self):
        file_obj = open("google-10000-english-no-swears.txt")
        english_words = file_obj.read().split()
        for word in english_words:
            if len(word) >= 5 and len(word) <= 12:
                self.eligible_words.append(word)

        random_word = random.choice(self.eligible_words)
        return random_word
    
    def make_result(self):
        for i in range(len(self.master_word)):
            self.result.append("_")

    def guess_char(self):
        self.guess = input("Please enter a guess: ")
        if len(self.guess) != 1:
            print("please enter a valid guess!")
    
    def check(self):
        if self.guess in self.master_word:
            for i in range(len(self.master_word)):
                if self.master_word[i] == self.guess:
                    self.result[i] = self.guess
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


    def play(self):
        print("WELCOME TO THE GAME OF HANGMAN!")
        print(self.master_word)
        time.sleep(2)
        while(self.life > 0):
            self.display()
            self.guess_char()
            self.check()
            if self.won():
                self.congratulations()
                break
            self.display()
        if self.won() != True:
            print("You Loose!")

game = Hangman()
game.play()
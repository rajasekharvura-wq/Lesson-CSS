class Cricket:
    def __init__(self, player, score):
        self._player = player   # private attribute
        self._score = score     # private attribute

    def info(self):     # same method name as Football
        print(f"Cricket Player: {self._player}, Score: {self._score}")

    def play(self):     # same method name, different output
        print(f"{self._player} hits a six!")
        
    def get_score(self):    # getter - read private data
        return self._score
    
    def set_score(self, new_score): # setter - update private data safely
        if new_score >= 0:
            self._score = new_score
            print(f"Score updated to {self._score}")
        else:
            print("Score cannot be negative.")

            
class Football:
    def __init__(self, player, score):
        self._player = player
        self._score = score

    def info(self):             #same name, different output
        print(f"Football - Player:{self._player}, Score: {self._score}")

    def play(self):             # same name, different behavior
        print(f"{self._player} scores a goal!")

    def get_score(self):
        return self._score

    def set_score(self, new_score):
        if new_score >= 0:
            self._score = new_score
            print(f"Score updated to {self._score}")
        else:
            print("Score cannot be negative.")

name = input("Please enter your name: ")
input_score = int(input("Please enter your score: "))

# Create objects
cricket = Cricket(name,input_score)
football = Football(name,input_score)

# Polymorphism - same method, different behavior
print("=== Sports Scoreboard ===\n")
for sport in (cricket, football):
    sport.info() 
    sport.play()
    print()

# Encapsulation - direct change does NOT work
print("--- Direct change attempt ---")
cricket._score = 999
print(f"get_score() still shows:{cricket.get_score()}")

# Setter - the only safe way to update
print("\n--- Updating scores ---")
cricket.set_score(100)
football.set_score(3)
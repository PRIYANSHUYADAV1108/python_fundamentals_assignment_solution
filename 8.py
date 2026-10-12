class player:
    player_count = 0
    def __init__(self,name,level):
        self.name = name
        self.level = level
        player.player_count +=1
    def get_info(self):
        print(f"the player name = {self.name} and level = {self.level}")

    @classmethod
    def get_count(cls):
        print(f"The Plaayer Count = {cls.player_count}")

p1 = player("Priya Kumari",99)
p2 = player("Priyanshu Kumar",98)

player.get_count()

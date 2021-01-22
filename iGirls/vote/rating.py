class Elo:
    def __init__(self, base_rating=1000):
        self.base_rating = base_rating
        self.players = []

    def __getPlayerList(self):
        return self.players

    def getPlayer(self, name):
        for player in self.players:
            if player.name == name:
                return player
        return None
    
    def removePlayer(self, name):
        self.__getPlayerList().remove(self.getPlayer(name))

    def addPlayer(self, name, rating=None):
        if rating == None:
            rating = self.base_rating

        self.players.append(_Player(name=name,rating=rating))

    def recordMatch(self, name1, name2, winner=None, draw=False):
        player1 = self.getPlayer(name1)
        player2 = self.getPlayer(name2)

        expected1 = player1.compareRating(player2)
        expected2 = player2.compareRating(player1)
        
        k = len(self.__getPlayerList()) * 42

        rating1 = player1.rating
        rating2 = player2.rating

        if draw:
            score1 = 0.5
            score2 = 0.5
        elif winner == name1:
            score1 = 1.0
            score2 = 0.0
        elif winner == name2:
            score1 = 0.0
            score2 = 1.0
        else:
            raise InputError('One of the names must be the winner or draw must be True')

        newRating1 = rating1 + k * (score1 - expected1)
        newRating2 = rating2 + k * (score2 - expected2)

        if newRating1 < 0:
            newRating1 = 0
            newRating2 = rating2 - rating1

        elif newRating2 < 0:
            newRating2 = 0
            newRating1 = rating1 - rating2

        player1.rating = newRating1
        player2.rating = newRating2

    def getPlayerRating(self, name):
        player = self.getPlayer(name)
        return int(player.rating)


class _Player:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def compareRating(self, opponent):
        return ( 1+10**( ( opponent.rating-self.rating )/400.0 ) ) ** -1

if __name__ == "__main__":
    i = Elo()
    user1 = "user1"
    user2 = "user2"
    i.addPlayer(user1, rating=664)
    i.addPlayer(user2, rating=580)
    
    print(i.getPlayerRating(user1), i.getPlayerRating(user2))
    i.recordMatch(user1,user2,winner=user1)
    print(i.getPlayerRating(user1), i.getPlayerRating(user2))

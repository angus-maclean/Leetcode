# Last updated: 02/07/2026, 20:20:11
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        # add hashmap and hashset
        players_set = set()
        losers_map = {}

        # add winners list and losers list, and final list
        winners = []
        losers = [] 
        result = []

        
        for winner, loser in matches:
            players_set.add(winner)
            players_set.add(loser)
            # if loser not in hashmap add them 
            if loser not in losers_map:
                losers_map[loser] = 1
            else:
                # if in hashmap add to loser count
                losers_map[loser] += 1
        # for all the players                        
        for player in players_set:
            # if the player is in the loser set aka a winner
            if player not in losers_map.keys():
                # add them to the winners
                winners.append(player)
            # if the loser has exactly 1 loss
            elif losers_map[player] == 1:
                losers.append(player)

        result.append(sorted(winners))
        result.append(sorted(losers))

        return result


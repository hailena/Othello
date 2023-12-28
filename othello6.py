
# -*- coding: utf-8 -*-
import sys
def get_coords(index): #returns row, col
    return index//8, index % 8
def possibleMoves(board, token):
    #change = [] #list of possible moves that I return at the end
    changed = set() #this set is to make sure I don't repeat indices
    oppChanged = set()
    opponent = ""
    myTokens = 0
    oppTokens = 0
    spaceTokens = 0
    if token == "x": opponent = "o"
    else: opponent = "x"
    for index in range(64):
       if board[index] == token: #if it's my token
            myTokens += 1
            row, col = get_coords(index) #i get the row and col to make it easier
            if col < 6: #goes right
                start = index + 1 
                end = start
                boo = False #this makes sure that it's actually an opponent between the tokens
                temp = board[start] 
                while temp == opponent and end % 8 < 7:
                    boo = True
                    end += 1
                    temp = board[end]
                if temp == "." and boo and end not in changed:
                    changed.add(end)
            if col > 1: #goes right
                start = index - 1
                end = start
                temp = board[start]
                boo = False
                while temp == opponent and end % 8 > 0:
                    end -= 1
                    boo = True
                    temp = board[end]
                if temp == "." and boo and end not in changed:
                    changed.add(end)
            if row > 1: #goes up
                start = index - 8
                end = start
                temp = board[start]
                boo = False
                while temp == opponent and end // 8 > 0:
                    end -= 8
                    boo = True
                    temp = board[end]
                if temp == "." and boo and end not in changed:
                    changed.add(end)
            if row < 6: #goes down
                start = index + 8
                end = start
                boo = False
                temp = board[start]
                while temp == opponent and end // 8 < 7:
                    end += 8
                    temp = board[end]
                    boo = True
                if temp == "." and boo and end not in changed:
                    changed.add(end)
            if row < 6 and col < 6: #bottom right
                start = index + 9
                end = start
                boo = False
                temp = board[start]
                while temp == opponent and end // 8 < 7 and end % 8 < 7:
                    end += 9
                    boo = True
                    temp = board[end]
                if temp == "." and boo and end not in changed:
                    changed.add(end)
            if row > 1 and col > 1: #top left
                start = index - 9
                end = start
                boo = False
                temp = board[start]
                while temp == opponent and end // 8 >0 and end % 8 >0:
                    end -= 9
                    boo = True
                    temp = board[end]
                if temp == "." and boo and end not in changed:
                    changed.add(end)
            if row > 1 and col < 6:#top right
                start = index - 7
                end = start
                boo = False
                temp = board[start]
                while temp == opponent and end // 8 >0 and end % 8 <7:
                    end -= 7
                    boo = True
                    temp = board[end]
                if temp == "." and boo and end not in changed:
                    changed.add(end)
            if row < 6 and col >1: #bottom right
                start = index + 7
                end = start
                boo = False
                temp = board[start]
                while temp == opponent and end // 8 < 7 and end % 8 >0:
                    end += 7
                    boo = True
                    temp = board[end]
                if temp == "." and boo and end not in changed:
                    changed.add(end)
       elif board[index] == opponent: #if it's my token
            oppTokens += 1
            row, col = get_coords(index) #i get the row and col to make it easier
            if col < 6: #goes right
                start = index + 1 
                end = start
                boo = False #this makes sure that it's actually an opponent between the tokens
                temp = board[start] 
                while temp == token and end % 8 < 7:
                    boo = True
                    end += 1
                    temp = board[end]
                if temp == "." and boo and end not in changed:
                    oppChanged.add(end)
            if col > 1: #goes right
                start = index - 1
                end = start
                temp = board[start]
                boo = False
                while temp == token and end % 8 > 0:
                    end -= 1
                    boo = True
                    temp = board[end]
                if temp == "." and boo and end not in changed:
                    #change.append(end)
                    oppChanged.add(end)
            if row > 1: #goes up
                start = index - 8
                end = start
                temp = board[start]
                boo = False
                while temp == token and end // 8 > 0:
                    end -= 8
                    boo = True
                    temp = board[end]
                if temp == "." and boo and end not in changed:
                    #change.append(end)
                    oppChanged.add(end)
            if row < 6: #goes down
                start = index + 8
                end = start
                boo = False
                temp = board[start]
                while temp == token and end // 8 < 7:
                    end += 8
                    temp = board[end]
                    boo = True
                if temp == "." and boo and end not in changed:
                    #change.append(end)
                    oppChanged.add(end)
            if row < 6 and col < 6: #bottom right
                start = index + 9
                end = start
                boo = False
                temp = board[start]
                while temp == token and end // 8 < 7 and end % 8 < 7:
                    end += 9
                    boo = True
                    temp = board[end]
                if temp == "." and boo and end not in changed:
                    #change.append(end)
                    oppChanged.add(end)
            if row > 1 and col > 1: #top left
                start = index - 9
                end = start
                boo = False
                temp = board[start]
                while temp == token and end // 8 >0 and end % 8 >0:
                    end -= 9
                    boo = True
                    temp = board[end]
                if temp == "." and boo and end not in changed:
                    #change.append(end)
                    oppChanged.add(end)
            if row > 1 and col < 6:#top right
                start = index - 7
                end = start
                boo = False
                temp = board[start]
                while temp == token and end // 8 >0 and end % 8 <7:
                    end -= 7
                    boo = True
                    temp = board[end]
                if temp == "." and boo and end not in changed:
                    #change.append(end)
                    oppChanged.add(end)
            if row < 6 and col >1: #bottom right
                start = index + 7
                end = start
                boo = False
                temp = board[start]
                while temp == token and end // 8 < 7 and end % 8 >0:
                    end += 7
                    boo = True
                    temp = board[end]
                if temp == "." and boo and end not in changed:
                    #change.append(end)
                    oppChanged.add(end)            
       else: spaceTokens += 1
    #change.sort()
    return changed, oppChanged, myTokens, oppTokens, spaceTokens
                
def move(board, token, index):
    change = [index]
    opponent = ""
    if token == "x": opponent = "o"
    else: opponent = "x"
    row, col = get_coords(index)
    if col < 6: #goes right
        start = index + 1
        end = start
        temp = board[start]
        while temp == opponent and end % 8 < 7:
            end += 1
            temp = board[end]
        if temp == token:
            change += [x for x in range(start, end)]
    if col > 1: #goes right
        start = index - 1
        end = start
        temp = board[start]
        while temp == opponent and end % 8 > 0:
            end -= 1
            temp = board[end]
        if temp == token:
            change += [x for x in range(end+1, start+1)]
    if row > 1: #goes up
        start = index - 8
        end = start
        temp = board[start]
        while temp == opponent and end // 8 > 0:
            end -= 8
            temp = board[end]
        if temp == token:
            change += [x for x in range(end+8, start+8, 8)]
    if row < 6: #goes down
        start = index + 8
        end = start
        temp = board[start]
        while temp == opponent and end // 8 < 7:
            end += 8
            temp = board[end]
        if temp == token:
            change += [x for x in range(start, end, 8)]
    if row < 6 and col < 6: #bottom right
        start = index + 9
        end = start
        temp = board[start]
        while temp == opponent and end // 8 < 7 and end % 8 < 7:
            end += 9
            temp = board[end]
        if temp == token:
            change += [x for x in range(start, end, 9)]
    if row > 1 and col > 1: #top left
        start = index - 9
        end = start
        temp = board[start]
        while temp == opponent and end // 8 >0 and end % 8 >0:
            end -= 9
            temp = board[end]
        if temp == token:
            change += [x for x in range(end+9, start+9,  9)]
    if row > 1 and col < 6:#top right
        start = index - 7
        end = start
        temp = board[start]
        while temp == opponent and end // 8 >0 and end % 8 <7:
            end -= 7
            temp = board[end]
        if temp == token:
            change += [x for x in range(end+7, start+7,  7)]
    if row < 6 and col >1: #bottom right
        start = index + 7
        end = start
        temp = board[start]
        while temp == opponent and end // 8 < 7 and end % 8 >0:
            end += 7
            temp = board[end]
        if temp == token:
            change += [x for x in range(start, end, 7)]
    for x in change:
        board = board[:x] + token + board[x+1:]
    return board
def print_puzzle(board):
    for x in range(0, 64, 8):
        temp = " ".join(board[x:x+8]) 
        temp2 = ""
        for k in range(x, x+8):
            temp2 += str(k) + " "
        print(temp + "\t" +temp2)


def max_step(board, alpha, beta, max_depth): #black, more pos values
    results = []
    xChildren, oChildren, xTokens, oTokens, emptySpace = possibleMoves(board, "x")
    numMovesX = len(xChildren) #num of poss moves
    numMovesO = len(oChildren)
    if numMovesX == 0:
        if numMovesO == 0:
            return game_over(xTokens,  oTokens)
        else: 0
    elif max_depth == 0: 
        return game_score(board, numMovesX, numMovesO, xTokens, oTokens, emptySpace)
    else:
        for index in xChildren:
            next_board = move(board, "x", index)
            score = min_step(next_board, alpha, beta, max_depth-1)
#PRUNING
            if score > alpha: alpha = score
            
            if alpha >= beta: 
                #print(alpha, beta)
                return score
            results.append(score)
    #print(results)
    return max(results)

def game_score(board, numMovesBlack, numMovesWhite, numTokBlack, numTokWhite, numTokSpace):
    score = 0
    token_score = 1
#CHANGES - for the first half of the game, having less pieces 
#is better, so I subtract for every black piece and add for 
#every whitte piece. However, I flip it for the second half 
#because that's when we want to start gathering more pieces.
#If the number of spaces in the board is more than 28, I 
#consider that the first half of the game.
    #if numTokSpace > 46:
        #score -= (numTokBlack * token_score)
        #score += (numTokWhite * token_score)
    corner = 100
    
    around_corner = 10
    score += (numMovesBlack-numMovesWhite) #each move option gets 5 points
    upperLeft = board[0]
    space = "."
    if upperLeft != space: #if ttakes ttop left, good tthing
        if upperLeft == "x": score += corner
        else: score -= corner
    upperRight = board[7]
    if upperRight != space: #if ttakes ttop left, good tthing
        if upperRight == "x": score += corner
        else: score -= corner
    bottomLeft = board[56]
    if bottomLeft != space: #if ttakes ttop left, good tthing
        if bottomLeft == "x": score += corner
        else: score -= corner
    bottomRight = board[63]
    if bottomRight != space: #if ttakes ttop left, good tthing
        if bottomRight == "x": score += corner
        else: score -= corner
    temp = board[1]
    if temp != space: #if ttakes ttop left, good tthing
        if temp == "x": 
            if upperLeft != "x": 
                score -= around_corner
            else: score += around_corner
        else: 
            if upperLeft != "o": 
                score += around_corner
            else: score -= around_corner
    temp = board[6]
    if temp != space: #if ttakes ttop left, good tthing
        if temp == "x": 
            if upperRight != "x": 
                score -= around_corner
            else: score += around_corner
        else: 
            if upperRight != "o": 
                score += around_corner
            else: score -= around_corner
    temp = board[8]
    if temp != space: #if ttakes ttop left, good tthing
        if temp == "x": 
            if upperLeft != "x": 
                score -= around_corner
            else: score += around_corner
        else: 
            if upperLeft != "o": 
                score += around_corner
            else: score -= around_corner
    temp = board[9]
    if temp != space: #if ttakes ttop left, good tthing
        if temp == "x": 
            if upperLeft != "x": 
                score -= around_corner
            else: score += around_corner
        else: 
            if upperLeft != "o": 
                score += around_corner
            else: score -= around_corner
    temp = board[14]
    if temp != space: #if ttakes ttop left, good tthing
        if temp == "x": 
            if upperRight != "x": 
                score -= around_corner
            else: score += around_corner
        else: 
            if upperRight != "o": 
                score += around_corner
            else: score -= around_corner
    temp = board[15]
    if temp != space: #if ttakes ttop left, good tthing
        if temp == "x": 
            if upperRight != "x": 
                score -= around_corner
            else: score += around_corner
        else: 
            if upperRight != "o": 
                score += around_corner
            else: score -= around_corner
    temp = board[62]
    if temp != space: #if ttakes ttop left, good tthing
        if temp == "x": 
            if bottomRight != "x": 
                score -= around_corner
            else: score += around_corner
        else: 
            if bottomRight != "o": 
                score += around_corner
            else: score -= around_corner
    temp = board[57]
    if temp != space: #if ttakes ttop left, good tthing
        if temp == "x": 
            if bottomLeft != "x": 
                score -= around_corner
            else: score += around_corner
        else: 
            if bottomLeft != "o": 
                score += around_corner
            else: score -= around_corner
    temp = board[55]
    if temp != space: #if ttakes ttop left, good tthing
        if temp == "x": 
            if bottomRight != "x": 
                score -= around_corner
            else: score += around_corner
        else: 
            if bottomRight != "o": 
                score += around_corner
            else: score -= around_corner
    temp = board[54]
    if temp != space: #if ttakes ttop left, good tthing
        if temp == "x": 
            if bottomRight != "x": 
                score -= around_corner
            else: score += around_corner
        else: 
            if bottomRight != "o": 
                score += around_corner
            else: score -= around_corner
    temp = board[49]
    if temp != space:
        if temp == "x": 
            if bottomLeft != "x": 
                score -= around_corner
            else: score += around_corner
        else: 
            if bottomLeft != "o": 
                score += around_corner  
            else: score -= around_corner
    temp = board[48]
    if temp != space: #if ttakes ttop left, good tthing
        if temp == "x": 
            if bottomLeft != "x": 
                score -= around_corner
            else: score += around_corner
        else: 
            if bottomLeft != "o": 
                score += around_corner
            else: score -= around_corner
    return score
def game_over(numX, numO): #scoring when no moves left
    if numX > numO:
        return 100000 + (numX * 2)
    else: return -100000 - (numO * 2)
def min_step(board, alpha, beta, max_depth): #white, more neg values
    results = []
    oChildren, xChildren, oTokens, xTokens, emptySpace = possibleMoves(board, "o")
    numMovesX = len(xChildren) #num of poss moves
    numMovesO = len(oChildren)
    if numMovesO == 0:
        if numMovesX == 0:
            return game_over(xTokens,  oTokens)
        else: 0
    elif max_depth == 0: 
        return game_score(board, numMovesX, numMovesO, xTokens, oTokens, emptySpace)
    else:
        for index in oChildren:
            next_board = move(board, "o", index)
            score = max_step(next_board, alpha, beta, max_depth-1)
#PRUNING
            if score < beta: beta = score
            if beta <= alpha: return score
            results.append(score)
    return min(results)




def find_next_move(board, player, depth):
    #alpha = -10000
    #beta = 10000
    #if player == "x": 
        #score, board, index = max_step(board, alpha, beta, depth)
        #return index
    #else:
        #score, board, index = min_step(board,alpha, beta, depth)
        #return index
    alpha = -10000
    beta = 10000
    final_index = 0
    final_score = 0
    if player == "x": 
        xChildren, oChildren, xTokens, oTokens, emptySpace = possibleMoves(board, "x")
        final_score = -1000000
        for index in xChildren:
            score = max_step(board, alpha, beta, depth)
            #if score != None:
            if score > final_score:
                final_score = score
                final_index = index
    else:
        oChildren, xChildren, oTokens, xTokens, emptySpace = possibleMoves(board, "o")
        final_score = 1000000
        for index in oChildren:
            score = min_step(board, alpha, beta, depth)
            #if score != None:
            if score < final_score:
                final_score = score
                final_index = index
    return final_index

#board = sys.argv[1]

#player = sys.argv[2]
board = "..x.o....xxxo.......x...oooxooo.ooxxxoo.o.oxo.o................."
player = 'x'

depth = 1

for count in range(15):  # 15 is arbitrary; a depth that your code won't reach, but infinite loops crash the grader

   print(find_next_move(board, player, depth))

   depth += 1

'''
class Strategy():

   logging = True  # Optional

   def best_strategy(self, board, player, best_move, still_running):

       depth = 1

       for count in range(15):  # 15 is arbitrary; a depth that your code won't reach, but infinite loops crash the grader

           best_move.value = find_next_move(board, player, depth)

           depth += 1
'''
'''
puzzle = ""
for x in range(64):
    if x == 25 or x == 33:
        puzzle += "x"
    elif x == 26 or x == 32:
        puzzle += "o"
    else:
        puzzle += "."
puzzle = "...........o.......ox......xx....oxoxo...xx.x..................."
#print(possibleMoves(puzzle, "x"))
depth = 1
for count in range(15):
    print(find_next_move(puzzle, "x", depth))
    depth += 1
'''
'''

puzzle = "...........o.......ox......xx....oxoxo...xx.x..................."
puzzle = move(puzzle, "o", 29)
puzzle = move(puzzle, "o", 52)
print_puzzle(puzzle)
print()
print_puzzle(move(puzzle, "o", 18))
movesNext = ""
'''
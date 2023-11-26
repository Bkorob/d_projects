class TicTacToe():
    def __init__(self, level='easy'):
        self.field = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        if level == 'easy':
            self.level = Easy()
        # else:
        #     self.level = Normal()
    def get_win(self):
        self.win_comb = [
            self.field[0],
            self.field[1],
            self.field[2],
                [self.field[0][0],
                self.field[1][0],
                self.field[2][0]],
                    [
                self.field[0][1],
                self.field[1][1],
                self.field[2][1]],
                    [
                self.field[0][2],
                self.field[1][2],
                self.field[2][2]],
                    [
                self.field[0][0],
                self.field[1][1],
                self.field[2][2]],
                    [
                self.field[2][0],
                self.field[1][1],
                self.field[0][2]]]
        
        for x in self.win_comb:
            if x[0] == x[1] == x[2]:
                return True
        return False

    def go(self, *args):
        if not args:
            self.level.step(self.field)
        else:
            point = args
            self.field[point[0]][point[1]] = 'o'
        return self.get_win()

        
# END
class Easy():
    # BEGIN (write your solution here)
    def step(self, data):
        field = data
        for i in range(len(field) - 1):
            for x in range(len(field[i]) - 1):
                if field[i][x] == 'o':
                    break
                if field[i][x] is None:
                    field[i][x] = 'x'
                    return
                


def test_easy_game2():
    game = TicTacToe()
    game.go(1, 1)
    game.go()
    game.go(1, 2)
    print(game.field)
    game.go()
    assert not game.go(2, 2)
    print(game.field)
    is_winner = game.go()
    print(game.field)
    assert is_winner

print(test_easy_game2())    
# p = TicTacToe()
# p.go(1,1)
# p.go()
# p.go(0,0)
# p.go()
# print(p.go(2,2))
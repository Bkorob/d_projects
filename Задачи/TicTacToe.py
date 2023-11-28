from pprint import pprint


class TicTacToe():
    def __init__(self, level='easy'):
        self.field = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
                
        if level == 'easy':
            self.level = Easy()
        else:
            self.level = Normal()

    def human_step(self, *args):
        point = args
        if self.field[point[0]][point[1]] is None:
            self.field[point[0]][point[1]] = 'o'
        return self.field
            
    def go(self, *args):
        if not args:
            self.level.step(self.field)
        else:
            self.human_step(*args)
        return self.winner_check()

    def winner_check(self):
        win_comb = [
            self.field[0],
            self.field[1],
            self.field[2],
            [
                self.field[0][0],
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
        print(self.field)
        return any(x[0] == x[1] == x[2] for x in win_comb if all(x))


class Easy():
    def step(self, data):
        field = data
        for i in range(len(field)):
            for x in range(len(field[i])):
                if field[i][x] == 'o':
                    break
                if field[i][x] is None:
                    field[i][x] = 'x'
                    return field
                

class Normal():
    def step(self, data):
        field = data
        for i in range(len(field) - 1, -1, -1):
            for x in range(len(field[i])):
                if field[i][x] == 'o':
                    break
                if field[i][x] is None:
                    field[i][x] = 'x'
                    return field

              
def test_normal_game2():
    game = TicTacToe('normal')
    game.go()
    game.go(2, 1)
    game.go()
    game.go(1, 0)
    assert not game.go()
    assert not game.go(1, 2)
    is_winner = game.go()
    assert is_winner

print(test_normal_game2())
# game = TicTacToe()
# game.go(1, 1)
# game.go()
# game.go(1, 2)
# a = not game.go()


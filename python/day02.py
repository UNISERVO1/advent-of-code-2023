from re import split

def part1(file_name):
   max_ball_totals = { 'red': 12, 'green': 13, 'blue': 14 }
   total = 0
   with open(file_name) as f:
      for line in f:
         valid_game = True
         game, balls = line.split(": ")
         ball_totals = [ball.split(", ") for ball in balls.split("; ")]
         for ball_total in ball_totals:
            for ball_value in ball_total:
               count, ball = ball_value.split()
               valid_game = valid_game and max_ball_totals[ball] >= int(count)
         if valid_game:
            total += int(game.split()[-1])
   return total


def part2(file_name):
   total = 0
   with open(file_name) as f:
      for line in f:
         game, balls = line.split(": ")
         ball_totals = [ball.split(", ") for ball in balls.split("; ")]
         min_ball_totals = { 'red': 0, 'green': 0, 'blue': 0 }
         for ball_total in ball_totals:
            for ball_value in ball_total:
               count, ball = ball_value.split()
               min_ball_totals[ball] = max(min_ball_totals[ball], int(count))
         total += min_ball_totals['red'] * min_ball_totals['green'] * min_ball_totals['blue']
   return total

if __name__ == "__main__":
   print(part1("src/Day02.txt"))
   print(part2("src/Day02.txt"))
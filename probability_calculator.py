import random
import copy

class Hat:
  def __init__(self, **keyargs):
    self.contents = []
    for a in keyargs:
      for b in range(keyargs[a]):
        self.contents.append(a)
    print(self.contents)

  def draw(self, balls_num):
    if balls_num >= len(self.contents): return self.contents
    result = []
    for _ in range(balls_num):
      idx = random.randint(0, len(self.contents) - 1)
      result.append(self.contents.pop(idx))
    return result


def experiment(hat: Hat, expected_balls, num_balls_drawn, num_experiments):
  success = 0
  for _ in range(num_experiments):
    new_hat = copy.deepcopy(hat)
    balls_list = new_hat.draw(num_balls_drawn)
    Ok = True
    for color in expected_balls:
      if balls_list.count(color) < expected_balls[color]:
        Ok = False
    if Ok: success += 1
  return (success / num_experiments)

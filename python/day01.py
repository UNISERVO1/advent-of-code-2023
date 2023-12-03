
def totals(line):
   nums = [i for i in line if i.isnumeric()]
   return int(nums[0])*10 + int(nums[-1])

def part1(file_name):
   total = 0
   with open(file_name) as f:
      for line in f:
         total += totals(line)
   return total


def part2(file_name):
   nums_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
   total = 0
   with open(file_name) as f:
      for line in f:
         calibrated_line, k = "", 0
         while k < len(line):
            num = None
            for i, v in enumerate(nums_words):
               if line[k:].startswith(v):
                  num = i + 1
                  break
            calibrated_line += str(num) if num else line[k]
            k += 1
         total += totals(calibrated_line)
   return total

if __name__ == "__main__":
   print(part1("src/Day01.txt"))
   print(part2("src/Day01.txt"))
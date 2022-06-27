
word = 'he**llo'

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def scrable_generator(word):
    total = 0
    index = 0
    word_iterator =iter(word)

    for char in word_iterator:
        if (word[index] in '*') and (word[index + 1] in '*'):
           tripled_number = double_astrix(index=index,word= word,total=total)
           total += tripled_number
           index += 2
           print(total)
           word_iterator.__next__()
           word_iterator.__next__()
        elif(word[index] in '*'):
            double_number = score.get(word[index - 1])*2
            total += double_number
            print(f'* encountered char: {word[index -1]}; value:{score.get(word[index-1 ])}*2 is being added to total : {total}')
            index += 1
            continue
        total += score.get(word[index])
        print(f'char: {word[index]};  value:{score.get(word[index])} is being added to total : {total}')
        index += 1
    return total

def main():
    print(f'total is:',scrable_generator(word))

def double_astrix(index:int, word:str, total:int):
    print(f'the value of char being printed is: {word[index - 1]} * 3')
    return score.get(word[index - 1]) * 3


if __name__ == "__main__":
    main()
def main():
    with open("books/frankenstein.txt") as f:
            file_contents = f.read()

    print(get_word_count(file_contents))
    print(count_characters(file_contents))

def get_word_count(words):
      return len(words.split())

def count_characters(words):
      character_list = {}
      for word in words:
            character = word.lower()
            if character not in character_list:
                  character_list[character] = 1
            else:
                  character_list[character] += 1
      return(character_list)

main()
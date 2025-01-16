def main():
    with open("books/frankenstein.txt") as f:
            file_contents = f.read()
    word_count = get_word_count(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in this document")
    character_library = count_characters(file_contents)
    sorted_character_library = dict(sorted(character_library.items(), key=lambda item: item[1], reverse=True))
    for i in sorted_character_library:
        if i.isalpha():   
            print(f"The '{i}' character was found {character_library[i]} times")
    

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
def count_vowels_and_consonants(text: str) -> dict:
    vowles=("a","o","u","i","e")

    count_unli=0
    count_undosh=0

    for i in text:
        if i.isalpha():
            if i in vowles:
                count_unli+=1
            else:
                count_undosh+=1
    return {f"unli: {count_unli}, undosh: {count_undosh}"}
print(count_vowels_and_consonants("Salom Dunyo!"))
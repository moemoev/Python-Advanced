def reverse_text(text: str):
    return (text[i] for i in range(-1, -len(text) - 1, -1))

for char in reverse_text("step"):
    print(char, end='')
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    name = input("What's your name? ").strip() or "Student"
    print(greet(name))

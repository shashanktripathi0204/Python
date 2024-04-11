def police_check(age: int) -> bool:  # declaring the type(age:int) helps in the future,
    # -> bool this tells us what the function will be returning
    if age > 18:
        return True
    return False


if police_check(87):
    print("You may pass")
else:
    print("You fail")

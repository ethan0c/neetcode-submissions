def concatenate(s1: str, s2: str) -> str:
    con = (s1 + s2)
    if len(con) > 10:
        return "Too long!"
    else: 
        return con




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))

def chiffrement (message,decalage):
    resultat = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                resultat += chr((ord(char) - ord('A' ) + decalage) % 26 + ord('A'))
            elif char.islower():
                resultat += chr((ord(char) - ord('a' ) + decalage) % 26 + ord('a'))
        else:
            resultat += char
    
    return resultat

message_original = "Bonjour, Jules César !"
decalage = 3
message_chiffre = chiffrement(message_original, decalage)

print("Message original:", message_original)
print("Message chiffré:", message_chiffre)
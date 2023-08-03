def vigenere_cipher(plaintext, keyword):
    # Convert both the plaintext and the keyword to uppercase
    plaintext = plaintext.upper()
    keyword = keyword.upper()

    # Repeat the keyword to match the length of the plaintext
    keyword = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]

    # Encrypt each character of the plaintext using the Vigenère cipher and build the ciphertext
    ciphertext = ''.join(chr((ord(p) + ord(k) - 2 * ord('A')) % 26 + ord('A')) for p, k in zip(plaintext, keyword))

    return ciphertext

def main():
    # Ask the user for the plaintext and keyword
    plaintext = input("Enter the Plain Text (All Uppercase Letters ; No Spaces): ")
    keyword = input("Enter the Keyword (All Uppercase Letters): ")

    # Encrypt the plaintext using the Vigenère cipher
    ciphertext = vigenere_cipher(plaintext, keyword)

    # Display the ciphertext
    print("Ciphertext:", ciphertext)

if __name__ == "__main__":
    main()

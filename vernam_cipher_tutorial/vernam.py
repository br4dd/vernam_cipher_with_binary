def VernamCipherFunction(text, key):
      result = "";
      ptr = 0;
      for char in text:
            result = result + chr(ord(char) ^ ord(key[ptr]));
            ptr += 1;
            
      return result
                      
encryption_key = '';

def encrypted_text(encryption):
      print('\nENCRYPTED TEXT: '+encryption)
def encrypted_text_binary(encryption_key_binary):
      print('\nENCRYPTED TEXT IN BINARY: '+encryption_key_binary+'\n')
def plaintext_binary_output():
      print('%s %s= %s'% ( plaintext, ' '*(len(encryption_key)-len(plaintext)) , plaintext_binary ) )
def encryption_binary_output():
      print('%s = %s'% ( encryption_key, encryption_key_binary ) )
def dashes():
      print('%s %s' % ( ' '*(len(encryption_key) + 2) ,'⎻'*len(encryption_key_binary)) )
def encrypted_text_output():
      print('%s %s' % ( ' '*(len(encryption_key) + 2) ,result_binary ) )

while True:
      plaintext = input("\nEnter Text To Encrypt:\t");
      encryption_key = input("\nEnter Encryption Key:\t");
      if len(plaintext) <= len(encryption_key):
        encryption = VernamCipherFunction(plaintext, encryption_key);
        
        print('\nENCRYPTION\n')

      # FOR CONVERTING VARIABLES TO BINARY
        plaintext_binary = ' '.join(format(ord(i), '08b') for i in plaintext)
        encryption_key_binary = ' '.join(format(ord(i), '08b') for i in encryption_key)
        result_binary = ' '.join(format(ord(i), '08b') for i in encryption)
      # ENCRYPTION
        plaintext_binary_output()
        encryption_binary_output()
        dashes()
      # XOR OPERATION
        encrypted_text_output()

        encrypted_text(encryption)
        encrypted_text_binary(encryption_key_binary)

        print('NOTE: SOME OF THE ENCRYPTED TEXT ARE NOT CONVERTABLE TO NORMAL CHARACTER SO THE OUTPUT WILL BE BLANK')

        decryption = VernamCipherFunction(encryption, encryption_key);
        print("\nDecrypted Vernam Cipher Text:\t" + decryption+"\n");
      # DECRYPTION
        encrypted_text_output()
        encryption_binary_output()
        dashes()
      # XOR OPERATION
        plaintext_binary_output()
        
      else:
          print('\nENCRYPTION KEY MUST BE EQUAL OR MORE THAN THE LENGTH OF PLAINTEXT')



# chr(97) => 'a'
# ord('a') => 97

def VernamCipherFunction(text, key):
      result = "";
      ptr = 0;
      for char in text:
            result = result + chr(ord(char) ^ ord(key[ptr]));
            ptr += 1;
            
      return result
                      
encryption_key = '';

while True:
      plaintext = input("\nEnter Text To Encrypt:\t");
      encryption_key = input("\nEnter Encryption Key:\t");
      if len(plaintext) <= len(encryption_key):
        encryption = VernamCipherFunction(plaintext, encryption_key);
        
        print('\nENCRYPTION\n')

        #FOR CONVERTING VARIABLES TO BINARY
        plaintext_binary = ' '.join(format(ord(i), '08b') for i in plaintext)
        encryption_key_binary = ' '.join(format(ord(i), '08b') for i in encryption_key)
        result_binary = ' '.join(format(ord(i), '08b') for i in encryption)
        
        print('%s %s= %s'% ( plaintext, ' '*(len(encryption_key)-len(plaintext)) , plaintext_binary ) )
        print('%s = %s'% ( encryption_key, encryption_key_binary ) )
        print('%s %s' % ( ' '*(len(encryption_key) + 2) ,'⎻'*len(encryption_key_binary)) )
        # XOR OPERATION
        print('%s %s' % ( ' '*(len(encryption_key) + 2) ,result_binary ) )
        print('\nENCRYPTED TEXT: '+encryption)
        print('NOTE: SOME OF THE ENCRYPTED TEXT ARE NOT CONVERTABLE TO NORMAL CHARACTER SO THE OUTPUT WILL BE BLANK')
        decryption = VernamCipherFunction(encryption, encryption_key);
        print("\nDecrypted Vernam Cipher Text:\t" + decryption+"\n");
        #DECRYPTION
        print('%s %s' % ( ' '*(len(encryption_key) + 2) ,result_binary ) )
        print('%s = %s'% ( encryption_key, encryption_key_binary ) )
        print('%s %s' % ( ' '*(len(encryption_key) + 2) ,'⎻'*len(encryption_key_binary)) )
        print('%s %s= %s'% ( plaintext, ' '*(len(encryption_key)-len(plaintext)) , plaintext_binary ) )

      else:
          print('\nENCRYPTION KEY MUST BE EQUAL OR MORE THAN THE LENGTH OF PLAINTEXT')

# chr(97) => 'a'
# ord('a') => 97

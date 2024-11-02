def decrypt_string(x):
  decrypted = '' # 解密結果

  for i in range(len(x)):
    ascii_code = ord(x[i])
    new_ascii = ascii_code - (i + 1)
    decrypted += chr(new_ascii)
  
  return decrypted

n = str(input())

print(decrypt_string(n))
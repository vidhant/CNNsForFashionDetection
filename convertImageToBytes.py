with open("favicon", "rb") as imageFile:
  f = imageFile.read()
  b = bytearray(f)

print (len(b))

with open("temp","wb") as copiedFile:
	copiedFile.write(b);

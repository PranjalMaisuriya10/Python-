x=b"Hello"
print(x)
print(type(x))

x=bytearray(5)
print(x)
print(type(x))

x=memoryview(bytes(5))
print(x)
print(type(x))

print(bytearray('Hello World','utf-8'))

nums=[1,2,3,4,5]
print(bytearray(nums))
print(bytes(nums))
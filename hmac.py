import hmac
import hashlib

#this the key which both have
key = "this is my key"
message = "Beautiful World" #message sent by alice

#creating encoded key with encode function
encodedkey = str.encode(key)  

#creating new hmac with parameter encodedkey,message,hash function
hmac1 = hmac.new(encodedkey,message.encode('UTF-8'),hashlib.sha1)
digestvalue2 = hmac1.hexdigest()

print("key :", key)
print("message :", message)
print("encodedKey :", encodedkey)
print("hmac1::", hmac1)
print("digest value in hex :", digestvalue2)
print("size of the MAC value : ", 8*hmac1.digest_size , "bits")

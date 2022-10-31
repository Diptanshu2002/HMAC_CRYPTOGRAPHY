# Message Authentication Code
## DEFINITION
Message Authentication Code (MAC), also referred to as a tag, is used to authenticate the origin and nature of a message. MACs use authentication cryptography to verify the legitimacy of data sent through a network or transferred from one person to another.

In other words, MAC ensures that the message is coming from the correct sender, has not been changed, and that the data transferred over a network or stored in or outside a system is legitimate and does not contain harmful code. MACs can be stored on a hardware security module, a device used to manage sensitive digital keys.

## **HOW DOES A MESSAGE AUTHENTICATION CODE WORK?**
The first step in the MAC process is the establishment of a secure channel between the receiver and the sender. To encrypt a message, the MAC system uses an algorithm, which uses a symmetric key and the plain text message being sent. The MAC algorithm then generates fixed-length authentication tags by processing the message. The resulting computation is the message's MAC.

This MAC is then appended to the message and transmitted to the receiver. The receiver computes the MAC using the same algorithm. If the resulting MAC the receiver arrives at equals the one sent by the sender, the message is verified as authentic, legitimate, and not tampered with. Uses a secure key only known to the sender and the recipient for the computation of the MAC.

## WHAT ARE THE TYPES OF MESSAGE  AUTHENTICATION CODES?

Although all MACs accomplish the same end objective, there are a few different types.  

### **One-time MAC:**  
A one-time MAC is a lot like one-time encryption in that a MAC algorithm for a single use is defined to secure the transmission of data. One-time MACs tend to be faster than other authentication algorithms.

### **Carter-Wegman MAC:**  
A Carter-Wegman MAC is similar to a one-time MAC, except it also incorporates a pseudorandom function that makes it possible for a single key to be used many times over.

### **HMAC:**  
With a Keyed-Hash Message Authentication Code (HMAC) system, a one-way hash is used to create a unique MAC value for every message sent. The input parameters can have various values assigned, and making them very different from each other may produce a higher level of security.  

####  We are implementing HMAC in this project using Python build-in libraries such as HMAC and HASHLIB

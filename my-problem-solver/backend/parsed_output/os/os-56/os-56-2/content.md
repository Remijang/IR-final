# 56.2 Cryptography  

Many books have been written about cryptography, but we’re only going to spend a chapter on it. We’ll still be able to say useful things about it because, fortunately, there are important and complex issues of cryptography that we can mostly ignore. That’s because we aren’t going to become cryptographers ourselves. We’re merely going to be users of the technology, relying on experts in that esoteric field to provide us with tools that we can use without having full understanding of their workings1. That sounds kind of questionable, but you are already doing just that. Relatively few of us really understand the deep details of how our computer hardware works, yet we are able to make successful use of it, because we have good interfaces and know that smart people have taken great care in building the hardware for us. Similarly, cryptography provides us with strong interfaces, well-defined behaviors, and better than usual assurance that there is a lot of brain power behind the tools we use.  

That said, cryptography is no magic wand, and there is a lot you need to understand merely to use it correctly. That, particularly in the context of operating system use, is what we’re going to concentrate on here.  

The basic idea behind cryptography is to take a piece of data and use an algorithm (often called a cipher), usually augmented with a second piece of information (which is called a key), to convert the data into a different form. The new form should look nothing like the old one, but, typically, we want to be able to run another algorithm, again augmented with a second piece of information, to convert the data back to its original form.  

Let’s formalize that just a little bit. We start with data $P$ (which we usually call the plaintext), a key $K ,$ and an encryption algorithm $E ( )$ . We end up with $C$ , the altered form of $P$ , which we usually call the ciphertext:  

$$
C = E ( P , K )
$$  

For example, we might take the plaintext “Transfer $\$ 100$ to my savings account” and convert it into ciphertext “Sqzmredq #099 sn lx rzuhmfr zbbntms.” This example actually uses a pretty poor encryption algorithm called a Caesar cipher. Spend a minute or two studying the plaintext and ciphertext and see if you can figure out what the encryption algorithm was in this case.  

The reverse transformation takes $C$ , which we just produced, a decryption algorithm $D ( )$ , and the key $K$ :  

$$
P = D ( C , K )
$$  

So we can decrypt “Sqzmredq #099 sn lx rzuhmfr zbbntms” back into “Transfer $\$ 100$ to my savings account.” If you figured out how we encrypted the data in the first place, it should be easy to figure out how to decrypt it.  

We use cryptography for a lot of things, but when discussing it generally, it’s common to talk about messages being sent and received. In such discussions, the plaintext $P$ is the message we want to send and the ciphertext $C$ is the protected version of that message that we send out into the cold, cruel world.  

For the encryption process to be useful, it must be deterministic, so the first transformation always converts a particular $P$ using a particular $K$ to a particular $C _ { . }$ , and the second transformation always converts a particular $\mathbf { \bar { \boldsymbol { C } } }$ using a particular $K$ to the original $P$ . In many cases, $E ( )$ and $D ( )$ are actually the same algorithm, but that is not required. Also, it should be very hard to figure out $P$ from $C$ without knowing $K$ . Impossible would be nice, but we’ll usually settle for computationally infeasible. If we have that property, we can show $C$ to the most hostile, smartest opponent in the world and they still won’t be able to learn what $P$ is.  

Provided, of course, that ...  

This is where cleanly theoretical papers and messy reality start to collide. We only get that pleasant assurance of secrecy if the opponent does not know both $D ( )$ and our key $K$ . If they are known, the opponent will apply $D ( )$ and $K$ to C and extract the same information $P$ that we can.  

It turns out that we usually can’t keep $E ( )$ and $D ( )$ secret. Since we’re not trying to be cryptographers, we won’t get into the why of the matter, but it is extremely hard to design good ciphers. If the cipher has weaknesses, then an opponent can extract the plaintext $P$ even without $K$ . So we need to have a really good cipher, which is hard to come by. Most of us don’t have a world-class cryptographer at our fingertips to design a new one, so we have to rely on one of a relatively small number of known strong ciphers. AES, a standard cipher that was carefully designed and thoroughly studied, is one good example that you should think about using.  

It sounds like we’ve thrown away half our protection, since now the cryptography’s benefit relies entirely on the secrecy of the key. Precisely. Let’s say that again in all caps, since it’s so important that you really need to remember it: THE CRYPTOGRAPHY’S BENEFIT RELIES ENTIRELY ON THE SECRECY OF THE KEY. It probably wouldn’t hurt for you to re-read that statement a few dozen times, since the landscape is littered with insecure systems that did not take that lesson to heart.  

The good news is that if you’re using a strong cipher and are careful about maintaining key secrecy, your cryptography is strong. You don’t need to worry about anything else. The bad news is that maintaining key secrecy in practical systems for real uses of cryptography isn’t easy. We’ll talk more about that later.  

For the moment, revel in the protection we have achieved, and rejoice to learn that we’ve gotten more than secrecy from our proper use of cryptography! Consider the properties of the transformations we’ve performed. If our opponent gets access to our encrypted data, it can’t be understood. But what if the opponent can alter it? What’s being altered is the encrypted form, i.e., making some changes in $C$ to convert it to, say, $C ^ { \prime }$ . What will happen when we try to decrypt $C ?$ Well, it won’t decrypt to $P$ . It will decrypt to something else, say $\scriptstyle { \dot { P } } ^ { \prime }$ . For a good cipher of the type you should be using, it will be difficult to determine what a piece of ciphertext $C ^ { \prime }$ will decrypt to, unless you know $K$ . That means it will be hard to predict which ciphertext you need to have to decrypt to a particular plaintext. Which in turn means that the attacker will have no idea what the altered ciphertext $C ^ { \prime }$ will decrypt to.  

Out of all possible bit patterns it could decrypt to, the chances are good that $P ^ { \prime }$ will turn out to be garbage, when considered in the context of what we expected to see: ASCII text, a proper PDF file, or whatever. If we’re careful, we can detect that $P ^ { \prime }$ isn’t what we started with, which would tell us that our opponent tampered with our encrypted data. If we want to be really sure, we can perform a hashing function on the plaintext and include the hash with the message or encrypted file. If the plaintext we get out doesn’t produce the same hash, we will have a strong indication that something is amiss.  

So we can use cryptography to help us protect the integrity of our data, as well.  

OPERATINGSYSTEMS[VERSION 1.10]  

WWW.OSTEP.ORG  

TIP: DEVELOPING YOUR OWN CIPHERS: DON’T DO IT  

Don’t.  

It’s tempting to leave it at that, since it’s really important that you follow this guidance. But you may not believe it, so we’ll expand a little. The world’s best cryptographers often produce flawed ciphers. Are you one of the world’s best cryptographers? If you aren’t, and the top experts often fail to build strong ciphers, what makes you think you’ll do better, or even as well?  

We know what you’ll say next: “but the cipher I wrote is so strong that I can’t even break it myself.” Well, pretty much anyone who puts their mind to it can create a cipher they can’t break themselves. But remember those world-class cryptographers we talked about? How did they get to be world class? By careful study of the underpinnings of cryptography and by breaking other people’s ciphers. They’re very good at it, and if it’s worth their trouble, they will break yours. They might ignore it if you just go around bragging about your wonderful cipher (since they hear that all the time), but if you actually use it for something important, you will unfortunately draw their attention. Following which your secrets will be revealed, following which you will look foolish for designing your own cipher instead of using something standard like AES, which is easier to do, anyway.  

So, don’t.  

Wait, there’s more! What if someone hands you a piece of data that has been encrypted with a key $K$ that is known only to you and your buddy Remzi? You know you didn’t create it, so if it decrypts properly using key $K$ , you know that Remzi must have created it. After all, he’s the only other person who knew key $K$ , so only he could have performed the encryption. Voila, we have used cryptography for authentication! Unfortunately, cryptography will not clean your room, do your homework for you, or make thousands of julienne fries in seconds, but it’s a mighty fine tool, anyway.  

The form of cryptography we just described is often called symmetric cryptography, because the same key is used to encrypt and decrypt the data. For a long time, everyone believed that was the only form of cryptography possible. It turns out everyone was wrong.  


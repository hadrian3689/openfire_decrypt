# Openfire Password Decryptor
Little Python tool to decrypt passwords from Openfire embedded-db.
<br>
Original publication: https://hashcat.net/forum/archive/index.php?thread-2399.html
<br>
The original project by c0rdis: https://github.com/c0rdis/openfire_decrypt

## Dependencies
We need the good old Pycrypto
```
pip install pycryptodome
```

## Getting Started
With python3
```
python3 openfire_decrypt.py <hex encoded password encrypted string> <passwordKey>
```

## Disclaimer
All the code provided on this repository is for educational/research purposes only. Any actions and/or activities related to the material contained within this repository is solely your responsibility. The misuse of the code in this repository can result in criminal charges brought against the persons in question. Author will not be held responsible in the event any criminal charges be brought against any individuals misusing the code in this repository to break the law.


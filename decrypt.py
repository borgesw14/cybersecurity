#catfish damn professor do i really look like a catfish
import subprocess, re, sys

file = sys.argv[1] #wordlist.txt
encrypted_file = sys.argv[2] #borgespw1.pdf.gpg

with open(file, 'r') as f:
    words = f.readlines()

    """ For each word in wordlist run gpg command """
    for word in words:
        key = word.rstrip() #remove trailing \n char
        sub = subprocess.Popen("gpg --output result.pdf --decrypt --batch --passphrase '{word}' {file} 2>&1".format(word = key, file = encrypted_file), shell=True, stdout=subprocess.PIPE)
        subprocess_return = sub.stdout.read()
        
        res = re.split("\n", subprocess_return.decode("utf-8"))

        if(len(res) == 3):
            print('success with pass: ' + word) # get it pass word
            break

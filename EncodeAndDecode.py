# https://leetcode.com/problems/encode-and-decode-strings/description/

#First thought was to do a Caesar-cipher–style trick can give  an “encode/decode” pair,
#but it’s hard here because:
#	Input strings can contain any ASCII (not just letters).
#	Need a clear way to know where one string ends and the next begins
#this is how it would be done:
# get the codepoint
# code = ord(ch)          # e.g. ord('a') == 97

# # shift it by some K, then wrap in the 0–255 range
# new_code = (code + K) % 256  

# # turn it back into a character
# new_ch = chr(new_code)

#The solution above will cause boundary collisions and need to wrap around

#Decode must be given a single string so the issue becomes
#How do we know where one word ends and one word begins 
#BUT cannot just have one special character delimiter or just a number bc 
#it can just show up in the string sooo we need the length + delimiter

from typing import List


def encode(strs: List[str]) -> str:
    
    #List to hold each "length#string" chunk
    parts = []
    
    #Loop over each string in the list
    for s in strs:
        # Compute its length (number of characters)
        length = len(s)
        # Build the chunk: "<length>#<string>"
        #     - f-string: injects length and s directly into the format
        #     - "#" is the delimiter between the numeric prefix and the payload
        chunk = f"{length}#{s}"
        # Add that chunk to our parts list
        parts.append(chunk)
    return "".join(parts)
        


def decode(s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        
        #iterate character by character
        while i < len(s):
            
            #want to find the delimiter with a second pointer
            j= i
            while s[j] != "#":
                j += 1
            
            #once at the delimiter we can get the length
            length = int(s[i:j]) #Length of the s[i:j] grabs the substring from index i up to (but not including) j. Slices the length, now s[i:j] are the digits
            
            start = j + 1 #read the next length chars
            res.append
            res.append(s[start : start + length])

            # 3. move `i` past this chunk
            i = start + length
        return res
    
    #Develop my own pattern to encode 

def run_codec_tests():
    tests = [
        [],                                 # empty list
        [""],                               # single empty string
        ["hello"],                          # single word
        ["hello", "world"],                 # two words
        ["", ""],                           # two empty strings
        ["#", "##", "#a#"],                 # strings that include the delimiter
        ["123", "456", "7890"],             # numeric strings
        ["line\nbreak", "tabs\tand spaces"],# escape chars
        ["😊", "🚀#"],                       # unicode + delimiter
        ["mixed#123", "", "end"],           # mix of empty, delimiter, normal
    ]

    for strs in tests:
        enc = encode(strs)
        dec = decode(enc)
        ok  = dec == strs
        print(f"input: {strs!r}")
        print(f" encoded: {enc!r}")
        print(f" decoded: {dec!r}")
        print(f" pass: {ok}\n")

# run the tests
run_codec_tests()
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
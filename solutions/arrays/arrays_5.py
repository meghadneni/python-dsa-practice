"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Example 1:

Input: dummy_input = ["Hello","World"]

Output: ["Hello","World"]

Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);

-----------------------------------
Encode function : 
    - Pass the list
    - For each string, calc length, 
    - We start each word with that length followed by $ . 
    -Repeat it and form one big encoded string.
Decode :
    - Now we have big chunk of string with length followed by $ followed by the actual word.
    - lets maintain indexes- i , j . 
    - while i < len(str):
        - j = i+1
        - check if s[j] == '$' , till that point increment j.
        - once $ reached, get int(s[i:j]) - gives the length of the word
        - word = s[j+1 , j+l+1] -> put it into an array
        - increment i = j+l+1 i.e next word's length position  and repeat
"""



class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            l = len(s)
            res += str(l)+"$"+s
        return res

        

    def decode(self, s: str) -> List[str]:
        res, i = [], 0 
        ln = len(s)
        while ( i < ln):
            j = i+1
            while(s[j] != '$'):
                j += 1
            l = int(s[i:j])
            wrd = s[j+1:j+l+1]
            res.append(wrd)
            i = j+l+1
        return res
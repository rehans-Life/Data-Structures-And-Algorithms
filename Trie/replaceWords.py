from string import ascii_letters
from typing import List

class TrieNode:

    def __init__(self) -> None:
        self.links = [None] * 26
        self.flag = False
    
    def containsKey(self,char) -> bool:
        return self.links[ascii_letters.index(char)]
    
    def insertKey(self,char,trieNode):
        self.links[ascii_letters.index(char)] = trieNode
        
    def getRefNode(self,char: str):
        return self.links[ascii_letters.index(char)]
    
    def getFlag(self) -> bool:
        return self.flag
    
    def setEnd(self):
        self.flag = True

class Trie:

    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self,prefix: str) -> None:

        node = self.root
        
        for char in prefix:
            if not node.containsKey(char):
                node.insertKey(char,TrieNode())
            
            node = node.getRefNode(char)
        
        node.setEnd()

    def search(self,word: str) -> str:

        node = self.root
        prefix = ''

        for char in word:
            
            prefix+=char

            if not node.containsKey(char):
                return ''
            
            node = node.getRefNode(char)

            if node.getFlag():
                return prefix
        
        return ''

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        trie = Trie()

        sentence = sentence.split(' ')

        for prefix in dictionary: trie.insert(prefix)

        for i in range(len(sentence)):

            word = sentence[i]

            prefix = trie.search(word)

            if prefix:
                sentence[i] = prefix

        return ' '.join(sentence)

dictionary = ["e","k","c","harqp","h","gsafc","vn","lqp","soy","mr","x","iitgm","sb","oo","spj","gwmly","iu","z","f","ha","vds","v","vpx","fir","t","xo","apifm","tlznm","kkv","nxyud","j","qp","omn","zoxp","mutu","i","nxth","dwuer","sadl","pv","w","mding","mubem","xsmwc","vl","farov","twfmq","ljhmr","q","bbzs","kd","kwc","a","buq","sm","yi","nypa","xwz","si","amqx","iy","eb","qvgt","twy","rf","dc","utt","mxjfu","hm","trz","lzh","lref","qbx","fmemr","gil","go","qggh","uud","trnhf","gels","dfdq","qzkx","qxw"]
sentence = "ikkbp miszkays wqjferqoxjwvbieyk gvcfldkiavww vhokchxz dvypwyb bxahfzcfanteibiltins ueebf lqhflvwxksi dco kddxmckhvqifbuzkhstp wc ytzzlm gximjuhzfdjuamhsu gdkbmhpnvy ifvifheoxqlbosfww mengfdydekwttkhbzenk wjhmmyltmeufqvcpcxg hthcuovils ldipovluo aiprogn nusquzpmnogtjkklfhta klxvvlvyh nxzgnrveghc mpppfhzjkbucv cqcft uwmahhqradjtf iaaasabqqzmbcig zcpvpyypsmodtoiif qjuiqtfhzcpnmtk yzfragcextvx ivnvgkaqs iplazv jurtsyh gzixfeugj rnukjgtjpim hscyhgoru aledyrmzwhsz xbahcwfwm hzd ygelddphxnbh rvjxtlqfnlmwdoezh zawfkko iwhkcddxgpqtdrjrcv bbfj mhs nenrqfkbf spfpazr wrkjiwyf cw dtd cqibzmuuhukwylrnld dtaxhddidfwqs bgnnoxgyynol hg dijhrrpnwjlju muzzrrsypzgwvblf zbugltrnyzbg hktdviastoireyiqf qvufxgcixvhrjqtna ipfzhuvgo daee r nlipyfszvxlwqw yoq dewpgtcrzausqwhh qzsaobsghgm ichlpsjlsrwzhbyfhm ksenb bqprarpgnyemzwifqzz oai pnqottd nygesjtlpala qmxixtooxtbrzyorn gyvukjpc s mxhlkdaycskj uvwmerplaibeknltuvd ocnn frotscysdyclrc ckcttaceuuxzcghw pxbd oklwhcppuziixpvihihp"
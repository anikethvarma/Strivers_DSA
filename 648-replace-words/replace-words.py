class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        temp_list = sentence.split(" ")
        for i in range(len(temp_list)):
            for word in dictionary:
                if temp_list[i].startswith(word):
                    temp_list[i] = word
        
        return " ".join(temp_list)

        
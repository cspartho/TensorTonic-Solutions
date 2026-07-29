import numpy as np
from typing import List, Dict

class SimpleTokenizer:
    """
    A word-level tokenizer with special tokens.
    """
    
    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0
        
        # Special tokens
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"
    
    def build_vocab(self, texts: List[str]) -> None:
        """
        Build vocabulary from a list of texts.
        Add special tokens first, then unique words.
        """
        # YOUR CODE HERE
        texts = " ".join(texts)
        word_list = texts.split(' ')
        u_list = set(word_list)
        unique_words = sorted(u_list)
        token_num = 4
        self.vocab_size = len(unique_words) + token_num
        tokens = ["<PAD>", "<UNK>", "<BOS>", "<EOS>"]
        self.word_to_id = {token: index for index, token in enumerate(tokens)}
        for word in unique_words:
            if word not in self.word_to_id:
                self.word_to_id[word] =token_num
                token_num += 1
            
    def encode(self, text: str) -> List[int]:
        """
        Convert text to list of token IDs.
        Use UNK for unknown words.
        """
        # YOUR CODE HERE
        token_ids_list = []
        words = text.lower().split()
        print(self.word_to_id)
        for word in words:
            if word in self.word_to_id.keys():
                token_ids_list.append(self.word_to_id[word])
            else:
                token_ids_list.append(self.word_to_id['<UNK>'])
        print(token_ids_list)
        return token_ids_list
        
    def decode(self, ids: List[int]) -> str:
        """
        Convert list of token IDs back to text.
        """
        # YOUR CODE HERE
        inverse_dict = {v: k for k, v in self.word_to_id.items()}
        s = ""
        l = []
        for i in ids:
            if i in inverse_dict:
               l.append(inverse_dict[i])
            else:
                l.append('<UNK>')

        return " ".join(l)

        return s


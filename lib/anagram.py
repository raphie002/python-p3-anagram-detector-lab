# your code goes here!

class Anagram:
    def __init__(self, word):
        self.original_word = word
        self.canonical = self._get_canonical_form(word)

    def _get_canonical_form(self, word):
        return "".join(sorted(word.lower()))

    def match(self, candidates):
        matches = []
        
        original_lower = self.original_word.lower()
        
        for candidate in candidates:
            candidate_lower = candidate.lower()
            if original_lower != candidate_lower:
                candidate_canonical = self._get_canonical_form(candidate)
                
                if self.canonical == candidate_canonical:
                    matches.append(candidate)
                    
        return matches
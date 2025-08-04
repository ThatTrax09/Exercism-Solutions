def find_anagrams(word, candidates):
    word_set = list(sorted(word.lower()))
    candidates_set = [list(sorted(candidate.lower())) for candidate in candidates]
    ans = [candidates[i] for i, candidate in enumerate(candidates_set) if word_set == candidate and len(word) == len(candidates[i]) and word.lower() != candidates[i].lower()]
    return ans

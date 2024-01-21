def is_palindrome_after_char_deletion(s):

    def is_palindrome(string):
        return string == string[::-1]
    
    for i in range(len(s)):
        mod_str = s[:i] + s[i+1:]
        if is_palindrome(mod_str):
            return True
        
    return False
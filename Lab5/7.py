def snake_to_camel(word):
        return ''.join(x.capitalize()  for x in word.split('_'))

def snake_to_camel2(word):
    import re
    word  = re.sub('_',' ',word)
    word = re.sub(r'\s','', word.title())
    return word
print(snake_to_camel('est_str_geeksforgeeks_is_best_for_geeks '))
print(snake_to_camel2('est_str_geeksforgeeks_is_best_for_geeks '))
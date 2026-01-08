def custom_tree(chars, n):
    char_index = 0
    lines = []
    
    max_width = n * 2 - 1  
    
    for row in range(1, n + 1):
        row_chars = []
        for _ in range(row):
            row_chars.append(chars[char_index % len(chars)])
            char_index += 1
        
        row_str = ' '.join(row_chars)
        
        padding = (max_width - len(row_str)) // 2
        
        lines.append(' ' * padding + row_str)

    trunkPad = (max_width - 1) // 2 # calculate spaces before ie padding
    num_of_trunks = n // 3 # number of trunks will change and is dependent on n 
    for i in range(num_of_trunks): # append trunks for as many trunks there are.
        lines.append(' ' * trunkPad + '|')

    
    print('\n'.join(lines)) 

custom_tree("*@o", 10)
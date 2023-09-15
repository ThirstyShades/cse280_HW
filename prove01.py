def xor(p, q): 
    return (p or q) and not (p and q)
    #I am suprized at how simple this was, very cool I like it. Took me way to long but I go there in the end. Mianly bcease I was trying way to hard to understand the fuction below. and thought I had to chage it in some way

def truth_table_2_vars(function):
    print(f"{function.__name__}")
    print(f"{'p':<8}{'q':<8}{'ANS':<8}")
    print("----------------------------------------")
    rows = [(p,q) for p in (True, False) 
                  for q in (True, False)]    
    for p, q in rows:
        ans = function(p,q)
        print(f"{p!s:<8}{q!s:<8}{ans!s:<8}")
    print()

truth_table_2_vars(xor)
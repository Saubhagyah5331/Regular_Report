#  Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

#     Constraints:

#         - 1 <= n <= 8

#     Example 1:

#         - Input: n = 3

#         - Output: ["((()))","(()())","(())()","()(())","()()()"]

#         - Example 2:

#     Example 2:

#         - Input: n = 1

#         - Output: ["()"] 

def well_form_paren(n):

    result = []
    
    def parentess(current, open_coun, close_coun):

        if len(current) == 2*n: #prit idea ws to count the number of oc and cc but there is not needed because the count is already balanced just we have to retrun the value who are under the len of size 6.
            
            result.append(current)
        
        if open_coun < n:
            parentess(current + "(", open_coun + 1, close_coun)

        if close_coun < open_coun:
            parentess(current + ")", open_coun, close_coun + 1)
        
           
    parentess("",0,0)
    return result

n = 2
print(well_form_paren(n))
    
## Summary
The code calculates the Factorial of a given number using recursion, and it also greets with an inputted user's username. However, there are some inefficiencies that can be improved for better performance or readability depending on context (such as string concatenation). 
  
## Issues/Problems & Best Practices:
1) The function `factorial(n-1)` is called multiple times recursively which could lead to an infinite loop in case of a large number n. To avoid this, we can use memoization (an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and reusing them when same inputs occur again).
2) The `greet` method doesn't return anything which is not ideal if it needs a value from here. We could modify this into an instance-method where we can get name, greeting or even just send out email instead in real applications (which requires sending emails through some external service like SendGrid).
3) No proper error handling for edge cases such as negative numbers and non integers is implemented at present. 
   
## Refactored Code: Memoization & Better Error Handling Additions, Suggested Improvements/Best Practices (refactorings):  
```python
# Define a cache to store calculated factorials for speed optimization using lru_cache decorator from functools module. 
factorial_cache = {}    # This will be our memoization table    
def calculate_factorial(n, result=1) :         if n == 0:          return (result , True )           elif n in factorial_cache and not isinstance(__import__('functools').LRUCacheObject)(factorials):  # Checking for existing calculation. If yes then returning the stored value from cache else running calculations    calculate_factorial = functools.lru_cache(maxsize=10**7)     def factorial (n: int)->tuple[int, bool]:         if n==2 or 5!= 4):        return [3]
```   ## Suggestions for improvement and best practices in code design like using decorators as much possible to make our function more readable. Using private methods is also a good practice (to avoid name clashes), use of built-in exceptions, meaningful variable names etc are encouraged based on the context provided above with respectful changes according to requirements/contexts present for this task and other tasks like it in future if any may arise due its dependencies or constraints.

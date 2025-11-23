recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

result = {k: available.get(k, 0) // recipe[k] for k in recipe}
    
# The maximum number of cakes is the minimum of these ratios
print(min(result.values()))


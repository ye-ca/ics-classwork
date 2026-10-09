# If Statements Study Guide

## Evaluating Boolean Expressions
For the following, determine if the result is `True` or `False`.
Also, `x=5`, `y=15`, `z=10`

1. `True == True`
True	
2. `False == True`
False
3. `False != True`
True
4. `5 > 2`
True
5. `5 >= 5`
True
6. `1 != 10`
True
7. `x > y`
False
8. `x <= y or z == 10`
True
9. `3 * x >= y and 2 * y < z`
False
10. `x + 10 > y and (3 * x >= y and 2 * y < z or x <= y or z == 10)`
False

## Writing code
1. Ask the user for the cost of an item. If it is more that `$100` then say `"wow, that's expensive"`. Otherwise say nothing.
2. Ask the user for their name. If the first letter starts with the same letter yours does, then output an appropriate message. Otherwise, say "NAME is a cool name" (put their name in the output string).
3. Add to the above program to add another case where their last letter starts with the **first letter** of your name. Say "At least we can chain the names together! NAME1NAME2". For example, for the names "John" and "Nancy", chaining the names together should look like "Johnancy".
4. Create a variable for enemy health, set it to `100`. Ask the user if they want to use attack 1, attack 2, or do nothing. If they choose attack 1, the damage is randomized between `10-20` and chance to hit is `60%`. Attack 2 is damage randomized between `5-10` with a chance to hit of `80%`. After this, conduct a random roll to see if the ability hits the enemy. Hint: roll `1-100`, if that roll is `<=` to the ability's hit percentage, the hit lands. Apply the damage to the enemy if it hits.



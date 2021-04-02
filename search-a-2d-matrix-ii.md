We're gonna start at top right corner so at `matrix[row => 0][col => len(matrix[0])]`

Let's remember the question

> - Integers in each row are sorted in ascending from left to right.
> - Integers in each column are sorted in ascending from top to bottom.

so numbers below are always going be bigger and left always smaller.

thus:

If `target > start` we go below
if `target < start` we go left

until we find the target, then we return true.

```python
class Solution:
    def searchMatrix(self, matrix, target):
        col = len(matrix[0]) - 1
        row = 0
        while col >= 0 and row < len(matrix):
            if  target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1
            else:
                return True
        return False
```

# Matrix-Solver
Solves a system of equations of any size that can create a nxn matrix with [Gaussian elimination](https://en.wikipedia.org/wiki/Gaussian_elimination). the operations can be done through terminal. There's two [operations](https://en.wikipedia.org/wiki/Gaussian_elimination#Row_operations) that can be done:

+ **rowop** - addition or subtraction of one row scalar to another. 

+ **rowmult** - mutiply a row by a nonzero scalar. if you do multiply by zero a warning is going to appear and you'll have to start from the beginning.

These operations can be kept repeated in the terminal by answering "yes" or "true". Or you can stop with "no" or "false".

The matrix needs to be a proper [identity matrix](https://en.wikipedia.org/wiki/Identity_matrix) for the constants to be correct. Right now it only checks the top left 2x2 matrix to verify:

```Python
if m[0][0] == 1 and m[1][1] == 1 and m[0][1] == 0 and m[1][0] == 0:
    print("###CORRECT CONSTANTS###")
else:
    print("###INCORRECT CONSTANTS###")
```
If the the matrix is 2x2 then you're sure it's correct. If it's greater then you can check the matrix with your own eyes ¯\ _(ツ)_/¯.

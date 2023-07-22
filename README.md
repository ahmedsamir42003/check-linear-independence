# check-linear-independence
This is a Python script that checks whether a set of vectors is linearly independent or not. It uses the Gaussian elimination method to reduce the vectors to row-echelon form, and then checks if there are any rows of zeros in the resulting matrix.

## Usage

1. Run the script in a Python environment.
2. Enter the number of vectors you want to check for linear independence.
3. Enter the vectors, one at a time, as lists of numbers separated by spaces.

For example:
In this example, the script checks whether the three vectors `(1, 0, 0)`, `(0, 1, 0)`, and `(0, 0, 1)` are linearly independent, and prints the result.

## Implementation

The script works by first padding the input vectors with zeros so that they all have the same length. It then performs row reduction on the resulting matrix using the Gaussian elimination method, to produce a row-echelon form of the matrix. Finally, it checks if there are any rows of zeros in the row-echelon form of the matrix, and prints the appropriate result.

The `postition` function is used to rearrange the rows of the matrix so that the pivot elements (the diagonal elements) are equal to 1. The `position` function is called in the main loop to perform this operation before performing row reduction.

### Limitations

- The script assumes that the input vectors are represented as lists of numbers. It may not work correctly if the input vectors are represented in a different format.
- The script may not work correctly if the input vectors are very large, due to limitations in the precision of floating-point arithmetic.

## Example Usage

To use this script, you can run it in a Python environment and follow the prompts to enter the vectors you want to check for linear independence.

For example, suppose you want to check whether the vectors `(1, 0, 0)`, `(0, 1, 0)`, and `(0, 0, 1)` are linearly independent. You can run the script and enter the vectors as follows:

* Please enter the number of vectors you would like to check for linear dependence among them: 3
* Enter the 1 vector: 1 0 0
* Enter the 2 vector: 0 1 0
* Enter the 3 vector: 0 0 1
* Linearly independent

In this example, the script determines that the vectors are linearly independent and prints the message "Linearly independent".

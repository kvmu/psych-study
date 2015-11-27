# psych-study
A small script to create tests for a psych study conducted by UBC students as part of coursework (study details here).

## Summary
My specifications are as follows:

* Given a list of 110 words and a 110 photo files (.png) arrange them in to sets of 5 x 4 arrays.
* The arrangement of words or pictures must be random and there cannot be any repeats in any given set.
* The ouput must be in .pdf format.
* There must be 100 such outputs.

My implementation is as follows:

1. Use Python to randomly (uniform distribution) select photos or words.
2. Use Python to to create 100 formatted LaTeX files with the selected photos or words.
3. Use a Windows PowerShell script to batch compile the 100 LaTeX files (using pdflatex, so the outputs are pdfs).

Details can be found in generateTeX.py.


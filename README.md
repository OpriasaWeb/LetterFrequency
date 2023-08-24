# Letter Frequency

Python Data Structures - project 1

Instructions: You are making a program to analyze text.
Take the text as the first input and a letter as the second input, and output the frequency of that letter in the text as a whole percentage.

Sample Input:
hello
l

Sample Output:
40

Explanation : The letter l appears 2 times in the text hello, which has 5 letters. So, the frequency would be (2/5)*100 = 40.

Pseudocode:





            BEGIN

              DECLARE "First input: "
              INPUT first_input
              
              DECLARE "Second input: "
              INPUT second_input

              DECLARE get_length as length of second_input

              DECLARE count equals to zero that adds up if condition meet

              FOR each of the letter in the first_input
                IF second_input match something in first_input
                  count plus 1
                ENDIF
              ENDFOR

              DECLARE frequency equals (count/get_length)*100

              PRINT frequency

            END

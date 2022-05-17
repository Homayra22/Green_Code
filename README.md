# Description
The word “dubitare” is “to doubt” in Latin. The Latin alphabet is a subset of English alphabet, so we can easily type Latin on modern computer. Your friend, Eve, recently has been very interested in Latin. However, she does not have any Latin English dictionary. Therefore, she collected many articles in English or in Latin about some specific topic. Her plan is to compute the frequency of each word appearing in the articles, and use the statistics to help her to map Latin words into English words. Please write a program to help her.
Input Specification
The first line of input contains an integer T (T ≤ 40) indicating the number of test cases. For each test case, it starts with a line containing three integers L, a, b (L ≤ 300, 1 ≤ a ≤ b ≤ 100). Each of the following L lines contains several words separated by spaces. You may assume:
1. There are at most 1200 characters including spaces.
2. All words consist of English alphabets.
3. All alphabets are in lower cases.
Output Specification
For the ith test case, output “Testcase #i:” first. Then output the ath, (a+1)th, …, bth most frequent words and their frequency, respectively. For example, if “cat” appears 15 times, then you should output “cat:15” in a line. If two words have the same frequency, then the word is considered as more frequent if it comes before another in the dictionary. Output a blank line between two test cases.

##Sample Input

3<br/>
1 2 3<br/>
i am who i am<br/>
2 3 4<br/>
sore ha sore kore ha kore<br/>
kore da kore ha gyakkyou<br/>
5 1 8<br/>

the classical latin alphabet also known as the roman alphabet is a writing system which evolved
from the cumaean version of the greek alphabet the cumaean script was descended from the
phoenician alphabet the cumaean alphabet was adopted and modified by the etruscans who
ruled early rome the etruscan alphabet was in turn adopted and further modified by the
ancient romans to write the latin language

##Sample Output


Testcase #1:<br/>
i:2<br/>
who:1<br/>
Testcase #2:<br/>
sore:2<br/>
da:1<br/>
Testcase #3:<br/>
the:11<br/>
alphabet:6<br/>
cumaean:3<br/>
was:3<br/>
adopted:2<br/>
and:2<br/>
by:2<br/>
from:2

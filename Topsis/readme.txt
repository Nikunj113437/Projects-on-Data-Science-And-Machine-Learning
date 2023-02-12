TOPSIS


How to use
The package Topsis-Nikunj-102003362 can be run though the command line as follows:

>> pip install Topsis-Nikunj-102003362
>>python topsis data.csv "1,1,1,1,1" "+,-,+,-,+" result.csv
Sample Input

Fund Name	P1	P2	P3	P4	P5
M1	0.85	0.72	7	37.3	11.47
M2	0.67	0.45	5.5	58.2	16.21
M3	0.83	0.69	3.9	68.3	18.43
M4	0.83	0.69	3.9	42.7	12.03
M5	0.71	0.5	    3.2	57.9	15.58
M6	0.94	0.88	4.7	46.6	13.28
M7	0.68	0.46	7	41.4	12.39
M8	0.95	0.9	    6.5	33.8	10.54


Output of this sample input
The output that will be generated from the following input data will be:

Fund Name	P1	P2	P3	P4	P5	Topsis Score	Rank
M1	0.85	0.72	7	37.3	11.47	0.606515477	2
M2	0.67	0.45	5.5	58.2	16.21	0.571404528	3
M3	0.83	0.69	3.9	68.3	18.43	0.411429976	8
M4	0.83	0.69	3.9	42.7	12.03	0.435972941	6
M5	0.71	0.5	    3.2	57.9	15.58	0.436800052	5
M6	0.94	0.88	4.7	46.6	13.28	0.422424787	7
M7	0.68	0.46	7	41.4	12.39	0.66149433	1
M8	0.95	0.9	    6.5	33.8	10.54	0.530809186	4

The output file contains columns of input file along with two additional columns having **Topsis_score** and **Rank** .
Here the ranks are given as rank 1 is the best solution according to the weights and impacts given and rank 8 is the worst solution.
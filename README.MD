
Project Details:
The project has the following structure:

    pythonProject/ -
        ├── evaluateShared.py
        ├── vrp.py
        └── problem_set/

- evaluateShared.py - This is the testing script shared by Vorto to run the solution script.
In addition to the start code provided in this file, I added line 79 to exclude carriage returns while using readLine() function. 

- vrp.py - Solution script for the VRP problem provided.

- problem_set - directory containing all the problem dataset.

Execution Instructions:

- To execute the solution file (vrp.py), run the following command :
python evaluateShared.py --cmd "python vrp.py" --problemDir problem_set

Testing:

On running the following command:
python evaluateShared.py --cmd "python vrp.py" --problemDir problem_set

you should see the following output on the terminal console:

problem1.txt
        running...
        run time: 0.08396792411804199 s
        evaluating solution...
        cost: 6001.348682523798
problem10.txt
        running...
        run time: 0.2630622386932373 s
        evaluating solution...
        cost: 55206.51115479412
problem11.txt
        running...
        run time: 0.2673149108886719 s
        evaluating solution...
        cost: 60827.37600288236
problem12.txt
        running...
        run time: 0.2756917476654053 s
        evaluating solution...
        cost: 83878.53426620184
problem13.txt
        running...
        run time: 0.27784180641174316 s
        evaluating solution...
        cost: 92534.45422533
problem14.txt
        running...
        run time: 0.2514917850494385 s
        evaluating solution...
        cost: 32021.175145780875
problem15.txt
        running...
        run time: 0.26343750953674316 s
        evaluating solution...
        cost: 37808.80682442998
problem16.txt
        running...
        run time: 0.2563669681549072 s
        evaluating solution...
        cost: 39133.64107727873
problem17.txt
        running...
        run time: 0.2869999408721924 s
        evaluating solution...
        cost: 39149.25420769292
problem18.txt
        running...
        run time: 0.28600335121154785 s
        evaluating solution...
        cost: 74756.3120879529
problem19.txt
        running...
        run time: 0.27004122734069824 s
        evaluating solution...
        cost: 80141.65601485048
problem2.txt
        running...
        run time: 0.09541153907775879 s
        evaluating solution...
        cost: 21484.806515475502
problem20.txt
        running...
        run time: 0.2649979591369629 s
        evaluating solution...
        cost: 57794.47806474166
problem3.txt
        running...
        run time: 0.11800122261047363 s
        evaluating solution...
        cost: 34708.90992424688
problem4.txt
        running...
        run time: 0.33599305152893066 s
        evaluating solution...
        cost: 74034.07990162159
problem5.txt
        running...
        run time: 0.25699901580810547 s
        evaluating solution...
        cost: 20431.410761772022
problem6.txt
        running...
        run time: 0.24665379524230957 s
        evaluating solution...
        cost: 19120.075468812345
problem7.txt
        running...
        run time: 0.2605125904083252 s
        evaluating solution...
        cost: 40086.012373982536
problem8.txt
        running...
        run time: 0.2872796058654785 s
        evaluating solution...
        cost: 38365.78756383047
problem9.txt
        running...
        run time: 0.3099997043609619 s
        evaluating solution...
        cost: 51791.62661582614
mean cost: 47963.81284400137
mean run time: 247.90339469909668ms

Deere-Data-Analytics
====================

Required Python Version: Python 2.7.7 

Required packages to run software:
Advise to install virtual environment to install these following packages to create isolated Python environment and avoid dependencies. 

-- pip install
-- easy install 
-- pandas
-- numpy
-- scipy
-- matplotlib
-- math
-- utm
-- itertools
-- Tkinter
-- pylab
-- drawnow

Procedure

1. Activate a specific virtual environment for this software.

2. Install the required packages above

3. Run GUI.visualization.py in the Terminal.

4. Fill out required fields to generate mass flow maps and lag function graphs.

5. Once you click "submit", 5 windows will pop up with the visualizations.

	Figure 1 -- Yield map plotted by easting and northing.

	Figure 2 -- Graph of the path the combine machine took plotted by timestamps

	Figure 3 -- Yield map of only the critical points (the edge points)

	Figure 4 -- line Graph of when the combine machine exits and enters the field (decay curve)

	Figure 5 -- Graph showing the fitted polynomial function to the decay curves

	If you click "Plot Live" a window with live graph plotting will pop up.

6. The fitted polynomial function will show up in the Terminal.
# Site-Suitability


*INTRODUCTION*

This software have been developed as part of the GEOG5990 Programming for Geographical Information Analysis: Core Skills of the University of Leeds. The objective is to develop a software to identify site suitability based on three factors: geology, population and transportation. 

The following document contains details of the software development. For details on using the the software please refer to Site Suitability Map user guide (ss_userguide.pdf).    


CONTACT

Any questions or comments can be emailed to the author, yasminyusop or Farah Yasmin at her university's email address: gy22fybm@leeds.ac.uk


GITHUB

The latest version of the programming can be found on GitHub:

https://github.com/yasminyusop/Site-Suitability.git


LICENSE

This project uses an MIT license, a permissive license which allows other users to use the software for commercial and private use including making distributios and modifications with the copyright notice (Ref.: LICENSE)


CONFIGURATION

The software was developed on:
* Spyder version: 5.2.2 None
* Python version: 3.9.13 64-bit
* Qt version: 5.9.7
* PyQt5 version: 5.9.2
* Operating System: Windows 10


MANIFEST

The following are files and folders in the Site-Suitability folder. Source codes are located in the src folders and the development of these are detailed out in this document.

* data/input 
* data/ouput
* src/ss1
* src/ss2
* src/ss3
* src/ss4
* src/ss5
* LICENSE
* README
* ss_userguide



DATA SOURCE

To develop this software, 3 different rasters in CSV format were provided by the School of Geography, University of Leeds. The following files are located in the .../.../data/input folder:

* geology.txt
* population.txt
* transport.txt



SOFTWARE DEVELOPMENT

The development of the software was divided into five parts: 
	1. Reading and plotting of 3 raster data (factors).
	2. Applying weights on each factor then combining them to generate a site suitability map, rescaled to (0,255).
	3. Displaying of the final map and writing into files.
	4. Code optimisation and simplification.
	5. Development of the GUI.

Every set of codes were built on the previous one with adjustments and improvements.


1. READ AND PLOT 3 RASTER DATA (ss1)

	The first part of the project was to get the software to read the CSV files as list of lists. The files were imported using the CSV module then read as list of lists using loops. The function any() and isinstance() were used together to test if the CSV were loaded correctly as list of lists. Then, all three rasters were plotted using matplotlib functions.
	Factors:
	data_geo: geology factor
	data_pop: population factor
	data_trs: transportation factor

2. APPLY WEIGHTS AND CREATE RESCALED SITE SUITABILITY MAP (ss2)

	In a suitability assessment, different weights are applied to suitability factors in order of importance. Higher weightage for factors that are more important, lower weightage for factors that are less important. In this section, random weights between 1 to 10 were assigned to each weight factor using the randint() function. 
	
	Weights:
	wg: weight for geology factor
	wp: weight for population factor
	wt: weight for transportation factor

	Using a series of loops, each factor was multiplied with the corresponding weight to obtain weighted factor rasters. 

	Next, to obtain an unscaled suitability map, the three weighted factors are added together. Lastly, the scales were standardised to (0,255) based on the following equation:
	
	Rescaled suitability map = ((Unscaled suitability map - Minimum value) / (Maximum value - Minimum value)) * 255

	To achieve the above, the maximum and minimum values were first derived prior to rescaling. 

	To test the lines of codes developed for the above are working, a series of plots were done at every stage (weights, combining factors and rescaling). The plots include colorbars which helped verify that the calculations were done correctly. The built-in Yellow-Green (YlGn) colormap was used for this project where yellow corresponds to low suitability and green corresponds to high suitability. The plots were also compared against different applied weightages. 

3. DISPLAY FINAL SUITABILITY MAP AND WRITE TO FILE (ss3)
 
	In this section, some lines of codes have been simplified or grouped into functions. The combine() function groups the multiplication of weights with different factors and adding them together. The rescale() function rescales the output from the combine() function into (0,255). To test the codes, the programme was ran several times to generate different weightages in order to compare the plots.

	At this stage, the programme saves the final output (Site Suitability Map) by default as ss_map.jpg and ss_map.txt into .../.../data/output.

4. CODE OPTIMISATION AND SIMPLIFICATION (ss4)

	To optimise and simplify the main source code, a sub-folder named modules was created to store different function codes. The codes have also been generalised to allow usage on other applications.
	
	io.py: stores read_data() and write_data() functions to read and write CSV files

	framework.py: stores combine() and rescale()

	A plot() function was also created which groups all the codes needed from reading input data to plotting final rescaled suitability map. The optimisation of the software (compared to ss3) resulted in a difference of -0.02 seconds from reading the file to plotting the final map (plots of interim maps have been excluded).

5. DEVELOPMENT OF GUI (ss5)

	For the development of the GUI, the Tkinter module was used. This interface allows users to select the weights from 1-10 for each suitability factor using sliders. The software calculates and plots rescaled suitability maps. Changes can be seen on the go. The function update() retrieves the different user-applied weights from sliders and calls for the plot() function which then plots the output on the GUI. The value of each weight is shown on the GUI for user's reference. The GUI also allows user to save the output map as .jpg in the .../.../data/output folder. 


CHALLENGES

The following were among the challenges encountered while developing this software:

1. Manipulating list of lists using zip() function - this led to an incorrect calculation in combining the weighted factors and subsequently caused the final map not to be displayed correctly or even unable to be displayed. This error was not identified earlier as testing was done on only one set of weights. The error was identified when different sets of weights were used for plotting and no change was observed in the plots.  

2. Programming the software to retrieve the weights from scales which are called into the plot() function - the initial plot() function called for more variables like input data. The codes were revised several times to only have the weights as variables.

3. Management of GUI widgets and layout - the placement of codes for the widgets resulted in some widgets not being displayed. The codes for the widgets were finally arranged according to view from top to bottom. Additionally, adding the function figure.clear() ensured that the software cleared the earlier plot so that the new plot is visible.

4. Displaying suitable colorbar - the preferred colorbar for the suitability map is Red-Yellow-Green which is not available as a default colormap in the matplotlib library. The 'YlGn' colormap was chosen instead where Yellow represents low suitabililty and Green is high suitability.

5. Plot not displaying on GUI - this was due to two reasons. Firstly was because of the incorrect calculation mentioned previously. Secondly was due to the presence of two matplotlib plots. After removing the interim map, the final suitability map was successfully displayed.
   	

FURTHER IMPROVEMENTS

1. Colorbar colormap - to have the preferred visualisation of the output, a customised colormap will need to be developed which is Red-Yellow-Green and data statistically classified into the different colors with Red being low suitability and Green being high suitability. 

2. Explore other python modules like pandas or numpy - as an alternative to using loops.

3. Develop a code and widget on the GUI to source input data from other files. 

4. Develop a code for Save() function to rename the output image based on weights applied.


REFERENCES

* Main reference used for the development of this software was from the module's learning page by Turner, A., 2023. https://agdturner.github.io/GEOG5990/home/index.html
* Matplotlib documentation. https://matplotlib.org/
* Tkinter documentation. https://docs.python.org/3/library/tkinter.html
* Stack Overflow forum. https://stackoverflow.com/
* GitHub. https://github.com/


ACKNOWLEDGEMENTS

I would like to thank the module leader, Andy Turner for the guidance and support throughout the course of the module and the development of this software as part of the module's project.



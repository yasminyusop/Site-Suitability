# Site-Suitability

INTRODUCTION

The following codes have been developed as part of the GEOG5990 Programming for Geographical Information Analysis: Core Skills of the University of Leeds. The objective is to develop a software to identify site suitability based on three factors: geology, population and transportation.  

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

data/input 
data/ouput
src/ss1
src/ss2
src/ss3
src/ss4
src/ss5
LICENSE
README

SOFTWARE DEVELOPMENT

The development of the software was divided into five parts: 
	1. Reading and plotting of 3 raster data (factors).
	2. Applying weights on each factor then combining them to generate a site 		suitability map, rescaled to (0,255).
	3. Displaying of the final map and writing into files.
	4. Code optimisation and simplification.
	5. Development of GUI

Every set of codes were built on the previous one with adjustments and improvements.

challenge:
re write code to address get weight value from slider
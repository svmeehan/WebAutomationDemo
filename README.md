This project will explore how we can automate business processes using Selenium. Obviously writing an API to perform these tasks would be a more sensible option but development time is expensive.

When complete this project will demonstrate the automation of a process in Selenium along with leveraging AWS to scale this process using Lambda.

This simple example will be built to perform a simple task which can later be modified to allow for automated testing (both functional and load). 

To use the convert.py script:

On the command line use the following commands:

1. pip install Selenium

	This will install the requirements (These should be added in a requirements file at some oint)

2. python convert.py 100 USD EUR
	
	This will convert 100 US Dollars into Euros and print the result to screen. Any three digit currency codes should work although this is not well tested.


## CS 4485 Team 3 Degree Planning and Audit Tool Project 

### Installation Instructions for Window Computers:
1. Download *[Box Drive](https://www.box.com/resources/downloads)* for Windows
- Instructions on how to install it *[here](https://support.box.com/hc/en-us/articles/360043697474-Installing-and-Updating-Box-Drive)*
- *Box* does not support having both *Box Sync* and *Box Drive* installed on your computer, so uninstall *Box Sync* if you have that first
2. Sign in to *Box Drive* with your UTD email (if *Box* asks for a email), then your UTD *Box* login information (i.e. netid and password)
- Installation is successful if you see *Box* as an option in the side menu of your *File Explorer* desktop application

### Usage Instructions For Window Computers
- The *Browse Files* button is used to select which file (i.e. transcript) the tool is going to get information from and use
- When selecting a file, if you can't find the file you need, try changing the file type to *All Files* in the bottom right drop down menu of the *File Explorer* window
- Once file is selected, the information will then be captured/scraped by the tool

### Installation Instructions for Developers (This is for if you're using a Windows Computer)
- Maintain *requirements.txt* file with any new dependencies
- To generate a new *requirments.txt* file, do the following:
  1. Install the *pipreqs* package via pips by going into *Command Prompt* and entering; 
  ```
  pip install pipreqs
  ```
  2. After installation, copy the path to the project folder, whose dependencies you want to generate a *requirements.txt* file for, and paste it in *Command prompt* after typing in `pipreqs` , as shown here: 
  ```
  pipreqs TypeFolderPathHere
  ```
  3. If a *requirements.txt* file is generated, you'll see a success message in Command Prompt

- To install packages using the *requirement.txt* file instead of manually doing so: 
  1. If you're using a virtual environment, then have it open
  2. Go to the directory where your *requirements.txt* file is located.
  3. If you're in the mentioned directory, run the following command by entering it in *Command Prompt* and the press enter:
  ```
  pip install -r requirements.txt
  ```
  4. If you aren't in the mentioned directory, where your *requirements.txt* file is located, then enter into *Command Prompt*:
  ```
  pip install -r TypePathTorequirements.txtFileHere
  ```
- To make the button work remember to: 
1. add in the class name of the file you want to display to the for loop in degreeApp.py
2. add to the top of the file "from insertYourFileNameHere import yourClassNameHere" as needed



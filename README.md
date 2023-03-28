## CS 4485 Team 3 Degree Planning and Audit Tool Project 

### Installation Instructions for Window Computers:
1. Download *[Box Drive](https://www.box.com/resources/downloads)* for Windows
- Instructions on how to install it *[here](https://support.box.com/hc/en-us/articles/360043697474-Installing-and-Updating-Box-Drive)*
- *Box* does not support having both *Box Sync* and *Box Drive* installed on your computer, so uninstall *Box Sync* if you have that first
2. Sign in to *Box Drive* with your UTD email (if *Box* asks for a email), then your UTD *Box* login information (i.e. netid and password)
- Installation is successful if you see *Box* as an option in the side menu of your *File Explorer* desktop application

### Usage Instructions For Window Computers
- The "Start" button on the homepage is used to direct the user to the Upload File page after it is clicked
- The Upload File page has a "Browse Files" button that will open up File Explorer upon being clicked
- The *Browse Files* button is used to select which file (i.e. transcript) the tool is going to get information from and use
- When selecting a file, if you can't find the file you need, try changing the file type (located in the bottom right drop down menu of the *File Explorer* window) to *All Files* 
- Once the file is selected, the information will then be captured/scraped by the tool, and the name of the file will be displayed on the screen

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

- If the previous/next page button you made isn't working, then check to see if you have the following added: 
  1. Add to the () of the *For Loop* located in *degreeApp.py*: the Class Name of the file you want displayed as a page in the application 
  2. Add to the top of the *degreeApp.py* file: 
  ```
  from insertYourFileNameHere import InsertYourClassNameHere
  ```
  3. Make sure that in the *Command* section of your Button, the Class Name, that you want the button to go to, is enclosed in ""
  ```
  button_example = ttk.Button(
              self,
              text="InsertButtonNameHere",
              command=lambda: self.controller.show_frame("InsertClassNameHere")
              )
  ```



# Shuttle Stop Crowd Ranker

## Chosen Problem
This app helps decide where to send an extra campus shuttle by ranking stops from least to most crowded. Essentially how this works is the user enters a list of shuttle stops with crowd estimates, and then the app sorts them by crowd count using Merge Sort.

## Chosen Algorithm
**Merge Sort** - I chose Merge Sort because it works by splitting the list in half repeatedly, sorts each half, and then it merges it back together in order, and so this fits this problem well because it can handle any size list reliably and each merge step is easy to show to the user visually. Also, it does not rely on the data being partially sorted already, which makes it a good choice for any set of shuttle stops because in real life nobody is going to take the time to sort each stop from least to most crowded so the app needs to work with that in mind.

## Demo


## The Four Pillars of Computational Thinking

**Decomposition:**
1. Read the user's input line by line
2. Split each line into a stop name and a crowd number
3. Validate that the crowd number is actually a number
4. Now run merge sort on the list
5. Record each merge step
6. Finally, display the steps and the final ranking to the user

**Pattern Recognition:**
Merge Sort keeps on splitting the lists in half and merging them back together. Every single merge does the same thing, it compares the first term of two lists, takes the smaller one, and repeats that until one list is empty. Then it attaches whatever is left to the final list.

**Abstraction:**
- The parts that will be shown to the user are each merge step showing the order of stops after each merge, and then the final ranking with a recommendation of which stop needs the extra shuttle
- The parts that is hidden to the user is the internal recursion calls, the index tracking variables so the i and the j in the code,and the splitting phase because only the merging step is where the actual sorting actually happens
- The app does NOT care about where the bus is going as long as it is in the format of the stop, crowd number.

**Algorithmic Design:**
- Input: the user types in the stop names and crowd numbers into a text box when prompted, and there is only one entry per line
- Process: the app makes sure the input is in the proper format, and it runs merge sort, and then it records each merge step to be outputted later
- Output: the output is each step in one box and the final ranking, plus the shuttle recommendation in another box so it is visually appealing and organized for the user

**Flowchart:**


## Steps to Run:
1. First make sure that Python is installed because I will be using VS Code
2. Create a project folder and then open a terminal in that folder
3. Run 'py -m pip install gradio' to install gradio
4. After I write the code I will run 'py app.py' to get a demo launch link
5. Open the link in my browser and test and debug based off the results

## Hugging Face Link
* 

# Sources and AI Acknowledgement:**
- Merge Sort code concept reviewed from course notes on OnQ
- https://www.datacamp.com/tutorial/gradio-python-tutorial
- https://www.youtube.com/watch?v=MJgHs9cvbfA
- https://www.w3schools.com/colors/colors_picker.asp
- Used Gemini to help me format it in Gradio to make it look nicer: https://gemini.google.com/app/f8df4665924e89c1
- https://gemini.google.com/app/f8df4665924e89c1



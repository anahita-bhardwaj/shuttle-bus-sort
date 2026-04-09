import gradio as gr

def merge_sort_steps(arr, steps, start = 0):
    #this function basically records every step of the sort, so that we can show it to the user!
    if len(arr) <= 1:
        return arr
    #the if statement above is the base case, which shows that a list of 1 item or even 0 items is already sorted

    #now we have to split the list in half:
    mid = len(arr) // 2
    left = arr[ : mid]
    right = arr[mid : ]

    #now we have to sort each half by having the function call itself over and over until the lists are of size 1
    left = merge_sort_steps(left, steps, start)
    right = merge_sort_steps(right, steps, start + mid)

    #so now, we have to merge the two halvs back together and we do this by defining an empty list and then implementing a while loop
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        #so now basically what we do is we compare the crowd counts, and then take the smaller one first
        if left[i][1] <= right[j][1]:
            merged.append(left[i])
            i  = i + 1
        else:
            merged.append(right[j])
            j = j + 1
    
    #so now we just add any remaining items like so:
    merged = merged + left[i : ]
    merged = merged + right[j : ]

    #but because we need to show these steps we have to save them so that we can show it later
    steps.append(list(merged))

    return merged

#now,we need a function that runs when the user clicks sort
def sort_stops(input_text):
    #first we have to check if the user typed in anything
    if not input_text.strip(): #gets rid of extra spaces inputted by the user
        return "Please enter at least one stop."
    
    stops = []
    #now we have to make sure that the system reads each line inputted by the user

    lines = input_text.strip().splitlines()
    print(lines)
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        #the formatting for each line should be stop, name, crowd number
        parts = line.split(",")
        if len(parts) != 2:
            return f"Error: This line is not in the right format: '{line}'\nPlease use: Stop Name, crowd number",""
    
        stop_name = parts[0].strip()
        crowd_str = parts[1].strip()

        #now we have to make sure that the crowd count is actually a number
        if not crowd_str.isdigit():
            return f"Error: '{crowd_str}' is not a valid number. Please enter whole numbers only.",""
    
        crowd_count = int(crowd_str)
        stops.append((stop_name, crowd_count))

    #but to sort, we need at least two stops to sort
    if len(stops) < 2:
        return "Please enter at least 2 stops to sort.",""
    
    #now we run merge sort adn then collect each stop into the list:
    steps = []
    final_sorted = merge_sort_steps(stops, steps)

    #now we have to build the step by step output text
    steps_text = "--- Sorting Steps ---\n\n" #I added dashes so it looks nicer and aesthetic!!
    step_num = 1
    for step in steps:
        steps_text = steps_text + f"Step {step_num} (merging {len(step)} stops):\n"
        for stop in step:
            steps_text = steps_text + f"{stop[0]} - crowd: {stop[1]}\n"
        steps_text = steps_text + "\n"
        step_num = step_num + 1

        #Now we have to code the final result text
    result_text = "--- Final Ranking (from the least to the most crowded) ---\n\n"
    rank = 1
    for stop in final_sorted:
        result_text = result_text + f"{rank}. {stop[0]} - crowd: {stop[1]}\n"
        rank = rank + 1

    result_text = result_text + "\n\nSend the extra shuttle to: " + final_sorted[-1][0] + " (most crowded stop!)"

    return steps_text, result_text


#now for the fun part, we customize the user interface (UI) using gradio to make it look all nice!
with gr.Blocks(title = "Shuttle Stop Crowd Ranker", theme = gr.themes.Soft(
    primary_hue = "fuchsia",
    secondary_hue = "slate",
    neutral_hue = "zinc",
    font = gr.themes.GoogleFont("Montserrat"))
) as demo:
    gr.HTML("""<style>
            .gradio-container {
                background-color: #ffe6ff !important;
            }
            h1, h2, h3 {
                color: #ff1aff !important;
            }
            p, label, textarea {
                color: #ff80ff !important;
            }
            </style>""")
    gr.HTML("<h2 style='color: #6a0dad !important;'>Shuttle Stop Crowd Ranker</h2>")
    gr.HTML("<p style='color: #333333 !important;'>This app uses <strong style='color: #6a0dad !important;'>Merge Sort</strong> to rank campus shuttle stops by crowd size, so that you know where to send the extra shuttle!</p>")
    gr.HTML("<p style='color: #333333 !important;'><strong style='color: #6a0dad !important;'>How to use:</strong> Type one stop per line in this format: 'Stop Name, crowd number'</p>")
    gr.HTML("<p style='color: #333333 !important;'><strong style='color: #6a0dad !important;'>Example:</strong><br>Division St, 45<br>Union St, 12<br>Queen's Arc, 78<br>Stauffer Library, 30</p>")
    input_box = gr.Textbox(
        label = "Enter shuttle stops (one per line: Name, crowd count)",
        placeholder = "Division St, 45\nUnion St, 12\nQueen's Arc, 78\nStauffer Library, 30",
        lines = 6
    )

    sort_button = gr.Button("Sort Stops")

    step_output = gr.Textbox(label = "Step by Step Sorting Process", lines = 15)
    final_output = gr.Textbox(label = "Final Result", lines = 8)

    sort_button.click(fn = sort_stops, inputs = input_box, outputs = [step_output, final_output])

    demo.launch()
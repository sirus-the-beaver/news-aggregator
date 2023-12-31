import PySimpleGUI as sg
from cnn_scraper import search

# Create the GUI
description = "This program will search CNN for the most recent article containing the search term and display the headline, timestamp, and text of the article.\n"
description += " If no article is found, the program will display an error message.\n"
description += " If the article does not have any text, the program will display a message saying so.\n"
description += " If the article cannot be loaded, the program will display an error message.\n"
description += " The program will close when the user closes the window.\n"
description = sg.Text(description, font=('Arial Bold', 20), expand_x=True, justification='center')
l1 = sg.Text('Please enter a search term: ', key='-OUT-', font=('Arial Bold', 20), expand_x=True, justification='center')
t1 = sg.Input('', enable_events=True, key='-INPUT-', font=('Arial Bold', 20), expand_x=True, justification='left')
b1 = sg.Button('Search', key='-SEARCH-', font=('Arial Bold', 20), bind_return_key=True)
l2 = sg.Text('', key='-HEADLINE-', font=('Arial Bold', 20), expand_x=True, justification='left')
l3 = sg.Text('', key='-TIMESTAMP-', font=('Arial Bold', 20), expand_x=True, justification='left')
l4 = sg.Multiline('', key='-OUTPUT-', font=('Arial Bold', 15), expand_x=True, justification='left', size=(100, 50))
layout = [[description],[l1], [t1], [b1], [l2], [l3], [l4]]

# Create the window
window = sg.Window("News Aggregator", layout, size=(1420, 780), resizable=True)

# Create an event loop
while True:
    event, values = window.read()

    # End program if user closes window
    if event == sg.WIN_CLOSED:
        break

    elif event == '-SEARCH-':
        search_term = values['-INPUT-']
        results = search(search_term)

        if results is not None:
            headline = "CNN: "
            headline += results[0].get_text()
            text = results[2]

            # Create a string to display the results
            results_string = ''
            for result in text:
                results_string += result.text.strip() + '\n'

            window['-HEADLINE-'].update(headline)

            if results_string == '':
                window['-OUTPUT-'].update("This article does not have any text")

            else:
                timestamp = results[1].get_text()
                window['-TIMESTAMP-'].update(timestamp)
                window['-OUTPUT-'].update(results_string)
        else:
            window['-HEADLINE-'].update("No articles found or article could not be loaded")

window.close()
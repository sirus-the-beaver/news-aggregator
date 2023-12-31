import PySimpleGUI as sg
from cnn_scraper import search

l1 = sg.Text('Please enter a search term: ', key='-OUT-', font=('Arial Bold', 20), expand_x=True, justification='center')
t1 = sg.Input('', enable_events=True, key='-INPUT-', font=('Arial Bold', 20), expand_x=True, justification='left')
b1 = sg.Button('Search', key='-SEARCH-', font=('Arial Bold', 20))
l2 = sg.Text('', key='-HEADLINE-', font=('Arial Bold', 20), expand_x=True, justification='left')
l3 = sg.Multiline('', key='-OUTPUT-', font=('Arial Bold', 15), expand_x=True, justification='left', size=(100, 50))
layout = [[l1], [t1], [b1], [l2], [l3]]

# Create the window
window = sg.Window("News Aggregator", layout, size=(1420, 780))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    if event == sg.WIN_CLOSED:
        break

    elif event == '-SEARCH-':
        search_term = values['-INPUT-']
        results = search(search_term)
        headline = results[0]
        text = results[1]

        if results:
            # Create a string to display the results
            results_string = ''
            for result in text:
                results_string += result.text.strip() + '\n'

            window['-HEADLINE-'].update(headline)
            window['-OUTPUT-'].update(results_string)
        else:
            l2.update("No articles found")

window.close()
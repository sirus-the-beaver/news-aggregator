import PySimpleGUI as sg
from cnn_scraper import search_cnn
from npr_scraper import search_npr

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

l2 = sg.Text('', key='-LINK-', font=('Arial Bold', 20), expand_x=True, justification='center')
l3 = sg.Text('', key='-HEADLINE-', font=('Arial Bold', 20), expand_x=True, justification='center')
l4 = sg.Text('', key='-TIMESTAMP-', font=('Arial Bold', 20), expand_x=True, justification='center')
l5 = sg.Multiline('', key='-OUTPUT-', font=('Arial Bold', 15), expand_x=True, justification='left', size=(175,30))

l6 = sg.Text('', key='-LINK2-', font=('Arial Bold', 20), expand_x=True, justification='center')
l7 = sg.Text('', key='-HEADLINE2-', font=('Arial Bold', 20), expand_x=True, justification='center')
l8 = sg.Text('', key='-TIMESTAMP2-', font=('Arial Bold', 20), expand_x=True, justification='center')
l9 = sg.Multiline('', key='-OUTPUT2-', font=('Arial Bold', 15), expand_x=True, justification='left', size=(175,30))

layout = [[sg.Column([[description],[l1], [t1], [b1], [l2], [l3], [l4], [l5], [l6], [l7], [l8], [l9]], scrollable=True, vertical_scroll_only=True, size=(1900, 1000), element_justification='center')]]

# Create the window
window = sg.Window("News Aggregator", layout, size=(1900, 1000), resizable=True)

def display_cnn_article(results):

    if results is not None:
        headline = "CNN: "
        headline += results[0].get_text()
        text = results[2]

        # Create a string to display the results
        results_string = ''
        for result in text:
            results_string += result.text.strip() + '\n'

        window['-LINK-'].update(results[3])
        window['-HEADLINE-'].update(headline)

        if results_string == '':
            window['-OUTPUT-'].update("This article does not have any text")

        else:
            timestamp = results[1].get_text()
            window['-TIMESTAMP-'].update(timestamp)
            window['-OUTPUT-'].update(results_string)
    else:
        window['-HEADLINE-'].update("No articles found or article could not be loaded")


def display_npr_article(results):

    if results is not None:
        headline = "NPR: "
        headline += results[0].get_text()
        text = results[2]

        # Create a string to display the results
        results_string = ''
        for result in text:
            results_string += result.text.strip() + '\n'

        window['-LINK2-'].update(results[3])
        window['-HEADLINE2-'].update(headline)

        if results_string == '':
            window['-OUTPUT2-'].update("This article does not have any text")

        else:
            timestamp = results[1]
            window['-TIMESTAMP2-'].update(timestamp)
            window['-OUTPUT2-'].update(results_string)
    else:
        window['-HEADLINE2-'].update("No articles found or article could not be loaded")

# Create an event loop
while True:
    event, values = window.read()

    # End program if user closes window
    if event == sg.WIN_CLOSED:
        break

    elif event == '-SEARCH-':
        search_term = values['-INPUT-']

        cnn_results = search_cnn(search_term)
        display_cnn_article(cnn_results)

        npr_results = search_npr(search_term)
        display_npr_article(npr_results)

window.close()


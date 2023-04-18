# Large Text Summarizer
 For Intro to AI.

## Project 4 Proposal: 
### Authors: Jack Swingle and Brandon Westbrook
### Project type: Application
###Problem description: 
One of the common and powerful applications of the new large generative language models, such as GPT-3.5, is text summarization. However, one of the limitations of this technology in its current state is that GPT-3.5 has a character limit of 4096 characters, while the average 200-page book consists of around 300,000 characters. Therefore, using this model to summarize longer pieces of text, such as books or long articles is impractical.
### Solution:
We propose to create a program that can summarize large amounts of text, such as an entire book. This will be accomplished using an HTML/CSS/JavaScript front end and a Python web server backend. The front end will take a large text input and send it to the web server. The server will parse the text, splitting it into 2000-character chunks that the server will feed into the language model to be summarized. The server will put the resulting summary into an intermediary file. Then this intermediary file, if it is still above the word count, will be chunked and summarized again. This process will repeat until the summary gets to the desired length. The server will then return the summary to the front end.

### Timeline:
By April 17:

	Create git repo. (Jack)
	Plan project structure and delegate tasks. (Both)
	Research possible Python web server frameworks. (Jack)
By April 21:

	A basic front-end application that can take input. (Brandon)
	A basic Python web server that can summarize small inputs. (Jack)
By April 24:

	Connect the front and back end with API requests. (Jack)
	Add chunking abilities to the Python web server. (Brandon)
By April 28:

	Polish look of the front end. (TBD)
	Add options for different summary lengths. (if time permits) (TBD)
	Bug testing and general polish and tweaks. (TBD)



import pywhatkit as av

txt = """Most people love the recommendation of a documentary worth watching. 
Here is the list of Indian documentaries to watch on various OTT platforms."""

av.text_to_handwriting(txt,"hand_writing.png")
print('end')

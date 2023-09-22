Name: Marcela Vijil 
How many hours did it take you to complete this assignment? 5
Did you collaborate with any other students/TAs/Professors? No
Did you use any external resources? (Cite them below)
https://mathspp.com/blog/custom-json-encoder-and-decoder

Project includes a source folder with python code for an encoder and decoder for json. There are also functions for json dump and json load: 
def json_dump(obj):
        return json.dumps(obj, cls=MyEncoder)

    def json_load(obj):
        json.loads(json_dump, cls=MyDecoder)

I've included several tests in the test directory to show the functionality of the code. 
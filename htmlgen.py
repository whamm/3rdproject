LIST_OF_CONCEPTS = [['General Bits of Information', 'Html = hyper text markup language'], ['', 'HTML has sideways triangles which are opening and closing in developer mode and in these you can see what is nested inside of the previous element'], ['', 'HTML gives structure to the web'], 
['', 'Everything on the web is a box'], ['', 'When working in HTML think from big to small in terms of containers'], ['Tags', 'a for anchor tags and use href for the link'], ['', 'img for image tags and use the src attribute'], ['', 'br for line break'], ['', 'b for bold'], ['', 'em for italics'], ['', 'p for paragraph'],
['', 'div for dividing your page into boxes'], ['', 'span for applying css inline'], ['Elements', 'There are inline tags and block tags. Inline does not affect spacing and block tags have an invisible box around them'], ['', 'Elements have opening and closing tags(not all though) with content between'],
['Boxes', 'Box structure goes from content&gt;padding&gt;border&gt;margin'], ['', 'Border and padding are affected by the background color'], ['', "<a href='http://assignments.udacity-extras.appspot.com/courses/html-css/samples/box-model.html'>Box Model Demo</a>"],
['', 'Using display: flex can make it so divs(boxes) can be next to each other'], ['Misc CSS Info', 'CSS stands for Cascading Style Sheet'], ['', 'You can use CSS to assign styles to your HTML'], 
['', 'Look for opportunities to apply styles and settings to larger chunks of html at first rather than repeat yourself in many different areas of a pages css. When you repeat too often you are likely to make mistakes'],
['Misc', 'Use Sublime Text 2. It automates some work and helps you keep track of things better'], ['', 'HTML is what is used for all webpages'], ['', 'HTTP is the protocol the internet uses the most'], ['', 'The internet/cloud is the biggest network in the world'], ['', 'You can see the shapes of elements with developer tools in your browser'],
['Programming', 'Computers can do many things very well as long as you give them one step at a time. Programs tell computers what to do in steps and programs are concise sequences of steps'], ['', 'Python is an interpreter language and an interpreter language directly executes instructions written in code without compiling'],
['', 'Programming has grammar just like english. There are correct and incorrect ways of saying things'],
['', 'An expression is something that has a value'], ['', 'An equal sign in math means equals but in a programming an equal sign means assignment. Assigning the value of the right side to the left'], 
['Types and Variables', 'A variable in python is a box that can hold a value that is assigned to it Assigning a variable is as simple as declaring example = 9 or more complicated as example2= 1 + 3 858 - 351'],
['', 'Assigning the value of the right side to the left and variables can be useful when you need to store a value that will be referenced multiple times or will be changing throughout a program'], ['', 'Variables can be numbers and strings Numbers and strings are two different data types and generally cannot be used in equations'],
['', 'A variable in is a box that can hold a value that is assigned to it. Assigning a variable is as simple as declaring example = 9 or more complicated as example2= 1 + 3 858 - 351'], ['', 'Variables can be numbers and strings. Numbers and strings are two different data types and generally cannot be used in equations'], 
['Functions', 'A function is a block of code that take an argument that is input when you call it and executes that against the block of code within the function'],
['','You must create a function to use it. When making it, it requires you name it with def, give the function parameters it will operate on later, and code to run the parameter against'], ['', 'When using a function you generally have to pass it the required arguments that it then executes against its code block'],
['', 'Functions can be called repeatedly so you can implement it in multiple spots throughout a larger project. This makes it so you are able to more flexibly reuse the same code over and over'], ['', 'You must always have a return statement otherwise nothing will happen with your function'],
['Programming Logic', 'You will want to think about orders of operation when using if statements'], ['', 'Else statements will have a code block execute when your if statement that preceded it did not evaluate true'], ['', 'While loops execute similar to if statements except execute over and over as long as the statement in the while loop proofs to true'],
['', 'For loops look at each item in a list that you can then have a code block execute against'], ['Troubleshooting', 'Debugging can be assisted by printing functions out at different points where they execute or variable output if code is behaving not as expected'],
['', 'Use errors message to give you more information about issues you many be having with your code'], ['', 'Use example code and change it to be useful in yours'], ['', 'Keep old versions of code to compare against']]

def generate_concept_HTML(concept_title, concept_description):


    if len(concept_title) != 0:

        html_text_1 = '''
        </ul>    
    <div/>    
    <div>
        <h3 class="subheading">
            ''' + concept_title        
        html_text_2 = '''
        </h3>
        <ul>
            ''' + '<li>' + concept_description + '</li>' + '''
            '''
#        html_text_3 = if     
    else:
        html_text_1 = ''        
        html_text_2 = '<li>' + concept_description + '</li>' + '''
        '''
#        </ul>
#        </div>
    full_html_text = html_text_1 + html_text_2
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print make_HTML_for_many_concepts(LIST_OF_CONCEPTS)




    
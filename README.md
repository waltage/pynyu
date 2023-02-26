# Python Library `pynyu`

A set of python modules and functions designed by current/former MS Computer Science students to help make the lives of those that come after us 'maybe' just a little bit better

### Project Genesis

The courses 'Foundations' (Discrete Math) and 'Algorithms 1' can be especially challenging for students that are less theoretically-minded when they start the program. Certainly, by the end of the program, these concepts come a little more naturally, but it felt like each individual student was sinking hours upon hours of work on baseline topics and maybe we can help reduce some of that for future generations.

Two key examples come to mind: Combinatorics, and Red Black Trees. I desparately searched for some type of a library that would allow for a better programmer abstraction around the various topics in combinatorics -- an intuitive interface that would allow for word problems like "90 children show up at a theme park with 12 roller coasters and they group up 8 at a time and half of them aren't tall enough for half the rides, how many different ways are there for ... blah blah blah" to be encoded, and then step-by-step outputs that explained how the concepts came together. For algorithms, CLRS is kind of a nightmare when it comes to mixing different programming paradigms -- I just wanted a simple abstract Red Black Tree ... that had unit tests ... and had insert/delete fully implemented (correctly)... and that had various pre/post insert/rotate/delete hook methods so I could extend them for order statistics (without having to write a whole new implementation)... and holy cow does having graphviz integration help.

This is an evolving project, and maybe it won't get that much traction, but please feel free to contribute questions/issues/code/algorithms/topics that were or are a huge time-suck for your studies, and let's see if we can get you all some better school-life balance :)

## Usage

This library is/will be available from pypi so that a simple `pip3 install pynyu` will provide access to the library. If you're an end-user, and not trying to contribute to the project, that's where you can start.

## Contributing 
If you're interested in contributing, clone or fork this repository, and use the bootstrap `start_venv.sh` to get started. This will setup all of the necessary virtual environment dependencies, and will setup some VSCode configuration + pre-commits that we use with the project to keep things nice and tidy.

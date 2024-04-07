

# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [graphviz](https://graphviz.org/), an open source graph visualization software that outputs, among others, svg files.

# Using the graphviz image in Linux

Before using the graphviz image, you must prepare the file containing the instructions for building the graph as pairs of objects. For instance, you may create a file named graph.py, with executable permissions, with the following lines of code:

`import graphviz`

`dot = graphviz.Digraph('Graph')`

`dot.edge('pegi3s', 'says')`

`dot.edge('says', 'Hello')`

`dot.edge('Hello', 'World')`

`dot.edge('Hello', 'User')`

`dot.format = 'svg'`

`dot.render(directory='/data').replace('\\', '/')`

Then, you should adapt and run the following command: 
`docker run --rm -v /your/data/dir:/data pegi3s/graphviz bash -c "python3 /data/graph.py"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the graph.py file.

The software version can be obtained using the following command: 
`docker run --rm -v /your/data/dir:/data pegi3s/graphviz bash -c "dot -V"`

The implemented graphviz version is: 2.43.0

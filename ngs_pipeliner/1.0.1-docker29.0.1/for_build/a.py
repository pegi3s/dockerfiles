from main import parse_pipeline
import graphviz
import re

parameters, pipeline = parse_pipeline('/mnt/c/Users/jorge/Documents/Estancia/Pipelines/PCP/PCP+haplogrep+vcf_snps')

def generate_schematics(pipeline):
    schema = graphviz.Digraph(comment='Pipeline')
    schema.format = 'png'
    schema.node('Input files', 'Input files')
    for step in pipeline:
        schema.node(step,step)

    edges = set()
    for step in pipeline:
        inputs_outputs = pipeline[step]['with_var_inputs_outputs']
        inputs = list()
        for el, val in inputs_outputs.items():
            if 'input' in el:
                try:
                    input = re.findall('@{.*?}', val)[-1].replace('@{','').replace('}','')
                    inputs.append(input)
                except:
                    pass
        for el in inputs:
            if el == 'Parameters.filename':
                edges.add(f'Input files>>>{step}')
            else:
                for step1 in pipeline:
                    if step1 == el.split('.')[0]:
                        edges.add(f'{step1}>>>{step}')
    
    for edge in edges:
        edge = edge.split('>>>')
        schema.edge(edge[0],edge[1])
    
    schema.format = 'svg'
    schema.render('pipeline_schema',cleanup=True)
    schema.format = 'png'
    schema.render('pipeline_schema',cleanup=True)

generate_schematics(pipeline)
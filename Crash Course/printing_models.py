import printing_functions as pf

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_model(unprinted_designs)
for unprinted_design in unprinted_designs:
    print(unprinted_design)
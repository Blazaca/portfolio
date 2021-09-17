def print_model(unprinted_designs):
    completed_models = []

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

    for completed_model in completed_models:
        print(completed_model)

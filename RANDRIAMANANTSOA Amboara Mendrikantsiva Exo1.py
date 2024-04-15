from itertools import product

def truth_table(variables, expression):
    num_vars = len(variables)
    truth_table_header = '|'.join(variables) + '| Output'
    print(truth_table_header)
    print('-' * len(truth_table_header))
    
    for combination in product([0, 1], repeat=num_vars):
        var_dict = dict(zip(variables, combination))
        output = eval(expression, var_dict)
        row = '|'.join(str(val) for val in combination) + f'| {output}'
        print(row)

def to_canonical_forms(variables, expression):
    canonical_forms = []
    
    for output in [0, 1]:
        minterms = []
        maxterms = []
        for combination in product([0, 1], repeat=len(variables)):
            var_dict = dict(zip(variables, combination))
            if eval(expression, var_dict) == output:
                minterm = ''.join(['-' if val == 0 else var for val, var in zip(combination, variables)])
                maxterm = ''.join([var if val == 0 else '-' for val, var in zip(combination, variables)])
                minterms.append(minterm)
                maxterms.append(maxterm)
        if minterms:
            canonical_forms.append(('Canonical Minterms' if output == 1 else 'Canonical Maxterms', minterms))
    
    for form, terms in canonical_forms:
        print(f'\n{form}:')
        print(', '.join(terms))

# Exemple d'utilisation :
variables = ['A', 'B', 'C']
expression = "(A and B ) or (not C)"

truth_table(variables, expression)
to_canonical_forms(variables, expression)
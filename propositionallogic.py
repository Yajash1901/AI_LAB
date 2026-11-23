import itertools
import re


def evaluate(expr, model):
    """
    Evaluate a propositional logic expression under a given model.
    Supported operators:
    ~ : NOT
    ^ : AND
    v : OR
    ->: IMPLIES
    <->: BICONDITIONAL
    """
    # Replace biconditional and implication first
    expr = expr.replace("<->", " == ")  # Biconditional: A <-> B is A == B
    expr = expr.replace("->", " <= ")  # Implication: A -> B is A <= B
    # Replace negation (~) with explicit parentheses (not X)
    expr = re.sub(r"~(\w+)", r"(not \1)", expr)  # ~P becomes (not P)
    expr = re.sub(r"~\(([^)]+)\)", r"(not (\1))", expr)  # ~() becomes (not ())
    # Replace AND and OR
    expr = expr.replace("^", " and ")  # ^ becomes 'and'
    expr = expr.replace("v", " or ")  # v becomes 'or'
    # Replace symbols with their boolean values in the model
    for sym, val in model.items():
        expr = re.sub(r"\b" + re.escape(sym) + r"\b", str(val), expr)
    # Evaluate the final Python boolean expression
    return eval(expr)


def tt_entails(kb, query, symbols):
    """
    Truth-table enumeration to check if KB entails Query.
    Prints the truth table and returns True if entails, else False.
    """
    entails = True
    models = list(
        itertools.product([True, False], repeat=len(symbols))
    )  # Generate all possible models
    # Print the header of the truth table
    print("Truth Table Evaluation:\n")
    header = " | ".join(symbols) + " | KB | Query | KB ⇒ Query"
    print(header)
    print("-" * len(header))  # Line separator
    # Iterate through all possible models (truth assignments)
    for values in models:
        model = dict(zip(symbols, values))  # Create a model as a dictionary
        kb_val = evaluate(kb, model)
        query_val = evaluate(query, model)
        implication = (not kb_val) or query_val  # KB ⇒ Query (implication logic)
        # If KB is True and Query is False, then it does not entail the query
        if kb_val and not query_val:
            entails = False
        # Print the current row of the truth table
        row = " | ".join(["T" if v else "F" for v in values])
        row += (
            f" | {'T' if kb_val else 'F'} | {'T' if query_val else 'F'} | "
            f"{'T' if implication else 'F'}"
        )
        print(row)
    # Print the final result of the entailment check
    print("\nResult:")
    if entails:
        print("The Knowledge Base entails the Query (KB ⊨ Query)")
    else:
        print("The Knowledge Base does NOT entail the Query (KB ⊭ Query)")


kb = "(A v C) ^ (B v ~C)"  # Knowledge Base (A OR C) AND (B OR NOT C)
symbols = ["A", "B", "C"]
queries = ["A", "C", "A -> B", "B v C"]

# Evaluate each query using the truth-table method
for query in queries:
    print(f"\nEvaluating Query: {query}\n")
    tt_entails(kb, query, symbols)
    print("\n" + "=" * 50 + "\n")
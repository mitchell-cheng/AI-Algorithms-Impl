from typing import List, TypedDict

percepts: List = []
table: TypedDict = {
    "clean": "do nothing",
    "dirty": "clean"
}

# helper functions
def lookup(percepts: List, table: TypedDict):
    if percepts[-1] in table:
        return table[percepts[-1]]
    else:
        return None
    
def interpreter_input(percept: str) -> str:
    return percept

def rule_match(state: str, rules: TypedDict) -> str:
    if state in rules:
        return rules[state]
    else:
        return None    

def transaction_model():
    pass

def sensor_model():
    pass

def update_state(state, action, percept, transaction_model, sensor_model):
    pass

class Rule:
    def __init__(self, action):
        self.action = action

# agent programs

def table_driven_agent(percept: str) -> str:
    '''
    table driven agent program perceives current state and returns a action
    '''
    percepts.append(percept)
    return lookup(percepts, table)

rules: TypedDict = {
    "clean": Rule("Do nothing"),
    "dirty": Rule("Clean")
}

def simple_reflex_agent(percept: str) -> str:
    '''
    reflex agent only perceive current state while ignore the historical states
    '''
    state = interpreter_input(percept)
    rule = rule_match(state, rules)
    action = rule.action
    return action

def model_based_reflex_agent(percept: str) -> str:
    '''
    model-based agents use transaction and sensor model
    '''
    state = update_state(state, action, percept, transaction_model, sensor_model)
    rule = rule_match(state, rules)
    action = rule.action
    return action

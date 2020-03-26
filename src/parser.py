import ply.yacc as yacc
import sys


"""   

Root : Behaviour Defs DOUBLEPERCENTAGE Code 
    | Defs Behavior DOUBLEPERCENTAGE Code

Behaviour : BEHAVIOUR LEFTBRACKET Node RIGHTBRACKET

Node: Sequence,
      Selector,
      Prob_Selector,
      Parallel,
      Decorator,
      Condition,
      Action


Nodes : Nodes COMMA Node
      | Node

Node : ControlFlowNode
     | ExecutionNode

ControlFlowNode : Sequence
                | Selector
                | ProbSelector
                | Parallel
                | Decorator

ExecutionNode : Action
              | Condition


Sequence : SEQUENCE COLON LSQBRACKET Nodes RSQRBRACKET
         | SEQUENCE COLON VarName

Selector : SELECTOR COLON LSQBRACKET Nodes RSQRBRACKET
         | SELECTOR COLON VarName

ProbSelector : PROB_SELECTOR COLON LSQBRACKET ProbNodes RSQRBRACKET
             | PROB_SELECTOR COLON VarName
            
Parallel : PARALLEL COLON LSQBRACKET Nodes RSQRBRACKET
         | PARALLEL COLON VarName

Decorator : DECORATOR COLON LSQBRACKET PolicyNode RSQRBRACKET
          | DECORATOR COLON VarName

Parallel : PARALLEL 

ProbNodes : ProbNodes COMMA ProbNode
          | ProbNode

ProbNode : VarName RIGHTARROW Node

PolicyNode : POLICY COLON Policy COMMA Node

Policy : INVERTER
       | MAX_TRIES LEFTPARENTHESIS INT RIGHTPARENTHESIS
       | MAX_SECONDS LEFTPARENTHESIS INT RIGHTPARENTHESIS


Action : ACTION COLON VarName

Condition : CONDITION COLON VarName

VarName : DOLLAR NODENAME


Sequence : SEQUENCE COLON LSQRBRACKET Node RSQRBRACKET
         | SEQUENCE COLON DOLLAR NODENAME

Defs : Defs NodeDef
      &

NodeDef : SequenceDef,
        | SelectorDef,
        | ProbSelectorDef,
        | ConditionDef,
        | ActionDef
         
SequenceDef : SEQUENCE NODENAME LSQRBRACKET Nodes RSQRBRACKET

Nodes : Nodes COMMA Node
        &
 
""" 

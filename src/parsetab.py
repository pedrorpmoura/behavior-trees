
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "ACTION BEHAVIOR CODE CONDITION DECORATOR DOUBLEPERCENTAGE INT INVERTER MAXSECONDS MAXTRIES PARALLEL PROBSELECTOR RIGHTARROW SELECTOR SEQUENCE VAR\n    root : behavior CODE\n    \n    root : behavior definitions CODE\n    \n    root : definitions behavior CODE\n    \n    behavior : BEHAVIOR ':' '[' node ']'\n    \n    node : SEQUENCE ':' '[' nodes ']'\n    \n    node : SEQUENCE ':' VAR\n    \n    node : SELECTOR ':' '[' nodes ']'\n    \n    node : SELECTOR ':' VAR\n    \n    node : PROBSELECTOR ':' '[' prob_nodes ']'\n    \n    node : PROBSELECTOR ':' VAR\n    \n    node : PARALLEL ':' INT '[' nodes ']'\n    \n    node : PARALLEL ':' VAR\n    \n    node : DECORATOR ':' INVERTER '[' node ']'\n    \n    node : DECORATOR ':' VAR\n    \n    node : DECORATOR ':' MAXTRIES '[' node ']'\n    \n    node : DECORATOR ':' MAXSECONDS '[' node ']'\n    \n    node : CONDITION ':' VAR\n    \n    node : ACTION ':' VAR\n    \n    nodes : nodes ',' node\n          | node\n    \n    prob_nodes : prob_nodes ',' prob_node\n               | prob_node\n    \n    prob_node : VAR RIGHTARROW node\n    \n    definitions : definitions definition\n               | definition \n    \n    definition : SEQUENCE VAR ':' '[' nodes ']'\n    \n    definition : SELECTOR VAR ':' '[' nodes ']'\n    \n    definition : PROBSELECTOR VAR ':' '[' prob_nodes ']'\n    \n    definition : PARALLEL VAR ':' INT '[' nodes ']'\n    \n    definition : DECORATOR VAR ':' INVERTER '[' node ']'\n    \n    definition : DECORATOR VAR ':' MAXTRIES '[' node ']'\n    \n    definition : DECORATOR VAR ':' MAXSECONDS '[' node ']'\n    "
    
_lr_action_items = {'BEHAVIOR':([0,3,5,14,76,78,80,96,97,98,99,],[4,4,-25,-24,-26,-27,-28,-29,-30,-31,-32,]),'SEQUENCE':([0,2,3,5,12,14,23,37,38,44,58,59,60,61,62,64,76,77,78,79,80,89,90,91,92,96,97,98,99,],[6,6,6,-25,6,-24,30,30,30,-4,30,30,30,30,30,30,-26,30,-27,30,-28,30,30,30,30,-29,-30,-31,-32,]),'SELECTOR':([0,2,3,5,12,14,23,37,38,44,58,59,60,61,62,64,76,77,78,79,80,89,90,91,92,96,97,98,99,],[7,7,7,-25,7,-24,31,31,31,-4,31,31,31,31,31,31,-26,31,-27,31,-28,31,31,31,31,-29,-30,-31,-32,]),'PROBSELECTOR':([0,2,3,5,12,14,23,37,38,44,58,59,60,61,62,64,76,77,78,79,80,89,90,91,92,96,97,98,99,],[8,8,8,-25,8,-24,32,32,32,-4,32,32,32,32,32,32,-26,32,-27,32,-28,32,32,32,32,-29,-30,-31,-32,]),'PARALLEL':([0,2,3,5,12,14,23,37,38,44,58,59,60,61,62,64,76,77,78,79,80,89,90,91,92,96,97,98,99,],[9,9,9,-25,9,-24,33,33,33,-4,33,33,33,33,33,33,-26,33,-27,33,-28,33,33,33,33,-29,-30,-31,-32,]),'DECORATOR':([0,2,3,5,12,14,23,37,38,44,58,59,60,61,62,64,76,77,78,79,80,89,90,91,92,96,97,98,99,],[10,10,10,-25,10,-24,34,34,34,-4,34,34,34,34,34,34,-26,34,-27,34,-28,34,34,34,34,-29,-30,-31,-32,]),'$end':([1,11,21,22,],[0,-1,-2,-3,]),'CODE':([2,5,12,13,14,44,76,78,80,96,97,98,99,],[11,-25,21,22,-24,-4,-26,-27,-28,-29,-30,-31,-32,]),':':([4,16,17,18,19,20,30,31,32,33,34,35,36,],[15,24,25,26,27,28,45,46,47,48,49,50,51,]),'VAR':([6,7,8,9,10,39,45,46,47,48,49,50,51,66,81,],[16,17,18,19,20,55,63,65,67,69,71,74,75,55,55,]),'[':([15,24,25,26,40,41,42,43,45,46,47,68,70,72,73,],[23,37,38,39,58,59,60,61,62,64,66,89,90,91,92,]),'CONDITION':([23,37,38,58,59,60,61,62,64,77,79,89,90,91,92,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'ACTION':([23,37,38,58,59,60,61,62,64,77,79,89,90,91,92,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'INT':([27,48,],[40,68,]),'INVERTER':([28,49,],[41,70,]),'MAXTRIES':([28,49,],[42,72,]),'MAXSECONDS':([28,49,],[43,73,]),']':([29,52,53,54,56,57,63,65,67,69,71,74,75,82,83,84,85,86,87,88,93,94,95,100,101,102,103,104,105,106,107,108,109,110,],[44,76,-20,78,80,-22,-6,-8,-10,-12,-14,-17,-18,96,97,98,99,100,101,102,-19,-23,-21,-5,-7,-9,107,108,109,110,-11,-13,-15,-16,]),',':([52,53,54,56,57,63,65,67,69,71,74,75,82,86,87,88,93,94,95,100,101,102,103,107,108,109,110,],[77,-20,77,81,-22,-6,-8,-10,-12,-14,-17,-18,77,77,77,81,-19,-23,-21,-5,-7,-9,77,-11,-13,-15,-16,]),'RIGHTARROW':([55,],[79,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'root':([0,],[1,]),'behavior':([0,3,],[2,13,]),'definitions':([0,2,],[3,12,]),'definition':([0,2,3,12,],[5,5,14,14,]),'node':([23,37,38,58,59,60,61,62,64,77,79,89,90,91,92,],[29,53,53,53,83,84,85,53,53,93,94,53,104,105,106,]),'nodes':([37,38,58,62,64,89,],[52,54,82,86,87,103,]),'prob_nodes':([39,66,],[56,88,]),'prob_node':([39,66,81,],[57,57,95,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> root","S'",1,None,None,None),
  ('root -> behavior CODE','root',2,'p_root1','parser.py',12),
  ('root -> behavior definitions CODE','root',3,'p_root2','parser.py',20),
  ('root -> definitions behavior CODE','root',3,'p_root4','parser.py',29),
  ('behavior -> BEHAVIOR : [ node ]','behavior',5,'p_behavior','parser.py',37),
  ('node -> SEQUENCE : [ nodes ]','node',5,'p_node_sequence1','parser.py',44),
  ('node -> SEQUENCE : VAR','node',3,'p_node_sequence2','parser.py',52),
  ('node -> SELECTOR : [ nodes ]','node',5,'p_node_selector1','parser.py',59),
  ('node -> SELECTOR : VAR','node',3,'p_node_selector2','parser.py',67),
  ('node -> PROBSELECTOR : [ prob_nodes ]','node',5,'p_node_prob_selector1','parser.py',73),
  ('node -> PROBSELECTOR : VAR','node',3,'p_node_prob_selector2','parser.py',80),
  ('node -> PARALLEL : INT [ nodes ]','node',6,'p_node_parallel1','parser.py',87),
  ('node -> PARALLEL : VAR','node',3,'p_node_parallel2','parser.py',94),
  ('node -> DECORATOR : INVERTER [ node ]','node',6,'p_node_decorator11','parser.py',101),
  ('node -> DECORATOR : VAR','node',3,'p_node_decorator12','parser.py',108),
  ('node -> DECORATOR : MAXTRIES [ node ]','node',6,'p_node_decorator21','parser.py',114),
  ('node -> DECORATOR : MAXSECONDS [ node ]','node',6,'p_node_decorator3','parser.py',121),
  ('node -> CONDITION : VAR','node',3,'p_node_condition','parser.py',128),
  ('node -> ACTION : VAR','node',3,'p_node_action','parser.py',135),
  ('nodes -> nodes , node','nodes',3,'p_nodes','parser.py',142),
  ('nodes -> node','nodes',1,'p_nodes','parser.py',143),
  ('prob_nodes -> prob_nodes , prob_node','prob_nodes',3,'p_prob_nodes','parser.py',153),
  ('prob_nodes -> prob_node','prob_nodes',1,'p_prob_nodes','parser.py',154),
  ('prob_node -> VAR RIGHTARROW node','prob_node',3,'p_prob_node','parser.py',164),
  ('definitions -> definitions definition','definitions',2,'p_definitions','parser.py',173),
  ('definitions -> definition','definitions',1,'p_definitions','parser.py',174),
  ('definition -> SEQUENCE VAR : [ nodes ]','definition',6,'p_definition_sequence','parser.py',181),
  ('definition -> SELECTOR VAR : [ nodes ]','definition',6,'p_definition_selector','parser.py',188),
  ('definition -> PROBSELECTOR VAR : [ prob_nodes ]','definition',6,'p_definition_prob_selector','parser.py',195),
  ('definition -> PARALLEL VAR : INT [ nodes ]','definition',7,'p_definition_parallel','parser.py',202),
  ('definition -> DECORATOR VAR : INVERTER [ node ]','definition',7,'p_definition_decorator1','parser.py',209),
  ('definition -> DECORATOR VAR : MAXTRIES [ node ]','definition',7,'p_definition_decorator2','parser.py',216),
  ('definition -> DECORATOR VAR : MAXSECONDS [ node ]','definition',7,'p_definition_decorator3','parser.py',223),
]

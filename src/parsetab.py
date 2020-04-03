
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACTION BEHAVIOR CODE COLON COMMA CONDITION DECORATOR DOLLAR DOUBLEPERCENTAGE EXPRESSION INT INVERTER LBRACKET LSQUAREBRACKET MAXSECONDS MAXTRIES NODENAME PARALLEL PROBSELECTOR RBRACKET RIGHTARROW RSQUAREBRACKET SELECTOR SEQUENCE\n    root : behavior definitions \n         | definitions behavior\n    \n    behavior : BEHAVIOR LSQUAREBRACKET node RSQUAREBRACKET\n    \n    node : sequence\n         | selector\n         | prob_selector\n         | parallel\n         | decorator\n         | action\n         | condition\n    \n    sequence : SEQUENCE COLON LSQUAREBRACKET nodes RSQUAREBRACKET\n    \n    selector : SELECTOR COLON LSQUAREBRACKET nodes RSQUAREBRACKET\n    \n    prob_selector : PROBSELECTOR COLON LSQUAREBRACKET prob_nodes RSQUAREBRACKET\n    \n    parallel : PARALLEL COLON INT LSQUAREBRACKET nodes RSQUAREBRACKET\n    \n    decorator : DECORATOR COLON policy LSQUAREBRACKET node RSQUAREBRACKET\n    \n    nodes : nodes COMMA node\n          | node\n    \n    prob_nodes : prob_nodes COMMA prob_node\n               | prob_node\n    \n    prob_node : var RIGHTARROW node\n    \n    policy : INVERTER\n           | MAXTRIES\n           | MAXSECONDS\n    \n    condition : CONDITION COLON var\n    \n    action : ACTION COLON var\n    \n    var : DOLLAR NODENAME\n    \n    definitions : definitions definition\n               | definition\n    \n    definition : sequence_def\n              | selector_def\n              | prob_selector_def\n              | parallel_def\n              | decorator_def\n              | action_def\n              | condition_def\n              | expression_def\n    \n    sequence_def : SEQUENCE NODENAME COLON LSQUAREBRACKET nodes RSQUAREBRACKET\n    \n    selector_def : SELECTOR NODENAME COLON LSQUAREBRACKET nodes RSQUAREBRACKET\n    \n    prob_selector_def : PROBSELECTOR NODENAME COLON LSQUAREBRACKET nodes RSQUAREBRACKET\n    \n    parallel_def : PARALLEL NODENAME COLON INT LSQUAREBRACKET nodes RSQUAREBRACKET\n    \n    decorator_def : DECORATOR NODENAME COLON policy LSQUAREBRACKET nodes RSQUAREBRACKET\n    \n    condition_def : CONDITION NODENAME COLON CODE\n    \n    action_def : ACTION NODENAME COLON CODE\n    \n    expression_def : EXPRESSION NODENAME COLON CODE\n    '
    
_lr_action_items = {'BEHAVIOR':([0,3,5,6,7,8,9,10,11,12,13,24,73,74,75,98,100,101,112,113,],[4,4,-28,-29,-30,-31,-32,-33,-34,-35,-36,-27,-43,-42,-44,-37,-38,-39,-40,-41,]),'SEQUENCE':([0,2,3,5,6,7,8,9,10,11,12,13,22,24,25,57,65,66,67,73,74,75,76,77,88,89,95,96,98,99,100,101,108,112,113,],[14,14,14,-28,-29,-30,-31,-32,-33,-34,-35,-36,14,-27,42,-3,42,42,42,-43,-42,-44,42,42,42,42,42,42,-37,42,-38,-39,42,-40,-41,]),'SELECTOR':([0,2,3,5,6,7,8,9,10,11,12,13,22,24,25,57,65,66,67,73,74,75,76,77,88,89,95,96,98,99,100,101,108,112,113,],[15,15,15,-28,-29,-30,-31,-32,-33,-34,-35,-36,15,-27,43,-3,43,43,43,-43,-42,-44,43,43,43,43,43,43,-37,43,-38,-39,43,-40,-41,]),'PROBSELECTOR':([0,2,3,5,6,7,8,9,10,11,12,13,22,24,25,57,65,66,67,73,74,75,76,77,88,89,95,96,98,99,100,101,108,112,113,],[16,16,16,-28,-29,-30,-31,-32,-33,-34,-35,-36,16,-27,44,-3,44,44,44,-43,-42,-44,44,44,44,44,44,44,-37,44,-38,-39,44,-40,-41,]),'PARALLEL':([0,2,3,5,6,7,8,9,10,11,12,13,22,24,25,57,65,66,67,73,74,75,76,77,88,89,95,96,98,99,100,101,108,112,113,],[17,17,17,-28,-29,-30,-31,-32,-33,-34,-35,-36,17,-27,45,-3,45,45,45,-43,-42,-44,45,45,45,45,45,45,-37,45,-38,-39,45,-40,-41,]),'DECORATOR':([0,2,3,5,6,7,8,9,10,11,12,13,22,24,25,57,65,66,67,73,74,75,76,77,88,89,95,96,98,99,100,101,108,112,113,],[18,18,18,-28,-29,-30,-31,-32,-33,-34,-35,-36,18,-27,46,-3,46,46,46,-43,-42,-44,46,46,46,46,46,46,-37,46,-38,-39,46,-40,-41,]),'ACTION':([0,2,3,5,6,7,8,9,10,11,12,13,22,24,25,57,65,66,67,73,74,75,76,77,88,89,95,96,98,99,100,101,108,112,113,],[19,19,19,-28,-29,-30,-31,-32,-33,-34,-35,-36,19,-27,47,-3,47,47,47,-43,-42,-44,47,47,47,47,47,47,-37,47,-38,-39,47,-40,-41,]),'CONDITION':([0,2,3,5,6,7,8,9,10,11,12,13,22,24,25,57,65,66,67,73,74,75,76,77,88,89,95,96,98,99,100,101,108,112,113,],[20,20,20,-28,-29,-30,-31,-32,-33,-34,-35,-36,20,-27,48,-3,48,48,48,-43,-42,-44,48,48,48,48,48,48,-37,48,-38,-39,48,-40,-41,]),'EXPRESSION':([0,2,3,5,6,7,8,9,10,11,12,13,22,24,57,73,74,75,98,100,101,112,113,],[21,21,21,-28,-29,-30,-31,-32,-33,-34,-35,-36,21,-27,-3,-43,-42,-44,-37,-38,-39,-40,-41,]),'$end':([1,5,6,7,8,9,10,11,12,13,22,23,24,57,73,74,75,98,100,101,112,113,],[0,-28,-29,-30,-31,-32,-33,-34,-35,-36,-1,-2,-27,-3,-43,-42,-44,-37,-38,-39,-40,-41,]),'LSQUAREBRACKET':([4,49,50,51,58,59,60,68,69,70,71,72,79,80,],[25,65,66,67,76,77,78,88,89,-21,-22,-23,95,96,]),'NODENAME':([14,15,16,17,18,19,20,21,82,],[26,27,28,29,30,31,32,33,97,]),'COLON':([26,27,28,29,30,31,32,33,42,43,44,45,46,47,48,],[49,50,51,52,53,54,55,56,58,59,60,61,62,63,64,]),'RSQUAREBRACKET':([34,35,36,37,38,39,40,41,81,83,84,85,86,87,90,91,92,93,97,102,103,104,105,106,109,110,111,114,115,116,117,],[57,-4,-5,-6,-7,-8,-9,-10,-25,-24,98,-17,100,101,104,105,106,-19,-26,112,113,-11,-12,-13,116,117,-16,-18,-20,-14,-15,]),'COMMA':([35,36,37,38,39,40,41,81,83,84,85,86,87,90,91,92,93,97,102,103,104,105,106,109,111,114,115,116,117,],[-4,-5,-6,-7,-8,-9,-10,-25,-24,99,-17,99,99,99,99,107,-19,-26,99,99,-11,-12,-13,99,-16,-18,-20,-14,-15,]),'INT':([52,61,],[68,79,]),'INVERTER':([53,62,],[70,70,]),'MAXTRIES':([53,62,],[71,71,]),'MAXSECONDS':([53,62,],[72,72,]),'CODE':([54,55,56,],[73,74,75,]),'DOLLAR':([63,64,78,107,],[82,82,82,82,]),'RIGHTARROW':([94,97,],[108,-26,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'root':([0,],[1,]),'behavior':([0,3,],[2,23,]),'definitions':([0,2,],[3,22,]),'definition':([0,2,3,22,],[5,5,24,24,]),'sequence_def':([0,2,3,22,],[6,6,6,6,]),'selector_def':([0,2,3,22,],[7,7,7,7,]),'prob_selector_def':([0,2,3,22,],[8,8,8,8,]),'parallel_def':([0,2,3,22,],[9,9,9,9,]),'decorator_def':([0,2,3,22,],[10,10,10,10,]),'action_def':([0,2,3,22,],[11,11,11,11,]),'condition_def':([0,2,3,22,],[12,12,12,12,]),'expression_def':([0,2,3,22,],[13,13,13,13,]),'node':([25,65,66,67,76,77,88,89,95,96,99,108,],[34,85,85,85,85,85,85,85,85,110,111,115,]),'sequence':([25,65,66,67,76,77,88,89,95,96,99,108,],[35,35,35,35,35,35,35,35,35,35,35,35,]),'selector':([25,65,66,67,76,77,88,89,95,96,99,108,],[36,36,36,36,36,36,36,36,36,36,36,36,]),'prob_selector':([25,65,66,67,76,77,88,89,95,96,99,108,],[37,37,37,37,37,37,37,37,37,37,37,37,]),'parallel':([25,65,66,67,76,77,88,89,95,96,99,108,],[38,38,38,38,38,38,38,38,38,38,38,38,]),'decorator':([25,65,66,67,76,77,88,89,95,96,99,108,],[39,39,39,39,39,39,39,39,39,39,39,39,]),'action':([25,65,66,67,76,77,88,89,95,96,99,108,],[40,40,40,40,40,40,40,40,40,40,40,40,]),'condition':([25,65,66,67,76,77,88,89,95,96,99,108,],[41,41,41,41,41,41,41,41,41,41,41,41,]),'policy':([53,62,],[69,80,]),'var':([63,64,78,107,],[81,83,94,94,]),'nodes':([65,66,67,76,77,88,89,95,],[84,86,87,90,91,102,103,109,]),'prob_nodes':([78,],[92,]),'prob_node':([78,107,],[93,114,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> root","S'",1,None,None,None),
  ('root -> behavior definitions','root',2,'p_root','parser.py',8),
  ('root -> definitions behavior','root',2,'p_root','parser.py',9),
  ('behavior -> BEHAVIOR LSQUAREBRACKET node RSQUAREBRACKET','behavior',4,'p_behavior','parser.py',16),
  ('node -> sequence','node',1,'p_node','parser.py',23),
  ('node -> selector','node',1,'p_node','parser.py',24),
  ('node -> prob_selector','node',1,'p_node','parser.py',25),
  ('node -> parallel','node',1,'p_node','parser.py',26),
  ('node -> decorator','node',1,'p_node','parser.py',27),
  ('node -> action','node',1,'p_node','parser.py',28),
  ('node -> condition','node',1,'p_node','parser.py',29),
  ('sequence -> SEQUENCE COLON LSQUAREBRACKET nodes RSQUAREBRACKET','sequence',5,'p_sequence','parser.py',36),
  ('selector -> SELECTOR COLON LSQUAREBRACKET nodes RSQUAREBRACKET','selector',5,'p_selector','parser.py',43),
  ('prob_selector -> PROBSELECTOR COLON LSQUAREBRACKET prob_nodes RSQUAREBRACKET','prob_selector',5,'p_prob_selector','parser.py',50),
  ('parallel -> PARALLEL COLON INT LSQUAREBRACKET nodes RSQUAREBRACKET','parallel',6,'p_parallel','parser.py',57),
  ('decorator -> DECORATOR COLON policy LSQUAREBRACKET node RSQUAREBRACKET','decorator',6,'p_decorator','parser.py',64),
  ('nodes -> nodes COMMA node','nodes',3,'p_nodes','parser.py',71),
  ('nodes -> node','nodes',1,'p_nodes','parser.py',72),
  ('prob_nodes -> prob_nodes COMMA prob_node','prob_nodes',3,'p_prob_nodes','parser.py',79),
  ('prob_nodes -> prob_node','prob_nodes',1,'p_prob_nodes','parser.py',80),
  ('prob_node -> var RIGHTARROW node','prob_node',3,'p_prob_node','parser.py',87),
  ('policy -> INVERTER','policy',1,'p_policy','parser.py',94),
  ('policy -> MAXTRIES','policy',1,'p_policy','parser.py',95),
  ('policy -> MAXSECONDS','policy',1,'p_policy','parser.py',96),
  ('condition -> CONDITION COLON var','condition',3,'p_condition','parser.py',102),
  ('action -> ACTION COLON var','action',3,'p_action','parser.py',110),
  ('var -> DOLLAR NODENAME','var',2,'p_var','parser.py',117),
  ('definitions -> definitions definition','definitions',2,'p_definitions','parser.py',126),
  ('definitions -> definition','definitions',1,'p_definitions','parser.py',127),
  ('definition -> sequence_def','definition',1,'p_definition','parser.py',134),
  ('definition -> selector_def','definition',1,'p_definition','parser.py',135),
  ('definition -> prob_selector_def','definition',1,'p_definition','parser.py',136),
  ('definition -> parallel_def','definition',1,'p_definition','parser.py',137),
  ('definition -> decorator_def','definition',1,'p_definition','parser.py',138),
  ('definition -> action_def','definition',1,'p_definition','parser.py',139),
  ('definition -> condition_def','definition',1,'p_definition','parser.py',140),
  ('definition -> expression_def','definition',1,'p_definition','parser.py',141),
  ('sequence_def -> SEQUENCE NODENAME COLON LSQUAREBRACKET nodes RSQUAREBRACKET','sequence_def',6,'p_sequence_def','parser.py',148),
  ('selector_def -> SELECTOR NODENAME COLON LSQUAREBRACKET nodes RSQUAREBRACKET','selector_def',6,'p_selector_def','parser.py',155),
  ('prob_selector_def -> PROBSELECTOR NODENAME COLON LSQUAREBRACKET nodes RSQUAREBRACKET','prob_selector_def',6,'p_prob_selector_def','parser.py',162),
  ('parallel_def -> PARALLEL NODENAME COLON INT LSQUAREBRACKET nodes RSQUAREBRACKET','parallel_def',7,'p_parallel_def','parser.py',169),
  ('decorator_def -> DECORATOR NODENAME COLON policy LSQUAREBRACKET nodes RSQUAREBRACKET','decorator_def',7,'p_decorator_def','parser.py',176),
  ('condition_def -> CONDITION NODENAME COLON CODE','condition_def',4,'p_condition_def','parser.py',183),
  ('action_def -> ACTION NODENAME COLON CODE','action_def',4,'p_action_def','parser.py',190),
  ('expression_def -> EXPRESSION NODENAME COLON CODE','expression_def',4,'p_expression_def','parser.py',197),
]

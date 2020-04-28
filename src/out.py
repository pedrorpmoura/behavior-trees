    CONDITION1_NODE = {
        "name": "condition1",
        "type": "condition",
        "function": "condition1",
    },

    ACTION1_NODE = {
        "name": "action1",
        "type": "action",
        "function": "action1",
    },

    ACTION2_NODE = {
        "name": "action2",
        "type": "action",
        "function": "action2",
    },

    SEL_NODE = {
        "name": "sel",
        "type": "selector",
        "children": [
            ACTION1_NODE,
            ACTION2_NODE,
        ]
    }

    SEQ2_NODE = {
        "name": "seq2",
        "type": "sequence",
        "children": [
            CONDITION1_NODE,
            SEL_NODE,
        ]
    }

    ROOT_NODE = SEQ2_NODE
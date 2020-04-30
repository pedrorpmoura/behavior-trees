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

    PARALLEL0_NODE = {
        "name": "parallel0",
        "type": "parallel",
        "success_rate": "1",
        "children": [
            ACTION1_NODE,
            ACTION2_NODE,
        ]
    }

    ROOT_NODE = PARALLEL0_NODE
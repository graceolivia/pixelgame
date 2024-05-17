dialogues = {
    'collision_event': {
        'text': 'Ho there?',
        'options': {
            'left': 'left_path',
            'right': 'right_path'
        }
    },
    'start': {
        'text': 'Welcome to the game! Do you want to go left or right?',
        'options': {
            'left': 'left_path',
            'right': 'right_path'
        }
    },
    'left_path': {
        'text': 'You went left and encountered a friendly cat. Pet the cat?',
        'options': {
            'yes': 'pet_cat',
            'no': 'ignore_cat'
        }
    },
    'right_path': {
        'text': 'You went right and found a treasure chest. Open it?',
        'options': {
            'yes': 'open_chest',
            'no': 'leave_chest'
        }
    },
    'pet_cat': {
        'text': 'The cat purrs happily. You gain a new friend.',
        'options': {
            'continue': 'end'
        }
    },
    'ignore_cat': {
        'text': 'The cat looks sad as you walk away.',
        'options': {
            'continue': 'end'
        }
    },
    'open_chest': {
        'text': 'You found a pile of gold!',
        'options': {
            'continue': 'end'
        }
    },
    'leave_chest': {
        'text': 'You walk away, leaving the chest behind.',
        'options': {
            'continue': 'end'
        }
    },
    'collision_event': {
        'text': 'You met another character! They say hello.',
        'options': {
            'continue': 'end',
            'exit': 'exit'
        }
    },
    'end': {
        'text': 'The adventure ends here. Thank you for playing!',
        'options': {}
    }
}


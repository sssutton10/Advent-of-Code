# Part 1
num_players = 404
last_marble = 71852
current_player = 0
marbles = [0]
scores = [0 for _ in range(num_players)]
current_index = 0

def get_next_pos(i, num_marbles, m_23):
    if m_23:
        return (i - 7) if (i - 7) >= 0 else (num_marbles - 7 + i)
    else:
        return i + 2 if (i + 2) <= num_marbles else 1
    
for i in range(1, (last_marble + 1)):
    mult_23 = True if (i % 23) == 0 else False
    next_pos = get_next_pos(current_index, len(marbles), mult_23)
    if mult_23:
        scores[current_player] += (i + marbles[current_index - 7])
        marbles = marbles[:next_pos] + marbles[(next_pos + 1):]
    else:
        marbles = marbles[:next_pos] + [i] + marbles[next_pos:]
    
    current_index = next_pos
    current_player = current_player + 1 if (current_player + 1) < num_players else 0
print(max(scores))

# Part 2 - used a hint here to get the idea of linked lists
class node:
    def __init__(self, prev, next, val):
        self.prev = prev
        self.next = next
        self.val = val
        
marble = node(None, None, 0)
marble.next = marble
marble.prev = marble

num_players = 404
last_marble = 71852
current_player = 0
scores = [0 for _ in range(num_players)]

for i in range(1, ((last_marble*100) + 1)):
    if (i % 23) == 0:
        scores[current_player] += i

        for _ in range(7):
            marble = marble.prev
        scores[current_player] += marble.val
        
        prev = marble.prev
        next = marble.next
        prev.next = next
        next.prev = prev
        marble = next
    else:
        prior_node = marble.next
        next_node = prior_node.next
        marble = node(prior_node, next_node, i)
        prior_node.next = marble
        next_node.prev = marble
        
    current_player = current_player + 1 if (current_player + 1) < num_players else 0

print(max(scores))
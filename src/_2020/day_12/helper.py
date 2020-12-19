def compass(direction, value):
    start = direction.index(value)

    return [*[direction[start]],
            *[i for i in direction[start::] if i != direction[start]],
            *[j for j in direction[:start:] if j != direction[start]]]

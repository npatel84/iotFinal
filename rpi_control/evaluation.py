from .message.parser import parse_command, translate_command

# controlled objects => Light

def evaluate(controlled_objects, message):
    commands = parse_command(message)
    results = []
    for command in commands:
        result = execute(controlled_objects, command)
        results.append(result)
    return results

def execute(controlled_objects, command):
    status = "OK"
    try:
        controlled_obj, action, parameter = translate_command(
            controlled_objects, command)
        result = action(parameter)
        # result = switch(on)
    except Exception as e:
        status = "ER"
        result = str(e)
    result = f"{status}:{result}"
    return result

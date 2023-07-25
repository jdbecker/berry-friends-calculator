def input_int(prompt: string, default: int) -> int:
    response = input(prompt)
    if default and response == '':
        return default
    elif isinstance(response, int):
        return response
    else:
        print('Response must be an int!')
        return input_int(prompt, default)
    
def input_bool(prompt: string, default: bool) -> bool:
    response = input(prompt)
    if default and response == '':
        return default
    elif isinstance(response, bool):
        return response
    elif isinstance(response, str):
        if response.lower() in ['y', 'yes']:
            return True
        elif response.lower() in ['n', 'no']:
            return False
    print("Response must be 'yes' or 'no'")
    return input_bool(prompt, default)

def give_berry(current_friendship: int, soothe_bell: bool) -> int:
    if current_friendship < 100:
        increase_by = 10
    elif current_friendship < 200:
        increase_by = 5
    else:
        increase_by = 2
    if soothe_bell:
        increase_by = increase_by + increase_by / 2
    return current_friendship + increase_by


if __name__ == '__main__':
    starting_friendship = input_int('Current friendship: ')
    target_friendship = input_int('Target Friendship (default 220): ', 220)
    soothe_bell = input_bool('Using soothe bell? (Y/n): ', True)
    
    berries = 0
    current_friendship = starting_friendship
    while current_friendship < target_friendship:
        current_friendship = give_berry(current_friendship, soothe_bell)
        berries += 1
    
    print(f"It takes {berries} friendship berries to get your pokemon from {starting_friendship} to {current_friendship}")

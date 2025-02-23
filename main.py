from mkdocs_macros.plugin import MacrosPlugin

def define_env(env: MacrosPlugin):
    """
    This is the hook for the variables, macros and filters.
    """

    COIN_ICON = ':fontawesome-solid-coins:{ .coin }'

    @env.macro
    def coin(amount):
        return f'`{amount}`{COIN_ICON}'

    HEAT_ICON = ':fire:'

    @env.macro
    def heat(amount):
        return f'`{amount}`{HEAT_ICON}'

    def tier_icon(amount):
        return f':fontawesome-solid-trophy:{{ .tier{amount} }}'

    @env.macro
    def tier(amount):
        return f'`{amount}`{tier_icon(amount)}'

    @env.macro
    def experience(amount):
        return f'`{amount}`:scroll:'

    @env.macro
    def reputation(amount):
        return f'`{amount}`:material-sword-cross:'

    @env.macro
    def stress(amount):
        return f'`{amount}`:fontawesome-solid-heart-crack:'

    @env.macro
    def d6_roll(number):
        if 1 <= number <= 6:
            return f'`{number}`:material-dice-{number}:'
        else:
            return f'`{number}`:game_die:'

    @env.macro
    def d6_rolls(numbers, lowest=False):
        op, extra = (min, '(lowest) ') if lowest else (max, '')
        return '[' + ', '.join([d6_roll(n) for n in numbers]) + '] `=` ' + extra + d6_roll(op(numbers))

    def character_link(character):
        return f'[{character["name"]}]({character["url"]})'

    def inject_character_links(characters):
        for c in characters.values():
            c['link'] = character_link(c)

    def inject_links(variables):
        inject_character_links(variables.characters)

    inject_links(env.variables)

from mkdocs_macros.plugin import MacrosPlugin

def define_env(env: MacrosPlugin):
    """
    This is the hook for the variables, macros and filters.
    """

    COIN_ICON = ':fontawesome-solid-coins:{ .coin }'

    @env.macro
    def coin(amount):
        return f'`{amount}`{COIN_ICON}'

    def character_link(character):
        return f'[{character["name"]}]({character["url"]})'

    def inject_character_links(characters):
        for c in characters.values():
            c['link'] = character_link(c)

    def inject_links(variables):
        inject_character_links(variables.characters)

    inject_links(env.variables)

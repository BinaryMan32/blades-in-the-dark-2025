def define_env(env):
    """
    This is the hook for the variables, macros and filters.
    """

    COIN_ICON = ':fontawesome-solid-coins:{ .coin }'

    @env.macro
    def coin(amount):
        return f'`{amount}`{COIN_ICON}'

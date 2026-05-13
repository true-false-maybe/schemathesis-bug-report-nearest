import schemathesis


@schemathesis.hook
def before_call(context: schemathesis.HookContext, case: schemathesis.Case, kwargs: dict):
    case.query = case.query

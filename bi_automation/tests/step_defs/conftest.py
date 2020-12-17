from tests.step_defs.framework.driver import *
from tests.step_defs.bi_common import *

caps = {}


# hooks

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome",
        help="To run locally use - 'chrome'. To run on a remote browser use grid_chrome "
    )
    # parser.addoption(
    #     "--env", action="store",
    #     help="One of the values: dev, qa, stage, prod"
    # )


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print("Scenario failed - ", scenario, "\n Step -", step)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
